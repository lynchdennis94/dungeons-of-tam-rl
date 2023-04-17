from __future__ import annotations

import copy
from enum import auto, Enum

from typing import TYPE_CHECKING
from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributesEnum

if TYPE_CHECKING:
    from entity import Actor


class SkillEnum(Enum):
    HEAVY_ARMOR = auto()
    MEDIUM_ARMOR = auto()
    SPEAR = auto()
    ACROBATICS = auto()
    ARMORER = auto()
    AXE = auto()
    BLUNT_WEAPON = auto()
    LONG_BLADE = auto()
    BLOCK = auto()
    LIGHT_ARMOR = auto()
    MARKSMAN = auto()
    SNEAK = auto()
    ATHLETICS = auto()
    HAND_TO_HAND = auto()
    SHORT_BLADE = auto()
    UNARMORED = auto(),
    ILLUSION = auto()
    MERCANTILE = auto()
    SPEECHCRAFT = auto()
    ALCHEMY = auto()
    CONJURATION = auto()
    ENCHANT = auto()
    SECURITY = auto()
    ALTERATION = auto()
    DESTRUCTION = auto()
    MYSTICISM = auto()
    RESTORATION = auto()


COMBAT_SKILLS = [
    copy.deepcopy(SkillEnum.ARMORER),
    copy.deepcopy(SkillEnum.ATHLETICS),
    copy.deepcopy(SkillEnum.AXE),
    copy.deepcopy(SkillEnum.BLOCK),
    copy.deepcopy(SkillEnum.BLUNT_WEAPON),
    copy.deepcopy(SkillEnum.HEAVY_ARMOR),
    copy.deepcopy(SkillEnum.LONG_BLADE),
    copy.deepcopy(SkillEnum.MEDIUM_ARMOR),
    copy.deepcopy(SkillEnum.SPEAR)
]

MAGIC_SKILLS = [
    copy.deepcopy(SkillEnum.ALCHEMY),
    copy.deepcopy(SkillEnum.ALTERATION),
    copy.deepcopy(SkillEnum.CONJURATION),
    copy.deepcopy(SkillEnum.DESTRUCTION),
    copy.deepcopy(SkillEnum.ENCHANT),
    copy.deepcopy(SkillEnum.ILLUSION),
    copy.deepcopy(SkillEnum.MYSTICISM),
    copy.deepcopy(SkillEnum.RESTORATION),
    copy.deepcopy(SkillEnum.UNARMORED)
]

STEALTH_SKILLS = [
    copy.deepcopy(SkillEnum.ACROBATICS),
    copy.deepcopy(SkillEnum.HAND_TO_HAND),
    copy.deepcopy(SkillEnum.LIGHT_ARMOR),
    copy.deepcopy(SkillEnum.MARKSMAN),
    copy.deepcopy(SkillEnum.MERCANTILE),
    copy.deepcopy(SkillEnum.SECURITY),
    copy.deepcopy(SkillEnum.SHORT_BLADE),
    copy.deepcopy(SkillEnum.SNEAK),
    copy.deepcopy(SkillEnum.SPEECHCRAFT)
]

SKILL_TO_ATTRIBUTE_MAPPING = {
    SkillEnum.HEAVY_ARMOR: PrimaryAttributesEnum.ENDURANCE,
    SkillEnum.MEDIUM_ARMOR: PrimaryAttributesEnum.ENDURANCE,
    SkillEnum.SPEAR: PrimaryAttributesEnum.ENDURANCE,
    SkillEnum.ACROBATICS: PrimaryAttributesEnum.STRENGTH,
    SkillEnum.ARMORER: PrimaryAttributesEnum.STRENGTH,
    SkillEnum.AXE: PrimaryAttributesEnum.STRENGTH,
    SkillEnum.BLUNT_WEAPON: PrimaryAttributesEnum.STRENGTH,
    SkillEnum.LONG_BLADE: PrimaryAttributesEnum.STRENGTH,
    SkillEnum.BLOCK: PrimaryAttributesEnum.AGILITY,
    SkillEnum.LIGHT_ARMOR: PrimaryAttributesEnum.AGILITY,
    SkillEnum.MARKSMAN: PrimaryAttributesEnum.AGILITY,
    SkillEnum.SNEAK: PrimaryAttributesEnum.AGILITY,
    SkillEnum.ATHLETICS: PrimaryAttributesEnum.SPEED,
    SkillEnum.HAND_TO_HAND: PrimaryAttributesEnum.SPEED,
    SkillEnum.SHORT_BLADE: PrimaryAttributesEnum.SPEED,
    SkillEnum.UNARMORED: PrimaryAttributesEnum.SPEED,
    SkillEnum.ILLUSION: PrimaryAttributesEnum.PERSONALITY,
    SkillEnum.MERCANTILE: PrimaryAttributesEnum.PERSONALITY,
    SkillEnum.SPEECHCRAFT: PrimaryAttributesEnum.PERSONALITY,
    SkillEnum.ALCHEMY: PrimaryAttributesEnum.INTELLIGENCE,
    SkillEnum.CONJURATION: PrimaryAttributesEnum.INTELLIGENCE,
    SkillEnum.ENCHANT: PrimaryAttributesEnum.INTELLIGENCE,
    SkillEnum.SECURITY: PrimaryAttributesEnum.INTELLIGENCE,
    SkillEnum.ALTERATION: PrimaryAttributesEnum.WILLPOWER,
    SkillEnum.DESTRUCTION: PrimaryAttributesEnum.WILLPOWER,
    SkillEnum.MYSTICISM: PrimaryAttributesEnum.WILLPOWER,
    SkillEnum.RESTORATION: PrimaryAttributesEnum.WILLPOWER
}


