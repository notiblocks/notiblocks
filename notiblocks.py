#          )    )        (        (       )           ) (     
#         ( /( ( /(   *   ))\ )  (  )\ ) ( /(   (    ( /( )\ )  
#        )\()))\())` )  /(()/(( )\(()/( )\())  )\   )\()|()/(  
#       ((_)\((_)\  ( )(_))(_))((_)/(_)|(_)\ (((_)|((_)\ /(_)) 
#       _((_) ((_)(_(_()|_))((_)_(_))   ((_))\___|_ ((_|_))   
#      | \| |/ _ \|_   _|_ _|| _ ) |   / _ ((/ __| |/ // __|  
#     | .` | (_) | | |  | | | _ \ |__| (_) | (__  ' < \__ \  
#    |_|\_|\___/  |_| |___||___/____|\___/ \___|_|\_\|___/  
# ===============================================================                                      
# Easy and colorful terminal notifications for logs and debugging
#                  -- Deyan Sirakov @ 2023 --

# TODO: time format

# imports
from enum import Enum
from datetime import datetime
import calendar
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
DEFAULT_TIME_SIGN = "%H:%M:%S"

DEFAULT_WARN_BACKGROUND_COLOR = None
DEFAULT_FAIL_BACKGROUND_COLOR = None
DEFAULT_SUCCESS_BACKGROUND_COLOR = None
DEFAULT_TIME_BACKGROUND_COLOR = None

DEFAULT_BRACKET_STYLE = Brackets.SQUARE
DEFAULT_IS_UNDERLINED = False


class FGColors(Enum):
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

#TODO: Time stamps as enum

#TODO: Document, Add Background and Underlined

