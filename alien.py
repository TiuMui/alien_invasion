from pygame import image, sprite


class Alien(sprite.Sprite):
    """Класс одного пришельца."""

    def __init__(self, ai):
        """Инициализирует пришельца и задает его начальную позицию."""

        super().__init__()
        self.settings = ai.settings
        self.image = image.load('images/alien.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Смещает пришельца."""

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
