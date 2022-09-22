from typing import Optional

import tcod.event

from actions import *


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_KP_8:
            action = BumpAction(0, -1)
        elif key == tcod.event.K_KP_9:
            action = BumpAction(1, -1)
        elif key == tcod.event.K_KP_6:
            action = BumpAction(1, 0)
        elif key == tcod.event.K_KP_3:
            action = BumpAction(1, 1)
        elif key == tcod.event.K_KP_2:
            action = BumpAction(0, 1)
        elif key == tcod.event.K_KP_1:
            action = BumpAction(-1, 1)
        elif key == tcod.event.K_KP_4:
            action = BumpAction(-1, 0)
        elif key == tcod.event.K_KP_7:
            action = BumpAction(-1, -1)
        elif key == tcod.event.K_KP_5:
            action = MovementAction(0, 0) # Is this going to be a problem? Eventually this should be 'wait'
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action
