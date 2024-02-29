# Inline formatter class, wrapper of the il_config
from .il_config import ILConfig

from ..ansi import ANSI
from ..enums.colors.fgcolors import FGColors
from ..constants import RESET_STYLE

DEFAULT_COLOR = None

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

    # Private method for conversion between ilconfig and string
    def convert_formats(inline_configurations: list) -> str:
        out = ""
        for element in inline_configurations:
            if element.color == None:
                out += f"{RESET_STYLE}{element.text}"
            else:
                out += f"{ANSI.color_text(FGColors[element.color].value)}{element.text}"

        return out

        
    @staticmethod
    def format(message: str, args: list) -> str:

        message_args = message.split('$')
        inline_configurations = [] # holder for the configuration classes

        configuration_args = 0

        # Define the configurations
        for i in range(0, len(message_args)):
            if i % 2 != 0:
                inline_configurations.append(ILConfig(message_args[i], args[configuration_args].lower()))
                configuration_args += 1
            else:
                inline_configurations.append(ILConfig(message_args[i], DEFAULT_COLOR))

        return ILFormatter.convert_formats(inline_configurations)