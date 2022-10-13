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

    def is_collide(self, ship):
        """is_collide - checking for a collision with another ship (a collision is considered if another ship
        either intersects with the current one or simply touches, including diagonally);

        Return True - if is a collision, else - return False."""

        assert isinstance(ship, Ship), 'ship не экземпляр Ship'
        if self._tp == 1:
            x_start = self._x - 1
            x_end = self._x + self._length
            y_start = self._y - 1
            y_end = self._y + 1

        elif self._tp == 2:
            x_start = self._x - 1
            x_end = self._x + 1
            y_start = self._y - 1
            y_end = self._y + self._length

        if ship._tp == 1:
            ship_x_start = ship._x
            ship_x_stop = ship._x + ship._length - 1
            ship_y_start = ship_y_stop = ship._y

        elif ship._tp == 2:
            ship_x_start = ship_x_stop = ship._x
            ship_y_start = ship._y
            ship_y_stop = ship._y + ship._length - 1

        if x_start <= ship_x_start <= x_end and y_start <= ship_y_start <= y_end:
            return True

        if x_start <= ship_x_stop <= x_end and y_start <= ship_y_stop <= y_end:
            return True

        return False


if __name__ == "__main__":
    s = Ship(1)
    s2 = Ship(1, 1, 2, 5)
    s.set_start_coords(1, 2)
    print(s.get_start_coords())
    s3 = Ship(1, 1, 3, 4)
    print(s2.is_collide(s3))
    s4 = Ship(1, 1, 6, 6)
    print(s2.is_collide(s4))
