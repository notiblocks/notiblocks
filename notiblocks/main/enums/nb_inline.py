from enum import Enum

class NBInline(Enum):
    """
    The Notiblocks inline formatting module
    You can use it for inline message formatting, just import it
    into your module and use this syntax for example @{%RESET%}
    
    Note, that some of these may not work with your terminal emulator.
    It depends only on the terminal and the terminal itself.
    """
    RESET = 0
    BOLD = 1
    FAINT = 2
    ITALIC = 3
    UNDERLINE = 4
    SLOW_BLINK = 5
    RAPID_BLINK = 6
    REVERSE_VIDEO = 7
    CONCEAL = 8
    CROSSED_OUT = 9
    PRIMARY_FONT = 10
    FRAKTUR = 20
    BOLD_OFF_OR_DOUBLE_UNDERLINE = 21
    NORMAL_INTENSITY = 22
    NOT_ITALIC_NOT_FRAKTUR = 23
    UNDERLINE_OFF = 24
    BLINK_OFF = 25
    INVERSE_OFF = 27
    REVEAL = 28
    NOT_CROSSED_OUT = 29
    SET_FOREGROUND_COLOR = 38
    DEFAULT_FOREGROUND_COLOR = 39
    SET_BACKGROUND_COLOR = 48
    DEFAULT_BACKGROUND_COLOR = 49
    FRAMED = 51
    ENCIRCLED = 52
    OVERLINED = 53
    NOT_FRAMED_OR_ENCIRCLED = 54
    NOT_OVERLINED = 55
    IDEOGRAM_UNDERLINE = 60
    IDEOGRAM_DOUBLE_UNDERLINE = 61
    IDEOGRAM_OVERLINE = 62
    IDEOGRAM_DOUBLE_OVERLINE = 63
    IDEOGRAM_STRESS_MARKING = 64
    IDEOGRAM_ATTRIBUTES_OFF = 65