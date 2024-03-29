"""Handle the loading and initialization of game sessions"""
from __future__ import annotations

import copy
import lzma
import pickle
import traceback
from typing import Optional

import tcod

import colors
from factories import entity_factories
import input_handlers
from engine import Engine
from game_map import GameWorld

# Load the background image and remove the alpha channel
background_image = tcod.image.load("resources/new_menu_background.png")[:, :, :3]


def new_game() -> Engine:
    """Return a brand new game session as an engine instance"""
    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height
    )
    engine.game_world.generate_floor()
    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", colors.WELCOME_TEXT
    )

    return engine


def load_game(filename: str) -> Engine:
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
    assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input"""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image"""
        console.draw_semigraphics(background_image, 0, 2)

        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "Dungeons of Tam RL",
            fg=colors.MENU_TITLE,
            alignment=tcod.CENTER
        )

        menu_width = 24
        for i, text in enumerate(
                ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=colors.MENU_TEXT,
                bg=colors.BLACK,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64)
            )

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.K_q, tcod.event.K_ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.K_c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load")
            except Exception as exc:
                traceback.print_exc()
                return input_handlers.PopupMessage(self, f"Failure\n{exc}")
        elif event.sym == tcod.event.K_n:
            return input_handlers.NameSelectionEventHandler(new_game())

        return None
