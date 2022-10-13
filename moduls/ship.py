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

    def __setattr__(self, key, value):
        if key == '_length':
            assert type(value) == int and 0 <= value <= 4, 'Неверная длина корабля'
            super().__setattr__(key, value)

        elif key == '_tp':
            assert value in (1, 2), 'Неверное положение корабля'
            super().__setattr__(key, value)
            
        elif key in ('_x', '_y'):
            if value is None:
                super().__setattr__(key, value)
            else:
                assert type(value) == int, 'Координаты корабля не int'
                if (key == '_x' and self._tp == 1) or (key == '_y' and self._tp == 2):
                    assert 0 <= value < 10 and value + self._length - 1 < 10, 'Карабль такой длинны не на этих x, y'
                    super().__setattr__(key, value)
                else:
                    assert 0 <= value < 10, 'Карабль за координатами поля'
                    super().__setattr__(key, value)
                    
        elif key == '_cells':
            assert isinstance(value, list) and len(value) == self._length, 'Неверные палубы для карабля'
            super(Ship, self).__setattr__(key, value)

        else:
            raise ValueError('Не создавать новые атрибуты кораблям')

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

if __name__ == "__main__":
    s = Ship(1)
    s2 = Ship(1, 1, 2, 5)
    s.set_start_coords(1, 2)
    print(s.get_start_coords())