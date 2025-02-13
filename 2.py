import sys
from random import randint, choice


class Bot:
    def __init__(self):
        self.board = [[0 for i in range(12)] for j in range(12)]

    def generate_placement(self):
        self.used = [[0] * 12 for i in range(12)]
        pos = choice([0, 1])
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

        count = 0
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

        count = 0
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    bot = Bot()
    sys.excepthook = except_hook
    bot.generate_placement()
    for i in range(1, 11):
        print(*bot.board[i][1:11])
    print()
    for i in range(1, 11):
        print(*bot.used[i][1:11])