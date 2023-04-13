from __future__ import annotations
from enum import auto, Enum

from random import Random
from typing import TYPE_CHECKING, Dict

import colors
from components.base_component import BaseComponent
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class PrimaryAttributesEnum(Enum):
    STRENGTH = auto()
    INTELLIGENCE = auto()
    WILLPOWER = auto()
    AGILITY = auto()
    SPEED = auto()
    ENDURANCE = auto()
    PERSONALITY = auto()
    LUCK = auto()


class PrimaryAttributes(BaseComponent):
    parent: Actor
    primary_attribute_map: Dict = {}

    def __init__(
            self,
            strength: int = 40,
            intelligence: int = 40,
            willpower: int = 40,
            agility: int = 40,
            speed: int = 40,
            endurance: int = 40,
            personality: int = 40,
            luck: int = 40):

        # Primary attributes
        self.primary_attribute_map[PrimaryAttributesEnum.STRENGTH] = ("Strength", strength)
        self.primary_attribute_map[PrimaryAttributesEnum.INTELLIGENCE] = ("Intelligence", intelligence)
        self.primary_attribute_map[PrimaryAttributesEnum.WILLPOWER] = ("Willpower", willpower)
        self.primary_attribute_map[PrimaryAttributesEnum.AGILITY] = ("Agility", agility)
        self.primary_attribute_map[PrimaryAttributesEnum.SPEED] = ("Speed", speed)
        self.primary_attribute_map[PrimaryAttributesEnum.ENDURANCE] = ("Endurance", endurance)
        self.primary_attribute_map[PrimaryAttributesEnum.PERSONALITY] = ("Personality", personality)
        self.primary_attribute_map[PrimaryAttributesEnum.LUCK] = ("Luck", luck)

        # Derived Attributes
        self.max_health = (strength + endurance) // 2
        self._health = self.max_health
        self.max_magicka = intelligence  # TODO: Add racial modifiers and birthsign modifiers
        self._magicka = self.max_magicka
        self.max_fatigue = strength + willpower + agility + endurance
        self._fatigue = self.max_fatigue

        # Rand generator to generate rolls
        self.rand_generator = Random()

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, min(value, self.max_health))
        if self._health == 0 and self.parent.ai:
            self.die()

    @property
    def magicka(self) -> int:
        return self._magicka

    @magicka.setter
    def magicka(self, value: int) -> None:
        self._magicka = max(0, min(value, self.max_magicka))

    @property
    def fatigue(self) -> int:
        return self._fatigue

    @fatigue.setter
    def fatigue(self, value: int) -> None:
        self._fatigue = max(0, min(value, self.max_fatigue))

    def heal(self, amount: int) -> int:
        if self.health == self.max_health:
            return 0

        new_health_value = self.health + amount

        if new_health_value > self.max_health:
            new_health_value = self.max_health

        amount_recovered = new_health_value - self.health
        self.health = new_health_value
        return amount_recovered

    def pa_take_damage(self, amount: int) -> None:
        self.health -= amount  # TODO: Refactor out once magic damage is in

    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "You died!"
            self.engine.message_log.add_message(death_message, colors.PLAYER_DIE)
        else:
            death_message = f"{self.parent.name} is dead!"
            self.engine.message_log.add_message(death_message, colors.ENEMY_DIE)
            self.engine.player.level.add_xp(self.parent.level.xp_given)

        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.render_order = RenderOrder.CORPSE
        self.parent.name = f"remains of {self.parent.name}"
