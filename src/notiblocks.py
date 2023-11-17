#         )    )        (        (       )           ) (     
#      ( /( ( /(   *   ))\ )  (  )\ ) ( /(   (    ( /( )\ )  
#      )\()))\())` )  /(()/(( )\(()/( )\())  )\   )\()|()/(  
#     ((_)\((_)\  ( )(_))(_))((_)/(_)|(_)\ (((_)|((_)\ /(_)) 
#      _((_) ((_)(_(_()|_))((_)_(_))   ((_))\___|_ ((_|_))   
#     | \| |/ _ \|_   _|_ _|| _ ) |   / _ ((/ __| |/ // __|  
#     | .` | (_) | | |  | | | _ \ |__| (_) | (__  ' < \__ \  
#     |_|\_|\___/  |_| |___||___/____|\___/ \___|_|\_\|___/  
# ===============================================================                                      
# Easy and colorful terminal notifications for logs and debugging
#                  -- Deyan Sirakov @ 2023 --

#   TODO: Reformat the names
#   TODO: Repeating code in the logs 
#   TODO: Document, Underlined
#   TODO: Configuration files
#   TODO: Intext backgrounds and underlining

### IMPORTS
from enum import Enum
from datetime import datetime
import time

# ANSI 
class ANSI():
    def background(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)
    
    def style_text(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)
    
    def color_text(ansi_code):
        return "\33[{ansi_code}m".format(ansi_code=ansi_code)

class Brackets(Enum):
    SQUARE = 1
    CURLY = 2
    ANGLE = 3
    ROUND = 4

class TimeStampFormats(Enum):
    """
    Date and time enumeration for indexing the correct timestamp to be used in the `logs`

    Possible options (case insensitive, you can also separate them by white space):
        * DATE_AND_TIME ->                  @example  2021-07-03 16:21:12
        * DATE_AND_TIME_DOT_SEPARATION ->   @example 2021.07.03 16:21:12
        * TIME          ->                  @example  12:51:32
        * DATE          ->                  @example  03 July, 2023
        * TIME_EXPLICIT ->                  @example  04PM 21:12 (HH:MM:SS)

    NOTE: You can add custom timestamps yourself by putting an annotation 
    and then the timestamp value. For example, instead of "TIME_EXPLICIT" you can write "@%I%p %M:%S".
    """
    DATE_AND_TIME = 1
    DATE_AND_TIME_DOT_SEPARATION = 2
    TIME = 3
    DATE = 4
    TIME_EXPLICIT = 5

# ANSI COLORS
RESET_STYLE = "\033[0m"

FG_RESET = 1
FG_BLACK = 30
FG_RED = 31
FG_GREEN = 32
FG_YELLOW = 33
FG_BLUE = 34
FG_MAGENTA = 35
FG_CYAN = 36
FG_WHITE = 37
FG_GRAY = 90
FG_BRIGHT_RED = 91
FG_BRIGHT_GREEN = 92
FG_BRIGHT_YELLOW = 93
FG_BRIGHT_BLUE = 94
FG_BRIGHT_MAGENTA = 95
FG_BRIGHT_CYAN = 96
FG_BRIGHT_WHITE = 97

BG_RESET = 31
BG_BLACK = 40
BG_RED = 41
BG_GREEN = 42
BG_YELLOW = 43
BG_BLUE = 44
BG_MAGENTA = 45
BG_CYAN = 46
BG_WHITE = 47
BG_GRAY = 100
BG_BRIGHT_RED = 101
BG_BRIGHT_GREEN = 102
BG_BRIGHT_YELLOW = 103
BG_BRIGHT_BLUE = 104
BG_BRIGHT_MAGENTA = 105
BG_BRIGHT_CYAN = 106
BG_BRIGHT_WHITE = 107

DEFAULT_WARN_COLOR = "yellow"
DEFAULT_FAIL_COLOR = "red"
DEFAULT_SUCCESS_COLOR = "green"
DEFAULT_TIME_COLOR = "blue"

