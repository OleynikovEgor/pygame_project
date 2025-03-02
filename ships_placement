import pygame
from board import boarder


def ships():
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Расставьте свои корабли')
    pygame.font.init()
    letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
    numbers = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10']
    ship11 = pygame.Rect(100, 150, 25, 25)
    ship12 = pygame.Rect(140, 150, 25, 25)
    ship13 = pygame.Rect(180, 150, 25, 25)
    ship14 = pygame.Rect(220, 150, 25, 25)
    ship21 = pygame.Rect(100, 200, 25, 60)
    ship22 = pygame.Rect(140, 200, 25, 60)
    ship23 = pygame.Rect(180, 200, 25, 60)
    ship31 = pygame.Rect(100, 270, 25, 80)
    ship32 = pygame.Rect(140, 270, 25, 80)
    ship41 = pygame.Rect(100, 360, 25, 120)
    game_button = pygame.Rect(100, 300, 200, 50)
    dragging11 = False
    dragging12 = False
    dragging13 = False
    dragging14 = False
    dragging21 = False
    dragging22 = False
    dragging23 = False
    dragging31 = False
    dragging32 = False
    dragging41 = False
    count = 0
    pygame.mixer.init()
    pygame.mixer.music.load('background_music.ogg')
    pygame.mixer.music.play(-1)

    class Player_Board():
        # создание поля
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.board = [[0] * width for _ in range(height)]
            # значения по умолчанию
            self.left = 570
            self.top = 150
            self.cell_size = 35
            self.button = []
            self.turn = 1

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

    player_board = Player_Board(10, 10)
    font = pygame.font.Font(None, 47)
    info_text1 = font.render('Расставьте свои корабли', True, (255, 255, 255))
    text_g = font.render('Играть', True, (255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and ship11.collidepoint(event.pos):
                    dragging11 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship11.x - mouse_x
                    offset_y = ship11.y - mouse_y
                elif event.button == 1 and ship12.collidepoint(event.pos):
                    dragging12 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship12.x - mouse_x
                    offset_y = ship12.y - mouse_y
                elif event.button == 1 and ship13.collidepoint(event.pos):
                    dragging13 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship13.x - mouse_x
                    offset_y = ship13.y - mouse_y
                elif event.button == 1 and ship14.collidepoint(event.pos):
                    dragging14 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship14.x - mouse_x
                    offset_y = ship14.y - mouse_y
                elif event.button == 1 and ship21.collidepoint(event.pos):
                    dragging21 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship21.x - mouse_x
                    offset_y = ship21.y - mouse_y
                elif event.button == 1 and ship22.collidepoint(event.pos):
                    dragging22 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship22.x - mouse_x
                    offset_y = ship22.y - mouse_y
                elif event.button == 1 and ship23.collidepoint(event.pos):
                    dragging23 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship23.x - mouse_x
                    offset_y = ship23.y - mouse_y
                elif event.button == 1 and ship31.collidepoint(event.pos):
                    dragging31 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship31.x - mouse_x
                    offset_y = ship31.y - mouse_y
                elif event.button == 1 and ship32.collidepoint(event.pos):
                    dragging32 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship32.x - mouse_x
                    offset_y = ship32.y - mouse_y
                elif event.button == 1 and ship41.collidepoint(event.pos):
                    dragging41 = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ship41.x - mouse_x
                    offset_y = ship41.y - mouse_y
                elif event.button == 1 and game_button.collidepoint(event.pos):
                    boarder(player_board.board)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if dragging11:
                        dragging11 = False
                        if ship11.x <= player_board.left + player_board.cell_size * player_board.height and ship11.x >= player_board.left and ship11.y <= player_board.top + player_board.cell_size * player_board.width and ship11.y >= player_board.top:
                            y1 = (ship11.x - player_board.left) // player_board.cell_size
                            x1 = (ship11.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            print(x1, y1)
                    elif dragging12:
                        dragging12 = False
                        if ship12.x <= player_board.left + player_board.cell_size * player_board.height and ship12.x >= player_board.left and ship12.y <= player_board.top + player_board.cell_size * player_board.width and ship12.y >= player_board.top:
                            y1 = (ship12.x - player_board.left) // player_board.cell_size
                            x1 = (ship12.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            print(x1, y1)
                    elif dragging13:
                        dragging13 = False
                        if ship13.x <= player_board.left + player_board.cell_size * player_board.height and ship13.x >= player_board.left and ship13.y <= player_board.top + player_board.cell_size * player_board.width and ship13.y >= player_board.top:
                            y1 = (ship13.x - player_board.left) // player_board.cell_size
                            x1 = (ship13.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            print(x1, y1)
                    elif dragging14:
                        dragging14 = False
                        if ship14.x <= player_board.left + player_board.cell_size * player_board.height and ship14.x >= player_board.left and ship14.y <= player_board.top + player_board.cell_size * player_board.width and ship14.y >= player_board.top:
                            y1 = (ship14.x - player_board.left) // player_board.cell_size
                            x1 = (ship14.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            print(x1, y1)
                    elif dragging21:
                        dragging21 = False
                        if ship21.x <= player_board.left + player_board.cell_size * player_board.height and ship21.x >= player_board.left and ship21.y <= player_board.top + player_board.cell_size * player_board.width and ship21.y >= player_board.top:
                            y1 = (ship21.x - player_board.left) // player_board.cell_size
                            x1 = (ship21.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                    elif dragging22:
                        dragging22 = False
                        if ship22.x <= player_board.left + player_board.cell_size * player_board.height and ship22.x >= player_board.left and ship22.y <= player_board.top + player_board.cell_size * player_board.width and ship22.y >= player_board.top:
                            y1 = (ship22.x - player_board.left) // player_board.cell_size
                            x1 = (ship22.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                            print(x1, y1)
                    elif dragging23:
                        dragging23 = False
                        if ship23.x <= player_board.left + player_board.cell_size * player_board.height and ship23.x >= player_board.left and ship23.y <= player_board.top + player_board.cell_size * player_board.width and ship23.y >= player_board.top:
                            y1 = (ship23.x - player_board.left) // player_board.cell_size
                            x1 = (ship23.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                            print(x1, y1)
                    elif dragging31:
                        dragging31 = False
                        if ship31.x <= player_board.left + player_board.cell_size * player_board.height and ship31.x >= player_board.left and ship31.y <= player_board.top + player_board.cell_size * player_board.width and ship31.y >= player_board.top:
                            y1 = (ship31.x - player_board.left) // player_board.cell_size
                            x1 = (ship31.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                            player_board.board[x1 + 2][y1] = 1
                            print(x1, y1)
                    elif dragging32:
                        dragging32 = False
                        if ship32.x <= player_board.left + player_board.cell_size * player_board.height and ship32.x >= player_board.left and ship32.y <= player_board.top + player_board.cell_size * player_board.width and ship32.y >= player_board.top:
                            y1 = (ship32.x - player_board.left) // player_board.cell_size
                            x1 = (ship32.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                            player_board.board[x1 + 2][y1] = 1
                            print(x1, y1)
                    elif dragging41:
                        dragging41 = False
                        if ship41.x <= player_board.left + player_board.cell_size * player_board.height and ship41.x >= player_board.left and ship41.y <= player_board.top + player_board.cell_size * player_board.width and ship41.y >= player_board.top:
                            y1 = (ship41.x - player_board.left) // player_board.cell_size
                            x1 = (ship41.y - player_board.top) // player_board.cell_size
                            player_board.board[x1][y1] = 1
                            player_board.board[x1 + 1][y1] = 1
                            player_board.board[x1 + 2][y1] = 1
                            player_board.board[x1 + 3][y1] = 1
                            print(x1, y1)
                print(player_board.board)
            elif event.type == pygame.MOUSEMOTION:
                if dragging11:
                    mouse_x, mouse_y = event.pos
                    ship11.x = mouse_x + offset_x
                    ship11.y = mouse_y + offset_y
                if dragging12:
                    mouse_x, mouse_y = event.pos
                    ship12.x = mouse_x + offset_x
                    ship12.y = mouse_y + offset_y
                if dragging13:
                    mouse_x, mouse_y = event.pos
                    ship13.x = mouse_x + offset_x
                    ship13.y = mouse_y + offset_y
                if dragging14:
                    mouse_x, mouse_y = event.pos
                    ship14.x = mouse_x + offset_x
                    ship14.y = mouse_y + offset_y
                if dragging21:
                    mouse_x, mouse_y = event.pos
                    ship21.x = mouse_x + offset_x
                    ship21.y = mouse_y + offset_y
                if dragging22:
                    mouse_x, mouse_y = event.pos
                    ship22.x = mouse_x + offset_x
                    ship22.y = mouse_y + offset_y
                if dragging23:
                    mouse_x, mouse_y = event.pos
                    ship23.x = mouse_x + offset_x
                    ship23.y = mouse_y + offset_y
                if dragging31:
                    mouse_x, mouse_y = event.pos
                    ship31.x = mouse_x + offset_x
                    ship31.y = mouse_y + offset_y
                if dragging32:
                    mouse_x, mouse_y = event.pos
                    ship32.x = mouse_x + offset_x
                    ship32.y = mouse_y + offset_y
                if dragging41:
                    mouse_x, mouse_y = event.pos
                    ship41.x = mouse_x + offset_x
                    ship41.y = mouse_y + offset_y
            screen.fill((51, 153, 255))
            player_board.render(screen)
            for i in range(10):
                for j in range(10):
                    count += player_board.board[i][j]
                if count == 20:
                    pygame.draw.rect(screen, 'Black', game_button)
                    screen.blit(text_g, (150, 308))
            count = 0
            x = 578
            for i in letters:
                text = font.render(i, True, (255, 44, 44))
                text_pos = (x, 110)
                screen.blit(text, text_pos)
                x += player_board.cell_size
            y = 150
            for i in numbers:
                text = font.render(i, True, (255, 44, 44))
                text_pos = (925, y)
                screen.blit(text, text_pos)
                y += player_board.cell_size

            pygame.draw.rect(screen, 'Black', ship11)
            pygame.draw.rect(screen, 'Black', ship12)
            pygame.draw.rect(screen, 'Black', ship13)
            pygame.draw.rect(screen, 'Black', ship14)
            pygame.draw.rect(screen, 'Black', ship21)
            pygame.draw.rect(screen, 'Black', ship22)
            pygame.draw.rect(screen, 'Black', ship23)
            pygame.draw.rect(screen, 'Black', ship31)
            pygame.draw.rect(screen, 'Black', ship32)
            pygame.draw.rect(screen, 'Black', ship41)

            screen.blit(info_text1, (320, 65))
            pygame.display.flip()
