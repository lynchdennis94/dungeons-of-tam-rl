from __future__ import annotations

import math
from typing import TYPE_CHECKING, List

import colors
from components import skills
from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributesEnum
from components.skills import SkillEnum

if TYPE_CHECKING:
    from entity import Actor


class Level(BaseComponent):
    parent: Actor

    def __init__(self, current_level: int = 1, can_level_up: bool = False):
        self.current_level = current_level
        self.can_level_up = can_level_up
        self.skill_attribute_increases = {
            PrimaryAttributesEnum.STRENGTH: 0,
            PrimaryAttributesEnum.INTELLIGENCE: 0,
            PrimaryAttributesEnum.AGILITY: 0,
            PrimaryAttributesEnum.ENDURANCE: 0,
            PrimaryAttributesEnum.WILLPOWER: 0,
            PrimaryAttributesEnum.SPEED: 0,
            PrimaryAttributesEnum.LUCK: 0,
            PrimaryAttributesEnum.PERSONALITY: 0
        }
        self.total_major_minor_skill_increases = 0
        self.skill_progress = {}

        for skill in SkillEnum:
            self.skill_progress[skill] = 0

    @property
    def requires_level_up(self) -> bool:
        return self.total_major_minor_skill_increases >= 10

    def increase_skill(self, skill_to_increase: SkillEnum, base_increase_value: float):
        # Increase the skill's progress using the formula
        skill_level = self.parent.skills.skill_map[skill_to_increase][1]
        skill_level_factor = self.parent.character_class.skill_level_factors[skill_to_increase]

        self.skill_progress[skill_to_increase] += base_increase_value / ((skill_level + 1) * skill_level_factor)

        # If enough progress made, increase the skill and add a count to the right attribute
        if self.skill_progress[skill_to_increase] > 1.0:
            name, val = self.parent.skills.skill_map[skill_to_increase]
            self.parent.skills.skill_map[skill_to_increase] = (name, val + 1)
            self.skill_attribute_increases[skills.SKILL_TO_ATTRIBUTE_MAPPING[skill_to_increase]] += 1
            self.skill_progress[skill_to_increase] = 0

            # If the skill is major/minor, increase major/minor skills towards next level
            if skill_to_increase in \
                    self.parent.character_class.minor_skills_list + self.parent.character_class.major_skills_list:
                self.total_major_minor_skill_increases += 1

            self.engine.message_log.add_message(f"{name.lower().capitalize()} increased to {val + 1}",
                                                colors.LEVEL_UP_COLOR)

        print(f"Increased skill {skill_to_increase.name}, current progress: {self.skill_progress[skill_to_increase]}")

    def increase_attribute(self, attribute_to_increase: PrimaryAttributesEnum) -> None:
        multiplier = self.get_multiplier_for_attribute(attribute_to_increase)
        self.parent.primary_attributes.primary_attribute_map[attribute_to_increase] = multiplier

    def get_multiplier_for_attribute(self, attribute_to_increase: PrimaryAttributesEnum) -> int:
        times_increased_by_skills = self.skill_attribute_increases[attribute_to_increase]

        if times_increased_by_skills == 0:
            return 1
        elif 1 <= times_increased_by_skills <= 4:
            return 2
        elif 5 <= times_increased_by_skills <= 7:
            return 3
        elif 8 <= times_increased_by_skills <= 9:
            return 4
        else:
            return 5

    def increase_level(self, attributes_to_increase: List[PrimaryAttributesEnum]) -> None:
        # Increase the level
        self.current_level += 1

        # Increase the selected attributes
        for attribute in attributes_to_increase:
            self.increase_attribute(attribute)

        # Increase health
        player_endurance = self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.ENDURANCE][1]
        self.increase_max_health(math.floor(player_endurance * 0.1))

        # Zero out major/minor count and increases counting towards next level multiplier
        self.total_major_minor_skill_increases = 0
        for attribute_enum in self.skill_attribute_increases:
            self.skill_attribute_increases[attribute_enum] = 0

    def increase_max_health(self, amount: int = 20) -> None:
        self.parent.primary_attributes.max_health += amount
        self.parent.primary_attributes.health += amount
