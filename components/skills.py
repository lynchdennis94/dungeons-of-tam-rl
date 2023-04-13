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
