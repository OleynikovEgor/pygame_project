import sys
from random import randint, choice


class Bot:
    def __init__(self):
        self.board = [[0 for i in range(10)] for j in range(10)]

    def generate_placement(self):
        used = [[0] * 10 for i in range(10)]
        pos = choice([0, 1])
        if pos:
            x, y = randint(0, 6), randint(0, 9)
            for i in range(4):
                self.board[x + i][y] = 1
        else:
            x, y = randint(0, 9), randint(0, 6)
            for i in range(4):
                self.board[x][y + i] = 1

        for sheep in range(2):
            pos = choice([0, 1])
            if pos:
                x, y = randint(0, 6), randint(0, 9)
                for i in range(4):
                    self.board[x + i][y] = 1
            else:
                x, y = randint(0, 9), randint(0, 6)
                for i in range(4):
                    self.board[x][y + i] = 1


def except_hook(cls, exception, traceback):    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    bot = Bot()
    sys.excepthook = except_hook
    bot.generate_placement()
    for i in range(10):
        print(*bot.board[i])
