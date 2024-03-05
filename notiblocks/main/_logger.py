# Logger utility for notiblocks

DEFAULT_LOGGER_SIGN = '[+]'

class Logger:
    """
    Logger utility for notiblocks, it provides a simple inline logging functionality.
    """
    def __init__(self):
        pass

        # TODO: add the four types of logging here

    # TODO: more data?
    def __repr__(self):
        return "<notiblocks.logger>"

    @staticmethod
    def log(message: str, sign: str):
        if sign.trim() == '':
            sign = DEFAULT_LOGGER_SIGN

        if message.trim == '':
            pass # TODO: Throw and handle an exception

        print(sign, message) 


# Got an idea. Expose only the logger, so you could
# internally configure it, but when it comes to logging,
# use only this utility class.