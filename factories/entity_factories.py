import colors
from components.ai import HostileEnemy
from components import consumable
from components.creature_fighter import CreatureFighter
from components.equipment import Equipment
from components.fighter import Fighter
from components.primary_attributes import PrimaryAttributes
from components.inventory import Inventory
from components.level import Level
from components.skills import Skills, CreatureSkills
from entity import Actor, Item, Bandit, Creature
from factories import weapon_factories

player = Actor(
    char="@",
    color=(255, 255, 255),
    eyesight_radius=8,
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(),
    primary_attributes=PrimaryAttributes(),
    skills=Skills(),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200)
)

bandit = Bandit(
    char="b",
    eyesight_radius=8
)

rat = Creature(
        char="r",
        color=colors.BROWN,
        eyesight_radius=8,
        name="rat",
        ai_cls=HostileEnemy,
        equipment=Equipment(),
        fighter=CreatureFighter(min_power=1, max_power=2),
        primary_attributes=PrimaryAttributes(),
        skills=CreatureSkills(combat_skills=25),
        inventory=Inventory(capacity=0),
        level=Level(xp_given=20),
        health=23,
        )

mudcrab = Creature(
        char="m",
        color=colors.DRAB,
        eyesight_radius=4,
        name="mudcrab",
        ai_cls=HostileEnemy,
        equipment=Equipment(),
        fighter=CreatureFighter(min_power=1, max_power=1),
        primary_attributes=PrimaryAttributes(),
        skills=CreatureSkills(combat_skills=20),
        inventory=Inventory(capacity=0),
        level=Level(xp_given=20),
        health=15,
        )

kagouti = Creature(
        char="k",
        color=colors.SAND,
        eyesight_radius=8,
        name="kagouti",
        ai_cls=HostileEnemy,
        equipment=Equipment(),
        fighter=CreatureFighter(min_power=4, max_power=12),
        primary_attributes=PrimaryAttributes(),
        skills=CreatureSkills(combat_skills=40),
        inventory=Inventory(capacity=0),
        level=Level(xp_given=20),
        health=45,
        )

guar = Creature(
        char="g",
        color=colors.SAND,
        eyesight_radius=8,
        name="guar",
        ai_cls=HostileEnemy,
        equipment=Equipment(),
        fighter=CreatureFighter(min_power=1, max_power=9),
        primary_attributes=PrimaryAttributes(),
        skills=CreatureSkills(combat_skills=30),
        inventory=Inventory(capacity=0),
        level=Level(xp_given=20),
        health=38,
        )

alit = Creature(
        char="a",
        color=colors.DRAB,
        eyesight_radius=8,
        name="alit",
        ai_cls=HostileEnemy,
        equipment=Equipment(),
        fighter=CreatureFighter(min_power=1, max_power=9),
        primary_attributes=PrimaryAttributes(),
        skills=CreatureSkills(combat_skills=30),
        inventory=Inventory(capacity=0),
        level=Level(xp_given=20),
        health=30,
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