class Skills(BaseComponent):
    parent: Actor

    def __init__(self, 
                 heavy_armor: int = 0,
                 medium_armor: int = 0,
                 spear: int = 0,
                 acrobatics: int = 0,
                 armorer: int = 0,
                 axe: int = 0,
                 blunt_weapon: int = 0,
                 long_blade: int = 0,
                 block: int = 0,
                 light_armor: int = 0,
                 marksman: int = 0,
                 sneak: int = 0,
                 athletics: int = 0,
                 hand_to_hand: int = 0,
                 short_blade: int = 0,
                 unarmored: int = 0,
                 illusion: int = 0,
                 mercantile: int = 0,
                 speechcraft: int = 0,
                 alchemy: int = 0,
                 conjuration: int = 0,
                 enchant: int = 0,
                 security: int = 0,
                 alteration: int = 0,
                 destruction: int = 0,
                 mysticism: int = 0,
                 restoration: int = 0):
        self.skill_map = {SkillEnum.HEAVY_ARMOR: ("Heavy Armor", heavy_armor),
                          SkillEnum.MEDIUM_ARMOR: ("Medium Armor", medium_armor), SkillEnum.SPEAR: ("Spear", spear),
                          SkillEnum.ACROBATICS: ("Acrobatics", acrobatics), SkillEnum.ARMORER: ("Armorer", armorer),
                          SkillEnum.AXE: ("Axe", axe), SkillEnum.BLUNT_WEAPON: ("Blunt Weapon", blunt_weapon),
                          SkillEnum.LONG_BLADE: ("Long Blade", long_blade), SkillEnum.BLOCK: ("Block", block),
                          SkillEnum.LIGHT_ARMOR: ("Light Armor", light_armor),
                          SkillEnum.MARKSMAN: ("Marksman", marksman), SkillEnum.SNEAK: ("Sneak", sneak),
                          SkillEnum.ATHLETICS: ("Athletics", athletics),
                          SkillEnum.HAND_TO_HAND: ("Hand-to-Hand", hand_to_hand),
                          SkillEnum.SHORT_BLADE: ("Short Blade", short_blade),
                          SkillEnum.UNARMORED: ("Unarmored", unarmored), SkillEnum.ILLUSION: ("Illusion", illusion),
                          SkillEnum.MERCANTILE: ("Mercantile", mercantile),
                          SkillEnum.SPEECHCRAFT: ("Speechcraft", speechcraft), SkillEnum.ALCHEMY: ("Alchemy", alchemy),
                          SkillEnum.CONJURATION: ("Conjuration", conjuration), SkillEnum.ENCHANT: ("Enchant", enchant),
                          SkillEnum.SECURITY: ("Security", security), SkillEnum.ALTERATION: ("Alteration", alteration),
                          SkillEnum.DESTRUCTION: ("Destruction", destruction),
                          SkillEnum.MYSTICISM: ("Mysticism", mysticism),
                          SkillEnum.RESTORATION: ("Restoration", restoration)}


class CreatureSkills(Skills):

    def __init__(self,
                 combat_skills: int = 0,
                 magic_skills: int = 0,
                 stealth_skills: int = 0):
        super().__init__()
        self.combat_skills = combat_skills
        self.magic_skills = magic_skills
        self.stealth_skills = stealth_skills

