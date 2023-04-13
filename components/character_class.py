from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List

from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributesEnum
from components.skills import SkillEnum, STEALTH_SKILLS, COMBAT_SKILLS, MAGIC_SKILLS

if TYPE_CHECKING:
    from entity import Actor


class CharacterClass(BaseComponent):
    parent: Actor
    skill_level_factors: Dict

    def __init__(self,
                 name: str,
                 major_skills: List[SkillEnum],
                 minor_skills: List[SkillEnum],
                 specialization_skills: List[SkillEnum],
                 favored_attributes: List[PrimaryAttributesEnum]
                 ):
        self.name = name
        self.major_skills_list = major_skills
        self.minor_skills_list = minor_skills
        self.specialization_skills_list = specialization_skills
        self.favored_attributes_list = favored_attributes
        self.skill_level_factors = {}

    def set_skill_level_factor_weights(self):
        # Initialize the factors map
        for skill in SkillEnum:
            self.skill_level_factors[skill] = 1.25

        # Overwrite the major, minor, and specialized skills
        for skill in self.major_skills_list:
            self.skill_level_factors[skill] = 0.75
        for skill in self.specialization_skills_list:
            self.skill_level_factors[skill] = 0.8
        for skill in self.minor_skills_list:
            self.skill_level_factors[skill] = 1.0

    def set_base_skill_values(self):
        # Initialize the parent skills
        for skill in SkillEnum:
            self.parent.skills.skill_map[skill] = 5

        # Overwrite major and minor skills
        for skill in self.major_skills_list:
            self.parent.skills.skill_map[skill] = 30

        for skill in self.minor_skills_list:
            self.parent.skills.skill_map[skill] = 15

    def set_attribute_bonuses(self):
        for attribute in self.favored_attributes_list:
            self.parent.primary_attributes.primary_attribute_map[attribute] += 10


Acrobat = CharacterClass(name="Acrobat",
                         major_skills=[
                             SkillEnum.ATHLETICS,
                             SkillEnum.UNARMORED,
                             SkillEnum.ACROBATICS,
                             SkillEnum.MARKSMAN,
                             SkillEnum.SNEAK
                         ],
                         minor_skills=[
                             SkillEnum.SPEAR,
                             SkillEnum.ALTERATION,
                             SkillEnum.HAND_TO_HAND,
                             SkillEnum.LIGHT_ARMOR,
                             SkillEnum.SPEECHCRAFT
                         ],
                         specialization_skills=STEALTH_SKILLS,
                         favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.ENDURANCE])

Agent = CharacterClass(name="Agent",
                       major_skills=[
                           SkillEnum.ACROBATICS,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.SHORT_BLADE,
                           SkillEnum.SNEAK,
                           SkillEnum.SPEECHCRAFT
                       ],
                       minor_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.CONJURATION,
                           SkillEnum.ILLUSION,
                           SkillEnum.UNARMORED,
                           SkillEnum.MERCANTILE
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.PERSONALITY])

Archer = CharacterClass(name="Archer",
                       major_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN
                       ],
                       minor_skills=[
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.SPEAR,
                           SkillEnum.RESTORATION,
                           SkillEnum.UNARMORED,
                           SkillEnum.SNEAK
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.STRENGTH])

Assassin = CharacterClass(name="Assassin",
                       major_skills=[
                           SkillEnum.ACROBATICS,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN,
                           SkillEnum.SHORT_BLADE,
                           SkillEnum.SNEAK
                       ],
                       minor_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.ALCHEMY,
                           SkillEnum.SECURITY
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.INTELLIGENCE, PrimaryAttributesEnum.SPEED])

Barbarian = CharacterClass(name="Barbarian",
                       major_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.AXE,
                           SkillEnum.BLOCK,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.MEDIUM_ARMOR
                       ],
                       minor_skills=[
                           SkillEnum.ARMORER,
                           SkillEnum.UNARMORED,
                           SkillEnum.ACROBATICS,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.SPEED, PrimaryAttributesEnum.STRENGTH])

