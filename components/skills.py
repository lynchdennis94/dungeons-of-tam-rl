from __future__ import annotations
from enum import auto, Enum

from typing import TYPE_CHECKING
from components.base_component import BaseComponent

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
    SkillEnum.ARMORER,
    SkillEnum.ATHLETICS,
    SkillEnum.AXE,
    SkillEnum.BLOCK,
    SkillEnum.BLUNT_WEAPON,
    SkillEnum.HEAVY_ARMOR,
    SkillEnum.LONG_BLADE,
    SkillEnum.MEDIUM_ARMOR,
    SkillEnum.SPEAR
]

MAGIC_SKILLS = [
    SkillEnum.ALCHEMY,
    SkillEnum.ALTERATION,
    SkillEnum.CONJURATION,
    SkillEnum.DESTRUCTION,
    SkillEnum.ENCHANT,
    SkillEnum.ILLUSION,
    SkillEnum.MYSTICISM,
    SkillEnum.RESTORATION,
    SkillEnum.UNARMORED
]

STEALTH_SKILLS = [
    SkillEnum.ACROBATICS,
    SkillEnum.HAND_TO_HAND,
    SkillEnum.LIGHT_ARMOR,
    SkillEnum.MARKSMAN,
    SkillEnum.MERCANTILE,
    SkillEnum.SECURITY,
    SkillEnum.SHORT_BLADE,
    SkillEnum.SNEAK,
    SkillEnum.SPEECHCRAFT
]


class Skills(BaseComponent):
    parent: Actor
    skill_map = {}

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
        self.skill_map[SkillEnum.HEAVY_ARMOR] = ("Heavy Armor", heavy_armor)
        self.skill_map[SkillEnum.MEDIUM_ARMOR] = ("Medium Armor", medium_armor)
        self.skill_map[SkillEnum.SPEAR] = ("Spear", spear)
        self.skill_map[SkillEnum.ACROBATICS] = ("Acrobatics", acrobatics)
        self.skill_map[SkillEnum.ARMORER] = ("Armorer", armorer)
        self.skill_map[SkillEnum.AXE] = ("Axe", axe)
        self.skill_map[SkillEnum.BLUNT_WEAPON] = ("Blunt Weapon", blunt_weapon)
        self.skill_map[SkillEnum.LONG_BLADE] = ("Long Blade", long_blade)
        self.skill_map[SkillEnum.BLOCK] = ("Block", block)
        self.skill_map[SkillEnum.LIGHT_ARMOR] = ("Light Armor", light_armor)
        self.skill_map[SkillEnum.MARKSMAN] = ("Marksman", marksman)
        self.skill_map[SkillEnum.SNEAK] = ("Sneak", sneak)
        self.skill_map[SkillEnum.ATHLETICS] = ("Athletics", athletics)
        self.skill_map[SkillEnum.HAND_TO_HAND] = ("Hand-to-Hand", hand_to_hand)
        self.skill_map[SkillEnum.SHORT_BLADE] = ("Short Blade", short_blade)
        self.skill_map[SkillEnum.UNARMORED] = ("Unarmored", unarmored)
        self.skill_map[SkillEnum.ILLUSION] = ("Illusion", illusion)
        self.skill_map[SkillEnum.MERCANTILE] = ("Mercantile", mercantile)
        self.skill_map[SkillEnum.SPEECHCRAFT] = ("Speechcraft", speechcraft)
        self.skill_map[SkillEnum.ALCHEMY] = ("Alchemy", alchemy)
        self.skill_map[SkillEnum.CONJURATION] = ("Conjuration", conjuration)
        self.skill_map[SkillEnum.ENCHANT] = ("Enchant", enchant)
        self.skill_map[SkillEnum.SECURITY] = ("Security", security)
        self.skill_map[SkillEnum.ALTERATION] = ("Alteration", alteration)
        self.skill_map[SkillEnum.DESTRUCTION] = ("Destruction", destruction)
        self.skill_map[SkillEnum.MYSTICISM] = ("Mysticism", mysticism)
        self.skill_map[SkillEnum.RESTORATION] = ("Restoration", restoration)
