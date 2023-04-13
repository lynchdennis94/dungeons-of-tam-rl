from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType
from random import Random

if TYPE_CHECKING:
    from entity import Actor, Item


class Equipment(BaseComponent):
    parent: Actor

    def __init__(self,
                 weapon: Optional[Item] = None,
                 shield: Optional[Item] = None,
                 helmet: Optional[Item] = None,
                 cuirass: Optional[Item] = None,
                 left_shoulder: Optional[Item] = None,
                 left_hand_armor: Optional[Item] = None,
                 right_shoulder: Optional[Item] = None,
                 right_hand_armor: Optional[Item] = None,
                 greaves: Optional[Item] = None,
                 boots: Optional[Item] = None,):
        self.weapon = weapon
        self.shield = shield
        self.helmet = helmet
        self.cuirass = cuirass
        self.left_shoulder = left_shoulder
        self.left_hand_armor = left_hand_armor
        self.right_shoulder = right_shoulder
        self.right_hand_armor = right_hand_armor
        self.greaves = greaves
        self.boots = boots
        self.rand_generator = Random()

    def item_is_equipped(self, item: Item) -> bool:
        return self.weapon == item or self.armor == item

    def unequip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(f"You remove the {item_name}")

    def equip_message(self, item_name: str) -> None:
        self.parent.gamemap.engine.message_log.add_message(f"You equip the {item_name}")

    def equip_to_slot(self, slot: str, item: Item, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if current_item is not None:
            self.unequip_from_slot(slot, add_message)

        setattr(self, slot, item)

        if add_message:
            self.equip_message(item.name)

    def unequip_from_slot(self, slot: str, add_message: bool) -> None:
        current_item = getattr(self, slot)

        if add_message:
            self.unequip_message(current_item.name)

        setattr(self, slot, None)

    def toggle_equip(self, equippable_item: Item, add_message: bool = True) -> None:
        if equippable_item.equippable and equippable_item.equippable.equipment_type == EquipmentType.WEAPON:
            slot = "weapon"
        else:
            slot = "armor"

        if getattr(self, slot) == equippable_item:
            self.unequip_from_slot(slot, add_message)
        else:
            self.equip_to_slot(slot, equippable_item, add_message)