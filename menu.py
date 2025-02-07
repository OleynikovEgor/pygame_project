import pygame
import pygame_menu as pm

class Menu():
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

    if __name__ == "__main__":
        settings = pm.Menu(title="Настройки",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_BLUE)

        settings._theme.widget_font_size = 25
        settings._theme.widget_font_color = BLACK
        settings._theme.widget_alignment = pm.locals.ALIGN_LEFT


        settings.add.toggle_switch(
            title="Music", default=True, toggleswitch_id="music")
        settings.add.toggle_switch(
            title="Sounds", default=True, toggleswitch_id="sound")

        settings.add.button(title="")

        settings.add.button(title="Return To Main Menu",
                            action=pm.events.BACK, align=pm.locals.ALIGN_CENTER, background_color=RED, font_color=WHITE)

        mainMenu = pm.Menu(title="Морской Бой",
                           width=WIDTH,
                           height=HEIGHT,
                           theme=pm.themes.THEME_BLUE)

        mainMenu._theme.widget_alignment = pm.locals.ALIGN_CENTER

        mainMenu.add.button(title="Играть",
                            font_color=WHITE, background_color=GREEN)

        mainMenu.add.label(title="")

        mainMenu.add.button(title="Настройки", action=settings,
                            font_color=WHITE, background_color=SETT)

        mainMenu.add.label(title="")

        mainMenu.add.button(title="Выход", action=pm.events.EXIT,
                            font_color=WHITE, background_color=RED)

        mainMenu.mainloop(screen)


