from components.equippable import Equippable
from equipment_types import EquipmentType
from armor_type import ArmorType


class ChitinGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class GlassGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class NetchLeatherGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class BonemoldGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class ImperialChainGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=20)


class OrcishGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class DaedricGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class DwemerGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class EbonyGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class ImperialSteelGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class ImperialTemplarGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class IronGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class SteelGreaves(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.GREAVES,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)
