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

    def __init__(self, hp: int, base_defense: int, min_base_power: int, max_base_power: int, strength: int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense = base_defense
        self.min_base_power = min_base_power
        self.max_base_power = max_base_power
        self.strength = strength
        self.rand_generator = Random()

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    @property
    def defense(self) -> int:
        return self.base_defense + self.defense_bonus

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
        if self.parent.equipment:
            return self.parent.equipment.defense_bonus
        else:
            return 0

    @property
    def power_bonus(self) -> int:
        return (self.strength - 10) // 2

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp
        self.hp = new_hp_value
        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount

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
