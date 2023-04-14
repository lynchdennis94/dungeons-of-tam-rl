from components.equippable import Equippable
from equipment_types import EquipmentType
from weapon_types import WeaponType


class IronSaber(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=5,
            max_power=18)


class IronBroadsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=4,
            max_power=12)


class IronLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=18)


class SteelSaber(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=5,
            max_power=20)


class SteelBroadsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=4,
            max_power=14)


class ImperialBroadsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=6,
            max_power=12)


class SteelLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=20)


class NordicBroadsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=6,
            max_power=18)


class SteelKatana(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=3,
            max_power=20)


class SilverLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=20)


class GlassLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=33)


class EbonyBroadsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=4,
            max_power=26)


class EbonyLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=37)


class DaedricLongsword(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=44)


class DaedricKatana(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=3,
            max_power=44)


class IronClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=24)


class SteelClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=27)


class NordicClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=30)


class SteelDaikatana(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=27)


class SilverClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=27)


class DwarvenClaymore(Equippable):  # TODO: Treat Foeburner as separate?
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=33)


class GlassClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=45)


class DaedricClaymore(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=60)


class DaedricDaikatana(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.LONG_BLADES,
            min_power=1,
            max_power=60)