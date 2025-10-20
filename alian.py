import pygame

from pygame.sprite import Sprite


class Alian(Sprite):
    """Класс одного пришельца."""

    def __init__(self, ai):
        """Инициализирует пришельца и задает его начальную позицию."""

        super().__init__()
        self.screen = ai.screen
        self.settings = ai.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Проверяет нахождение пришельца у края экрана."""

        screen_rect = self.screen.get_rect()
        return self.rect.left <= 0 or self.rect.right >= screen_rect.right

    def update(self):
        """Смещает пришельца."""

        self.x += self.settings.alien_speed
        self.rect.x = self.x
