import pygame as pg


class Bullet(pg.sprite.Sprite):
    """Класс для управления снарядами корабля."""

    def __init__(self, ai):
        """Создает объект снарядов в текущей позиции корабля."""

        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.color = self.settings.bullet_color
        self.rect = pg.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_hight
        )
        self.rect.midbottom = ai.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает сняряд вверх."""

        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводит снаряд на экран."""

        pg.draw.rect(self.screen, self.color, self.rect)