Bard = CharacterClass(name="Bard",
                       major_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.ALCHEMY,
                           SkillEnum.ACROBATICS,
                           SkillEnum.SPEECHCRAFT
                       ],
                       minor_skills=[
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.ENCHANT,
                           SkillEnum.ILLUSION,
                           SkillEnum.MERCANTILE,
                           SkillEnum.SECURITY
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.INTELLIGENCE, PrimaryAttributesEnum.PERSONALITY])

Battlemage = CharacterClass(name="Battlemage",
                       major_skills=[
                           SkillEnum.AXE,
                           SkillEnum.HEAVY_ARMOR,
                           SkillEnum.ALTERATION,
                           SkillEnum.CONJURATION,
                           SkillEnum.DESTRUCTION
                       ],
                       minor_skills=[
                           SkillEnum.LONG_BLADE,
                           SkillEnum.ALCHEMY,
                           SkillEnum.ENCHANT,
                           SkillEnum.MYSTICISM,
                           SkillEnum.MARKSMAN
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.INTELLIGENCE, PrimaryAttributesEnum.STRENGTH])

Crusader = CharacterClass(name="Crusader",
                       major_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.HEAVY_ARMOR,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.DESTRUCTION
                       ],
                       minor_skills=[
                           SkillEnum.ARMORER,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.ALCHEMY,
                           SkillEnum.RESTORATION,
                           SkillEnum.HAND_TO_HAND
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.STRENGTH])

Healer = CharacterClass(name="Healer",
                       major_skills=[
                           SkillEnum.ALTERATION,
                           SkillEnum.MYSTICISM,
                           SkillEnum.RESTORATION,
                           SkillEnum.HAND_TO_HAND,
                           SkillEnum.SPEECHCRAFT
                       ],
                       minor_skills=[
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.ALCHEMY,
                           SkillEnum.ILLUSION,
                           SkillEnum.UNARMORED,
                           SkillEnum.HAND_TO_HAND
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.PERSONALITY, PrimaryAttributesEnum.WILLPOWER])

Knight = CharacterClass(name="Knight",
                       major_skills=[
                           SkillEnum.AXE,
                           SkillEnum.BLOCK,
                           SkillEnum.HEAVY_ARMOR,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.SPEECHCRAFT
                       ],
                       minor_skills=[
                           SkillEnum.ARMORER,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.ENCHANT,
                           SkillEnum.RESTORATION,
                           SkillEnum.MERCANTILE
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.PERSONALITY, PrimaryAttributesEnum.STRENGTH])

Mage = CharacterClass(name="Mage",
                       major_skills=[
                           SkillEnum.ALTERATION,
                           SkillEnum.DESTRUCTION,
                           SkillEnum.ILLUSION,
                           SkillEnum.MYSTICISM,
                           SkillEnum.RESTORATION
                       ],
                       minor_skills=[
                           SkillEnum.ALCHEMY,
                           SkillEnum.CONJURATION,
                           SkillEnum.ENCHANT,
                           SkillEnum.UNARMORED,
                           SkillEnum.SHORT_BLADE
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.INTELLIGENCE, PrimaryAttributesEnum.WILLPOWER])

Monk = CharacterClass(name="Monk",
                       major_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.UNARMORED,
                           SkillEnum.ACROBATICS,
                           SkillEnum.HAND_TO_HAND,
                           SkillEnum.SNEAK
                       ],
                       minor_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.RESTORATION,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.WILLPOWER])

Nightblade = CharacterClass(name="Nightblade",
                       major_skills=[
                           SkillEnum.ALTERATION,
                           SkillEnum.ILLUSION,
                           SkillEnum.MYSTICISM,
                           SkillEnum.SHORT_BLADE,
                           SkillEnum.SNEAK
                       ],
                       minor_skills=[
                           SkillEnum.DESTRUCTION,
                           SkillEnum.UNARMORED,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN,
                           SkillEnum.SECURITY
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.SPEED, PrimaryAttributesEnum.WILLPOWER])

