class Ship:
    """Ship - class for create ships."""

    def __init__(self, length, size=10, tp=1, x=None, y=None):
        """length - ship length;
        tp - ship orientation (1 - horizontal; 2 - vertical).;
        x, y - coordinates of the beginning of the location of the ship (integer);
        cells - a list of length length, consisting of ones, when hitting the ship, the cell will change from 1 to 0."""

        self._length = length
        self._size = size
        self._tp = tp
        self._x = x
        self._y = y
        self._cells = [1] * self._length
        self._is_move = True

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
                    if 0 <= value < self._size and value + self._length - 1 < self._size:
                        super().__setattr__(key, value)
                else:
                    if 0 <= value < self._size:
                        super().__setattr__(key, value)
                    
        elif key == '_cells':
            assert isinstance(value, list) and len(value) == self._length, 'Неверные палубы для карабля'
            super().__setattr__(key, value)

        elif key == '_size':
            assert type(value) == int and value > 8, 'Неверный размер поля'
            super().__setattr__(key, value)

        elif key == '_is_move':
            assert value in (True, False), '_is_move только булевое значение'
            super().__setattr__(key, value)

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

    def is_out_pole(self, size=10):
        if (not 0 <= self._x <= size - 1) or (not 0 <= self._y <= size - 1):
            return True

        if (self._tp == 1 and self._x + self._length > size) or (self._tp == 2 and self._y + self._length > size):
            return True

        return False

    def check_index_cells(self, index):
        assert type(index) == int, 'Индекс палубы не целое число'
        assert 0 <= index < self._length, 'У данного карабля такой палубы нет'

    def __getitem__(self, item):
        self.check_index_cells(item)
        return self._cells[item]

    def __setitem__(self, key, value):
        self.check_index_cells(key)
        assert value in (1, 0), 'Неверное значение для палубы'
        self._cells[key] = value

    def move(self, go, coords_shots=[]):
        if self._is_move and go in (-1, 1):
            if self.check_move(go, coords_shots):
                if self._tp == 1:
                    self._x += go
                    return True

                elif self._tp == 2:
                    self._y += go
                    return True

    def check_move(self, go, coords_shots):
        tmp_ship = Ship(length=self._length, tp=self._tp, x=self._x, y=self._y, size=self._size)
        assert type(tmp_ship._x) == int, 'Не двигать корабль без x и y'
        if tmp_ship._tp == 1:
            tmp_ship._x += go

            if not tmp_ship.is_out_pole():
                if (tmp_ship._x, tmp_ship._y) in coords_shots:
                    return False
                return True

        if tmp_ship._tp == 2:
            tmp_ship._y += go

            if not tmp_ship.is_out_pole():
                if (tmp_ship._x, tmp_ship._y) in coords_shots:
                    return False
                return True

        return False


if __name__ == "__main__":
    s = Ship(1, 10, 1, 4, 5)
    s.move(1)
