#!/usr/bin/env python3
import copy

import tcod

from engine import Engine
import entity_factories
import procgen


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
MAP_WIDTH = 80
MAP_HEIGHT = 45

room_max_size = 10
room_min_size = 6
max_rooms = 30
max_monsters_per_room = 2

TILESET = tcod.tileset.load_tilesheet("resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
WINDOW_TITLE = "Yet Another Roguelike Tutorial"


def main():
    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)
    engine.game_map = procgen.generate_dungeon(
        max_rooms,
        room_min_size,
        room_max_size,
        MAP_WIDTH,
        MAP_HEIGHT,
        max_monsters_per_room,
        engine)
    engine.update_fov()

    with tcod.context.new_terminal(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            tileset=TILESET,
            title=WINDOW_TITLE,
            vsync=True) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            engine.render(root_console, context)
            engine.event_handler.handle_events()


if __name__ == '__main__':
    main()
