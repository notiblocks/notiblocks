# Logger utility for notiblocks
class Logger:
    """
    Logger utility for notiblocks, it provides a simple inline logging functionality.
    """
    def __init__(self):
        pass

        # TODO: add the four types of logging here


    def log(message: str, sign: str):
        if sign.trim() == '':
            sign = '[+]'

        if message.trim == '':
            pass # TODO: Throw and handle an exception

        print(sign, message) 


# Got an idea. Expose only the logger, so you could
# internally configure it, but when it comes to logging,
# use only this utility class.