DEFAULT_WARN_SIGN_COLOR = "yellow"
DEFAULT_FAIL_SIGN_COLOR = "red"
DEFAULT_SUCCESS_SIGN_COLOR = "green"
DEFAULT_TIME_SIGN_COLOR = "blue"

DEFAULT_WARN_BRACKET_COLOR = "yellow"
DEFAULT_FAIL_BRACKET_COLOR = "red"
DEFAULT_SUCCESS_BRACKET_COLOR = "green"
DEFAULT_TIME_BRACKET_COLOR = "blue"

DEFAULT_WARN_SIGN = "!"
DEFAULT_FAIL_SIGN = "-"
DEFAULT_SUCCESS_SIGN = "+"
DEFAULT_TIME_SIGN = "TIME"

DEFAULT_WARN_BRACKET_SIGN = None
DEFAULT_FAIL_BRACKET_SIGN = None
DEFAULT_SUCCESS_BRACKET_SIGN = None
DEFAULT_TIME_BRACKET_SIGN = None

DEFAULT_WARN_BACKGROUND_COLOR = None
DEFAULT_FAIL_BACKGROUND_COLOR = None
DEFAULT_SUCCESS_BACKGROUND_COLOR = None
DEFAULT_TIME_BACKGROUND_COLOR = None

DEFAULT_BRACKET_STYLE = "SQUARE"
DEFAULT_IS_UNDERLINED = False


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

