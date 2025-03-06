import pygame
import sys
import time
from bot import Bot
from final import final

start_time = time.time()


def boarder(pl_board):
    screen = pygame.display.set_mode((1000, 800))
    explosion_image = pygame.image.load("explosion.png")
    explosion_image = pygame.transform.scale(explosion_image, (30, 30))
    pygame.display.set_caption('В бой!')
    pygame.font.init()
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
    numbers = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
    pygame.mixer.init()
    pygame.mixer.music.load('background_music.ogg')
    pygame.mixer.music.play(-1)

    bot = Bot(2)
    bot.add_player_board(pl_board)
    bot.generate_placement()
    board_bot = [bot.board[i][1:12] for i in range(1, 11)]

    class Bot_Board():
        # создание поля
        def __init__(self, width, height, board_pl):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            # значения по умолчанию
            self.left = 50
            self.top = 150
            self.cell_size = 35
            self.button = []
            self.turn = 1
            self.board_pl = board_pl

        # настройка внешнего вида
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size

        def render(self, screen):
            for i in range(self.height):
                for j in range(self.width):
                    x = self.left + j * self.cell_size
                    y = self.top + i * self.cell_size
                    pygame.draw.rect(screen, 'Black', (x, y, self.cell_size, self.cell_size), width=2)

                    if self.board_pl[i][j] >= 100:
                        pygame.draw.line(screen, 'Red', (j * 35 + 570, i * 35 + 150),
                                         ((j + 1) * 35 + 570, (i + 1) * 35 + 150))
                        pygame.draw.line(screen, 'Red', ((j + 1) * 35 + 570, i * 35 + 150),
                                         (j * 35 + 570, (i + 1) * 35 + 150))
                    elif self.board_pl[i][j] == 50:
                        pygame.draw.line(screen, 'Green', (j * 35 + 570, i * 35 + 150),
                                         ((j + 1) * 35 + 570, (i + 1) * 35 + 150))
                        pygame.draw.line(screen, 'Green', ((j + 1) * 35 + 570, i * 35 + 150),
                                         (j * 35 + 570, (i + 1) * 35 + 150))

    class Player_Board():
        # создание поля
        def __init__(self, width, height, board_pl):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            # значения по умолчанию
            self.left = 570
            self.top = 150
            self.cell_size = 35
            self.button = []
            self.turn = 0
            self.board_pl = board_pl
            self.goal = []

        # настройка внешнего вида
        def set_view(self, left, top, cell_size):
            self.left = left
            self.top = top
            self.cell_size = cell_size

        def render(self, screen):
            for i in range(self.height):
                for j in range(self.width):
                    x = self.left + j * self.cell_size
                    y = self.top + i * self.cell_size
                    pygame.draw.rect(screen, 'WHITE', (x, y, self.cell_size, self.cell_size), width=2)

                    if self.board[i][j] == 1 and self.turn == 0:
                        pygame.draw.rect(screen, 'Green', (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2),
                                         width=0)
                    if self.board_pl[i][j] >= 100:
                        pygame.draw.line(screen, 'Red', (j * 35 + 50, i * 35 + 150),
                                         ((j + 1) * 35 + 50, (i + 1) * 35 + 150))
                        pygame.draw.line(screen, 'Red', ((j + 1) * 35 + 50, i * 35 + 150),
                                         (j * 35 + 50, (i + 1) * 35 + 150))
                    elif self.board_pl[i][j] == 50:
                        pygame.draw.line(screen, 'Green', (j * 35 + 50, i * 35 + 150),
                                         ((j + 1) * 35 + 50, (i + 1) * 35 + 150))
                        pygame.draw.line(screen, 'Green', ((j + 1) * 35 + 50, i * 35 + 150),
                                         (j * 35 + 50, (i + 1) * 35 + 150))

        def get_click(self, mouse_pos):
            cell = self.get_cell(mouse_pos)
            self.on_click(cell)

        def get_cell(self, mouse_pos):
            x, y = mouse_pos
            i = (y - self.top) // self.cell_size
            j = (x - self.left) // self.cell_size
            if 0 <= i < self.height and 0 <= j < self.width:
                return (j, i)
            else:
                return None

        def on_click(self, cell):
            if cell and self.turn == 0:
                self.goal = [cell[1], cell[0]]
                print(self.goal)
                if not self.button:
                    cj, ci = cell
                    self.button = [cell]
                    for i in range(self.height):
                        self.board[i][cj] = 1 - self.board[i][cj]
                    for j in range(self.width):
                        self.board[ci][j] = 1 - self.board[ci][j]
                elif self.button[0] == cell:
                    cj, ci = cell
                    self.button = []
                    for i in range(self.height):
                        self.board[i][cj] = 1 - self.board[i][cj]
                    for j in range(self.width):
                        self.board[ci][j] = 1 - self.board[ci][j]
                    self.board[ci][cj] = 0

    # поле 5 на 7
    bot_board = Bot_Board(10, 10, board_bot)
    player_board = Player_Board(10, 10, pl_board)
    font = pygame.font.Font(None, 47)

    button_color = (255, 153, 52)
    font_but = pygame.font.Font(None, 36)
    text_but = font_but.render("Выстрелить", True, (255, 255, 255))
    info_text1 = font_but.render('Белые ходят', True, (255, 255, 255))
    info_text2 = font_but.render('Чёрные ходят', True, (0, 0, 0))
    running = True
    while running:
        screen.fill((51, 153, 255))
        bot_board.render(screen)
        player_board.render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                player_board.get_click(event.pos)
                if button_rect.collidepoint(event.pos):
                    if player_board.turn == 0 and player_board.button:
                        if bot_board.board_pl[player_board.goal[0]][player_board.goal[1]]:
                            bot_board.board_pl[player_board.goal[0]][player_board.goal[1]] = 100
                            print(bot_board.board_pl)
                        else:
                            bot_board.board_pl[player_board.goal[0]][player_board.goal[1]] = 50
                            print(bot_board.board_pl)
                        player_board.turn, bot_board.turn = 1, 0
                        player_board.button = []
                        bot_board.button = []
                        player_board.board = [[0] * player_board.width for _ in range(player_board.height)]
                        bot_board.board = [[0] * bot_board.width for _ in range(bot_board.height)]
            if bot_board.turn == 0:
                shoot = bot.shot()
                print(shoot)
                if shoot[2]:
                    player_board.board_pl[shoot[0]][shoot[1]] = 100
                    player_board.turn, bot_board.turn = 0, 1
                else:
                    player_board.board_pl[shoot[0]][shoot[1]] = 50
                    player_board.turn, bot_board.turn = 0, 1
                player_board.button = []
                bot_board.button = []
                player_board.board = [[0] * player_board.width for _ in range(player_board.height)]
                bot_board.board = [[0] * bot_board.width for _ in range(bot_board.height)]
                bot_board.turn = 1
                player_board.turn = 0

        x = 58
        for i in letters:
            text = font.render(i, True, (255, 44, 44))
            text_pos = (x, 110)
            screen.blit(text, text_pos)
            x += bot_board.cell_size
        x = 578
        for i in letters:
            text = font.render(i, True, (255, 44, 44))
            text_pos = (x, 110)
            screen.blit(text, text_pos)
            x += player_board.cell_size
        y = 150
        for i in numbers:
            text = font.render(i, True, (255, 44, 44))
            text_pos = (10, y)
            screen.blit(text, text_pos)
            y += bot_board.cell_size
        y = 150
        for i in numbers:
            text = font.render(i, True, (255, 44, 44))
            text_pos = (925, y)
            screen.blit(text, text_pos)
            y += player_board.cell_size

        button_rect = pygame.draw.rect(screen, button_color, (415, 300, 150, 50))  # (x, y, width, height)
        screen.blit(text_but, (button_rect.x + 5, button_rect.y + 10))
        if player_board.turn == 0:
            screen.blit(info_text2, (400, 80))
        else:
            screen.blit(info_text1, (400, 80))
        coin1 = 0
        coin2 = 0
        for i in range(10):
            for j in range(10):
                if bot_board.board_pl[i][j] == 100:
                    coin1 += 1
                if player_board.board_pl[i][j] == 100:
                    coin2 += 1
        if coin1 == 20:
            print('Победил бот')
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            running = False
            final('Победил бот', elapsed_time)
        elif coin2 == 20:
            print('Победил игрок')
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            with open('record', 'r', encoding='utf-8') as file:
                content = file.readline().strip()
            if content:
                if int(content) > int(elapsed_time):
                    with open('record', 'w', encoding='utf-8') as file:
                        file.write(f'{int(elapsed_time) // 1}')
            else:
                with open('record', 'w', encoding='utf-8') as file:
                    file.write(f'{int(elapsed_time)}')
            running = False
            final('Победил игрок', int(elapsed_time))
        pygame.display.flip()
