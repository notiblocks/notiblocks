from enum import Enum

from ...constants import *

class BGColors(Enum):
    """
    Enumeration, that stores the ANSI codes for the background values, 
    that are being used and implemented in the most of the terminal emulators
    """
    reset =             BG_RESET
    black =             BG_BLACK
    red =               BG_RED
    green =             BG_GREEN
    yellow =            BG_YELLOW
    blue =              BG_BLUE
    magenta =           BG_MAGENTA
    cyan =              BG_CYAN
    white =             BG_WHITE
    gray =              BG_GRAY
    bright_red =        BG_BRIGHT_RED
    bright_green =      BG_BRIGHT_GREEN
    bright_yellow =     BG_BRIGHT_YELLOW
    bright_blue =       BG_BRIGHT_BLUE
    bright_magenta =    BG_BRIGHT_MAGENTA
    bright_cyan =       BG_BRIGHT_CYAN
    bright_white =      BG_BRIGHT_WHITE