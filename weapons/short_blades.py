from components.equippable import Equippable
from equipment_types import EquipmentType
from weapon_types import WeaponType


class ChitinDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=4,
            max_power=4)


class IronDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=5,
            max_power=5)


class ChitinShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=4,
            max_power=9)


class IronTanto(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=6,
            max_power=6)


class SteelDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=5,
            max_power=5)


class IronShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=7,
            max_power=11)


class IronWakizashi(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=7,
            max_power=12)


class SteelTanto(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=6,
            max_power=11)


class ImperialShortsowrd(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=6,
            max_power=10)


class SilverDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=5,
            max_power=5)


class SteelShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=7,
            max_power=12)


class SteelWakizashi(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=7,
            max_power=12)


class SilverShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=7,
            max_power=10)


class DwarvenShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=8,
            max_power=15)


class GlassDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=6,
            max_power=15)


class DaedricDagger(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=8,
            max_power=12)


class EbonyShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=15,
            max_power=25)


class DaedricTanto(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=9,
            max_power=20)


class DaedricShortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=10,
            max_power=26)


class DaedricWakizashi(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.SHORT_BLADES,
            min_power=10,
            max_power=30)
