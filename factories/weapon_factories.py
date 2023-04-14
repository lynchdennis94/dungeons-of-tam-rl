import colors
from entity import Item
from weapons.axes import *
from weapons.blunt_weapons import *
from weapons.short_blades import *
from weapons.long_blades import *
from weapons.spears import *

'''Axes'''

chitin_war_axe = Item(
    char='\u2191',
    color=colors.CHITIN_COLOR,
    name="Chitin War Axe",
    equippable=ChitinWarAxe()
)

iron_war_axe = Item(
    char='\u2191',
    color=colors.IRON_COLOR,
    name="Iron War Axe",
    equippable=IronWarAxe()
)

steel_axe = Item(
    char='\u2191',
    color=colors.STEEL_COLOR,
    name="Steel Axe",
    equippable=SteelAxe()
)

steel_war_axe = Item(
    char='\u2191',
    color=colors.STEEL_COLOR,
    name="Steel War Axe",
    equippable=SteelWarAxe()
)

silver_war_axe = Item(
    char='\u2191',
    color=colors.SILVER_COLOR,
    name="Silver War Axe",
    equippable=SilverWarAxe()
)

dwarven_war_axe = Item(
    char='\u2191',
    color=colors.DWARVEN_COLOR,
    name="Dwarven War Axe",
    equippable=DwarvenWarAxe()
)

glass_war_axe = Item(
    char='\u2191',
    color=colors.GLASS_COLOR,
    name="Glass War Axe",
    equippable=GlassWarAxe()
)

ebony_war_axe = Item(
    char='\u2191',
    color=colors.EBONY_COLOR,
    name="Ebony War Axe",
    equippable=EbonyWarAxe()
)

daedric_war_axe = Item(
    char='\u2191',
    color=colors.DAEDRIC_COLOR,
    name="Daedric War Axe",
    equippable=DaedricWarAxe()
)

miners_pick = Item(
    char='\u2191',
    color=colors.IRON_COLOR,
    name="Miner's Pick",
    equippable=MinersPick()
)

iron_battle_axe = Item(
    char='\u2191',
    color=colors.IRON_COLOR,
    name="Iron Battle Axe",
    equippable=IronBattleAxe()
)

nordic_battle_axe = Item(
    char='\u2191',
    color=colors.NORDIC_COLOR,
    name="Nordic Battle Axe",
    equippable=NordicBattleAxe()
)

steel_battle_axe = Item(
    char='\u2191',
    color=colors.STEEL_COLOR,
    name="Steel Battle Axe",
    equippable=SteelBattleAxe()
)

dwarven_battle_axe = Item(
    char='\u2191',
    color=colors.DWARVEN_COLOR,
    name="Dwarven Battle Axe",
    equippable=DwarvenBattleAxe()
)

orcish_battle_axe = Item(
    char='\u2191',
    color=colors.ORCISH_COLOR,
    name="Orcish Battle Axe",
    equippable=OrcishBattleAxe()
)

daedric_battle_axe = Item(
    char='\u2191',
    color=colors.DAEDRIC_COLOR,
    name="Daedric Battle Axe",
    equippable=DaedricBattleAxe()
)

'''Blunt Weapons'''
chitin_club = Item(
    char='\u00B6',
    color=colors.CHITIN_COLOR,
    name="Chitin Club",
    equippable=ChitinClub()
)

'''Short Blades'''
chitin_dagger = Item(
    char="`",
    color=colors.CHITIN_COLOR,
    name="Chitin Dagger",
    equippable=ChitinDagger()
)

'''Long Blades'''
iron_saber = Item(
    char="\\",
    color=colors.IRON_COLOR,
    name="Iron Saber",
    equippable=IronSaber()
)

'''Spears'''
chitin_spear = Item(
    char='\u2192',
    color=colors.CHITIN_COLOR,
    name="Chitin Spear",
    equippable=ChitinSpear()
)