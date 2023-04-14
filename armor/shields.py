from components.equippable import Equippable
from equipment_types import EquipmentType
from armor_type import ArmorType


class ChitinShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=10)


class GlassShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=50)


class NetchLeatherShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class NordicLeatherShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class ChitinTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=12)


class GlassTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=55)


class NetchLeatherTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.LIGHT_ARMOR,
            defense_bonus=5)


class BonemoldShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=15)


class DreughShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=40)


class IndorilShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=45)


class BonemoldTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class DragonscaleTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=22)


class OrcishTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=32)


class HlaaluGuardShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class RedoranGuardShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class TelvanniGuardShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.MEDIUM_ARMOR,
            defense_bonus=17)


class DaedricShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class DwemerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=20)


class EbonyShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class IronShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=10)


class NordicTrollboneShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)


class SteelShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=15)


class DaedricTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=80)


class EbonyTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=60)


class ImperialShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=16)


class IronTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=12)


class SteelTowerShield(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.SHIELD,
            armor_type=ArmorType.HEAVY_ARMOR,
            defense_bonus=18)