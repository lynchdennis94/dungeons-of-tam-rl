from __future__ import annotations

from typing import TYPE_CHECKING

import colors

if TYPE_CHECKING:
    from tcod import Console


def render_bar(console: Console, current_value: int, max_value: int, total_width: int) -> None:
    bar_width = int(float(current_value / max_value) * total_width)

    console.draw_rect(x=0, y=45, width=total_width, height=1, ch=1, bg=colors.BAR_EMPTY)

    if bar_width > 0:
        console.draw_rect(x=0, y=45, width=bar_width, height=1, ch=1, bg=colors.BAR_FILLED)

    console.print(x=1, y=45, string=f"HP: {current_value}/{max_value}", fg=colors.BAR_TEXT)
