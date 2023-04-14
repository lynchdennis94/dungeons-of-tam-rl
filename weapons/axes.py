from components.equippable import Equippable
from equipment_types import EquipmentType
from weapon_types import WeaponType


class ChitinWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=11)


class IronWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=18)


class SteelAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=18)


class SilverWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=20)


class DwarvenWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=24)


class GlassWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=33)


class EbonyWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=37)


class DaedricWarAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.ONE_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=44)


class MinersPick(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=3,
            max_power=7)


class IronBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=32)


class NordicBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=30)


class SteelBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=36)


class DwarvenBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=35)


class OrcishBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=17,
            max_power=28)


class DaedricBattleAxe(Equippable):
    def __init__(self) -> None:
        super().__init__(
            equipment_type=EquipmentType.TWO_HANDED_WEAPON,
            weapon_type=WeaponType.AXES,
            min_power=1,
            max_power=80)
