from __future__ import annotations

import math
from random import Random
from typing import TYPE_CHECKING, Optional

from armor_type import ARMOR_TO_SKILL_MAP
from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributesEnum
from components.skills import SkillEnum
from weapon_types import WeaponType, WEAPON_TO_SKILL_MAP

if TYPE_CHECKING:
    from entity import Actor, Item


class Fighter(BaseComponent):
    parent: Actor

    def __init__(self):
        self.rand_generator = Random()
        self.fortify_attack = 0
        self.sanctuary = 0

    def hit_rate(self) -> int:
        # Get the equipment type
        weapon_skill = self.parent.skills.skill_map[SkillEnum.HAND_TO_HAND][1]
        if self.parent.equipment.weapon and self.parent.equipment.weapon.equippable.weapon_type:
            weapon_skill = self.parent.skills.skill_map[WEAPON_TO_SKILL_MAP[
                self.parent.equipment.weapon.equippable.weapon_type]][1]

        agility = self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1]
        luck = self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.LUCK][1]
        current_fatigue = self.parent.primary_attributes.fatigue
        max_fatigue = self.parent.primary_attributes.max_fatigue

        return (weapon_skill + (agility / 5) + (luck / 10)) * (0.75 + 0.5 * current_fatigue / max_fatigue) + self.fortify_attack

    def evasion(self) -> int:
        agility = self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1]
        luck = self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.LUCK][1]
        current_fatigue = self.parent.primary_attributes.fatigue
        max_fatigue = self.parent.primary_attributes.max_fatigue

        return ((agility / 5) + (luck / 10)) * (0.75 + 0.5*current_fatigue/max_fatigue) + self.sanctuary  # TODO: Add a chance to block

    def armor_rating(self) -> int:
        armor_rating = 0
        armor_rating += 0.3*self._calculate_armor_rating_from_current_piece(self.parent.equipment.cuirass)
        armor_rating += 0.1*self._calculate_armor_rating_from_current_piece(self.parent.equipment.shield)
        armor_rating += 0.1*self._calculate_armor_rating_from_current_piece(self.parent.equipment.helmet)
        armor_rating += 0.1 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.greaves)
        armor_rating += 0.1 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.boots)
        armor_rating += 0.1 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.right_shoulder)
        armor_rating += 0.1 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.left_shoulder)
        armor_rating += 0.05 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.right_hand_armor)
        armor_rating += 0.05 * self._calculate_armor_rating_from_current_piece(self.parent.equipment.left_hand_armor)
        return armor_rating

    def _calculate_armor_rating_from_current_piece(self, armor_piece: Optional[Item]) -> int:
        if armor_piece:
            base_armor_rating = armor_piece.equippable.defense_bonus
            armor_skill = ARMOR_TO_SKILL_MAP[armor_piece.equippable.armor_type]
            armor_skill_value = self.parent.skills.skill_map[armor_skill][1]
            weight = 0.3
        else:
            armor_skill_value = self.parent.skills.skill_map[SkillEnum.UNARMORED][1]
            base_armor_rating = armor_skill_value
            weight = 0.0065

        return base_armor_rating * armor_skill_value * weight

    def damage(self, target_armor_rating: int) -> int:
        if self.parent.equipment.weapon and self.parent.equipment.weapon.equippable.weapon_type:
            print("Handling weapon damage")
            equippable_weapon = self.parent.equipment.weapon.equippable
            weapon_damage = self.rand_generator.randint(equippable_weapon.min_power, equippable_weapon.max_power)
            strength_modifier = (self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.STRENGTH][
                                     1] + 50) / 100
            condition_modifier = 1  # TODO: Add in weapon conditioning
            critical_hit_modifier = 1  # TODO: Add in critical hit logic
        else:
            print(f"Handling unarmed damage from {self.parent.name}")
            print(self.parent.skills.skill_map)
            weapon_damage = self.parent.skills.skill_map[SkillEnum.HAND_TO_HAND][1]  # TODO: Add in fatigue damage
            strength_modifier = 0.075
            condition_modifier = 1  # This is always 'perfect' condition
            critical_hit_modifier = 1  # TODO: Add in critical hit logic

        print(f"Weapon damage: {weapon_damage}")
        print(f"Strength modifier: {strength_modifier}")
        unaltered_damage = weapon_damage * strength_modifier * condition_modifier * critical_hit_modifier
        damage_reduction = min(1 + target_armor_rating / unaltered_damage, 4)
        return math.floor(unaltered_damage / damage_reduction)
