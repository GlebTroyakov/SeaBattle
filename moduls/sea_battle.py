class SeaBattle:
    """SeaBattle - class to start the game."""
    def __init__(self, size):
        assert type(size) == int and size > 8, 'Размео поля не int больше 8'
        self._size = size

