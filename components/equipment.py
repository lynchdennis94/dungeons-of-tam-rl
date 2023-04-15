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
            if equippable_item.equippable.weapon_type:
                slot = "weapon"
            elif equippable_item.equippable.equipment_type == EquipmentType.CUIRASS:
                slot = "cuirass"
            elif equippable_item.equippable.equipment_type == EquipmentType.HELMET:
                slot = "helmet"
            elif equippable_item.equippable.equipment_type == EquipmentType.LEFT_PAULDRON:
                slot = "left_shoulder"
            elif equippable_item.equippable.equipment_type == EquipmentType.RIGHT_PAULDRON:
                slot = "right_shoulder"
            elif equippable_item.equippable.equipment_type == EquipmentType.LEFT_HAND:
                slot = "left_hand_armor"
            elif equippable_item.equippable.equipment_type == EquipmentType.RIGHT_HAND:
                slot = "right_hand_armor"
            elif equippable_item.equippable.equipment_type == EquipmentType.GREAVES:
                slot = "greaves"
            elif equippable_item.equippable.equipment_type == EquipmentType.BOOTS:
                slot = "boots"
            elif equippable_item.equippable.equipment_type == EquipmentType.SHIELD:
                weapon_item = getattr(self, "weapon")
                if weapon_item and weapon_item.equippable.equipment_type == EquipmentType.TWO_HANDED_WEAPON:
                    return  # We can't equip a shield AND a two handed weapon
                    # TODO: Put up some sort of error saying you can't do this
                slot = "shield"

            if getattr(self, slot) == equippable_item:
                self.unequip_from_slot(slot, add_message)
            else:
                self.equip_to_slot(slot, equippable_item, add_message)