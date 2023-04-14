from components.equippable import Equippable
from equipment_types import EquipmentType
from armor_type import ArmorType


class ChitinLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class ChitinRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class GlassLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class GlassRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class NetchLeatherLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NetchLeatherRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicFurRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class BonemoldLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class BonemoldRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class ArmunAnBonemoldLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class ArmunAnBonemoldRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class GahJulanBonemoldLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class GahJulanBonemoldRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class IndorilLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class IndorilRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class OrcishLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class OrcishRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=30)


class DwemerLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class DwemerRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class DaedricLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class DaedricRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class EbonyLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class EbonyRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class ImperialChainLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class ImperialChainRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class ImperialSteelLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class ImperialSteelRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class ImperialTemplarLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class ImperialTemplarRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class IronLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class IronRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class SteelLeftPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.LEFT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)


class SteelRightPauldron(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.RIGHT_PAULDRON,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)