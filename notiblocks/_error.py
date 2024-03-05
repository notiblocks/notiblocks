from abc import ABC, abstractmethod

from ._ansi import ANSI
from ._constants import *

class NBError(ABC):

    def __init__(self, message: str):
        slef._message = message

    @abstractmethod
    def __str__(self) -> str:
        pass

class InvalidFormatError(NBError, RuntimeError):
    def __str__(self) -> str:
        return f"{ANSI.background(BG_RED)}{ANSI.color_text(FG_YELLOW)}[{ANSI.color_text(FG_WHITE)}EXCEPTION{ANSI.color_text(FG_YELLOW)}]{ANSI.color_text(FG_WHITE)}{self._message}{RESET_STYLE}"

class InvalidOperationTypeError(NBError, RuntimeError):
    def __str__(self) -> str:
        return f"{ANSI.background(BG_RED)}{ANSI.color_text(FG_YELLOW)}[{ANSI.color_text(FG_WHITE)}EXCEPTION{ANSI.color_text(FG_YELLOW)}]{ANSI.color_text(FG_WHITE)}{self._message}{RESET_STYLE}"

class InvalidMessageError(NBError, RuntimeError):
    def __str__(self) -> str:
        return f"{ANSI.background(BG_RED)}{ANSI.color_text(FG_YELLOW)}[{ANSI.color_text(FG_WHITE)}EXCEPTION{ANSI.color_text(FG_YELLOW)}]{ANSI.color_text(FG_WHITE)}{self._message}{RESET_STYLE}"