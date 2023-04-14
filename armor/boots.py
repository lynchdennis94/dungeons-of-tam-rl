from components.equippable import Equippable
from equipment_types import EquipmentType
from armor_type import ArmorType


class ChitinBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class GlassBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class HeavyLeatherBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NetchLeatherBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class BonemoldBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class IndorilBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class OrishBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class DaedricBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class DwemerBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class EbonyBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class ImperialSteelBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class ImperialTemplarBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class IronBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class SteelBoots(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.BOOTS,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)