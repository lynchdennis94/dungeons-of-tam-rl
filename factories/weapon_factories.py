import math
from typing import Tuple, List

import colors
from components.equippable import Equippable
from entity import Item
from equipment_types import EquipmentType
from weapon_types import WeaponType


class WeaponMaterialConstructor:
    def __init__(self,
                 name: str,
                 color: Tuple,
                 min_power_multiplier: float,
                 max_power_multiplier: float):
        self.name = name
        self.color = color
        self.min_power_multiplier = min_power_multiplier
        self.max_power_multiplier = max_power_multiplier


class WeaponTypeConstructor:
    def __init__(self,
                 name: str,
                 glyph: str,
                 equipment_type: EquipmentType,
                 weapon_type: WeaponType,
                 min_power_base: int,
                 max_power_base: int):
        self.name = name
        self.glyph = glyph
        self.equipment_type = equipment_type
        self.weapon_type = weapon_type
        self.min_power_base = min_power_base
        self.max_power_base = max_power_base


def build_weapon_from_constructors(
        weapon_type_constructor: WeaponTypeConstructor,
        weapon_material_constructor: WeaponMaterialConstructor) -> Item:
    return Item(
        char=weapon_type_constructor.glyph,
        color=weapon_material_constructor.color,
        name=f"{weapon_material_constructor.name} {weapon_type_constructor.name}",
        equippable=Equippable(
            equipment_type=weapon_type_constructor.equipment_type,
            weapon_type=weapon_type_constructor.weapon_type,
            min_power=math.floor(
                weapon_type_constructor.min_power_base * weapon_material_constructor.min_power_multiplier),
            max_power=math.floor(
                weapon_type_constructor.max_power_base * weapon_material_constructor.max_power_multiplier)
        )
    )


def initialize_base_weapons(weapon_material_constructor: WeaponMaterialConstructor) -> List[Item]:
    result = []
    for weapon_type_constructor in WEAPON_TYPE_CONSTRUCTORS:
        result.append(build_weapon_from_constructors(weapon_type_constructor[0], weapon_material_constructor))

    return result


'''Weapon Constructors'''
war_axe_constructor = WeaponTypeConstructor(
    name="War Axe",
    glyph='\u2191',
    equipment_type=EquipmentType.ONE_HANDED_WEAPON,
    weapon_type=WeaponType.AXES,
    min_power_base=1,
    max_power_base=11),

battle_axe_constructor = WeaponTypeConstructor(
    name="Battle Axe",
    glyph='\u2191',
    equipment_type=EquipmentType.TWO_HANDED_WEAPON,
    weapon_type=WeaponType.AXES,
    min_power_base=1,
    max_power_base=20),

club_constructor = WeaponTypeConstructor(
    name="Club",
    glyph='\u00B6',
    equipment_type=EquipmentType.ONE_HANDED_WEAPON,
    weapon_type=WeaponType.BLUNT_WEAPONS,
    min_power_base=2,
    max_power_base=3),

warhammer_constructor = WeaponTypeConstructor(
    name="Warhammer",
    glyph='\u00B6',
    equipment_type=EquipmentType.TWO_HANDED_WEAPON,
    weapon_type=WeaponType.BLUNT_WEAPONS,
    min_power_base=1,
    max_power_base=18),

dagger_constructor = WeaponTypeConstructor(
    name="Dagger",
    glyph='`',
    equipment_type=EquipmentType.ONE_HANDED_WEAPON,
    weapon_type=WeaponType.SHORT_BLADES,
    min_power_base=2,
    max_power_base=3),

shortsword_constructor = WeaponTypeConstructor(
    name="Shortsword",
    glyph='`',
    equipment_type=EquipmentType.ONE_HANDED_WEAPON,
    weapon_type=WeaponType.SHORT_BLADES,
    min_power_base=3,
    max_power_base=7),

