from components.ai import HostileEnemy
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 255),
    eyesight_radius=8,
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26)
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    eyesight_radius=8,
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0)
)

troll = Actor(
    char="T",
    color=(0, 127, 0),
    eyesight_radius=9,
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0)
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
