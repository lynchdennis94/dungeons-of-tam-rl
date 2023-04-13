from __future__ import annotations

from typing import TYPE_CHECKING

from armor_type import ArmorType
from components.base_component import BaseComponent
from equipment_types import EquipmentType
from weapon_types import WeaponType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
            self,
            equipment_type: EquipmentType,
            weapon_type: WeaponType = None,
            armor_type: ArmorType = None,
            min_power: int = 0,
            max_power: int = 0,
            defense_bonus: int = 0
    ):
        self.equipment_type = equipment_type
        self.weapon_type = weapon_type
        self.armor_type = armor_type
        self.min_power = min_power
        self.max_power = max_power
        self.defense_bonus = defense_bonus


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=1,
            max_power=6)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=2,
            max_power=12)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.CUIRASS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.CUIRASS,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=3)
