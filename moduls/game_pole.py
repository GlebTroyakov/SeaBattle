from ship import Ship
from random import randint, choice


class GamePole:
    """GamePole - class for working with the playing field."""

    def __init__(self, size=10):
        self._size = size
        self._ships = []

    def init(self):
        """init - creates a field and ships on it."""

        self._ships = [Ship(4, tp=randint(1, 2), size=self._size), Ship(3, tp=randint(1, 2), size=self._size),
                       Ship(3, tp=randint(1, 2), size=self._size), Ship(2, tp=randint(1, 2), size=self._size),
                       Ship(2, tp=randint(1, 2), size=self._size), Ship(2, tp=randint(1, 2), size=self._size),
                       Ship(1, tp=randint(1, 2), size=self._size), Ship(1, tp=randint(1, 2), size=self._size),
                       Ship(1, tp=randint(1, 2), size=self._size), Ship(1, tp=randint(1, 2), size=self._size)]

        index_ship = 0
        tmp_ships = self.get_ships()[:]
        while index_ship != len(self.get_ships()):

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

    def get_ships(self):
        return self._ships

    def show(self):
        pole = self.get_pole()
        for row in pole:
            print(*row)

    def get_pole(self):
        pole = [['.' for _ in range(self._size)] for _ in range(self._size)]
        for ship in self.get_ships():
            for cell in range(ship._length):
                if ship._tp == 1:
                    pole[ship._y][ship._x + cell] = 1
                elif ship._tp == 2:
                    pole[ship._y + cell][ship._x] = 1
        return pole

    def move_ships(self, coords_shots=[]):
        for ship in self.get_ships():
            go = choice((-1, 1))

            if ship.move(go, coords_shots):  # если движение возможно то двигаем
                for another_shop in self.get_ships():  # идем по осталньым кораблям
                    if another_shop != ship:  #
                        if another_shop.is_collide(ship):  # если другой окарабль соприкасается с ПЕРЕДВИНУТЫМ

                            go *= -1  # то возвращаемя на шаг назад
                            ship.move(go, coords_shots)  #
                            if ship.move(go, coords_shots):  # проверяем еще шаг в обратном направлении и если он возможен
                                for another_shop_2 in self.get_ships():  # то проверяем другие корабли рна соприкоснование
                                    if another_shop_2 != ship:  #
                                        if another_shop_2.is_collide(ship):  # если снова столкновение

                                            go *= -1  # то меняем шаг
                                            ship.move(go, coords_shots)  # возвращяем корабль на место
            else:  # если жвиени в том направлении сразу обломалось
                go *= -1  # то меняем его
                if ship.move(go, coords_shots):  # проверяем двжиение в новом + ДЕЛАЕМ ШАГ
                    for another_shop in self.get_ships():
                        if another_shop != ship:
                            if another_shop.is_collide(ship):  # если не получилось

                                go *= -1
                                ship.move(go, coords_shots)
                else:  # если и в другую сторону нельзя то возвращаем снова на шаг назад
                    go *= -1
                    ship.move(go, coords_shots)


if __name__ == "__main__":
    p = GamePole(10)
    p.init()
    p.show()
    p.move_ships()
    print('___________________')
    p.show()
    p.move_ships()
    print('___________________')
    p.show()
    p.move_ships()
    print('___________________')
    p.show()