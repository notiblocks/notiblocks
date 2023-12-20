from .constants import *

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

class PosHolder:
        def __init__(self) -> None:
            self._format_type = "undefined"
            self._start_pos = 0
            self._end_pos = 0

        @property
        def format_type(self) -> str:
            return self._format_type
        
        @property
        def start_pos(self) -> int:
            return self._start_pos
        
        @property
        def end_pos(self) -> int:
            return self._end_pos
        
        @format_type.setter
        def format_type(self, value: str):
            self._format_type = value

        @start_pos.setter
        def start_pos(self, value: int):
            self._start_pos = value

        @end_pos.setter
        def end_pos(self, value: int):
            self._end_pos = value