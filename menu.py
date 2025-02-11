import pygame
import pygame_menu as pm

pygame.init()

WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SETT = (102, 255, 153)

pygame.mixer.init()
pygame.mixer.music.load('background_music.ogg')
pygame.mixer.music.play(-1)
play = 1

if __name__ == "__main__":
    difficulty = pm.Menu(title="Выберите сложность",
                         width=WIDTH,
                         height=HEIGHT,
                         theme=pm.themes.THEME_BLUE)

    sound = pygame.mixer.Sound('button_sound.ogg')

    difficulty._theme.widget_font_size = 30
    difficulty._theme.widget_font_color = GREEN
    difficulty._theme.widget_alignment = pm.locals.ALIGN_CENTER

    difficulty.add.selector('Сложность:  ', [('Easy', 1), ('Medium', 2), ('Hard', 3)])

    difficulty.add.label('')

    difficulty.add.button(title=' Начать игру ',
                      font_color=WHITE, background_color=GREEN)

    # ---------------------------------------------------------------------------------------------------

    player = pm.Menu(title="Выберите количество игроков",
                     width=WIDTH,
                     height=HEIGHT,
                     theme=pm.themes.THEME_BLUE)

    player._theme.widget_font_size = 25
    player._theme.widget_font_color = BLACK
    player._theme.widget_alignment = pm.locals.ALIGN_CENTER

    player.add.button(title=' 1 player ', action=difficulty,
                      font_color=WHITE, background_color=GREEN, font_size=30)

    player.add.label(title="")

    player.add.button(title='2 players',
                      font_color=WHITE, background_color=GREEN, font_size=30)

    # ----------------------------------------------------------------------------------------------------

    def music_sound(music):
        global play
        if play:
            pygame.mixer.music.pause()
            play = 0
        else:
            pygame.mixer.music.play(-1)
            play = 1


    settings = pm.Menu(title="Настройки",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_BLUE)

    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    settings.add.toggle_switch(
        title="Music", default=True, toggleswitch_id="music", onchange=music_sound)

    settings.add.toggle_switch(
        title="Sounds", default=True, toggleswitch_id="sound")

    settings.add.button(title="")

    settings.add.button(title="Return To Main Menu",
                        action=pm.events.BACK, align=pm.locals.ALIGN_CENTER,
                        background_color=RED, font_color=WHITE)

    # ----------------------------------------------------------------------------------------------------

    mainMenu = pm.Menu(title="Морской Бой",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_BLUE)

    mainMenu._theme.widget_font_size = 30
    mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

    mainMenu.add.button(title="Играть", action=player,
                        font_color=WHITE, background_color=GREEN)

    mainMenu.add.label(title="")

    mainMenu.add.button(title="Настройки", action=settings,
                        font_color=WHITE, background_color=SETT)

    mainMenu.add.label(title="")

    mainMenu.add.button(title="Выход", action=pm.events.EXIT,
                        font_color=WHITE, background_color=RED)

    mainMenu.mainloop(screen)
