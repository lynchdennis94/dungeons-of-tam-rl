from __future__ import annotations

import copy
import os
from typing import Callable, Optional, Tuple, TYPE_CHECKING, Union, List

import tcod.event

import actions
from actions import Action, BumpAction, DropItemAction, PickupAction, WaitAction, TakeStairsAction

import colors
import exceptions
from components import character_class, birthsign
from components.primary_attributes import *
from components.race import MALE_RACES, FEMALE_RACES
from components.skills import SkillEnum
from factories.weapon_factories import CHITIN_WEAPONS
from gender_types import GenderType
from weapon_types import WEAPON_TO_SKILL_MAP

if TYPE_CHECKING:
    from engine import Engine
    from entity import Item

MOVE_KEYS = {
    # Numpad keys
    tcod.event.K_KP_1: (-1, 1),
    tcod.event.K_KP_2: (0, 1),
    tcod.event.K_KP_3: (1, 1),
    tcod.event.K_KP_4: (-1, 0),
    tcod.event.K_KP_6: (1, 0),
    tcod.event.K_KP_7: (-1, -1),
    tcod.event.K_KP_8: (0, -1),
    tcod.event.K_KP_9: (1, -1),

    # vim keys
    tcod.event.K_b: (-1, 1),
    tcod.event.K_j: (0, 1),
    tcod.event.K_n: (1, 1),
    tcod.event.K_h: (-1, 0),
    tcod.event.K_l: (1, 0),
    tcod.event.K_y: (-1, -1),
    tcod.event.K_k: (0, -1),
    tcod.event.K_u: (1, -1),
}

CURSOR_Y_KEYS = {
    tcod.event.K_UP: -1,
    tcod.event.K_DOWN: 1,
    tcod.event.K_PAGEUP: -10,
    tcod.event.K_PAGEDOWN: 10
}

WAIT_KEYS = {
    tcod.event.K_KP_5,
    tcod.event.K_r
}

CONFIRM_KEYS = {
    tcod.event.K_RETURN,
    tcod.event.K_KP_ENTER
}

ActionOrHandler = Union[Action, "BaseEventHandler"]
"""An event handler return value which can trigger an action or switch active handlers.

If a handler is returned then it will become the active handler for future events.
If an action is returned it will be attempted and if it's valid then
MainGameEventHandler will become the active handler.
"""


class BaseEventHandler(tcod.event.EventDispatch[ActionOrHandler]):
    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle an event and return the next active event handler."""
        state = self.dispatch(event)
        if isinstance(state, BaseEventHandler):
            return state
        assert not isinstance(state, Action), f"{self!r} can not handle actions."
        return self

    def on_render(self, console: tcod.Console) -> None:
        raise NotImplementedError()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()


class EventHandler(BaseEventHandler):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle events for input handlers with an engine."""
        action_or_state = self.dispatch(event)
        if isinstance(action_or_state, BaseEventHandler):
            return action_or_state
        if self.handle_action(action_or_state):
            # A valid action was performed
            if not self.engine.player.is_alive:
                return GameOverEventHandler(self.engine)
            elif self.engine.player.level.requires_level_up:
                return LevelUpEventHandler(self.engine)
            return MainGameEventHandler(self.engine)
        return self

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """
        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.engine.message_log.add_message(exc.args[0], colors.IMPOSSIBLE)
            return False

        self.engine.handle_enemy_turns()
        self.engine.update_fov()
        return True

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
            self.engine.mouse_location = event.tile.x, event.tile.y

    def on_render(self, console: tcod.Console) -> None:
        self.engine.render(console)


class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated"""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        log_console = tcod.Console(console.width - 6, console.height - 6)

        log_console.draw_frame(0, 0, log_console.width, log_console.height)
        log_console.print_box(0, 0, log_console.width, 1, '[Message History]', alignment=tcod.CENTER)

        self.engine.message_log.render_messages(
            log_console,
            1,
            1,
            log_console.width - 2,
            log_console.height - 2,
            self.engine.message_log.messages[:self.cursor + 1])
        log_console.blit(console, 3, 3)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[MainGameEventHandler]:
        if event.sym in CURSOR_Y_KEYS:
            adjust = CURSOR_Y_KEYS[event.sym]
            if adjust < 0 and self.cursor == 0:
                self.cursor = self.log_length - 1
            elif adjust > 0 and self.cursor == self.log_length - 1:
                self.cursor = 0
            else:
                self.cursor = max(0, min(self.cursor + adjust, self.log_length - 1))
        elif event.sym == tcod.event.K_HOME:
            self.cursor = 0
        elif event.sym == tcod.event.K_END:
            self.cursor = self.log_length - 1
        else:
            return MainGameEventHandler(self.engine)
        return None


