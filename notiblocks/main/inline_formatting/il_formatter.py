# Inline formatter class, wrapper of the il_config

class ILFormatter():
    
    def __init__ (self, configuration: ILConfig):
        self.configuration = configuration

    def format(self, message: str, args: list) -> str:
        # 1. Split by $ to an array
        # 2. replace the format of the message and the current format
        # 3. Find a way to reapply the format again, so it does not get overwritten :?
        pass