longsword_constructor = WeaponTypeConstructor(
    name="Longsword",
    glyph='\\',
    equipment_type=EquipmentType.ONE_HANDED_WEAPON,
    weapon_type=WeaponType.LONG_BLADES,
    min_power_base=1,
    max_power_base=12),

claymore_constructor = WeaponTypeConstructor(
    name="Claymore",
    glyph='\\',
    equipment_type=EquipmentType.TWO_HANDED_WEAPON,
    weapon_type=WeaponType.LONG_BLADES,
    min_power_base=1,
    max_power_base=15),

spear_constructor = WeaponTypeConstructor(
    name="Spear",
    glyph='\u2192',
    equipment_type=EquipmentType.TWO_HANDED_WEAPON,
    weapon_type=WeaponType.SPEARS,
    min_power_base=2,
    max_power_base=12),

'''Material Constructors'''
chitin_material_constructor = WeaponMaterialConstructor(
    name="Chitin",
    color=colors.CHITIN_COLOR,
    min_power_multiplier=1,
    max_power_multiplier=1
)

iron_material_constructor = WeaponMaterialConstructor(
    name="Iron",
    color=colors.IRON_COLOR,
    min_power_multiplier=1.1,
    max_power_multiplier=1.6
)

steel_material_constructor = WeaponMaterialConstructor(
    name="Steel",
    color=colors.STEEL_COLOR,
    min_power_multiplier=1.2,
    max_power_multiplier=2
)

imperial_material_constructor = WeaponMaterialConstructor(
    name="Imperial",
    color=colors.IMPERIAL_COLOR,
    min_power_multiplier=1.4,
    max_power_multiplier=2.2
)

nordic_material_constructor = WeaponMaterialConstructor(
    name="Nordic",
    color=colors.NORDIC_COLOR,
    min_power_multiplier=1.6,
    max_power_multiplier=2.4
)

silver_material_constructor = WeaponMaterialConstructor(
    name="Silver",
    color=colors.SILVER_COLOR,
    min_power_multiplier=1.8,
    max_power_multiplier=2.6
)

dwemer_material_constructor = WeaponMaterialConstructor(
    name="Dwemer",
    color=colors.DWEMER_COLOR,
    min_power_multiplier=2,
    max_power_multiplier=2.8
)

glass_material_constructor = WeaponMaterialConstructor(
    name="Glass",
    color=colors.GLASS_COLOR,
    min_power_multiplier=2.2,
    max_power_multiplier=3
)

ebony_material_constructor = WeaponMaterialConstructor(
    name="Ebony",
    color=colors.EBONY_COLOR,
    min_power_multiplier=2.5,
    max_power_multiplier=3.5
)

daedric_material_constructor = WeaponMaterialConstructor(
    name="Daedric",
    color=colors.DAEDRIC_COLOR,
    min_power_multiplier=2.8,
    max_power_multiplier=4
)

WEAPON_TYPE_CONSTRUCTORS = [
    war_axe_constructor,
    battle_axe_constructor,
    club_constructor,
    warhammer_constructor,
    dagger_constructor,
    shortsword_constructor,
    longsword_constructor,
    claymore_constructor,
    spear_constructor
]

CHITIN_WEAPONS = initialize_base_weapons(chitin_material_constructor)

IRON_WEAPONS = initialize_base_weapons(iron_material_constructor)

STEEL_WEAPONS = initialize_base_weapons(steel_material_constructor)

IMPERIAL_WEAPONS = initialize_base_weapons(imperial_material_constructor)

NORDIC_WEAPONS = initialize_base_weapons(nordic_material_constructor)

SILVER_WEAPONS = initialize_base_weapons(silver_material_constructor)

DWEMER_WEAPONS = initialize_base_weapons(dwemer_material_constructor)

GLASS_WEAPONS = initialize_base_weapons(glass_material_constructor)

EBONY_WEAPONS = initialize_base_weapons(ebony_material_constructor)

DAEDRIC_WEAPONS = initialize_base_weapons(daedric_material_constructor)
