from ._nb_config import NBConfig
from .enums._brackets import Brackets

from ._error import InvalidFormatError
from ._error import InvalidOperationTypeError

from .enums.colors._bgcolors import BGColors
from .enums.colors._fgcolors import FGColors

from ._constants import RESET_STYLE

from .enums._timestampformat import TimeStampFormats

from ._ansi import ANSI

from pathlib import Path

import time
from datetime import datetime
import time

import yaml

script_dir = Path(__file__).resolve().parent
meta_path = script_dir / ".." / "meta.yaml"

class NBHandler:
    
    """
    NBHandler is a class, that wraps the NBConfig. It provides the main functionality, such as:
    * `.success(message)` - Prints a successful message on the console
    * `.fail(message)` - Prints a failure message on the console
    * `.warn(message)` - Prints a warning message on the console
    * `.log(message)` - Prints a log on the console, providing you the functionallity to define custom date before it.
    """
         
    def __init__(self, configuration: NBConfig):

        if configuration is None:
            configuration = NBConfig()
        else:
            self.configuration = configuration

        self.metainfo = self.get_app_version(meta_path)  
        self.version = self.metainfo.get('notiblocks', {}).get('release', {}).get('version', None)


    def get_app_version(self, path: str) -> str:

        with open(path, 'r') as file:
            try:
                data = yaml.safe_load(file)
                return data
            except yaml.YAMLError as e:
                print(e)
                return None

    def handle_operation(self, message: str, operation_type: str) -> str:
        operation_type = operation_type.lower().strip()

        bracket_sign = ""
        color_attr = ""
        sign_color_attr = ""
        bracket_color_attr = ""
        sign_attr = ""
        background_color_attr = ""

        if operation_type == "success":
            bracket_sign = self.configuration._success_bracket_sign if self.configuration._success_bracket_sign is not None else self.configuration._bracket_style
            color_attr = self.configuration._success_color
            sign_color_attr = self.configuration._success_sign_color
            bracket_color_attr = self.configuration._success_bracket_color
            sign_attr = self.configuration._success_sign
            background_color_attr = self.configuration._success_background_color
        elif operation_type == "warn":
            bracket_sign = self.configuration._warn_bracket_sign if self.configuration._warn_bracket_sign is not None else self.configuration._bracket_style
            color_attr = self.configuration._warn_color
            sign_color_attr = self.configuration._warn_sign_color
            bracket_color_attr = self.configuration._warn_bracket_color
            sign_attr = self.configuration._warn_sign
            background_color_attr = self.configuration._warn_background_color
        elif operation_type == "fail":
            bracket_sign = self.configuration._fail_bracket_sign if self.configuration._fail_bracket_sign is not None else self.configuration._bracket_style
            color_attr = self.configuration._fail_color
            sign_color_attr = self.configuration._fail_sign_color
            bracket_color_attr = self.configuration._fail_bracket_color
            sign_attr = self.configuration._fail_sign
            background_color_attr = self.configuration._fail_background_color
        else:
            raise InvalidOperationTypeError(f"This operation is not supported in the current version of notiblocks: {self.version}")

        try:
            return self.format_message(
                color_attr,
                sign_color_attr,
                bracket_color_attr,
                sign_attr,
                background_color_attr,
                bracket_t=bracket_sign,
                message=message
            )
        except InvalidFormatError as ie:
            print(ie)

    def success(self, message: str) -> str:
        return self.handle_operation(message, "success")

    def warn(self, message: str) -> str:
        return self.handle_operation(message, "warn")

    def fail(self, message: str) -> str:
        return self.handle_operation(message, "fail")

    def log(self, message: str) -> str:
        out = ""
        current_time = time.time()
        date_time = datetime.fromtimestamp(current_time)

        text_color =        self.configuration._time_color.lower().strip() if self.configuration._time_color is not None else None
        sign_color =        self.configuration._time_sign_color.lower().strip() if self.configuration._time_sign_color is not None else None
        bracket_color =     self.configuration._time_bracket_color.lower().strip() if self.configuration._time_bracket_color is not None else None
        time_stamp_ext =    self.configuration._time_sign_stamp
        background_color =  self.configuration._time_background_color.lower().strip() if self.configuration._time_background_color is not None else None

        bracket_type_str =  bracket_sign = self.configuration._time_bracket_sign if self.configuration._time_bracket_sign is not None else self.configuration._bracket_style
        opening_bracket = '['
        closing_bracket = ']'

        bracket_type_str = bracket_type_str.upper().strip() # Format the bracket type correctly

        bracket_type = Brackets[bracket_type_str] # Bracket

        if bracket_type == Brackets.ANGLE:
            opening_bracket = '<'
            closing_bracket = '>'
        elif bracket_type == Brackets.CURLY:
            opening_bracket = '{'
            closing_bracket = '}'
        elif bracket_type == Brackets.ROUND:
            opening_bracket = '('
            closing_bracket = ')'
        elif bracket_type == Brackets.SQUARE:
            opening_bracket = '['
            closing_bracket = ']'
        else:
            if bracket_type_str[0] == '@': # Then it's a custom '\[@s]'
                tokens = bracket_type_str.split('\[@s]')
                opening_bracket = tokens[0].strip()
                closing_bracket = tokens[1].strip()
            else:
                raise InvalidFormatError(f"The bracket type you have provided is not present in the current version of notiblocks: {self.version}")

        background_color_value = None
        time_stamp_value = None

        if text_color and sign_color and bracket_color in FGColors.__members__:
            text_color_value =          FGColors[text_color].value
            sign_color_value =          FGColors[sign_color].value
            bracket_color_value =       FGColors[bracket_color].value
            background_color_value =    BGColors.reset.value
            time_stamp_value =          "%H:%M:%S" # Fallback

            time_stamp_as_string = '_'.join(time_stamp_ext.split(' ')).upper()

            time_stamp = TimeStampFormats[time_stamp_as_string]

            if time_stamp == TimeStampFormats.DATE:
                time_stamp_value = "%d %B, %Y"
            elif time_stamp == TimeStampFormats.DATE_AND_TIME:
                time_stamp_value = "%d-%m-%Y %H:%M:%S"
            elif time_stamp == TimeStampFormats.TIME:
                time_stamp_value = "%H:%M:%S"
            elif time_stamp == TimeStampFormats.TIME_EXPLICIT:
                time_stamp_value = "%I%p %M:%S"
            elif time_stamp == TimeStampFormats.DATE_AND_TIME_DOT_SEPARATION:
                time_stamp_value = "%d.%m.%Y %H:%M:%S"
            elif time_stamp is None and time_stamp_as_string[0] == "@":
                time_stamp_as_string = time_stamp_as_string[1::]

                try:
                    date_time.strftime(time_stamp_as_string)
                except:
                    raise InvalidFormatError(f"The provided date time format is not present in the current version of notiblocks: {self.version}")

            if not background_color is None:
                background_color_value = BGColors[background_color].value
                out += f"{ANSI.background(background_color_value)}"

            out += f"{ANSI.color_text(bracket_color_value)}{opening_bracket}{ANSI.color_text(sign_color_value) + date_time.strftime(time_stamp_value) + ANSI.color_text(bracket_color_value)}{closing_bracket} {ANSI.color_text(text_color_value)}{message}"
            out += f"{RESET_STYLE}"

            return out
        else:
            raise InvalidFormatError(f"The provided time format is not present in the current version of notiblocks: {self.version}")


    def format_message(self, text_c: str, sign_c: str, bracket_c: str, sign: str, background_c: str, bracket_t: str, message: str) -> str:
        out = ""

        text_color =        text_c.lower().strip() if text_c is not None else None
        sign_color =        sign_c.lower().strip() if sign_c is not None else None
        bracket_color =     bracket_c.lower().strip() if bracket_c is not None else None
        sign =              sign
        background_color =  background_c.lower().strip() if background_c is not None else None

        bracket_type_str =  bracket_t.upper().strip() if bracket_t is not None else None # str
        opening_bracket = '['
        closing_bracket = ']'

        bracket_type = Brackets[bracket_type_str] # Bracket

        if bracket_type == Brackets.ANGLE:
            opening_bracket = '<'
            closing_bracket = '>'
        elif bracket_type == Brackets.CURLY:
            opening_bracket = '{'
            closing_bracket = '}'
        elif bracket_type == Brackets.ROUND:
            opening_bracket = '('
            closing_bracket = ')'
        elif bracket_type == Brackets.SQUARE:
            opening_bracket = '['
            closing_bracket = ']'
        else:
            if bracket_type_str[0] == '@': # Then it's a custom '\[@s]'
                tokens = bracket_type_str.split('\[@s]')
                opening_bracket = tokens[0].strip()
                closing_bracket = tokens[1].strip()
            else:
                raise InvalidFormatError(f"The provided bracket type is not present in the current version of notiblocks: {self.version}")

        background_color_value = None

        if text_color and sign_color and bracket_color in FGColors.__members__:
            text_color_value =          FGColors[text_color].value
            sign_color_value =          FGColors[sign_color].value
            bracket_color_value =       FGColors[bracket_color].value
            background_color_value =    BGColors.reset.value

            if not background_color is None:
                background_color_value = BGColors[background_color].value
                out += f"{ANSI.background(background_color_value)}"
            
            out += f"{ANSI.color_text(bracket_color_value)}{opening_bracket}{ANSI.color_text(sign_color_value) + sign + ANSI.color_text(bracket_color_value)}{closing_bracket} {ANSI.color_text(text_color_value)}{message}"
            out += f"{RESET_STYLE}"

            return out
        else:
            raise InvalidFormatError("Invalid format!")