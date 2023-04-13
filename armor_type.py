from enum import auto, Enum

from components.skills import SkillEnum


class ArmorType(Enum):
    LIGHT_ARMOR = auto()
    MEDIUM_ARMOR = auto()
    HEAVY_ARMOR = auto()
    UNARMORED = auto()


ARMOR_TO_SKILL_MAP = {
    ArmorType.LIGHT_ARMOR: SkillEnum.LIGHT_ARMOR,
    ArmorType.MEDIUM_ARMOR: SkillEnum.MEDIUM_ARMOR,
    ArmorType.HEAVY_ARMOR: SkillEnum.HEAVY_ARMOR,
    ArmorType.UNARMORED: SkillEnum.UNARMORED
}