class AskUserEventHandler(EventHandler):
    """Handles user input for actions which require special input"""

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        """By default any key exist this input handler."""
        if event.sym in {
            tcod.event.K_LSHIFT,
            tcod.event.K_RSHIFT,
            tcod.event.K_LCTRL,
            tcod.event.K_RCTRL,
            tcod.event.K_LALT,
            tcod.event.K_RALT,
        }:
            return None
        return self.on_exit()

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """By default, any mouse click exits this input handler."""
        return self.on_exit()

    def on_exit(self) -> Optional[ActionOrHandler]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        return MainGameEventHandler(self.engine)


def _format_skill_table_line(skill_map: Dict,
                             major_skill_list: List[SkillEnum],
                             minor_skill_list: List[SkillEnum],
                             misc_skill_list: List[SkillEnum],
                             current_index: int):

    if current_index < len(major_skill_list):
        major_skill_name, major_skill_value = skill_map[major_skill_list[current_index]]
        major_skill_line = " |" + "{:<18}".format(major_skill_name) + "{:<3}".format(major_skill_value)
    else:
        major_skill_line = " |" + "{:<21}".format(" ")

    if current_index < len(minor_skill_list):
        minor_skill_name, minor_skill_value = skill_map[minor_skill_list[current_index]]
        minor_skill_line = "|" + "{:<18}".format(minor_skill_name) + "{:<3}".format(minor_skill_value)
    else:
        minor_skill_line = "|" + "{:<21}".format(" ")

    if current_index < len(misc_skill_list):
        misc_skill_name, misc_skill_value = skill_map[misc_skill_list[current_index]]
        misc_skill_line = "|" + "{:<17}".format(misc_skill_name) + "{:<3}".format(misc_skill_value) + "|"
    else:
        misc_skill_line = "|" + "{:<20}".format(" ") + "|"

    return major_skill_line + minor_skill_line + misc_skill_line


