#!/usr/bin/env python3
import traceback

import tcod

import colors
import setup_game
import exceptions
import input_handlers


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

TILESET = tcod.tileset.load_tilesheet("resources/16x16-RogueYun-AgmEdit.png", 16, 16, tcod.tileset.CHARMAP_CP437)
WINDOW_TITLE = "Yet Another Roguelike Tutorial"

def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it"""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")

def main():

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            tileset=TILESET,
            title=WINDOW_TITLE,
            vsync=True) as context:
        root_console = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)
                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:
                    traceback.print_exc()
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(traceback.format_exc(), colors.ERROR)
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:
            save_game(handler, "savegame.sav")
            raise
        except BaseException:
            save_game(handler, "savegame.sav")
            raise


if __name__ == '__main__':
    main()
