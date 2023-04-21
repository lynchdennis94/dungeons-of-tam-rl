from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType
from random import Random

if TYPE_CHECKING:
    from entity import Actor, Item

WEAPON_SLOT = "weapon"
CUIRASS_SLOT = "cuirass"
HELMET_SLOT = "helmet"
LEFT_SHOULDER_SLOT = "left_shoulder"
RIGHT_SHOULDER_SLOT = "right_shoulder"
LEFT_HAND_SLOT = "left_hand_armor"
RIGHT_HAND_SLOT = "right_hand_armor"
GREAVES_SLOT = "greaves"
BOOTS_SLOT = "boots"
SHIELD_SLOT = "shield"

ARMOR_SLOTS = [
    CUIRASS_SLOT,
    HELMET_SLOT,
    LEFT_SHOULDER_SLOT,
    RIGHT_SHOULDER_SLOT,
    LEFT_HAND_SLOT,
    RIGHT_HAND_SLOT,
    GREAVES_SLOT,
    BOOTS_SLOT,
    SHIELD_SLOT
]

EQUIPMENT_TO_SLOT_MAP = {
    EquipmentType.ONE_HANDED_WEAPON: WEAPON_SLOT,
    EquipmentType.TWO_HANDED_WEAPON: WEAPON_SLOT,
    EquipmentType.CUIRASS: CUIRASS_SLOT,
    EquipmentType.HELMET: HELMET_SLOT,
    EquipmentType.LEFT_PAULDRON: LEFT_SHOULDER_SLOT,
    EquipmentType.RIGHT_PAULDRON: RIGHT_SHOULDER_SLOT,
    EquipmentType.LEFT_HAND: LEFT_HAND_SLOT,
    EquipmentType.RIGHT_HAND: RIGHT_HAND_SLOT,
    EquipmentType.GREAVES: GREAVES_SLOT,
    EquipmentType.BOOTS: BOOTS_SLOT,
    EquipmentType.SHIELD: SHIELD_SLOT
}


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
        return self.weapon == item or \
            self.cuirass == item or \
            self.helmet == item or \
            self.left_shoulder == item or \
            self.right_shoulder == item or \
            self.left_hand_armor == item or \
            self.right_hand_armor == item or \
            self.greaves == item or \
            self.boots == item or \
            self.shield == item

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
        slot = "none"
        if equippable_item.equippable:
            slot = EQUIPMENT_TO_SLOT_MAP[equippable_item.equippable.equipment_type]
            if equippable_item.equippable.equipment_type == EquipmentType.SHIELD:
                weapon_item = getattr(self, WEAPON_SLOT)
                if weapon_item and weapon_item.equippable.equipment_type == EquipmentType.TWO_HANDED_WEAPON:
                    return  # We can't equip a shield AND a two handed weapon
                    # TODO: Put up some sort of error saying you can't do this

            if getattr(self, slot) == equippable_item:
                self.unequip_from_slot(slot, add_message)
            else:
                self.equip_to_slot(slot, equippable_item, add_message)

    def get_item_name_in_slot(self, slot: str):
        item = getattr(self, slot)
        if item is None:
            return "Empty"
        else:
            return item.name
