from __future__ import annotations

from typing import List, TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: List[Item] = []

    def drop(self, item: Item) -> None:
        """
        Removes an item from the inventory and restores it to the game map at the player's current location
        """
        self.items.remove(item)
        item.place(self.parent.x, self.parent.y, self.gamemap)

        self.engine.message_log.add_message(f"You dropped the {item.name}")

    def get_equippables_by_type(self, equipment_type_list: List[EquipmentType]) -> List[Item]:
        output_list = []
        for item in self.items:
            if item.equippable and item.equippable.equipment_type in equipment_type_list:
                output_list.append(item)

        return output_list
