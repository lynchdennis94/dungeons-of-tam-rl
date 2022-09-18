#!/usr/bin/env python3
import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
TILESET = tcod.tileset.load_tilesheet("resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
WINDOW_TITLE = "Yet Another Roguelike Tutorial"
EVENT_HANDLER = EventHandler()


def main():
    player_x = int(SCREEN_WIDTH / 2)
    player_y = int(SCREEN_HEIGHT / 2)
    with tcod.context.new_terminal(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            tileset=TILESET,
            title=WINDOW_TITLE,
            vsync=True) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")
            context.present(root_console)
            root_console.clear()

            for event in tcod.event.wait():
                action = EVENT_HANDLER.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == '__main__':
    main()