class CharacterScreenEventHandler(AskUserEventHandler):
    TITLE = "Character Sheet"

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        x = 5
        y = 5

        width = 70

        strength_string = "{:<13}".format(
            f"Strength: {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.STRENGTH][1]}")
        speed_string = "{:<13}".format(
            f"Speed:    {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.SPEED][1]}")
        intelligence_string = "{:<17}".format(
            f"Intelligence: {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.INTELLIGENCE][1]}")
        endurance_string = "{:<17}".format(
            f"Endurance:    {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.ENDURANCE][1]}")
        personality_string = "{:<16}".format(
            f"Personality: {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.PERSONALITY][1]}")
        willpower_string = "{:<16}".format(
            f"Willpower:   {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.WILLPOWER][1]}")
        agility_string = "{:<12}".format(
            f"Agility: {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1]}")
        luck_string = "{:<12}".format(
            f"Luck:    {self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.LUCK][1]}")

        major_skill_list = self.engine.player.character_class.major_skills_list
        minor_skill_list = self.engine.player.character_class.minor_skills_list
        misc_skill_list = self.engine.player.character_class.misc_skills_list
        skill_map = self.engine.player.skills.skill_map

        items_to_print = [
            "",
            f"Name: {self.engine.player.name}",
            f"Gender: {self.engine.player.gender.name.lower().capitalize()}",
            f"Race: {self.engine.player.race.name}",
            f"Class: {self.engine.player.character_class.name}",
            "",
            f"Level: {self.engine.player.level.current_level}",
            f"Health: {self.engine.player.primary_attributes.health} / {self.engine.player.primary_attributes.max_health}",
            f"Magicka: {self.engine.player.primary_attributes.magicka} / {self.engine.player.primary_attributes.max_magicka}",
            f"Fatigue: {self.engine.player.primary_attributes.fatigue} / {self.engine.player.primary_attributes.max_fatigue}",
            "",
            "Attributes",
            f"{strength_string} {intelligence_string} {personality_string} {agility_string}",
            f"{speed_string} {endurance_string} {willpower_string} {luck_string}",
            "",
            " ================================================================== ",
            "{:<23}".format(" |Major Skills") + "{:<22}".format("|Minor Skills") + "{:<21}".format("|Misc Skills") + "|",
            " ================================================================== "
        ]

        for i in range(max(len(minor_skill_list), len(major_skill_list), len(misc_skill_list))):
            items_to_print.append(_format_skill_table_line(
                skill_map=skill_map,
                major_skill_list=major_skill_list,
                minor_skill_list=minor_skill_list,
                misc_skill_list=misc_skill_list,
                current_index=i))

        items_to_print.append(" ================================================================== ")
        items_to_print.append("")

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=len(items_to_print) + 1,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        for y_index, item_to_print in enumerate(items_to_print):
            console.print(
                x=x + 1,
                y=y + y_index,
                string=item_to_print
            )


class CharacterCreationEventHandler(AskUserEventHandler):
    TITLE = "Create a Character"

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        return None

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        return None


class NameSelectionEventHandler(CharacterCreationEventHandler):

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.name = ""

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        if event.sym in (tcod.event.K_RETURN, tcod.event.K_KP_ENTER):
            self.engine.player.name = self.name
            return GenderSelectionEventHandler(self.engine)
        elif event.sym in (tcod.event.K_DELETE, tcod.event.K_BACKSPACE):
            self.name = self.name[:-1]
        else:
            key = event.sym
            mod = event.mod

            if tcod.event.K_a <= key <= tcod.event.K_z:
                char_to_add = key
                if mod & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
                    print("TRUE")
                    char_to_add -= 32

                if len(self.name) < 30:
                    self.name += chr(char_to_add)

        return None

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=5,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(
            x=x + 1, y=y + 1,
            string=f"Enter your name:"
        )

        console.print(
            x=x + 1, y=y + 2,
            string=f""
        )

        console.print(
            x=x + 1, y=y + 3,
            string=f"{self.name}"
        )


class GenderSelectionEventHandler(CharacterCreationEventHandler):

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        match event.sym:
            case tcod.event.K_m:
                self.engine.player.gender = GenderType.MALE
            case tcod.event.K_f:
                self.engine.player.gender = GenderType.FEMALE
            case _:
                return None

        return RaceSelectionEventHandler(self.engine)

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=5,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(
            x=x + 1, y=y + 1,
            string=f"Choose your Gender:"
        )

        console.print(
            x=x + 1, y=y + 2,
            string=f"[M] Male"
        )

        console.print(
            x=x + 1, y=y + 3,
            string=f"[F] Female"
        )


