from ship import Ship
from random import randint


class GamePole:
    """GamePole - class for working with the playing field."""

    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        """init - creates a field and ships on it."""

        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]

        index_ship = 0
        tmp_ships = self._ships[:]
        while index_ship != len(self._ships):

            x = randint(0, 9)
            y = randint(0, 9)

            tmp_ships[index_ship]._x = x
            tmp_ships[index_ship]._y = y

            this_chip = tmp_ships[index_ship]

            if this_chip._x is not None and this_chip._y is not None:  # если эти координаты допустимы

                if not this_chip.is_out_pole():  # если корабль не выходят за поле
                    ship_ok = True
                    for ship in tmp_ships:
                        if ship != this_chip:
                            if ship._x is not None:
                                if ship.is_collide(this_chip):
                                    ship_ok = False
                                    break
                    if ship_ok:
                        index_ship += 1
        self._ships = tmp_ships[:]

