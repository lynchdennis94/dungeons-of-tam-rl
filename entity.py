from __future__ import annotations

import copy
import math
import random
from typing import Optional, Tuple, Type, TypeVar, TYPE_CHECKING, Union

import components.birthsign
from components import ai, fighter, equipment, primary_attributes, skills, inventory, level
from components.birthsign import Birthsign, BIRTHSIGN_LIST
from components.character_class import CharacterClass, CHARACTER_CLASS_LIST
from components.creature_fighter import CreatureFighter
from components.equipment import Equipment
from components.equippable import Equippable
from components.level import Level
from components.race import *
from gender_types import GenderType
from render_order import RenderOrder

if TYPE_CHECKING:
    from components.ai import BaseAI
    from components.consumable import Consumable
    from components.fighter import Fighter
    from components.primary_attributes import PrimaryAttributes
    from components.skills import Skills, CreatureSkills
    from components.inventory import Inventory
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    parent: Union[GameMap, Inventory]

    def __init__(
            self,
            parent: Optional[GameMap] = None,
            x: int = 0,
            y: int = 0,
            char: str = '?',
            color: Tuple[int, int, int] = (255, 255, 255),
            eyesight_radius: int = 0,
            name: str = "<Unnamed>",
            blocks_movement: bool = False,
            render_order: RenderOrder = RenderOrder.CORPSE
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.eyesight_radius = eyesight_radius
        self.name = name
        self.blocks_movement = blocks_movement
        self.render_order = render_order
        if parent:
            # If parent isn't provided now it will be set later.
            self.parent = parent
            parent.entities.add(self)

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.parent = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "parent"):  # Possibly uninitialized
                if self.parent is self.gamemap:
                    self.gamemap.entities.remove(self)
            self.parent = gamemap
            gamemap.entities.add(self)

    def distance(self, x: int, y: int) -> float:
        return math.sqrt(math.pow(x - self.x, 2) + math.pow(y - self.y, 2))


class Actor(Entity):
    def __init__(
            self,
            *,
            x: int = 0,
            y: int = 0,
            char: str = '?',
            color: Tuple[int, int, int] = (255, 255, 255),
            eyesight_radius: int = 0,
            name: str = "<Unnamed>",
            ai_cls: Type[BaseAI],
            gender: GenderType = None,
            race: Race = None,
            character_class: CharacterClass = None,
            birthsign: Birthsign = None,
            fighter: Fighter,
            equipment: Equipment,
            primary_attributes: PrimaryAttributes,
            skills: Skills,
            inventory: Inventory,
            level: Level
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            eyesight_radius=eyesight_radius,
            name=name,
            blocks_movement=True,
            render_order=RenderOrder.ACTOR
        )

        self.ai: Optional[BaseAI] = ai_cls(self)
        self.equipment = equipment
        self.equipment.parent = self
        self.gender = gender
        self.race = race
        if race:
            self.race.parent = self
        self.character_class = character_class
        if character_class:
            self.character_class.parent = self
        self.birthsign = birthsign
        if birthsign:
            self.birthsign.parent = self
        self.fighter = fighter
        self.fighter.parent = self
        self.primary_attributes = primary_attributes
        self.primary_attributes.parent = self
        self.skills = skills
        self.skills.parent = self

        self.inventory = inventory
        self.inventory.parent = self

        self.level = level
        self.level.parent = self

    @property
    def is_alive(self) -> bool:
        """Returns True as long as this actor can perform actions."""
        return bool(self.ai)

    def initialize_character_info(self):
        self.primary_attributes.primary_attribute_map = self.race.base_primary_attributes.primary_attribute_map
        self.character_class.set_skill_level_factor_weights()
        self.character_class.set_attribute_bonuses()
        self.character_class.set_skill_bonuses()
        self.race.set_skill_bonuses()
        self.birthsign.apply_abilities()
        self.birthsign.add_spell()
        self.birthsign.add_power()
        self.color = self.race.color


class Bandit(Actor):
    def __init__(self,
                 char: str = '?',
                 eyesight_radius: int = 0,
                 ):
        super().__init__(
            char=char,
            eyesight_radius=eyesight_radius,
            ai_cls=ai.HostileEnemy,
            fighter=fighter.Fighter(),
            equipment=equipment.Equipment(),
            primary_attributes=PrimaryAttributes(),
            skills=skills.Skills(),
            inventory=inventory.Inventory(capacity=26),
            level=level.Level()
        )

        print(self.primary_attributes is None)

    def randomize_bandit(self):
        rand_generator = random.Random()
        # Pick a random gender and race
        gender = rand_generator.choice([GenderType.FEMALE, GenderType.MALE])
        print(gender)

        if GenderType.FEMALE == gender:
            race = rand_generator.choice(FEMALE_RACES)
        else:
            race = rand_generator.choice(MALE_RACES)

        # Pick a random character class
        character_class = rand_generator.choice(CHARACTER_CLASS_LIST)

        # Pick a random birthsign
        birthsign = rand_generator.choice(BIRTHSIGN_LIST)

        # Initialize the character
        self.race = race
        self.race.parent = self
        self.character_class = character_class
        self.character_class.parent = self
        self.birthsign = birthsign
        self.birthsign.parent = self
        self.initialize_character_info()

        self.name = f"{race.name} {character_class.name}"


class Creature(Actor):
    def __init__(self,
                 char: str,
                 color: Tuple[int, int, int],
                 eyesight_radius: int,
                 name: str,
                 ai_cls: Type[BaseAI],
                 equipment: Equipment,
                 fighter: CreatureFighter,
                 primary_attributes: PrimaryAttributes,
                 skills: CreatureSkills,
                 inventory: Inventory,
                 level: Level,
                 health: int
                 ):
        super().__init__(
            char=char,
            color=color,
            eyesight_radius=eyesight_radius,
            name=name,
            ai_cls=ai_cls,
            fighter=fighter,
            equipment=equipment,
            primary_attributes=primary_attributes,
            skills=skills,
            inventory=inventory,
            level=level
        )
        self.primary_attributes.max_health = health
        self.primary_attributes.health = health


class Item(Entity):
    def __init__(
            self,
            *,
            x: int = 0,
            y: int = 0,
            char: str = '?',
            color: Tuple[int, int, int] = (255, 255, 255),
            name: str = "<Unnamed>",
            consumable: Optional[Consumable] = None,
            equippable: Optional[Equippable] = None
    ):
        super().__init__(
            x=x,
            y=y,
            char=char,
            color=color,
            name=name,
            eyesight_radius=0,
            blocks_movement=False,
            render_order=RenderOrder.ITEM
        )

        self.consumable = consumable
        if self.consumable:
            self.consumable.parent = self

        self.equippable = equippable
        if self.equippable:
            self.equippable.parent = self
