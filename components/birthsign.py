from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributesEnum

if TYPE_CHECKING:
    from entity import Actor


class Birthsign(BaseComponent):
    parent: Actor

    def __init__(self, name: str):
        self.name = name

    def apply_abilities(self):
        pass

    def add_spell(self):
        pass  # TODO: Add spells

    def add_power(self):
        pass  # TODO: Add powers


class WarriorBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Warrior")

    def apply_abilities(self):
        self.parent.fighter.fortify_attack = 10


class MageBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Mage")

    def apply_abilities(self):
        self.parent.primary_attributes.max_magicka += 0.5 * self.parent.primary_attributes.intelligence


class ThiefBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Thief")

    def apply_abilities(self):
        self.parent.fighter.sanctuary = 10


class SerpentBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Serpent")

    def add_spells(self):
        pass  # TODO: Add spell


class LadyBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Lady")

    def apply_abilities(self):
        self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.PERSONALITY][1] += 25
        self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.ENDURANCE][1] += 25


class SteedBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Steed")

    def apply_abilities(self):
        self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.SPEED][1] += 25


class LordBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Lord")

    def apply_abilities(self):
        pass  # TODO: Add ability after adding resistance support

    def add_spell(self):
        pass  # TODO: Add spell


class ApprenticeBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Apprentice")

    def apply_abilities(self):
        self.parent.primary_attributes.max_magicka += 1.5 * self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.INTELLIGENCE][1]
        # TODO: Add in additional ability after resistance support added


class AtronachBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Atronach")

    def apply_abilities(self):
        self.parent.primary_attributes.max_magicka += 2.0 * self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.INTELLIGENCE][1]
        # TODO: Add in additional ability after resistance support added for spell absorbtion, stunted magicka


class RitualBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Ritual")

    def add_spells(self):
        pass  # TODO: Add spell

    def add_power(self):
        pass  # TODO: Add power


class LoverBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Lover")

    def apply_abilities(self):
        self.parent.primary_attributes.primary_attribute_map[PrimaryAttributesEnum.AGILITY][1] += 25

    def add_power(self):
        pass  # TODO: Add power


class ShadowBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Shadow")

    def add_power(self):
        pass  # TODO: Add power


class TowerBirthsign(Birthsign):
    def __init__(self):
        super().__init__("The Tower")

    def add_spell(self):
        pass  # TODO: Add spell

    def add_power(self):
        pass  # TODO: Add power


BIRTHSIGN_LIST = [
    WarriorBirthsign(),
    MageBirthsign(),
    ThiefBirthsign(),
    SerpentBirthsign(),
    LadyBirthsign(),
    SteedBirthsign(),
    LordBirthsign(),
    ApprenticeBirthsign(),
    AtronachBirthsign(),
    RitualBirthsign(),
    LoverBirthsign(),
    ShadowBirthsign(),
    TowerBirthsign()
]
