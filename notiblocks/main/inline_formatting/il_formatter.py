# Inline formatter class, wrapper of the il_config
from il_config import ILConfig

from ..ansi import ANSI
from .enums.colors.fgcolors import FGColors

DEFAULT_COLOR = "none"

class ILFormatter:
    """
    ILFormatter is a class, that let's you format your message inline.
    It's job is to work like a factory - you provide a list of ILConfigs, and it returns
    a string, that represents them.

    To use it, just call the .format() method and provide the color names and the text.
    The way that you order them one next to another is how your code would be colored.

    You could tell it, that you want to format the text like $this$
    """

    def __init__ ():
        pass

    def __convert_formats(inline_configurations: list) -> str:
        pass
        

    def format(self, message: str, args: list) -> str:

        message_args = message.split('$')
        inline_configurations = [] # holder for the configuration classes

        # Define the configurations
        for i in range(0, len(message_args)):
            if i % 2 != 0:
                inline_configurations[i] = ILConfig(message_args[i], args[i].color.lower())
            else:
                inline_configurations[i] = ILConfig(message_args[i], DEFAULT_COLOR)

        return __convert_formats(inline_configurations)