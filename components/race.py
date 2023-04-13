from __future__ import annotations

import copy
from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from components.primary_attributes import PrimaryAttributes
from components.skills import Skills

if TYPE_CHECKING:
    from entity import Actor


class Race(BaseComponent):
    parent: Actor

    def __init__(self,
                 name: str,
                 base_primary_attributes: PrimaryAttributes,
                 base_skills: Skills,
                 magicka_multiplier: float = 0.0):  # TODO: Add resistances, and racial descriptions
        self.name = name
        self.base_primary_attributes = base_primary_attributes
        self.base_skills = base_skills
        self.magicka_multiplier = magicka_multiplier


ARGONIAN_MALE = Race(
    name="Argonian",
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=50, speed=50, endurance=30, personality=30
    ),
    base_skills=Skills(
        alchemy=5, athletics=15, illusion=5, medium_armor=5, mysticism=5, spear=5, unarmored=5
    ))

ARGONIAN_FEMALE = Race(
    name="Argonian",
    base_primary_attributes=PrimaryAttributes(
        intelligence=50, endurance=30, personality=30
    ),
    base_skills=Skills(
        alchemy=5, athletics=15, illusion=5, medium_armor=5, mysticism=5, spear=5, unarmored=5
    ))

BRETON_MALE = Race(
    name="Breton",
    base_primary_attributes=PrimaryAttributes(
        intelligence=50, willpower=50, agility=30, speed=30, endurance=30
    ),
    base_skills=Skills(
        alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10
    ),
    magicka_multiplier=0.5)

BRETON_FEMALE = Race(
    name="Breton",
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, willpower=50, agility=30, endurance=30
    ),
    base_skills=Skills(
        alchemy=5, alteration=5, conjuration=10, illusion=5, mysticism=10, restoration=10
    ),
    magicka_multiplier=0.5)

DUNMER_MALE = Race(
    name="Dunmer",
    base_primary_attributes=PrimaryAttributes(
        willpower=30, speed=50, personality=30
    ),
    base_skills=Skills(
        athletics=5, destruction=10, light_armor=5, long_blade=5, marksman=5, mysticism=5, short_blade=5
    ))

DUNMER_FEMALE = Race(
    name="Dunmer",
    base_primary_attributes=PrimaryAttributes(
        willpower=30, speed=50, endurance=30
    ),
    base_skills=Skills(
        athletics=5, destruction=10, light_armor=5, long_blade=5, marksman=5, mysticism=5, short_blade=5
    ))

ALTMER_MALE = Race(
    name="Altmer",
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, speed=30
    ),
    base_skills=Skills(
        alchemy=10, alteration=5, conjuration=5, destruction=10, enchant=10, illusion=5
    ),
    magicka_multiplier=1.5)

ALTMER_FEMALE = Race(
    name="Altmer",
    base_primary_attributes=PrimaryAttributes(
        strength=30, intelligence=50, endurance=30
    ),
    base_skills=Skills(
        alchemy=10, alteration=5, conjuration=5, destruction=10, enchant=10, illusion=5
    ),
    magicka_multiplier=1.5)

IMPERIAL_MALE = Race(
    name="Imperial",
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=30, personality=50
    ),
    base_skills=Skills(
        blunt_weapon=5, hand_to_hand=5, light_armor=5, long_blade=10, mercantile=10, speechcraft=10
    ))

IMPERIAL_FEMALE = Race(
    name="Imperial",
    base_primary_attributes=PrimaryAttributes(
        agility=30, speed=30, personality=50
    ),
    base_skills=Skills(
        blunt_weapon=5, hand_to_hand=5, light_armor=5, long_blade=10, mercantile=10, speechcraft=10
    ))

KHAJIIT_MALE = Race(
    name="Khajiit",
    base_primary_attributes=PrimaryAttributes(
        willpower=30, agility=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=15, athletics=5, hand_to_hand=5, light_armor=5, security=5, short_blade=5, sneak=5
    ))

KHAJIIT_FEMALE = Race(
    name="Khajiit",
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50
    ),
    base_skills=Skills(
        acrobatics=15, athletics=5, hand_to_hand=5, light_armor=5, security=5, short_blade=5, sneak=5
    ))

NORD_MALE = Race(
    name="Nord",
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, agility=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        axe=10, blunt_weapon=10, heavy_armor=5, long_blade=5, medium_armor=10, spear=5
    ))

NORD_FEMALE = Race(
    name="Nord",
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, willpower=50, agility=30, personality=30
    ),
    base_skills=Skills(
        axe=10, blunt_weapon=10, heavy_armor=5, long_blade=5, medium_armor=10, spear=5
    ))

ORSIMER_MALE = Race(
    name="Orsimer",
    base_primary_attributes=PrimaryAttributes(
        strength=45, intelligence=30, willpower=50, agility=35, speed=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        armorer=10, axe=5, block=10, heavy_armor=10, medium_armor=10
    ))

ORSIMER_FEMALE = Race(
    name="Orsimer",
    base_primary_attributes=PrimaryAttributes(
        strength=45, willpower=45, agility=35, speed=30, endurance=50, personality=25
    ),
    base_skills=Skills(
        armorer=10, axe=5, block=10, heavy_armor=10, medium_armor=10
    ))

REDGUARD_MALE = Race(
    name="Redguard",
    base_primary_attributes=PrimaryAttributes(
        strength=50, intelligence=30, willpower=30, endurance=50, personality=30
    ),
    base_skills=Skills(
        athletics=5, axe=5, blunt_weapon=5, heavy_armor=5, long_blade=15, medium_armor=5, short_blade=5
    ))

REDGUARD_FEMALE = Race(
    name="Redguard",
    base_primary_attributes=PrimaryAttributes(
        intelligence=30, willpower=30, endurance=50
    ),
    base_skills=Skills(
        athletics=5, axe=5, blunt_weapon=5, heavy_armor=5, long_blade=15, medium_armor=5, short_blade=5
    ))

BOSMER_MALE = Race(
    name="Bosmer",
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50, speed=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=5, alchemy=5, light_armor=10, marksman=15, sneak=10
    ))

BOSMER_FEMALE = Race(
    name="Bosmer",
    base_primary_attributes=PrimaryAttributes(
        strength=30, willpower=30, agility=50, speed=50, endurance=30
    ),
    base_skills=Skills(
        acrobatics=5, alchemy=5, light_armor=10, marksman=15, sneak=10
    ))

MALE_RACES = [
    copy.deepcopy(ARGONIAN_MALE),
    copy.deepcopy(BRETON_MALE),
    copy.deepcopy(DUNMER_MALE),
    copy.deepcopy(IMPERIAL_MALE),
    copy.deepcopy(ALTMER_MALE),
    copy.deepcopy(ORSIMER_MALE),
    copy.deepcopy(NORD_MALE),
    copy.deepcopy(BOSMER_MALE),
    copy.deepcopy(REDGUARD_MALE),
    copy.deepcopy(KHAJIIT_MALE)
]

FEMALE_RACES = [
    copy.deepcopy(ARGONIAN_FEMALE),
    copy.deepcopy(BRETON_FEMALE),
    copy.deepcopy(DUNMER_FEMALE),
    copy.deepcopy(IMPERIAL_FEMALE),
    copy.deepcopy(ALTMER_FEMALE),
    copy.deepcopy(ORSIMER_FEMALE),
    copy.deepcopy(NORD_FEMALE),
    copy.deepcopy(BOSMER_FEMALE),
    copy.deepcopy(REDGUARD_FEMALE),
    copy.deepcopy(KHAJIIT_FEMALE)
]