class RaceSelectionEventHandler(CharacterCreationEventHandler):
    def __init__(self, engine: Engine):
        super().__init__(engine)

        self.selection_list = []
        race_list = MALE_RACES if self.engine.player.gender == GenderType.MALE else FEMALE_RACES

        for i, race in enumerate(race_list):
            selection_character = chr(ord('a') + i)
            self.selection_list.append((selection_character, race))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        index = event.sym - tcod.event.K_a
        if 0 <= index <= len(self.selection_list):
            self.engine.player.race = self.selection_list[index][1]
            self.engine.player.race.parent = self.engine.player
            return ClassSelectionEventHandler(self.engine)

        return None

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=13,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(
            x=x + 1, y=y + 1,
            string=f"Choose your Race:"
        )

        y_index = y + 2
        for selection_character, race in self.selection_list:
            console.print(
                x=x + 1, y=y_index,
                string=f"[{selection_character}] {race.name}"
            )

            y_index += 1


class ClassSelectionEventHandler(CharacterCreationEventHandler):
    def __init__(self, engine: Engine):
        super().__init__(engine)

        self.selection_list = []
        class_list = character_class.CHARACTER_CLASS_LIST
        for i, class_choice in enumerate(class_list):
            selection_character = chr(ord('a') + i)
            self.selection_list.append((selection_character, class_choice))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        index = event.sym - tcod.event.K_a
        if 0 <= index <= len(self.selection_list):
            self.engine.player.character_class = self.selection_list[index][1]
            self.engine.player.character_class.parent = self.engine.player
            return BirthSignSelectionEventHandler(self.engine)

        return None

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=24,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(
            x=x + 1, y=y + 1,
            string=f"Choose your Class:"
        )

        y_index = y + 2
        for selection_character, race in self.selection_list:
            console.print(
                x=x + 1, y=y_index,
                string=f"[{selection_character}] {race.name}"
            )

            y_index += 1


class BirthSignSelectionEventHandler(CharacterCreationEventHandler):
    def __init__(self, engine: Engine):
        super().__init__(engine)

        self.selection_list = []
        birthsign_list = birthsign.BIRTHSIGN_LIST
        for i, birthsign_choice in enumerate(birthsign_list):
            selection_character = chr(ord('a') + i)
            self.selection_list.append((selection_character, birthsign_choice))

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        index = event.sym - tcod.event.K_a
        if 0 <= index <= len(self.selection_list):
            self.engine.player.birthsign = self.selection_list[index][1]
            self.engine.player.birthsign.parent = self.engine.player
            return CharacterConfirmationEventHandler(self.engine)

        return None

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=16,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(
            x=x + 1, y=y + 1,
            string=f"Choose your Birthsign:"
        )

        y_index = y + 2
        for selection_character, birthsign_element in self.selection_list:
            console.print(
                x=x + 1, y=y_index,
                string=f"[{selection_character}] {birthsign_element.name}"
            )

            y_index += 1


