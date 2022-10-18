from game_pole import GamePole
from random import randint


class SeaBattle:
    """SeaBattle - class to start the game."""
    def __init__(self, size):
        assert type(size) == int and size > 8, 'Размер поля не int или больше 8'
        self._size = size
        self._man = GamePole(self._size)
        self._man.init()
        self._man_pole_for_shot = [['.' for _ in range(self._size)] for _ in range(self._size)]
        self._man_pole_for_ships = self._man.get_pole()
        self._computer = GamePole(self._size)
        self._computer.init()
        self._computer_pole_for_ships = self._computer.get_pole()

        game_mode = False
        while game_mode not in (1, 2):
            try:
                game_mode = int(input('Выберете режим игры и ввердите его значение. \n'
                                      '1 - Классический, 2 - С перемещением кораблей.\n'
                                      'Режим: '))
                if game_mode not in (1, 2):
                    print('Неверно введен режим игры, повторите ввод снова.')
            except ValueError:
                print('Неверно введен режим игры, повторите ввод снова.')

        self._game_mode = game_mode
        self._list_shots_on_man_pole = []
        self._list_shots_on_computer_pole = []
        self._list_hits_on_man_pole = []
        self._list_hits_on_computer_pole = []

    def step(self, player):
        if player == 1:
            step = True
            hit = False

            while step:
                coords = input('Введите координаты x и y через пробел: ')
                try:
                    x, y = map(int, coords.split())
                    if not 1 <= x <= self._size or not 1 <= y <= self._size:
                        print('Координаты за предеалми поля, нужен повторный ввод.')
                    else:
                        x -= 1
                        y -= 1
                        if self._man_pole_for_shot[y][x] == '.':
                            step = False
                        else:
                            print('Выстрел по этим координатам уже был. Выберете новые.')
                except ValueError:
                    print('Неверно введены координаты x и y.')

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

            if self._game_mode == 2:
                if hit:
                    self._list_hits_on_computer_pole.append((x, y))
                else:
                    self._list_shots_on_computer_pole.append((x, y))

            self._show_man_pole_for_shots()

        if player == 2:
            shot = True
            hit = False

            while shot:

                x = randint(0, self._size - 1)
                y = randint(0, self._size - 1)

                if self._man_pole_for_ships[y][x] in ('.', '1', 1):
                    for ship in self._man.get_ships():
                        if self.check_shot(ship, x, y):  # если попал
                            self._man_pole_for_ships[y][x] = 'X'
                            hit = True
                            if self.check_health_ship(ship):  # если корабль убит
                                self._man._ships.remove(ship)
                                print('<<<Убит корабль человека>>>')

                            else:
                                print('<<<Ранен корабль человека>>>')

                            break

                    if hit is False:
                        print('<<<Промах по человеку>>>')
                        self._man_pole_for_ships[y][x] = 'O'

                    shot = False

            if self._game_mode == 2:
                if hit:
                    self._list_hits_on_man_pole.append((x, y))
                else:
                    self._list_shots_on_man_pole.append((x, y))

            self._show_man_pole_for_ships()  # чтоб было видно пападаения короче поле с кораблями человека
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

            if ship._tp == 1:
                cell = x - x_start
                ship[cell] = 0

            if ship._tp == 2:
                cell = y - y_start
                ship[cell] = 0

            hit = True
            if ship._is_move:
                ship._is_move = False

        return hit

    def check_health_ship(self, ship):
        if not any(ship._cells):
            return True
        return False

    def _show_man_pole_for_shots(self):
        print('____мои выстрелы___')
        for row in self._man_pole_for_shot:
            print(*row)

    def _show_man_pole_for_ships(self):
        print('____мои корабли____')
        if self._game_mode == 1:
            self._man.show()
        elif self._game_mode == 2:
            pole = self._man.get_pole()
            for coords in self._list_shots_on_man_pole:
                pole[coords[-1]][coords[0]] = '0'
            for coords in self._list_hits_on_man_pole:
                pole[coords[-1]][coords[0]] = 'X'
            for row in pole:
                print(*row)

    def _show_computer_pole_for_ships(self):
        print('___корабли компа___')
        if self._game_mode == 1:
            self._computer.show()
        elif self._game_mode == 2:
            pole = self._computer.get_pole()
            for coords in self._list_shots_on_computer_pole:
                pole[coords[-1]][coords[0]] = '0'
            for coords in self._list_hits_on_computer_pole:
                pole[coords[-1]][coords[0]] = 'X'
            for row in pole:
                print(*row)

    def check_game_over(self):
        if len(self._man._ships) == 0:
            print('Победа компьютера.')
            return True

        elif len(self._computer._ships) == 0:
            print('Победа игрока.')
            return True

        return False

    def play(self):

        game_over = self.check_game_over()
        self._show_man_pole_for_ships()
        self._show_computer_pole_for_ships()
        if self._game_mode == 1:
            while game_over is False:
                self.step(1)
                game_over = self.check_game_over()
                self.step(2)
                game_over = self.check_game_over()

        elif self._game_mode == 2:

            while game_over is False:
                self.step(1)
                game_over = self.check_game_over()
                self.step(2)
                game_over = self.check_game_over()
                self.move_ships(self._list_shots_on_man_pole, self._list_shots_on_computer_pole)

    def move_ships(self, list_shots_on_man_pole, list_shots_on_computer_pole):
        self._man.move_ships(list_shots_on_man_pole)
        self._computer.move_ships(list_shots_on_computer_pole)


if __name__ == "__main__":
    sb = SeaBattle(10)
    sb.play()




