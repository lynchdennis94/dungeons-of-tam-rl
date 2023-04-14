from components.equippable import Equippable
from equipment_types import EquipmentType
from armor_type import ArmorType


class ChitinLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class ChitinRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class ClothLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=4)


class ClothRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=4)


class LeftGlassBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class RightGlassBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class LeftLeatherBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class RightLeatherBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NetchLeatherLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NetchLeatherRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class BonemoldLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class BonemoldRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class IndorilLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class IndorilRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class OrcishLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class OrcishRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class DwemerLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class DwemerRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class EbonyLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class EbonyRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class IronLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class IronRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class ImperialTemplarLeftBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class ImperialTemplarRightBracer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class IronLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class IronRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class DaedricLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class DaedricRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class ImperialSteelLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class ImperialSteelRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class SteelLeftGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)


class SteelRightGauntlet(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_HAND,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)
