from enum import Enum

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