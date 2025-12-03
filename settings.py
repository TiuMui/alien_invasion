from constants import (ALIEN_POINTS, ALIEN_SPEED, BG_COLOR, BULLETS_ALLOWED,
                       BULLET_COLOR, BULLET_HIGHT, BULLET_SPEED, BULLET_WIDTH,
                       FLEET_DIRECTION, FLEET_DOWN_SPEED, SCREEN_HEIGHT,
                       SCREEN_WIDTH, SHIP_LIMIT, SHIP_SPEED, SPEEDUP_GAME,
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

        self.ship_limit = SHIP_LIMIT

        self.bullet_speed = BULLET_SPEED
        self.bullet_width = BULLET_WIDTH
        self.bullet_hight = BULLET_HIGHT
        self.bullet_color = BULLET_COLOR
        self.bullets_allowed = BULLETS_ALLOWED

        self.fleet_down_speed = FLEET_DOWN_SPEED

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры.

        Для возможности их сброса в первоначальное состояние.
        """

        self.ship_speed = SHIP_SPEED
        self.alien_speed = ALIEN_SPEED
        self.fleet_direction = FLEET_DIRECTION
        self.alien_points = ALIEN_POINTS

    def increas_speed_game(self):
        """Увеличивает скорость игры.

        За счет увеличения скорости пришельцев и корабля.
        """

        self.ship_speed *= SPEEDUP_GAME
        self.alien_speed *= SPEEDUP_GAME
