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