import sys
from random import randint, choice, random


class Bot:
    def __init__(self, hard_lvl):
        self.board = [[0 for i in range(12)] for j in range(12)]
        self.shotted = [[0] * 12 for i in range(12)]
        self.hard = hard_level[hard_lvl]

    def generate_placement(self):  # Генерация расстановки
        self.used = [[0] * 12 for i in range(12)]
        pos = choice([0, 1])  # Расстановка четырехпалубного корабля
        if pos:
            x, y = randint(1, 7), randint(1, 10)
            for i in range(4):
                self.board[x + i][y] = 1
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        self.used[x + i + dx][y + dy] = 1
        else:
            x, y = randint(1, 10), randint(1, 7)
            for i in range(4):
                self.board[x][y + i] = 1
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        self.used[x + dx][y + i + dy] = 1

        count = 0  # Расстановка трехпалубных кораблей
        while count < 2:
            pos = choice([0, 1])
            if pos:
                x, y = randint(1, 8), randint(1, 10)
                if self.used[x][y] or self.used[x + 1][y] or self.used[x + 2][y]:
                    continue
                for i in range(3):
                    self.board[x + i][y] = 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            self.used[x + i + dx][y + dy] = 1
                count += 1
            else:
                x, y = randint(1, 10), randint(1, 8)
                if self.used[x][y] or self.used[x][y + 1] or self.used[x][y + 2]:
                    continue
                for i in range(3):
                    self.board[x][y + i] = 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            self.used[x + dx][y + i + dy] = 1
                count += 1

        count = 0  # Расстановка двухпалубных кораблей
        while count < 3:
            pos = choice([0, 1])
            if pos:
                x, y = randint(1, 9), randint(1, 10)
                if self.used[x][y] or self.used[x + 1][y]:
                    continue
                for i in range(2):
                    self.board[x + i][y] = 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            self.used[x + i + dx][y + dy] = 1
                count += 1
            else:
                x, y = randint(1, 10), randint(1, 9)
                if self.used[x][y] or self.used[x][y + 1]:
                    continue
                for i in range(2):
                    self.board[x][y + i] = 1
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            self.used[x + dx][y + i + dy] = 1
                count += 1

        for c in range(4):  # Расстановка однопалубных кораблей
            clear = []
            for x in range(1, 11):
                for y in range(1, 11):
                    if not self.used[x][y]:
                        clear.append((x, y))
            x, y = choice(clear)
            self.board[x][y] = 1
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    self.used[x + dx][y + dy] = 1

    def add_player_board(self, player_board):  # добавление доски игрока
        self.player_board = player_board

    def shot(self):  # Имитация выстрела
        goal = random()
        if goal <= self.hard:  # Поражение корабля соперника
            clear = []
            for x in range(10):
                for y in range(10):
                    if not self.shotted[x + 1][y + 1] and self.player_board[x][y]:
                        clear.append((x, y))
            x, y = choice(clear)
            self.shotted[x + 1][y + 1] = 1
            killed = self.boat_is_killed(x, y)
            return x, y, True, killed[0], killed[1]
        else:  # Промах
            clear = []
            for x in range(10):
                for y in range(10):
                    if not self.shotted[x + 1][y + 1] and not self.player_board[x][y]:
                        clear.append((x, y))
            x, y = choice(clear)
            self.shotted[x + 1][y + 1] = 1
            return x, y, False, None, None

    def boat_is_killed(self, x, y):  # Проверка, что корабль игрока полность потоплен
        boat = set()
        board = self.player_board
        d = 0
        while 0 <= x - d - 1 <= 9 and board[x - d - 1][y]:
            d += 1
        while 0 <= x - d <= 9 and board[x - d][y]:
            if not self.shotted[x - d + 1][y + 1]:
                return False, []
            boat.add((x - d, y))
            d -= 1
        d = 0
        while 0 <= y - d - 1 <= 9 and board[x][y - d - 1]:
            d += 1
        while 0 <= y - d <= 9 and board[x][y - d]:
            if not self.shotted[x + 1][y - d + 1]:
                return False, []
            boat.add((x, y - d))
            d -= 1
        boat = sorted(list(boat))
        return True, boat


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


hard_level = [0, 0.2, 0.4, 0.6, 0.8]

if __name__ == "__main__":
    bot = Bot(2)
    sys.excepthook = except_hook
    bot.generate_placement()
    player_b = []
    for i in range(1, 11):
        print(*bot.board[i][1:11])
        player_b.append(bot.board[i][1:11])
    bot.add_player_board(player_b)
    for i in range(8):
        print(bot.shot())
