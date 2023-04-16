import math
from typing import Tuple, List

import colors
from components.equippable import Equippable
from entity import Item
from equipment_types import EquipmentType
from armor_type import ArmorType


class ArmorMaterialConstructor:
    def __init__(self,
                 name: str,
                 color: Tuple,
                 armor_type: ArmorType,
                 defense_multiplier: float):
        self.name = name
        self.color = color
        self.armor_type = armor_type
        self.defense_multiplier = defense_multiplier


class ArmorTypeConstructor:
    def __init__(self,
                 name: str,
                 glyph: str,
                 equipment_type: EquipmentType):
        self.name = name
        self.glyph = glyph
        self.equipment_type = equipment_type


def build_armor_from_constructors(
        armor_type_constructor: ArmorTypeConstructor,
        armor_material_constructor: ArmorMaterialConstructor) -> Item:
    return Item(
        char=armor_type_constructor.glyph,
        color=armor_material_constructor.color,
        name=f"{armor_material_constructor.name} {armor_type_constructor.name}",
        equippable=Equippable(
            equipment_type=armor_type_constructor.equipment_type,
            armor_type=armor_material_constructor.armor_type,
            defense_bonus=math.floor(
                5 * armor_material_constructor.defense_multiplier)
        )
    )


def initialize_base_armors(armor_material_constructor: ArmorMaterialConstructor) -> List[Item]:
    result = []
    for armor_type_constructor in ARMOR_TYPE_CONSTRUCTORS:
        result.append(build_armor_from_constructors(armor_type_constructor, armor_material_constructor))

    return result


'''Armor constructors'''

cuirass_constructor = ArmorTypeConstructor(
    name="Cuirass",
    glyph='\u256b',
    equipment_type=EquipmentType.CUIRASS
)

helmet_constructor = ArmorTypeConstructor(
    name="Helmet",
    glyph='\u2229',
    equipment_type=EquipmentType.HELMET
)

left_pauldron_constructor = ArmorTypeConstructor(
    name="Left Pauldron",
    glyph='^',
    equipment_type=EquipmentType.LEFT_PAULDRON
)


right_pauldron_constructor = ArmorTypeConstructor(
    name="Right Pauldron",
    glyph='^',
    equipment_type=EquipmentType.RIGHT_PAULDRON
)


greaves_constructor = ArmorTypeConstructor(
    name="Greaves",
    glyph='\u2565',
    equipment_type=EquipmentType.GREAVES
)


boots_constructor = ArmorTypeConstructor(
    name="Boots",
    glyph='\u03c0',
    equipment_type=EquipmentType.BOOTS
)


left_gauntlet_constructor = ArmorTypeConstructor(
    name="Left Gauntlet",
    glyph='\u03b1',
    equipment_type=EquipmentType.LEFT_HAND
)


right_gauntlet_constructor = ArmorTypeConstructor(
    name="Right Gauntlet",
    glyph='\u03b1',
    equipment_type=EquipmentType.RIGHT_HAND
)

shield_constructor = ArmorTypeConstructor(
    name="Shield",
    glyph='\u0398',
    equipment_type=EquipmentType.SHIELD
)

'''Material Constructors'''
netch_leather_material_constructor = ArmorMaterialConstructor(
    name="Netch Leather",
    color=colors.NETCH_LEATHER_COLOR,
    armor_type=ArmorType.LIGHT_ARMOR,
    defense_multiplier=1
)

chitin_material_constructor = ArmorMaterialConstructor(
    name="Chitin",
    color=colors.CHITIN_COLOR,
    armor_type=ArmorType.LIGHT_ARMOR,
    defense_multiplier=2
)

dreugh_leather_constructor = ArmorMaterialConstructor(
    name="Dreugh Leather",
    color=colors.DREUGH_COLOR,
    armor_type=ArmorType.LIGHT_ARMOR,
    defense_multiplier=8
)

glass_material_constructor = ArmorMaterialConstructor(
    name="Glass",
    color=colors.GLASS_COLOR,
    armor_type=ArmorType.LIGHT_ARMOR,
    defense_multiplier=10
)

bonemold_material_constructor = ArmorMaterialConstructor(
    name="Bonemold",
    color=colors.BONEMOLD_COLOR,
    armor_type=ArmorType.MEDIUM_ARMOR,
    defense_multiplier=3
)

chain_material_constructor = ArmorMaterialConstructor(
    name="Chain",
    color=colors.CHAIN_COLOR,
    armor_type=ArmorType.MEDIUM_ARMOR,
    defense_multiplier=4
)

orcish_material_constructor = ArmorMaterialConstructor(
    name="Orcish",
    color=colors.ORCISH_COLOR,
    armor_type=ArmorType.MEDIUM_ARMOR,
    defense_multiplier=6
)

indoril_material_constructor = ArmorMaterialConstructor(
    name="Indoril",
    color=colors.INDORIL_COLOR,
    armor_type=ArmorType.MEDIUM_ARMOR,
    defense_multiplier=9
)

iron_material_constructor = ArmorMaterialConstructor(
    name="Iron",
    color=colors.IRON_COLOR,
    armor_type=ArmorType.HEAVY_ARMOR,
    defense_multiplier=2
)

steel_material_constructor = ArmorMaterialConstructor(
    name="Steel",
    color=colors.STEEL_COLOR,
    armor_type=ArmorType.HEAVY_ARMOR,
    defense_multiplier=3
)

dwemer_material_constructor = ArmorMaterialConstructor(
    name="Dwemer",
    color=colors.DWEMER_COLOR,
    armor_type=ArmorType.HEAVY_ARMOR,
    defense_multiplier=4
)

ebony_material_constructor = ArmorMaterialConstructor(
    name="Ebony",
    color=colors.EBONY_COLOR,
    armor_type=ArmorType.HEAVY_ARMOR,
    defense_multiplier=12
)

daedric_material_constructor = ArmorMaterialConstructor(
    name="Daedric",
    color=colors.DAEDRIC_COLOR,
    armor_type=ArmorType.HEAVY_ARMOR,
    defense_multiplier=16
)

ARMOR_TYPE_CONSTRUCTORS = [
    cuirass_constructor,
    helmet_constructor,
    left_pauldron_constructor,
    right_pauldron_constructor,
    greaves_constructor,
    boots_constructor,
    left_gauntlet_constructor,
    right_gauntlet_constructor,
    shield_constructor
]

NETCH_LEATHER_ARMOR = initialize_base_armors(netch_leather_material_constructor)

CHITIN_ARMOR = initialize_base_armors(chitin_material_constructor)

DREUGH_LEATHER_ARMOR = initialize_base_armors(dreugh_leather_constructor)

GLASS_ARMOR = initialize_base_armors(glass_material_constructor)

BONEMOLD_ARMOR = initialize_base_armors(bonemold_material_constructor)

CHAIN_ARMOR = initialize_base_armors(chain_material_constructor)

ORCISH_ARMOR = initialize_base_armors(orcish_material_constructor)

INDORIL_ARMOR = initialize_base_armors(indoril_material_constructor)

IRON_ARMOR = initialize_base_armors(iron_material_constructor)

STEEL_ARMOR = initialize_base_armors(steel_material_constructor)

DWEMER_ARMOR = initialize_base_armors(dwemer_material_constructor)

EBONY_ARMOR = initialize_base_armors(ebony_material_constructor)

DAEDRIC_ARMOR = initialize_base_armors(daedric_material_constructor)



