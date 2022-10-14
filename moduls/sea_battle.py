from game_pole import GamePole
from random import randint


class SeaBattle:
    """SeaBattle - class to start the game."""
    def __init__(self, size):
        assert type(size) == int and size > 8, 'Размер поля не int или больше 8'
        self._size = size
        self._man = GamePole(self._size)  # сделать init в методе для запуска игры
        self._man_pole_for_shot = self._man.get_pole()
        self._man_pole_for_ships = self._man.get_pole()
        self._computer = GamePole(self._size)

    def step(self, player):
        if player == 1:
            x, y = map(int, input('Введите координаты x и y через пробел: ').split())

            while not 1 <= x <= self._size or not 1 <= y <= self._size:
                print('Координаты за предеалми поля, нужен повторный ввод.')
                x, y = map(int, input('Введите координаты x и y через пробел: ').split())

            x -= 1
            y -= 1

            hit = False

            for ship in self._computer.get_ships():
                if self.check_shot(ship, x, y):  # если попал
                    hit = True
                    self._man_pole_for_shot[y][x] = 'X'

                    if self.check_health_ship(ship):  # если корабль убит
                        print('<<<Убит корабль компа>>>')

                        self._computer._ships.remove(ship)

                    else:
                        print('<<<Ранен корабль компа>>>')
                    break

            if hit is False:
                print('<<<Промах по компу>>>')
                self._man_pole_for_shot[y][x] = 'O'

            self._show_man_pole_shots()

        if player == 2:
            shot = True

            while shot:

                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)

                if self._man_pole_ships[y][x] in ('.', '1', 1):
                    hit = False
                    for ship in self._man.get_ships():
                        if self.check_shot(ship, x, y):  # если попал
                            self._man_pole_ships[y][x] = 'X'
                            hit = True
                            if self.check_health_ship(ship):  # если корабль убит
                                self._man._ships.remove(ship)
                                print('<<<Убит корабль человека>>>')

                            else:
                                print('<<<Ранен корабль человека>>>')

                            shot = False
                            break

                    if hit is False:
                        print('<<<Промах по человеку>>>')
                        self._man_pole_ships[y][x] = 'O'

                    shot = False
            self._show_man_pole()  # чтоб было видно пападаения короче поле с кораблями человека
            # и с выстрелами компа и далее пустое поле с метками выстрела человека

    def check_shot(self, ship, x, y):
        hit = False

        if ship._tp == 1:
            x_start = ship._x
            x_end = ship._x + ship._length - 1
            y_start = y_end = ship._y

        elif ship._tp == 2:
            x_start = x_end = ship._x
            y_start = ship._y
            y_end = ship._y + ship._length - 1

        if x_start <= x <= x_end and y_start <= y <= y_end:
            if ship._is_move:
                ship._is_move = False

            if ship._tp == 1:
                cell = x - x_start
                ship._cells[cell] = 0

            if ship._tp == 2:
                cell = y - y_start
                ship._cells[cell] = 0

            hit = True

        return hit