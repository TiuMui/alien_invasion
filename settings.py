from constants import (ALIEN_SPEED, BG_COLOR, BULLETS_ALLOWED, BULLET_COLOR,
                       BULLET_HIGHT, BULLET_SPEED, FLEET_DOWN_SPEED,
                       SCREEN_HEIGHT, BULLET_WIDTH, SHIP_SPEED, SCREEN_WIDTH,
                       WINDOW_TITLE)


class Settings():
    """Класс для хранения всех настроек игры."""

    def __init__(
            self,
            screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            bg_color=BG_COLOR,
            window_title=WINDOW_TITLE
    ):
        """Инициализирует настройки игры."""

        self.screen_size = screen_size
        self.bg_color = bg_color
        self.window_title = window_title

        self.ship_speed = SHIP_SPEED

        self.bullet_speed = BULLET_SPEED
        self.bullet_width = BULLET_WIDTH
        self.bullet_hight = BULLET_HIGHT
        self.bullet_color = BULLET_COLOR
        self.bullets_allowed = BULLETS_ALLOWED

        self.alien_speed = ALIEN_SPEED
        self.fleet_down_speed = FLEET_DOWN_SPEED
