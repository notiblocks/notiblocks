from ..ansi import ANSI
from ..constants import *

class InvalidOperationTypeError(RuntimeError):
    """
    `Invalid Operation Type` is an exception, that is usually throwed whenever you try to call a method with a worng `type`. 
     > If you are using the `handle_operation` method somewhere in your code, check wherther you provide one of the following arguments as a type

      * success
      * warn
      * fail 

    How to debug:
        - Check the `type` parameter of the `handle_operation` method.
    """
    def __init__(self, message):
        self._message = message

    def __str__(self) -> str:
        return f"{ANSI.background(BG_RED)}{ANSI.color_text(FG_YELLOW)}[{ANSI.color_text(FG_WHITE)}EXCEPTION{ANSI.color_text(FG_YELLOW)}]{ANSI.color_text(FG_WHITE)}{self._message}{RESET_STYLE}"