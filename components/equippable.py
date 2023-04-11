from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
            self,
            equipment_type: EquipmentType,
            min_power: int = 0,
            max_power: int = 0,
            defense_bonus: int = 0
    ):
        self.equipment_type = equipment_type
        self.min_power = min_power
        self.max_power = max_power
        self.defense_bonus = defense_bonus


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, min_power=1, max_power=6)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, min_power=2, max_power=12)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3)