class NBConfig:
    """
    NotiBlocks configuration class
    This class is used to store the configuration details for the NotiBlock handler.

    Attributes:
        warn_color              (str): Color of the warning sign exterior                                   @default -> yellow
        fail_color              (str): Color of the failure sign exterior                                   @default -> red
        success_color           (str): Color of the success sign exterior                                   @default -> green
        time_color              (str): Color of the time stamp sign exterior                                @default -> blue 

        warn_bracket_color      (str): Color of the brackets around the warn sign                           @default -> yellow
        fail_bracket_color      (str): Color of the brackets around the fail sign                           @default -> red
        success_bracket_color   (str): Color of the brackets around the success sign                        @default -> green
        time_bracket_color      (str): Color of the brackets around the time sign                           @default -> blue
        
        warn_bracket_sign       (str): Bracket style, which is going to be applied on warning               @default -> None
        fail_bracket_sign       (str): Bracket style, which is going to be applied on failure               @default -> None
        success_bracket_sign    (str): Bracket style, which is going to be applied on success               @default -> None
        time_bracket_sign       (str): Bracket style, which is going to be applied on a log                 @default -> None

        warn_sign_color         (str): Color of the warning sign                                            @default -> white
        fail_sign_color         (str): Color of the failure sign                                            @default -> yellow
        success_sign_color      (str): Color of the success sign                                            @default -> blue
        time_sign_color         (str): Color of the time stamp sign                                         @default -> gray

        warn_sign               (str): The sign, which stays in between the warn braces                     @default -> "!"
        fail_sign               (str): The sign, which stays in between the fail braces                     @default -> "-"
        success_sign            (str): The sign, which stays in between the success braces                  @default -> "+"
        time_sign_stamp         (str): Time stamp instead of sign, for between the braces                   @default -> ss:mm:hh   

        warn_background_color   (str): The background behind the warn sigh                                  @default -> None
        fail_background_color   (str): The background behind the fail sigh                                  @default -> None
        success_background_color(str): The background behind the success sigh                               @default -> None
        time_background_color   (str):The background behind the time sigh                                   @default -> None

        is_underlined           (bool): Is the sign underlined?                                             @default -> False
        bracket_style           (str): Type of brackets to be used around the sign                          @default -> None
                (styles: SQUARE, CURLY, ANGLE, ROUND)
                Note: If you want to make your own bracket types, follow the pattern: @{opening_bracket}\[@s]{closing_bracket}
                This way the program would know how to split the provided brackets

    Supported colors:
        * black
        * red
        * green,
        * yellow
        * blue
        * magenta
        * cyan
        * white (bright gray)
        * gray (bright black)
        * bright_red
        * bright_green
        * bright_yellow
        * bright_blue
        * bright_magenta
        * bright_cyan
        * bright_white (actual white)

    Depending on your approach, you can set the attributes directly trough the constructor, or you can use the defined getters and setters.
    """
    def __init__(self,
                    warn_color =                DEFAULT_WARN_COLOR, 
                    fail_color =                DEFAULT_FAIL_COLOR,
                    success_color =             DEFAULT_SUCCESS_COLOR,
                    time_color =                DEFAULT_TIME_COLOR,
                    warn_bracket_color =        DEFAULT_WARN_BRACKET_COLOR,
                    fail_bracket_color =        DEFAULT_FAIL_BRACKET_COLOR,
                    success_bracket_color =     DEFAULT_SUCCESS_BRACKET_COLOR,
                    time_bracket_color =        DEFAULT_TIME_BRACKET_COLOR,
                    warn_bracket_sign =         DEFAULT_WARN_BRACKET_SIGN,
                    fail_bracket_sign =         DEFAULT_FAIL_BRACKET_SIGN,
                    success_bracket_sign =      DEFAULT_SUCCESS_BRACKET_SIGN,
                    time_bracket_sign =         DEFAULT_TIME_BRACKET_SIGN,
                    warn_sign_color =           DEFAULT_WARN_SIGN_COLOR,
                    fail_sign_color =           DEFAULT_FAIL_SIGN_COLOR,
                    success_sign_color =        DEFAULT_SUCCESS_SIGN_COLOR,
                    time_sign_color =           DEFAULT_TIME_SIGN_COLOR,
                    warn_sign =                 DEFAULT_WARN_SIGN,
                    fail_sign =                 DEFAULT_FAIL_SIGN,
                    success_sign =              DEFAULT_SUCCESS_SIGN,
                    time_sign_stamp =           DEFAULT_TIME_SIGN,
                    warn_background_color =     DEFAULT_WARN_BACKGROUND_COLOR,
                    fail_background_color =     DEFAULT_FAIL_BACKGROUND_COLOR,
                    success_background_color =  DEFAULT_SUCCESS_BACKGROUND_COLOR,
                    time_background_color =     DEFAULT_TIME_BACKGROUND_COLOR,
                    bracket_style =             DEFAULT_BRACKET_STYLE,
                    is_underlined =             DEFAULT_IS_UNDERLINED):

        self._warn_color = warn_color
        self._fail_color = fail_color
        self._success_color = success_color
        self._time_color = time_color

        self._warn_bracket_color = warn_bracket_color
        self._fail_bracket_color = fail_bracket_color
        self._success_bracket_color = success_bracket_color
        self._time_bracket_color = time_bracket_color  

        self._warn_bracket_sign = warn_bracket_sign
        self._fail_bracket_sign = fail_bracket_sign
        self._success_bracket_sign = success_bracket_sign
        self._time_bracket_sign = time_bracket_sign

        self._warn_sign_color = warn_sign_color
        self._fail_sign_color = fail_sign_color
        self._success_sign_color = success_sign_color
        self._time_sign_color = time_sign_color
        
        self._warn_sign = warn_sign
        self._fail_sign = fail_sign
        self._success_sign = success_sign
        self._time_sign_stamp = time_sign_stamp

        self._warn_background_color = warn_background_color
        self._fail_background_color = fail_background_color
        self._success_background_color = success_background_color
        self._time_background_color = time_background_color

        self._bracket_style = bracket_style
        self._is_underlined = is_underlined

        @property
        def warn_color(self) -> str:
            return self._warn_color
        
        @property
        def fail_color(self) -> str:
            return self._fail_color
        
        @property 
        def success_color(self) -> str:
            return self._success_color
        
        @property
        def time_color(self) -> str:
            return self._time_color
        
        @property
        def warn_bracket_color(self) -> str:
            return self._warn_bracket_color
        
        @property
        def fail_bracket_color(self) -> str:
            return self._fail_bracket_color
        
        @property
        def success_bracket_color(self) -> str:
            return self._success_bracket_color
        
        @property
        def time_bracket_color(self) -> str:
            return self._time_bracket_color

        @property
        def warn_bracket_sign(self) -> str:
            return self._warn_bracket_sign
        
        @property
        def fail_bracket_sign(self) -> str:
            return self._fail_bracket_sign
        
        @property
        def success_bracket_sign(self) -> str:
            return self._success_bracket_sign
        
        @property
        def time_bracket_sign(self) -> str:
            return self._time_bracket_sign

        @property
        def warn_sign_color(self) -> str:
            return self._warn_sign_color
        
        @property
        def fail_sign_color(self) -> str:
            return self._fail_sign_color
        
        @property
        def success_sign_color(self) -> str:
            return self._success_sign_color
        
        @property
        def time_sign_color(self) -> str:
            return self._time_sign_color

        @property
        def warn_sign(self) -> str:
            return self._warn_sign

        @property
        def fail_sign(self) -> str:
            return self._fail_sign 

        @property
        def success_sign(self) -> str:
            return self._success_sign       

        @property
        def time_sign_stamp(self) -> str:
            return self._time_sign_stamp
        
        @property
        def warn_background_color(self) -> str:
            return self._warn_background_color
        
        @property
        def fail_background_color(self) -> str:
            return self._fail_background_color
        
        @property
        def success_background_color(self) -> str:
            return self._success_background_color
        
        @property
        def time_background_color(self) -> str:
            return self._time_background_color
        
        @property
        def bracket_style(self) -> str:
            return self._bracket_style
        
        @property
        def is_underlined(self) -> bool:
            return self._is_underlined

        @warn_color.setter
        def warn_color(self, value: str):
            self._warn_color = value.lower().strip()
        
        @fail_color.setter
        def fail_color(self, value: str):
            self._fail_color = value.lower().strip()
        
        @success_color.setter 
        def success_color(self, value: str):
            self._success_color = value.lower().strip()
        
        @time_color.setter
        def time_color(self, value: str):
            self._time_color = value.lower().strip()
        
        @warn_bracket_color.setter
        def warn_bracket_color(self, value: str):
            self._warn_bracket_color = value.lower().strip()

        @fail_bracket_color.setter
        def fail_bracket_color(self, value: str):
            self._fail_bracket_color = value.lower().strip()

        @success_bracket_color.setter
        def success_bracket_color(self, value: str):
            self._success_bracket_color = value.lower().strip()

        @time_bracket_color.setter
        def time_bracket_color(self, value: str):
            self._time_bracket_color = value.lower().strip()

        @warn_bracket_sign.setter
        def warn_bracket_sign(self, value: str):
            self._warn_bracket_sign = value.strip()

        @fail_bracket_sign.setter
        def fail_bracket_sign(self, value: str):
            self._fail_bracket_sign = value.strip()

        @success_bracket_sign.setter
        def success_bracket_sign(self, value: str):
            self._success_bracket_sign = value.strip()

        @time_bracket_sign.setter
        def time_bracket_sign(self, value: str):
            self._time_bracket_sign = value.strip() 

        @warn_sign_color.setter
        def warn_sign_color(self, value: str):
            self._warn_sign_color = value.lower().strip()
        
        @fail_sign_color.setter
        def fail_sign_color(self, value: str):
            self._fail_sign_color = value.lower().strip()
        
        @success_sign_color.setter
        def success_sign_color(self, value: str):
            self._success_sign_color = value.lower().strip()
        
        @time_sign_color.setter
        def time_sign_color(self, value: str):
            self._time_sign_color = value.lower().strip()

        @warn_sign.setter
        def warn_sign(self, value: str):
            self._warn_sign = value.lower().strip()

        @fail_sign.setter
        def fail_sign(self, value: str):
            self._fail_sign = value.lower().strip()

        @success_sign.setter
        def success_sign(self, value: str):
            self._success_sign = value.lower().strip()

        @time_sign_stamp.setter
        def time_sign_stamp(self, value: str):
            self._time_sign_stamp = value.lower().strip()

        @warn_background_color.setter
        def warn_background_color(self, value: str):
            self._warn_background_color = value.lower().strip()

        @fail_background_color.setter
        def fail_background_color(self, value: str):
            self._fail_background_color = value.lower().strip()

        @success_background_color.setter
        def success_background_color(self, value: str):
            self._success_background_color = value.lower().strip()

        @time_background_color.setter
        def time_background_color(self, value: str):
            self._time_background_color = value.lower().strip()

        @bracket_style.setter
        def bracket_style(self, value: str):
            self._bracket_style = value

        @is_underlined.setter
        def is_underlined(self, value: bool):
            self._is_underlined = value


