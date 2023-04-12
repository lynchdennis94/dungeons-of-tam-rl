from __future__ import annotations

import math
from random import Random
from typing import TYPE_CHECKING
from components.base_component import BaseComponent
from weapon_types import WeaponType

if TYPE_CHECKING:
    from entity import Actor


class Fighter(BaseComponent):
    parent: Actor
    rand_generator: Random

    def __init__(self):
        self.rand_generator = Random()

    def hit_rate(self) -> int:
        # Get the equipment type
        weapon_skill = self.parent.skills.hand_to_hand
        if self.parent.equipment.weapon:
            pass

        agility = self.parent.primary_attributes.agility
        luck = self.parent.primary_attributes.luck
        current_fatigue = self.parent.primary_attributes.fatigue
        max_fatigue = self.parent.primary_attributes.max_fatigue

        return (weapon_skill + (agility / 5) + (luck / 10)) * (0.75 + 0.5 * current_fatigue / max_fatigue)

    def evasion(self) -> int:
        agility = self.parent.primary_attributes.agility
        luck = self.parent.primary_attributes.luck
        current_fatigue = self.parent.primary_attributes.fatigue
        max_fatigue = self.parent.primary_attributes.max_fatigue

        return ((agility / 5) + (luck / 10)) * (0.75 + 0.5*current_fatigue/max_fatigue)  # TODO: Add a chance to block

    def weapon_damage(self, target_armor_rating: int) -> int:
        if self.parent.equipment.weapon:
            skill = self.parent.skills.long_blade
            strength_modifier = (self.parent.primary_attributes.strength + 50)/100
            condition_modifier = 1 # TODO: Add in weapon conditioning
            critical_hit_modifier = 1  # TODO: Add in critical hit logic
        else:
            skill = self.parent.skills.hand_to_hand
            strength_modifier = 0.075
            condition_modifier = 1  # Always in 'perfect' condition
            critical_hit_modifier = 1  # TODO: Add in critical hit logic

        damage = skill * strength_modifier * condition_modifier * critical_hit_modifier
        damage_reduction = min(1 + target_armor_rating / damage, 4)
        return math.floor(damage / damage_reduction)
