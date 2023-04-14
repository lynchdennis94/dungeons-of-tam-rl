import colors
from entity import Item
from armor.boots import *
from armor.cuirass import *
from armor.greaves import *
from armor.hand_armor import *
from armor.helmet import *
from armor.pauldrons import *
from armor.shields import *

'''Cuirasses'''
boiled_netch_leather_cuirass = Item(
    char='\u256b',
    color=colors.NETCH_LEATHER_COLOR,
    name="Boiled Netch Leather Cuirass",
    equippable=BoiledNetchLeatherCuirass()
)

'''Helmets'''
boiled_netch_leather_helmet = Item(
    char='\u2229',
    color=colors.NETCH_LEATHER_COLOR,
    name="Boiled Netch Leather Helm",
    equippable=BoiledNetchLeatherHelm()
)

'''Pauldrons'''
chitin_left_pauldron = Item(
    char="^",
    color=colors.CHITIN_COLOR,
    name="Chitin Left Pauldron",
    equippable=ChitinLeftPauldron()
)

'''Greaves'''
chitin_greaves = Item(
    char='\u2565',
    color=colors.CHITIN_COLOR,
    name="Chitin Greaves",
    equippable=ChitinGreaves()
)

'''Boots'''
chitin_boots = Item(
    char='\u03c0',
    color=colors.CHITIN_COLOR,
    name="Chitin Boots",
    equippable=ChitinBoots()
)

'''Gauntlets/Bracers'''
chitin_left_gauntlet = Item(
    char='\u03b1',
    color=colors.CHITIN_COLOR,
    name="Chitin Left Gauntlet",
    equippable=ChitinLeftGauntlet()
)

'''Shields'''
chitin_shield = Item(
    char='\u0398',
    color=colors.CHITIN_COLOR,
    name="Chitin Shield",
    equippable=ChitinShield()
)
