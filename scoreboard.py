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
        self._prep_record_score()
        self.prep_level()

    def prep_score(self):
        """Размещает текущий счет в нужном месте на экране."""

        self.score_image = self._get_image_from_number(self.statistics.score)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def check_and_prep_record_score(self):
        """Проверяет появление нового рекорда.

        Если есть новый рекорд, размещает его на экране.
        """

        if self.statistics.score > self.statistics.record_score:
            self.statistics.record_score = self.statistics.score
            self._prep_record_score()

    def _prep_record_score(self):
        """Размещает рекордный счет в нужном месте на экране."""

        self.record_score_image = self._get_image_from_number(
            self.statistics.record_score
        )

        self.record_score_rect = self.record_score_image.get_rect()
        self.record_score_rect.centerx = self.screen_rect.centerx
        self.record_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Размещает текущий уровень в нужном месте на экране."""

        self.level_image = self._get_image_from_number(
            self.statistics.level,
            rounding=0
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top + 50

    def _get_image_from_number(self, number, rounding=-1):
        """Преобразует переданное число в графическое изображение."""

        if isinstance(number, (int, float)):
            rounded_number = round(number, rounding)
            rounded_number_str = f'{rounded_number:,}'.replace(',', ' ')
            result = self.font.render(
                rounded_number_str,
                True,
                self.text_color
            )
            return result
        else:
            raise ValueError('Переданное число должно быть "int" или "float".')

    def blitme(self):
        """Рисует счет, рекорд и уровень в нужных позициях на экране."""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_score_image, self.record_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