class CharacterConfirmationEventHandler(CharacterCreationEventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        match event.sym:
            case tcod.event.K_y:
                # Finalize the character creation and start the game
                self.engine.player.initialize_character_info()

                # Grant the most basic weapon in a preferred combat skill
                best_weapon_type = None
                best_weapon_skill_value = 0
                for weapon_type in WEAPON_TO_SKILL_MAP:
                    skill_type = WEAPON_TO_SKILL_MAP[weapon_type]
                    _, skill_value = self.engine.player.skills.skill_map[skill_type]
                    if skill_value > best_weapon_skill_value:
                        best_weapon_skill_value = skill_value
                        best_weapon_type = weapon_type

                starting_weapon = None
                for possible_weapon in CHITIN_WEAPONS:
                    if possible_weapon.equippable.weapon_type == best_weapon_type:
                        starting_weapon = possible_weapon
                        break

                if starting_weapon:
                    starting_weapon_instance = copy.deepcopy(starting_weapon)
                    self.engine.player.inventory.items.append(starting_weapon_instance)
                    self.engine.player.equipment.equip_to_slot("weapon", starting_weapon_instance, False)

                return MainGameEventHandler(self.engine)
            case tcod.event.K_n:
                # Return to start of character creation screen
                return GenderSelectionEventHandler(self.engine)
            case _:
                return None

    def on_render(self, console: tcod.Console) -> None:
        x = 5
        y = 5
        console.print(
            x=x + 1, y=y + 1,
            string=f""
        )

        width = 70

        items_to_print = [
            f"Your Character:",
            f"",
            f"Name: {self.engine.player.name}",
            f"Gender: {self.engine.player.gender.name.lower().capitalize()}",
            f"Race: {self.engine.player.race.name}",
            f"Class: {self.engine.player.character_class.name}",
            f"Birthsign: {self.engine.player.birthsign.name}",
            f"",
            f"[y] Yes",
            f"[n] No"
        ]

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=12,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        for y_index, item_to_print in enumerate(items_to_print):
            console.print(
                x=x + 1,
                y=y + y_index,
                string=item_to_print
            )


class LevelUpEventHandler(AskUserEventHandler):
    TITLE = "Level Up"

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        console.draw_frame(
            x=x,
            y=0,
            width=35,
            height=8,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        console.print(x=x + 1, y=1, string="Congratulations! You level up!")
        console.print(x=x + 1, y=2, string="Select an attribute to increase")

        console.print(
            x=x + 1,
            y=4,
            string=f"a) Constitution (+20 HP, from {self.engine.player.primary_attributes.max_health})"
        )

        console.print(
            x=x + 1,
            y=5,
            string=f"b) Strength:{self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.STRENGTH][1] + 1} "
                   f"(+{(self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.STRENGTH][1] + 1 - 10) // 2} to attack)"
        )

        console.print(
            x=x + 1,
            y=6,
            string=f"c) Agility:{self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1] + 1} "
                   f"(+{(self.engine.player.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1] + 1 - 10) // 2} to defense)"
        )

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        match index:
            case 0:
                player.level.increase_max_health()
            case 1:
                player.level.increase_power()
            case 2:
                player.level.increase_defense()
            case _:
                self.engine.message_log.add_message("Invalid entry.", colors.INVALID)
                return None

        return super().ev_keydown(event)

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """Don't allow the player to click to exit the menu, like normal"""
        return None


class InventoryEventHandler(AskUserEventHandler):
    """This handler lets the user select an item.

    What happens then depends on the subclass.
    """

    TITLE = "<missing title>"

    def on_render(self, console: tcod.Console) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console)
        number_of_items_in_inventory = len(self.engine.player.inventory.items)

        height = number_of_items_in_inventory + 2

        if height <= 3:
            height = 3

        half_of_map_width = int(self.engine.game_map.gamemap.width / 2)

        if self.engine.player.x <= half_of_map_width:
            x = half_of_map_width + 10
        else:
            x = 0

        y = 0

        width = len(self.TITLE) + 4

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0)
        )

        if number_of_items_in_inventory > 0:
            for i, item in enumerate(self.engine.player.inventory.items):
                item_key = chr(ord("a") + i)
                is_equipped = self.engine.player.equipment.item_is_equipped(item)
                item_string = f"({item_key}) {item.name}"

                if is_equipped:
                    item_string = f"{item_string} (E)"

                console.print(x + 1, y + i + 1, item_string)
        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 26:
            try:
                selected_item = player.inventory.items[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry", colors.INVALID)
                return None
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        raise NotImplementedError()


class InventoryActivateHandler(InventoryEventHandler):
    TITLE = "Select an item to use"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        if item.consumable:
            return item.consumable.get_action(self.engine.player)
        elif item.equippable:
            return actions.EquipAction(self.engine.player, item)
        else:
            return None


class InventoryDropHandler(InventoryEventHandler):
    TITLE = "Select an item to drop"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        return DropItemAction(self.engine.player, item)


class SelectIndexHandler(AskUserEventHandler):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        player = self.engine.player
        engine.mouse_location = player.x, player.y

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)
        x, y = self.engine.mouse_location
        console.tiles_rgb["bg"][x, y] = colors.WHITE
        console.tiles_rgb["fg"][x, y] = colors.BLACK

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        key = event.sym
        if key in MOVE_KEYS:
            modifier = 1
            if event.mod & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
                modifier *= 5
            if event.mod & (tcod.event.KMOD_LCTRL | tcod.event.KMOD_RCTRL):
                modifier *= 10
            if event.mod & (tcod.event.KMOD_LALT | tcod.event.KMOD_RALT):
                modifier *= 20

            x, y = self.engine.mouse_location
            dx, dy = MOVE_KEYS[key]
            x += modifier * dx
            y += modifier * dy

            x = max(0, min(x, self.engine.game_map.width - 1))
            y = max(0, min(y, self.engine.game_map.height - 1))
            self.engine.mouse_location = x, y
            return None
        elif key in CONFIRM_KEYS:
            return self.on_index_selected(*self.engine.mouse_location)
        return super().ev_keydown(event)

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        if self.engine.game_map.in_bounds(*event.tile):
            if event.button == 1:
                return self.on_index_selected(*event.tile)
        return super().ev_mousebuttondown(event)

    def on_index_selected(self, x: int, y: int) -> Optional[ActionOrHandler]:
        raise NotImplementedError()


