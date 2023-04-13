from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributes
from components.skills import Skills
from gender_types import GenderType

if TYPE_CHECKING:
    from entity import Actor


class Race(BaseComponent):
    parent: Actor

    def __init__(self,
                 name: str,
                 gender: GenderType,
                 base_primary_attributes: PrimaryAttributes,
                 base_skills: Skills,
                 magicka_multiplier: float = 0.0):  # TODO: Add resistances, and racial descriptions
        self.name = name
        self.gender = gender
        self.base_primary_attributes = base_primary_attributes
        self.base_skills = base_skills
        self.magicka_multiplier = magicka_multiplier

ARGONIAN_MALE = Race(
    name="Argonian",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=50, speed=50, endurance=30, personality=30
    ),
    base_skills=Skills(
        alchemy=5, athletics=15, illusion=5, medium_armor=5, mysticism=5, spear=5, unarmored=5
    ))

ARGONIAN_FEMALE = Race(
    name="Argonian",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        intelligence=50, endurance=30, personality=30
    ),
    base_skills=Skills(
        alchemy=5, athletics=15, illusion=5, medium_armor=5, mysticism=5, spear=5, unarmored=5
    ))

BRETON_MALE = Race(
    name="Breton",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        intelligence=50, willpower=50, agility=30, speed=30, endurance=30
    ),
    base_skills=Skills(
        alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10
    ),
    magicka_multiplier=0.5)

BRETON_FEMALE = Race(
    name="Breton",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, willpower=50, agility=30, endurance=30
    ),
    base_skills=Skills(
        alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10
    ),
    magicka_multiplier=0.5)

DUNMER_MALE = Race(
    name="Dunmer",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        willpower=30, speed=50, personality=30
    ),
    base_skills=Skills(
        athletics=5, destruction=10, light_armor=5, long_blade=5, marksman=5, mysticism=5, short_blade=5
    ))

DUNMER_FEMALE = Race(
    name="Dunmer",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        willpower=30, speed=50, endurance=30
    ),
    base_skills=Skills(
        athletics=5, destruction=10, light_armor=5, long_blade=5, marksman=5, mysticism=5, short_blade=5
    ))

ALTMER_MALE = Race(
    name="Altmer",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, speed=30
    ),
    base_skills=Skills(
        alchemy=10, alteration=5, conjuration=5, destruction=10, enchant=10, illusion=5
    ),
    magicka_multiplier=1.5)

ALTMER_FEMALE = Race(
    name="Altmer",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, endurance=30
    ),
    base_skills=Skills(
        alchemy=10, alteration=5, conjuration=5, destruction=10, enchant=10, illusion=5
    ),
    magicka_multiplier=1.5)

IMPERIAL_MALE = Race(
    name="Imperial",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=30, personality=50
    ),
    base_skills=Skills(
        blunt_weapon=5, hand_to_hand=5, light_armor=5, long_blade=10, mercantile=10, speechcraft=10
    ))

IMPERIAL_FEMALE = Race(
    name="Imperial",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        agility=30, speed=30, personality=50
    ),
    base_skills=Skills(
        blunt_weapon=5, hand_to_hand=5, light_armor=5, long_blade=10, mercantile=10, speechcraft=10
    ))

KHAJIIT_MALE = Race(
    name="Khajiit",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=15, athletics=5, hand_to_hand=5, light_armor=5, security=5, short_blade=5, sneak=5
    ))

KHAJIIT_FEMALE = Race(
    name="Khajiit",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50
    ),
    base_skills=Skills(
        acrobatics=15, athletics=5, hand_to_hand=5, light_armor=5, security=5, short_blade=5, sneak=5
    ))

NORD_MALE = Race(
    name="Nord",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, agility=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        axe=10, blunt_weapon=10, heavy_armor=5, long_blade=5, medium_armor=10, spear=5
    ))

NORD_FEMALE = Race(
    name="Nord",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, willpower=50, agility=30, personality=30
    ),
    base_skills=Skills(
        axe=10, blunt_weapon=10, heavy_armor=5, long_blade=5, medium_armor=10, spear=5
    ))

ORSIMER_MALE = Race(
    name="Orsimer",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        strength=45, intelligence=30, willpower=50, agility=35, speed=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        armorer=10, axe=5, block=10, heavy_armor=10, medium_armor=10
    ))

ORSIMER_FEMALE = Race(
    name="Orsimer",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=45, willpower=45, agility=35, speed=30, endurance=50, personality=25
    ),
    base_skills=Skills(
        armorer=10, axe=5, block=10, heavy_armor=10, medium_armor=10
    ))

REDGUARD_MALE = Race(
    name="Redguard",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, willpower=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        athletics=5, axe=5, blunt_weapon=5, heavy_armor=5, long_blade=15, medium_armor=5, short_blade=5
    ))

REDGUARD_FEMALE = Race(
    name="Redguard",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        intelligence=30, willpower=30, endurance=50
    ),
    base_skills=Skills(
        athletics=5, axe=5, blunt_weapon=5, heavy_armor=5, long_blade=15, medium_armor=5, short_blade=5
    ))

BOSMER_MALE = Race(
    name="Bosmer",
    gender=GenderType.MALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50, speed=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=5, alchemy=5, light_armor=10, marksman=15, sneak=10
    ))

BOSMER_FEMALE = Race(
    name="Bosmer",
    gender=GenderType.FEMALE,
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50, speed=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=5, alchemy=5, light_armor=10, marksman=15, sneak=10
    ))

MALE_RACES = [
    ARGONIAN_MALE,
    BRETON_MALE,
    DUNMER_MALE,
    IMPERIAL_MALE,
    ALTMER_MALE,
    ORSIMER_MALE,
    NORD_MALE,
    BOSMER_MALE,
    REDGUARD_MALE,
    KHAJIIT_MALE
]

FEMALE_RACES = [
    ARGONIAN_FEMALE,
    BRETON_FEMALE,
    DUNMER_FEMALE,
    IMPERIAL_FEMALE,
    ALTMER_FEMALE,
    ORSIMER_FEMALE,
    NORD_FEMALE,
    BOSMER_FEMALE,
    REDGUARD_FEMALE,
    KHAJIIT_FEMALE
]

