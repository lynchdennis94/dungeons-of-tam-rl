from components.equippable import Equippable
from equipment_types import EquipmentType
from weapon_types import WeaponType


class ChitinClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=3)


class IronClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=4,
            max_power=5)


class SteelClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=4,
            max_power=5)


class SpikedClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=4,
            max_power=5)


class DreughClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=7,
            max_power=8)


class DaedricClub(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=10,
            max_power=12)


class IronMace(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=12)


class SteelMace(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=14)


class DwarvenMace(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=5,
            max_power=17)


class EbonyMace(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=7,
            max_power=26)


class DaedricMace(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=30)


class IronWarhammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=28)


class SteelWarhammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=32)


class DwarvenWarhammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=39)


class OrcWarhammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=42)


class SixthHouseBellHammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=50)


class DaedricWarhammer(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=1,
            max_power=70)


class WoodenStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=6)


class SteelStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=7)


class SilverStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=7)


class DreughStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=10)


class GlassStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=12)


class EbonyStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=16)


class DaedricStaff(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.BLUNT_WEAPONS,
            min_power=3,
            max_power=16)