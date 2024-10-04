import curses
from enum import Enum
from typing import TypeAlias


class Colour(Enum):
    BLACK: int = curses.COLOR_BLACK
    BLUE: int = curses.COLOR_BLUE
    CYAN: int = curses.COLOR_CYAN
    GREEN: int = curses.COLOR_GREEN
    MAGENTA: int = curses.COLOR_MAGENTA
    RED: int = curses.COLOR_RED
    WHITE: int = curses.COLOR_WHITE
    YELLOW: int = curses.COLOR_YELLOW


Color: TypeAlias = Colour


class ReturnType(Enum):
    INDEX: int = 0
    LITERAL: int = 1