Pilgrim = CharacterClass(name="Pilgrim",
                       major_skills=[
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.RESTORATION,
                           SkillEnum.MARKSMAN,
                           SkillEnum.MERCANTILE,
                           SkillEnum.SPEECHCRAFT
                       ],
                       minor_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.ALCHEMY,
                           SkillEnum.ILLUSION,
                           SkillEnum.HAND_TO_HAND,
                           SkillEnum.SHORT_BLADE
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.ENDURANCE, PrimaryAttributesEnum.PERSONALITY])

Rogue = CharacterClass(name="Rogue",
                       major_skills=[
                           SkillEnum.AXE,
                           SkillEnum.HAND_TO_HAND,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MERCANTILE,
                           SkillEnum.SHORT_BLADE
                       ],
                       minor_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.SPEECHCRAFT
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.PERSONALITY, PrimaryAttributesEnum.SPEED])

Scout = CharacterClass(name="Scout",
                       major_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.SNEAK
                       ],
                       minor_skills=[
                           SkillEnum.ALCHEMY,
                           SkillEnum.ALTERATION,
                           SkillEnum.UNARMORED,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.ENDURANCE, PrimaryAttributesEnum.SPEED])

Sorcerer = CharacterClass(name="Sorcerer",
                       major_skills=[
                           SkillEnum.ALTERATION,
                           SkillEnum.CONJURATION,
                           SkillEnum.DESTRUCTION,
                           SkillEnum.ENCHANT,
                           SkillEnum.MYSTICISM
                       ],
                       minor_skills=[
                           SkillEnum.HEAVY_ARMOR,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.ILLUSION,
                           SkillEnum.MARKSMAN,
                           SkillEnum.SHORT_BLADE
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.ENDURANCE, PrimaryAttributesEnum.INTELLIGENCE])

Spellsword = CharacterClass(name="Spellsword",
                       major_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.ALTERATION,
                           SkillEnum.DESTRUCTION,
                           SkillEnum.RESTORATION
                       ],
                       minor_skills=[
                           SkillEnum.AXE,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.MEDIUM_ARMOR,
                           SkillEnum.ALCHEMY,
                           SkillEnum.ENCHANT
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.ENDURANCE, PrimaryAttributesEnum.WILLPOWER])

Thief = CharacterClass(name="Thief",
                       major_skills=[
                           SkillEnum.ACROBATICS,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.SECURITY,
                           SkillEnum.SHORT_BLADE,
                           SkillEnum.SNEAK
                       ],
                       minor_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.HAND_TO_HAND,
                           SkillEnum.MARKSMAN,
                           SkillEnum.MERCANTILE,
                           SkillEnum.SPEECHCRAFT
                       ],
                       specialization_skills=STEALTH_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.SPEED])

Warrior = CharacterClass(name="Warrior",
                       major_skills=[
                           SkillEnum.ATHLETICS,
                           SkillEnum.BLOCK,
                           SkillEnum.HEAVY_ARMOR,
                           SkillEnum.LONG_BLADE,
                           SkillEnum.MEDIUM_ARMOR
                       ],
                       minor_skills=[
                           SkillEnum.ARMORER,
                           SkillEnum.AXE,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.SPEAR,
                           SkillEnum.MARKSMAN
                       ],
                       specialization_skills=COMBAT_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.ENDURANCE, PrimaryAttributesEnum.STRENGTH])

Witchhunter = CharacterClass(name="Witchhunter",
                       major_skills=[
                           SkillEnum.ALCHEMY,
                           SkillEnum.CONJURATION,
                           SkillEnum.ENCHANT,
                           SkillEnum.LIGHT_ARMOR,
                           SkillEnum.MARKSMAN
                       ],
                       minor_skills=[
                           SkillEnum.BLOCK,
                           SkillEnum.BLUNT_WEAPON,
                           SkillEnum.MYSTICISM,
                           SkillEnum.UNARMORED,
                           SkillEnum.SNEAK
                       ],
                       specialization_skills=MAGIC_SKILLS,
                       favored_attributes=[PrimaryAttributesEnum.AGILITY, PrimaryAttributesEnum.INTELLIGENCE])
