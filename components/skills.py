from __future__ import annotations

from typing import TYPE_CHECKING
from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor


class Skills(BaseComponent):
    parent: Actor

    def __init__(self, 
                 heavy_armor: int,
                 medium_armor: int,
                 spear: int,
                 acrobatics: int,
                 armorer: int,
                 axe: int,
                 blunt_weapon: int,
                 long_blade: int,
                 block: int,
                 light_armor: int,
                 marksman: int,
                 sneak: int,
                 athletics: int,
                 hand_to_hand: int,
                 short_blade: int,
                 unarmored: int,
                 illusion: int,
                 mercantile: int,
                 speechcraft: int,
                 alchemy: int,
                 conjuration: int,
                 enchant: int,
                 security: int,
                 alteration: int,
                 destruction: int,
                 mysticism: int,
                 restoration: int):
        self.heavy_armor = heavy_armor
        self.medium_armor = medium_armor
        self.spear = spear
        self.acrobatics = acrobatics
        self.armorer = armorer
        self.axe = axe
        self.blunt_weapon = blunt_weapon
        self.long_blade = long_blade
        self.block = block
        self.light_armor = light_armor
        self.marksman = marksman
        self.sneak = sneak
        self.athletics = athletics
        self.hand_to_hand = hand_to_hand
        self.short_blade = short_blade
        self.unarmored = unarmored
        self.illusion = illusion
        self.mercantile = mercantile
        self.speechcraft = speechcraft
        self.alchemy = alchemy
        self.conjuration = conjuration
        self.enchant = enchant
        self.security = security
        self.alteration = alteration
        self.destruction = destruction
        self.mysticism = mysticism
        self.restoration = restoration
