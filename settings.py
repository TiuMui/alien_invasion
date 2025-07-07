from constants import (BG_COLOR, SCREEN_HEIGTH, SCREEN_WIDTH, SHIP_SPEED,
                       WINDOW_TITLE)


class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(
            self,
            screen_size=(SCREEN_WIDTH, SCREEN_HEIGTH),
            bg_color=BG_COLOR,
            window_title=WINDOW_TITLE
    ):
        """Инициализирует настройки игры."""

        self.screen_size = screen_size
        self.bg_color = bg_color
        self.window_title = window_title
        self.ship_speed = SHIP_SPEED
