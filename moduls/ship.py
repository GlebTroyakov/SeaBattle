class Ship:
    """Ship - class for create ships."""

    def __init__(self, length, tp=1, x=None, y=None):
        """length - ship length;
        tp - ship orientation (1 - horizontal; 2 - vertical).;
        x, y - coordinates of the beginning of the location of the ship (integer);
        cells - a list of length length, consisting of ones, when hitting the ship, the cell will change from 1 to 0."""
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._cells = [1] * self._length