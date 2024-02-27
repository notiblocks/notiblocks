from ..ansi import ANSI
from ..constants import *

class InvalidFormatError(RuntimeError):
    """
    Exception, which is throwed when the format you provided is not supported.

    How to debug:
        @Check the parameters you provided to the @NBConfig, there should be a wrong value, which is not getting indicated by the program.
    """
    def __init__(self, message):
        self._message = message

    def __str__(self) -> str:
        return f"{ANSI.background(BG_RED)}{ANSI.color_text(FG_YELLOW)}[{ANSI.color_text(FG_WHITE)}EXCEPTION{ANSI.color_text(FG_YELLOW)}]{ANSI.color_text(FG_WHITE)}{self._message}{RESET_STYLE}"