class LookHandler(SelectIndexHandler):
    def on_index_selected(self, x: int, y: int) -> MainGameEventHandler:
        return MainGameEventHandler(self.engine)


class SingleRangedAttackHandler(SelectIndexHandler):
    def __init__(self, engine: Engine, callback: Callable[[Tuple[int, int]], Optional[Action]]):
        super().__init__(engine)
        self.callback = callback

    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))


class AreaRangedAttackHandler(SelectIndexHandler):
    def __init__(
            self,
            engine: Engine,
            radius: int,
            callback: Callable[[Tuple[int, int]], Optional[Action]]
    ):
        super().__init__(engine)

        self.radius = radius
        self.callback = callback

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        x, y = self.engine.mouse_location

        console.draw_frame(
            x=x - self.radius - 1,
            y=y - self.radius - 1,
            width=self.radius ** 2,
            height=self.radius ** 2,
            fg=colors.RED,
            clear=False
        )

    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))


class MainGameEventHandler(EventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        action: Optional[Action] = None
        key = event.sym
        modifier = event.mod
        player = self.engine.player

        if key == tcod.event.K_PERIOD and modifier & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
            return TakeStairsAction(player)

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key == tcod.event.K_v:
            return HistoryViewer(self.engine)
        elif key == tcod.event.K_g:
            action = PickupAction(player)
        elif key == tcod.event.K_i:
            return InventoryActivateHandler(self.engine)
        elif key == tcod.event.K_d:
            return InventoryDropHandler(self.engine)
        elif key == tcod.event.K_c:
            return CharacterScreenEventHandler(self.engine)
        elif key == tcod.event.K_SLASH:
            return LookHandler(self.engine)
        elif key in WAIT_KEYS:
            action = WaitAction(player)
        elif key == tcod.event.K_ESCAPE:
            raise SystemExit()

        return action


class GameOverEventHandler(EventHandler):
    def on_quit(self) -> None:
        """Handle exiting out of a finished game"""
        if os.path.exists("savegame.sav"):
            os.remove("savegame.sav")
            raise exceptions.QuitWithoutSaving()

    def ev_quit(self, event: tcod.event.Quit) -> None:
        self.on_quit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()


class PopupMessage(BaseEventHandler):
    """Display a popup text window"""

    def __init__(self, parent_handler: BaseEventHandler, text: str):
        self.parent = parent_handler
        self.text = text

    def on_render(self, console: tcod.Console) -> None:
        """Render the parent and dim the result, then print the message on top"""
        self.parent.on_render(console)
        console.tiles_rgb["fg"] //= 8
        console.tiles_rgb["bg"] //= 8

        console.print(
            console.width // 2,
            console.height // 2,
            self.text,
            fg=colors.WHITE,
            bg=colors.BLACK,
            alignment=tcod.CENTER
        )

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:
        return self.parent
