from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, BumpAction, EscapeAction, MovementAction

if TYPE_CHECKING:
    from engine import Engine


class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()

            self.engine.handle_enemy_turns()
            self.engine.update_fov()
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        key = event.sym
        player = self.engine.player

        if key == tcod.event.K_KP_8:
            action = BumpAction(player, 0, -1)
        elif key == tcod.event.K_KP_9:
            action = BumpAction(player, 1, -1)
        elif key == tcod.event.K_KP_6:
            action = BumpAction(player, 1, 0)
        elif key == tcod.event.K_KP_3:
            action = BumpAction(player, 1, 1)
        elif key == tcod.event.K_KP_2:
            action = BumpAction(player, 0, 1)
        elif key == tcod.event.K_KP_1:
            action = BumpAction(player, -1, 1)
        elif key == tcod.event.K_KP_4:
            action = BumpAction(player, -1, 0)
        elif key == tcod.event.K_KP_7:
            action = BumpAction(player, -1, -1)
        elif key == tcod.event.K_KP_5:
            action = MovementAction(player, 0, 0) # Is this going to be a problem? Eventually this should be 'wait'
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        return action
