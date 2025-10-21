import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai):
        """инициализирует корабль и задает его начальную позицию."""

        self.settings = ai.settings
        self.screen = ai.screen
        self.screen_rect = ai.screen_rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.move_to_the_center()
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def move_to_the_center(self):
        """Перемещает корабль в центр нижнего края."""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x) # Дробная координата корабля по x.
