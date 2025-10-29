import pygame.font

from constants import (BUTTON_COLOR, BUTTON_HEIGHT, BUTTON_WIDTH,
                       BUTTON_TEXT_COLOR, BUTTON_TEXT_SIZE)


class Button():
    """Класс для кнопок в игровом окне."""

    def __init__(self, ai, text):
        self.screen = ai.screen
        self.screen_rect = ai.screen_rect
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT
        self.color = BUTTON_COLOR
        self.text_color = BUTTON_TEXT_COLOR
        self.font = pygame.font.SysFont(None, BUTTON_TEXT_SIZE)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(text)

    def _prep_msg(self, text):
        """Преобразует входной text в изображение
        и выравнивает его по центру."""

        self.text_image = self.font.render(
            text,
            True,
            self.text_color,
            self.color
        )
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """Рисует кнопку и текст на ней."""

        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
