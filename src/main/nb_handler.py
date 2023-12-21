from .nb_config import NBConfig
from .enums.brackets import Brackets

from .enums.nb_inline import NBInline

from .error.invalid_format_error import InvalidFormatError

from .enums.colors.bgcolors import BGColors
from .enums.colors.fgcolors import FGColors

from .constants import RESET_STYLE

from .enums.timestampformat import TimeStampFormats

from .posholder import PosHolder

from .ansi import ANSI

import time
from datetime import datetime
import time

class NBHandler:
    
    """
    NB Handler class..
    Document that shi
    """
         
    def __init__(self, configuration: NBConfig):

        if configuration is None:
            configuration = NBConfig()
        else:
            self.configuration = configuration

    
    def handle_message(self, message, color_prop, bracket_color_prop, bracket_sign_prop, sign_color_prop, sign_prop):
        try:
            return self.format_message(
                getattr(self, color_prop, None),
                getattr(self, sign_color_prop, None),
                getattr(self, bracket_color_prop, None),
                getattr(self, sign_prop, None),
                None,  # Assuming no background color needed for notifications
                bracket_t=getattr(self, bracket_sign_prop, None),
                message=message
            )
        except InvalidFormatError as ie:
            print(ie)
            # Handle the error appropriately

    def warn(self, message):
        return self.handle_message(message, '_warn_color', '_warn_bracket_color', '_warn_bracket_sign', '_warn_sign_color', '_warn_sign')

    def fail(self, message):
        return self.handle_message(message, '_fail_color', '_fail_bracket_color', '_fail_bracket_sign', '_fail_sign_color', '_fail_sign')

    def success(self, message):
        return self.handle_message(message, '_success_color', '_success_bracket_color', '_success_bracket_sign', '_success_sign_color', '_success_sign')

    def log(self, message):
        # Logic for logging with timestamp, etc.
        pass

    def format_message(self, text_c, sign_c, bracket_c, sign, background_c, bracket_t, message):
        out = ""

        # TODO: line parsing?

        # @{%RESET%}
        has_format = False
        message_ptr = 0
        format_contents = []
        while message_ptr < len(message):
            if message[message_ptr] == '@' and message[message_ptr + 1] == '{' and message[message_ptr + 2] == '%':
                has_format = True
                format_holder = PosHolder()
                format_holder.format_type = ""
                format_holder.start_pos = message_ptr
                format_holder.end_pos = 0
                
                message_ptr += 3 # move to the block after the iterator

                while message[message_ptr] != '%' and message[message_ptr + 1] != '}': # We hit a pass
                    format_holder.format_type += message[message_ptr]
                    message_ptr += 1

                message_ptr += 1
                format_holder.end_pos = message_ptr
                format_contents.append(format_holder)
            else: # No expression, so we move the iterator
                message_ptr += 1

        # This is a @{%TEST%} message
        # ['This is a', '@{%TEST%} successful message']
        
        if has_format:
            message_token_pointer = 0
            message_tokens = message.split("@")
            formatted_tokens = []
            for token in message_tokens: # Iterate over all of the message tokens
                if token[0] == '{' and token[1] == '%': # Check if we are at the right content
                    current_format = format_contents[message_token_pointer]

                    end_length = current_format.end_pos - current_format.start_pos
                    token = token[end_length::]
                    message_token_pointer += 1    

                    # TODO: Apply the format
                    # 1. Create a new ANSI object
                    # 2. Find the formating that is needed
                    # 3. Map and apply the formatting
                    # 4. Add the format as a string
                    # 5. put the stirng in the tokens


                token = token.strip()
                formatted_tokens.append(token)

            message = " ".join(formatted_tokens)
            print(message)

        # TODO: Apply formating where needed
        # TODO: Add time as a format :D

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
                raise InvalidFormatError("Invalud bracket type!")

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
            
    # def success(self, message) -> str: 
    #     bracket_sign = self.configuration._success_bracket_sign if self.configuration._success_bracket_sign is not None else self.configuration._bracket_style

    #     try:
    #         return self.format_message( self.configuration._success_color,
    #                                     self.configuration._success_sign_color,
    #                                     self.configuration._success_bracket_color,
    #                                     self.configuration._success_sign, 
    #                                     self.configuration._success_background_color,
    #                                     bracket_t=bracket_sign,
    #                                     message=message)
    #     except InvalidFormatError as ie:
    #         print(ie)

    # def warn(self, message) -> str:
    #     bracket_sign = self.configuration._warn_bracket_sign if self.configuration._warn_bracket_sign is not None else self.configuration._bracket_style

    #     try:
    #         return self.format_message( self.configuration._warn_color,
    #                                     self.configuration._warn_sign_color,
    #                                     self.configuration._warn_bracket_color,
    #                                     self.configuration._warn_sign,
    #                                     self.configuration._warn_background_color,
    #                                     bracket_t=bracket_sign,
    #                                     message=message)
    #     except InvalidFormatError as ie:
    #         print(ie)

    # def fail(self, message) -> str:
    #     bracket_sign = self.configuration._fail_bracket_sign if self.configuration._fail_bracket_sign is not None else self.configuration._bracket_style

    #     try:
    #         return self.format_message( self.configuration._fail_color,
    #                                     self.configuration._fail_sign_color,
    #                                     self.configuration._fail_bracket_color,
    #                                     self.configuration._fail_sign, 
    #                                     self.configuration._fail_background_color,
    #                                     bracket_t=bracket_sign,
    #                                     message=message)
    #     except InvalidFormatError as ie:
    #         print(ie)

    # def log(self, message) -> str:
    #     out = ""
    #     current_time = time.time()
    #     date_time = datetime.fromtimestamp(current_time)

    #     text_color =        self.configuration._time_color.lower().strip() if self.configuration._time_color is not None else None
    #     sign_color =        self.configuration._time_sign_color.lower().strip() if self.configuration._time_sign_color is not None else None
    #     bracket_color =     self.configuration._time_bracket_color.lower().strip() if self.configuration._time_bracket_color is not None else None
    #     time_stamp_ext =    self.configuration._time_sign_stamp
    #     background_color =  self.configuration._time_background_color.lower().strip() if self.configuration._time_background_color is not None else None

    #     bracket_type_str =  bracket_sign = self.configuration._time_bracket_sign if self.configuration._time_bracket_sign is not None else self.configuration._bracket_style
    #     opening_bracket = '['
    #     closing_bracket = ']'

    #     bracket_type_str = bracket_type_str.upper().strip() # Format the bracket type correctly

    #     bracket_type = Brackets[bracket_type_str] # Bracket

    #     if bracket_type == Brackets.ANGLE:
    #         opening_bracket = '<'
    #         closing_bracket = '>'
    #     elif bracket_type == Brackets.CURLY:
    #         opening_bracket = '{'
    #         closing_bracket = '}'
    #     elif bracket_type == Brackets.ROUND:
    #         opening_bracket = '('
    #         closing_bracket = ')'
    #     elif bracket_type == Brackets.SQUARE:
    #         opening_bracket = '['
    #         closing_bracket = ']'
    #     else:
    #         if bracket_type_str[0] == '@': # Then it's a custom '\[@s]'
    #             tokens = bracket_type_str.split('\[@s]')
    #             opening_bracket = tokens[0].strip()
    #             closing_bracket = tokens[1].strip()
    #         else:
    #             raise InvalidFormatError("Invalud bracket type!")

    #     background_color_value = None
    #     time_stamp_value = None

    #     if text_color and sign_color and bracket_color in FGColors.__members__:
    #         text_color_value =          FGColors[text_color].value
    #         sign_color_value =          FGColors[sign_color].value
    #         bracket_color_value =       FGColors[bracket_color].value
    #         background_color_value =    BGColors.reset.value
    #         time_stamp_value =          "%H:%M:%S" # Fallback

    #         time_stamp_as_string = '_'.join(time_stamp_ext.split(' ')).upper()

    #         time_stamp = TimeStampFormats[time_stamp_as_string]

    #         if time_stamp == TimeStampFormats.DATE:
    #             time_stamp_value = "%d %B, %Y"
    #         elif time_stamp == TimeStampFormats.DATE_AND_TIME:
    #             time_stamp_value = "%d-%m-%Y %H:%M:%S"
    #         elif time_stamp == TimeStampFormats.TIME:
    #             time_stamp_value = "%H:%M:%S"
    #         elif time_stamp == TimeStampFormats.TIME_EXPLICIT:
    #             time_stamp_value = "%I%p %M:%S"
    #         elif time_stamp == TimeStampFormats.DATE_AND_TIME_DOT_SEPARATION:
    #             time_stamp_value = "%d.%m.%Y %H:%M:%S"
    #         elif time_stamp is None and time_stamp_as_string[0] == "@":
    #             time_stamp_as_string = time_stamp_as_string[1::]

    #             try:
    #                 date_time.strftime(time_stamp_as_string)
    #             except:
    #                 raise InvalidFormatError("The provided date time format is invalid")

    #         if not background_color is None:
    #             background_color_value = BGColors[background_color].value
    #             out += f"{ANSI.background(background_color_value)}"

    #         out += f"{ANSI.color_text(bracket_color_value)}{opening_bracket}{ANSI.color_text(sign_color_value) + date_time.strftime(time_stamp_value) + ANSI.color_text(bracket_color_value)}{closing_bracket} {ANSI.color_text(text_color_value)}{message}"
    #         out += f"{RESET_STYLE}"

    #         return out
    #     else:
    #         raise InvalidFormatError("Invalid time format")