

class ILConfig:
    """
    ILConfig is a configuration class for the in-line formatting tool "ILFormatter".
    For the current version it supports only color formatting.
    """
    def __init__ (self, text: str, color: str):
        self._color = color
        self._text = text

    @property
    def color(self) -> str:
        return self._color

    @property
    def text(self) -> str:
        return self._text

    @color.setter
    def color(self, value: str):
        self._color = value.lower().strip()

    @text.setter
    def test(self, value: str):
        self._text = value.lower().strip()