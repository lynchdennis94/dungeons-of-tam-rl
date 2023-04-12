from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.primary_attributes import PrimaryAttributes
from components.inventory import Inventory
from components.level import Level
from components.skills import Skills
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    eyesight_radius=8,
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(),
    primary_attributes=PrimaryAttributes(
        strength=50,
        intelligence=50,
        willpower=50,
        agility=50,
        speed=50,
        endurance=50,
        personality=50,
        luck=50),
    skills=Skills(
        heavy_armor=50,
        medium_armor=50,
        spear=50,
        acrobatics=50,
        armorer=50,
        axe=50,
        blunt_weapon=50,
        long_blade=50,
        block=50,
        light_armor=50,
        marksman=50,
        sneak=50,
        athletics=50,
        hand_to_hand=100,
        short_blade=50,
        unarmored=50,
        illusion=50,
        mercantile=50,
        speechcraft=50,
        alchemy=50,
        conjuration=50,
        enchant=50,
        security=50,
        alteration=50,
        destruction=50,
        mysticism=50,
        restoration=50),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    eyesight_radius=8,
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(),
    primary_attributes=PrimaryAttributes(
        strength=50,
        intelligence=50,
        willpower=50,
        agility=50,
        speed=50,
        endurance=50,
        personality=50,
        luck=50),
    skills=Skills(
        heavy_armor=50,
        medium_armor=50,
        spear=50,
        acrobatics=50,
        armorer=50,
        axe=50,
        blunt_weapon=50,
        long_blade=50,
        block=50,
        light_armor=50,
        marksman=50,
        sneak=50,
        athletics=50,
        hand_to_hand=50,
        short_blade=50,
        unarmored=50,
        illusion=50,
        mercantile=50,
        speechcraft=50,
        alchemy=50,
        conjuration=50,
        enchant=50,
        security=50,
        alteration=50,
        destruction=50,
        mysticism=50,
        restoration=50),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35)
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    eyesight_radius=9,
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(),
    primary_attributes=PrimaryAttributes(
        strength=50,
        intelligence=50,
        willpower=50,
        agility=50,
        speed=50,
        endurance=50,
        personality=50,
        luck=50),
    skills=Skills(
        heavy_armor=50,
        medium_armor=50,
        spear=50,
        acrobatics=50,
        armorer=50,
        axe=50,
        blunt_weapon=50,
        long_blade=50,
        block=50,
        light_armor=50,
        marksman=50,
        sneak=50,
        athletics=50,
        hand_to_hand=50,
        short_blade=50,
        unarmored=50,
        illusion=50,
        mercantile=50,
        speechcraft=50,
        alchemy=50,
        conjuration=50,
        enchant=50,
        security=50,
        alteration=50,
        destruction=50,
        mysticism=50,
        restoration=50),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100)
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4)
)

scroll_of_lightning = Item(
    char="~",
    color=(255, 255, 0),
    name="Scroll of Lightning",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5)
)

scroll_of_confusion = Item(
    char="~",
    color=(207, 63, 255),
    name="Scroll of Confusion",
    consumable=consumable.ConfusionConsumable(number_of_turns=10)
)

scroll_of_fireball = Item(
    char="~",
    color=(255, 0, 0),
    name="Scroll of Fireball",
    consumable=consumable.FireballConsumable(damage=12, radius=3)
)

dagger = Item(
    char="/",
    color=(0, 191, 255),
    name="Dagger",
    equippable=equippable.Dagger()
)

sword = Item(
    char="/",
    color=(0, 191, 255),
    name="Sword",
    equippable=equippable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor()
)

chain_mail = Item(
    char="[",
    color=(139, 69, 19),
    name="Chain Mail",
    equippable=equippable.ChainMail()
)