class NBConfig:
    """
    NotiBlocks configuration class
    This class is used to store the configuration details for the NotiBlock handler.

    Attributes:
        warn_color              (str): Color of the warning sign exterior                       @default -> yellow
        fail_color              (str): Color of the failure sign exterior                       @default -> red
        success_color           (str): Color of the success sign exterior                       @default -> green
        time_color              (str): Color of the time stamp sign exterior                    @default -> blue 

        warn_bracket_color      (str): Color of the brackets around the warn sign               @default -> yellow
        fail_bracket_color      (str): Color of the brackets around the fail sign               @default -> red
        success_bracket_color   (str): Color of the brackets around the success sign            @default -> green
        time_bracket_color      (str): Color of the brackets around the time sign               @default -> blue
        
        warn_sign_color         (str): Color of the warning sign                                @default -> white
        fail_sign_color         (str): Color of the failure sign                                @default -> yellow
        success_sign_color      (str): Color of the success sign                                @default -> blue
        time_sign_color         (str): Color of the time stamp sign                             @default -> gray

        warn_sign               (str): The sign, which stays in between the warn braces         @default -> "!"
        fail_sign               (str): The sign, which stays in between the fail braces         @default -> "-"
        success_sign            (str): The sign, which stays in between the success braces      @default -> "+"
        time_sign_stamp         (str): Time stamp instead of sign, for between the braces       @default -> ss:mm:hh   

        warn_background_color   (str): The background behind the warn sigh                      @default -> None
        fail_background_color   (str): The background behind the fail sigh                      @default -> None
        success_background_color(str): The background behind the success sigh                   @default -> None
        time_background_color   (str):The background behind the time sigh                       @default -> None

        is_underlined           (bool): Is the sign underlined?                                 @default -> False
        bracket_style           (Brackets): Type of brackets to be used around the sign         @default -> SQUARE
                (styles: SQUARE, CURLY, ANGLE, ROUND)

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
                    warn_color=DEFAULT_WARN_COLOR, 
                    fail_color=DEFAULT_FAIL_COLOR,
                    success_color=DEFAULT_SUCCESS_COLOR,
                    time_color=DEFAULT_TIME_COLOR,
                    warn_bracket_color=DEFAULT_WARN_BRACKET_COLOR,
                    fail_bracket_color=DEFAULT_FAIL_BRACKET_COLOR,
                    success_bracket_color=DEFAULT_SUCCESS_BRACKET_COLOR,
                    time_bracket_color=DEFAULT_TIME_BRACKET_COLOR,
                    warn_sign_color=DEFAULT_WARN_SIGN_COLOR,
                    fail_sign_color=DEFAULT_FAIL_SIGN_COLOR,
                    success_sign_color=DEFAULT_SUCCESS_SIGN_COLOR,
                    time_sign_color=DEFAULT_TIME_SIGN_COLOR,
                    warn_sign=DEFAULT_WARN_SIGN,
                    fail_sign=DEFAULT_FAIL_SIGN,
                    success_sign=DEFAULT_SUCCESS_SIGN,
                    time_sign_stamp=DEFAULT_TIME_SIGN,
                    warn_background_color=DEFAULT_WARN_BACKGROUND_COLOR,
                    fail_background_color=DEFAULT_FAIL_BACKGROUND_COLOR,
                    success_background_color=DEFAULT_SUCCESS_BACKGROUND_COLOR,
                    time_background_color=DEFAULT_TIME_BACKGROUND_COLOR,
                    bracket_style=DEFAULT_BRACKET_STYLE,
                    is_underlined=DEFAULT_IS_UNDERLINED):
        

        self._warn_color = warn_color
        self._fail_color = fail_color
        self._success_color = success_color
        self._time_color = time_color

        self._warn_bracket_color = warn_bracket_color
        self._fail_bracket_color = fail_bracket_color
        self._success_bracket_color = success_bracket_color
        self._time_bracket_color = time_bracket_color

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
        def bracket_style(self) -> Brackets:
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
        def bracket_style(self, value: Brackets):
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

    def format_message(self, text_c, sign_c, bracket_c, sign, background_c, message):
        out = ""

        text_color =        text_c
        sign_color =        sign_c
        bracket_color =     bracket_c
        sign =              sign
        background_color =  background_c

        background_color_value = None

        if text_color and sign_color and bracket_color in FGColors.__members__:
            text_color_value =          FGColors[text_color].value
            sign_color_value =          FGColors[sign_color].value
            bracket_color_value =       FGColors[bracket_color].value
            background_color_value =    BGColors.reset.value

            if not background_color is None:
                background_color_value = BGColors[background_color].value
                out += f"{ANSI.background(background_color_value)}"
            
            out += f"{ANSI.color_text(bracket_color_value)}[{ANSI.color_text(sign_color_value) + sign + ANSI.color_text(bracket_color_value)}] {ANSI.color_text(text_color_value)}{message}"
            out += f"{RESET_STYLE}"

            return out
        else:
            # TODO: Make it exception
            return ANSI.background(BG_RED) + ANSI.color_text(FG_WHITE)  + f"[!!!] Invalid success color configuration!" + ANSI.background(BG_RESET) + RESET_STYLE
            
    def sucess(self, message) -> str:
        return self.format_message( self.configuration._success_color,
                                    self.configuration._success_sign_color,
                                    self.configuration._success_bracket_color,
                                    self.configuration._success_sign, 
                                    self.configuration._success_background_color,
                                    message=message)

    def warn(self, message) -> str:
        return self.format_message( self.configuration._warn_color,
                                    self.configuration._warn_sign_color,
                                    self.configuration._warn_bracket_color,
                                    self.configuration._warn_sign,
                                    self.configuration._warn_background_color,
                                    message=message)

    def fail(self, message) -> str:
        return self.format_message( self.configuration._fail_color,
                                    self.configuration._fail_sign_color,
                                    self.configuration._fail_bracket_color,
                                    self.configuration._fail_sign, 
                                    self.configuration._fail_background_color,
                                    message=message)
    
    def log(self, message) -> str:
        out = ""
        current_time = time.time()
        date_time = datetime.fromtimestamp(current_time)

        text_color =        self.configuration._time_color
        sign_color =        self.configuration._time_sign_color
        bracket_color =     self.configuration._time_bracket_color
        time_stamp =        self.configuration._time_sign_stamp
        background_color =  self.configuration._time_background_color

        background_color_value = None

        if text_color and sign_color and bracket_color in FGColors.__members__:
            text_color_value =          FGColors[text_color].value
            sign_color_value =          FGColors[sign_color].value
            bracket_color_value =       FGColors[bracket_color].value
            background_color_value =    BGColors.reset.value
            
            if not background_color is None:
                background_color_value = BGColors[background_color].value
                out += f"{ANSI.background(background_color_value)}"

            out += f"{ANSI.color_text(bracket_color_value)}[{ANSI.color_text(sign_color_value) + date_time.strftime(time_stamp) + ANSI.color_text(bracket_color_value)}] {ANSI.color_text(text_color_value)}{message}"
            out += f"{RESET_STYLE}"

            return out
        else:
            # TODO: Make it exception
            return ANSI.background(BG_RED) + ANSI.color_text(FG_WHITE)  + f"[!!!] Invalid success color configuration!" + ANSI.background(BG_RESET) + RESET_STYLE