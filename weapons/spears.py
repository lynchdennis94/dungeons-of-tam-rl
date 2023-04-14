from components.equippable import Equippable
from equipment_types import EquipmentType
from weapon_types import WeaponType


class ChitinSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=13)


class IronSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=6,
            max_power=15)


class IronLongSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=20)


class SteelSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=6,
            max_power=17)


class IronHalberd(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=20)


class SteelHalberd(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=23)


class SilverSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=23)


class DwarvenSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=21)


class DwarvenHalberd(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=28)


class EbonySpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=32)


class GlassHalberd(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=5,
            max_power=38)


class DaedricSpear(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.SPEARS,
            min_power=6,
            max_power=40)