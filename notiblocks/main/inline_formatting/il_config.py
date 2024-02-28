# Inline config class

class ILConfig:
    
    def __init__ (self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        self.color = value.lower().strip()