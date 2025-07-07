import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai):
        """инициализирует корабль и задает его начальную позицию."""

        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в начальной позиции."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
            