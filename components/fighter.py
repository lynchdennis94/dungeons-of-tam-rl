from __future__ import annotations

from random import Random
from typing import TYPE_CHECKING

import colors
from components.base_component import BaseComponent
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    parent: Actor
    rand_generator: Random

    def __init__(
            self,
            strength: int,
            intelligence: int,
            willpower: int,
            agility: int,
            speed: int,
            endurance: int,
            personality: int,
            luck: int):

        # Primary attributes
        self.strength = strength
        self.intelligence = intelligence
        self.willpower = willpower
        self.agility = agility
        self.speed = speed
        self.endurance = endurance
        self.personality = personality
        self.luck = luck

        # Derived Attributes
        self.max_health = (strength + endurance) // 2
        self._health = self.max_health
        self.max_magicka = intelligence # TODO: Add racial modifiers and birthsign modifiers
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

    @property
    def hit_rate(self) -> int:
        pass

    @property
    def defense(self) -> int:
        if self.parent.equipment.something_is_equipped():
            equipment_defense = self.parent.equipment.defense_bonus
            bonus = self.defense_bonus
            return equipment_defense + bonus
        else:
            return self.defense_bonus

    @property
    def power(self) -> int:
        if self.parent.equipment.something_is_equipped():
            # Return the power of the equipment plus the fighter's inherent power
            weapon_power = self.parent.equipment.power_bonus
            bonus = self.power_bonus
            return weapon_power + bonus
        else:
            # Return the power of the fighter's fists plus fighter's inherent power
            fist_power = self.rand_generator.randint(self.min_base_power, self.max_base_power)
            bonus = self.power_bonus
            return fist_power + bonus

    @property
    def defense_bonus(self) -> int:
        return (self.agility - 10) // 2

    @property
    def power_bonus(self) -> int:
        return (self.strength - 10) // 2

    def heal(self, amount: int) -> int:
        if self.health == self.max_health:
            return 0

        new_health_value = self.health + amount

        if new_health_value > self.max_health:
            new_health_value = self.max_health

        amount_recovered = new_health_value - self.health
        self.health = new_health_value
        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.health -= amount

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
