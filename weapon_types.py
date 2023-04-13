from enum import auto, Enum

from components.skills import SkillEnum


class WeaponType(Enum):
    AXES = auto()
    BLUNT_WEAPONS = auto()
    LONG_BLADES = auto()
    SHORT_BLADES = auto()
    SPEARS = auto()
    HAND_TO_HAND = auto()
    MARKSMAN = auto()


WEAPON_TO_SKILL_MAP = {
    WeaponType.AXES: SkillEnum.AXE,
    WeaponType.BLUNT_WEAPONS: SkillEnum.BLUNT_WEAPON,
    WeaponType.LONG_BLADES: SkillEnum.LONG_BLADE,
    WeaponType.SHORT_BLADES: SkillEnum.SHORT_BLADE,
    WeaponType.SPEARS: SkillEnum.SPEAR,
    WeaponType.HAND_TO_HAND: SkillEnum.HAND_TO_HAND,
    WeaponType.MARKSMAN: SkillEnum.MARKSMAN
}
