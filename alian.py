import pygame

from pygame.sprite import Sprite


class Alian(Sprite):
    """Класс одного пришельца."""

    def __init__(self, ai):
        """Инициализирует пришельца и задает его начальную позицию."""

        super().__init__()
        self.settings = ai.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Смещает пришельца."""

        self.x += self.settings.alien_speed
        self.rect.x = self.x
