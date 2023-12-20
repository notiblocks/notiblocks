from enum import Enum
from nb_inline import NBInline

class FGColors(Enum):
    """
    Enumeration, that stores the ANSI codes for the text styling values, 
    that are being used and implemented in the most of the terminal emulators
    """
    reset =             FG_RESET
    black =             FG_BLACK
    red =               FG_RED
    green =             FG_GREEN
    yellow =            FG_YELLOW
    blue =              FG_BLUE
    magenta =           FG_MAGENTA
    cyan =              FG_CYAN
    white =             FG_WHITE
    gray =              FG_GRAY
    bright_red =        FG_BRIGHT_RED
    bright_green =      FG_BRIGHT_GREEN
    bright_yellow =     FG_BRIGHT_YELLOW
    bright_blue =       FG_BRIGHT_BLUE
    bright_magenta =    FG_BRIGHT_MAGENTA
    bright_cyan =       FG_BRIGHT_CYAN
    bright_white =      FG_BRIGHT_WHITE