# Notification Block Handler
class NBHandler:
    def __init__(self, configuration: NBConfig):
        if configuration is None:
            configuration = NBConfig()
        else:
            self.configuration = configuration

    def format_message(self, text_c, sign_c, bracket_c, sign, background_c, bracket_t, message):
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
            
    def success(self, message) -> str: 
        bracket_sign = self.configuration._success_bracket_sign if self.configuration._success_bracket_sign is not None else self.configuration._bracket_style

        try:
            return self.format_message( self.configuration._success_color,
                                        self.configuration._success_sign_color,
                                        self.configuration._success_bracket_color,
                                        self.configuration._success_sign, 
                                        self.configuration._success_background_color,
                                        bracket_t=bracket_sign,
                                        message=message)
        except InvalidFormatError as ie:
            print(ie)

    def warn(self, message) -> str:
        bracket_sign = self.configuration._warn_bracket_sign if self.configuration._warn_bracket_sign is not None else self.configuration._bracket_style

        try:
            return self.format_message( self.configuration._warn_color,
                                        self.configuration._warn_sign_color,
                                        self.configuration._warn_bracket_color,
                                        self.configuration._warn_sign,
                                        self.configuration._warn_background_color,
                                        bracket_t=bracket_sign,
                                        message=message)
        except InvalidFormatError as ie:
            print(ie)

    def fail(self, message) -> str:
        bracket_sign = self.configuration._fail_bracket_sign if self.configuration._fail_bracket_sign is not None else self.configuration._bracket_style

        try:
            return self.format_message( self.configuration._fail_color,
                                        self.configuration._fail_sign_color,
                                        self.configuration._fail_bracket_color,
                                        self.configuration._fail_sign, 
                                        self.configuration._fail_background_color,
                                        bracket_t=bracket_sign,
                                        message=message)
        except InvalidFormatError as ie:
            print(ie)

    def log(self, message) -> str:
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
                raise InvalidFormatError("Invalud bracket type!")

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
                    raise InvalidFormatError("The provided date time format is invalid")

            if not background_color is None:
                background_color_value = BGColors[background_color].value
                out += f"{ANSI.background(background_color_value)}"

            out += f"{ANSI.color_text(bracket_color_value)}{opening_bracket}{ANSI.color_text(sign_color_value) + date_time.strftime(time_stamp_value) + ANSI.color_text(bracket_color_value)}{closing_bracket} {ANSI.color_text(text_color_value)}{message}"
            out += f"{RESET_STYLE}"

            return out
        else:
            raise InvalidFormatError("Invalid time format")
            
# FAILSON: time_sign_color="GrEEn"