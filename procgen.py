from __future__ import annotations

import random
from typing import Dict, Iterator, List, Tuple, TYPE_CHECKING

import tcod

from factories import entity_factories, weapon_factories, armor_factories
from game_map import GameMap
import tile_types

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity, Item

max_items_by_floor = [
    (1, 1),
    (4, 2),
]

max_monsters_by_floor = [
    (1, 2),
    (4, 3),
    (6, 5)
]


def initialize_items_for_floor(
        floor: int,
        item_list: List[Item],
        item_chance_dict: Dict[int,List[Tuple[Entity, int]]] ):
    if floor not in item_chances:
        item_chance_dict[floor] = []

    for item in item_list:
        item_chance_dict[floor].append((item, 10))


item_chances: Dict[int, List[Tuple[Entity, int]]] = {}

# Add armor chances
initialize_items_for_floor(0, armor_factories.NETCH_LEATHER_ARMOR, item_chances)
initialize_items_for_floor(5, armor_factories.CHITIN_ARMOR, item_chances)
initialize_items_for_floor(15, armor_factories.DREUGH_LEATHER_ARMOR, item_chances)
initialize_items_for_floor(30, armor_factories.GLASS_ARMOR, item_chances)
initialize_items_for_floor(2, armor_factories.CHAIN_ARMOR, item_chances)
initialize_items_for_floor(7, armor_factories.BONEMOLD_ARMOR, item_chances)
initialize_items_for_floor(17, armor_factories.ORCISH_ARMOR, item_chances)
initialize_items_for_floor(32, armor_factories.INDORIL_ARMOR, item_chances)
initialize_items_for_floor(4, armor_factories.IRON_ARMOR, item_chances)
initialize_items_for_floor(9, armor_factories.STEEL_ARMOR, item_chances)
initialize_items_for_floor(19, armor_factories.DWEMER_ARMOR, item_chances)
initialize_items_for_floor(35, armor_factories.EBONY_ARMOR, item_chances)
initialize_items_for_floor(45, armor_factories.DAEDRIC_ARMOR, item_chances)

# Add weapon chances
initialize_items_for_floor(0, weapon_factories.CHITIN_WEAPONS, item_chances)
initialize_items_for_floor(5, weapon_factories.IRON_WEAPONS, item_chances)
initialize_items_for_floor(10, weapon_factories.STEEL_WEAPONS, item_chances)
initialize_items_for_floor(15, weapon_factories.IMPERIAL_WEAPONS, item_chances)
initialize_items_for_floor(20, weapon_factories.NORDIC_WEAPONS, item_chances)
initialize_items_for_floor(25, weapon_factories.SILVER_WEAPONS, item_chances)
initialize_items_for_floor(30, weapon_factories.DWEMER_WEAPONS, item_chances)
initialize_items_for_floor(35, weapon_factories.GLASS_WEAPONS, item_chances)
initialize_items_for_floor(40, weapon_factories.EBONY_WEAPONS, item_chances)
initialize_items_for_floor(45, weapon_factories.DAEDRIC_WEAPONS, item_chances)


enemy_chances: Dict[int, List[Tuple[Entity, int]]] = {
    0: [(entity_factories.orc, 1)],
    3: [(entity_factories.troll, 15)],
    5: [(entity_factories.troll, 30)],
    7: [(entity_factories.troll, 60)],
}



def get_max_value_for_floor(weighted_chances_by_floor: List[Tuple[int, int]], floor: int) -> int:
    current_value = 0

    for floor_minimum, value in weighted_chances_by_floor:
        if floor_minimum > floor:
            break
        else:
            current_value = value

    return current_value


def get_entities_at_random(
        weighted_chances_by_floor: Dict[int, List[Tuple[Entity, int]]],
        number_of_entities: int, floor: int
) -> List[Entity]:
    entity_weighted_chances = {}

    for key, values in weighted_chances_by_floor.items():
        if key > floor:
            break
        else:
            for value in values:
                entity = value[0]
                weighted_chance = value[1]

                entity_weighted_chances[entity] = weighted_chance

    entities = list(entity_weighted_chances.keys())
    entity_weighted_chance_values = list(entity_weighted_chances.values())

    chosen_entities = random.choices(entities, weights=entity_weighted_chance_values, k=number_of_entities)

    return chosen_entities

class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        """Return the center point of the room as a Tuple (x, y)"""
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of the room as a 2D array index"""
        # The +1 to the top-left ensures we account for walls on the room.
        # The area defined should always be a carved out center, while (x1,y1) and (x2,y2) define
        # the top left and bottom right corners of the wall, respectively
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom"""
        return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1


def place_entities(room: RectangularRoom, dungeon: GameMap, floor_number: int) -> None:
    number_of_monsters = random.randint(0, get_max_value_for_floor(max_monsters_by_floor, floor_number))
    number_of_items = random.randint(0, get_max_value_for_floor(max_items_by_floor, floor_number))
    monsters: List[Entity] = get_entities_at_random(enemy_chances, number_of_monsters, floor_number)
    items: List[Entity] = get_entities_at_random(item_chances, number_of_items, floor_number)

    for chosen_entity in monsters + items:
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            chosen_entity.spawn(dungeon, x, y)


def tunnel_between(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end

    if random.random() < 0.5:
        corner_x, corner_y = x2, y1
    else:
        corner_x, corner_y = x1, y2

    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def generate_dungeon(
        max_rooms: int,
        room_min_size: int,
        room_max_size: int,
        map_width: int,
        map_height: int,
        engine: Engine) -> GameMap:
    """Generate a new dungeon map."""
    player = engine.player
    dungeon = GameMap(engine, map_width, map_height, entities={player})

    rooms: List[RectangularRoom] = []

    center_of_last_room = (0, 0)

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        new_room = RectangularRoom(x=x, y=y, width=room_width, height=room_height)

        if any(new_room.intersects(other_room) for other_room in rooms):
            continue

        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            player.place(*new_room.center, dungeon)
        else:
            for x, y in tunnel_between(new_room.center, rooms[-1].center):
                dungeon.tiles[x, y] = tile_types.floor

            center_of_last_room = new_room.center

        place_entities(new_room, dungeon, engine.game_world.current_floor)

        dungeon.tiles[center_of_last_room] = tile_types.down_stairs


        rooms.append(new_room)
    dungeon.downstairs_location = center_of_last_room
    return dungeon
