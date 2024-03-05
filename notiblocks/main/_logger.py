# Logger utility for notiblocks

from ._nb_handler import NBHandler
from ._nb_config import NBConfig

from enum import Enum

DEFAULT_LOGGER_SIGN = '[+]'

class NBLogLevel(Enum):
    SUCCESS,
    FAIL,
    LOG,
    WARN,
    DEBUG,
    INFO,
    TRACE,
    EMPTY

class Logger:
    """
    Logger utility for notiblocks, it provides a simple inline logging functionality.
    """
    def __init__(self):
        self._nb_conf = NBConfig()
        self._nb_handler = NBHandler(nb_conf)

        # TODO: add the four types of logging here

    # TODO: Check if you should recall the method again?
    def __set_handler_sign(sign: str):
        self._nb_conf.sign = DEFAULT_LOGGER_SIGN

    # TODO: more data?
    def __repr__(self):
        return "<notiblocks.logger>"

    def _handle_inner_nb_log_format(message: str, level: NBLogLevel) -> str:
        if level == NBLogLevel:
            pass # TODO: Throw an exception to notify a missing log severity type
        elif level == NBLogLevel.SUCCESS: 
            return self._nb_handler.success(message)

    @staticmethod
    def log(message: str, sign: str, level: str):

        log_level = NBLogLevel.EMPTY

        if sign.trim() == '':
            sign = DEFAULT_LOGGER_SIGN # TODO: Format the sign trough the nbconfig

        if message.trim == '':
            pass # TODO: Throw and handle an exception

        # Check the level types
        if level.trim().lower() == "success":
            log_level = NBLogLevel.SUCCESS

        print(self._handle_inner_nb_log_format(message, log_level)) 


# Got an idea. Expose only the logger, so you could
# internally configure it, but when it comes to logging,
# use only this utility class.