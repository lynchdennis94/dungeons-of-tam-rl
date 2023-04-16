from components.fighter import Fighter
from components.skills import SkillEnum
from weapon_types import WEAPON_TO_SKILL_MAP


class CreatureFighter(Fighter):
    def __init__(self, min_power: int, max_power: int):
        super().__init__()
        self.min_power = min_power
        self.max_power = max_power

    def hit_rate(self) -> int:
        if self.parent.equipment.weapon and self.parent.equipment.weapon.equippable.weapon_type:
            weapon_skill = self.parent.skills.skill_map[WEAPON_TO_SKILL_MAP[
                self.parent.equipment.weapon.equippable.weapon_type]][1]

            if SkillEnum.MARKSMAN == weapon_skill:
                return self.parent.skills.stealth_skills

        return self.parent.skills.combat_skills

    def damage(self, target_armor_rating: int) -> int:
        return self.rand_generator.randint(self.min_power, self.max_power)
