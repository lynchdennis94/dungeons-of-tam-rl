from __future__ import annotations

import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    gamemap: GameMap

    def __init__(
            self,
            gamemap: Optional[GameMap] = None,
            x: int = 0,
            y: int = 0,
            char: str = '?',
            color: Tuple[int, int, int] = (255, 255, 255),
            eyesight_radius: int = 0,
            name: str = "<Unnamed>",
            blocks_movement: bool = False
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.eyesight_radius = eyesight_radius
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone

    def place(self, x: int, y: int, gamemap: Optional[GameMap] = None) -> None:
        """Place this entity at a new location. Handles moving across GameMaps."""
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"): # Possibly uninitialized
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)
