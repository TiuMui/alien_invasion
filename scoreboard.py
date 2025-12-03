from pygame import font

from constants import SCORE_TEXT_COLOR, SCORE_TEXT_SIZE


class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = ai.screen_rect
        self.settings = ai.settings
        self.statistics = ai.statistics
        self.text_color = SCORE_TEXT_COLOR
        self.font = font.SysFont(None, SCORE_TEXT_SIZE)

        self.prep_score()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""

        self.score_image = self.font.render(
            str(self.statistics.score),
            True,
            self.text_color,
            # self.settings.bg_color
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def blitme(self):
        """Рисует счет в нужной позиции."""

        self.screen.blit(self.score_image, self.score_rect)
