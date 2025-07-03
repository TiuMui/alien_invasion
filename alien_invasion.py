import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        pygame.display.set_caption(self.settings.window_title)
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного цикла игры."""

        while True:
            self._tracking_events()
            self._update_screen()

    def _tracking_events(self):
        """Отслеживает события: нажатия клавишь, мышь."""

        current_iteration_event_list = pygame.event.get()
        for event in current_iteration_event_list:
            if event.type == pygame.QUIT:
                pygame.quit()  # Завершение работы Pygame.
                sys.exit()  # Завершение работы программы.

    def _update_screen(self):
        """Обновляет изображение на экране и отображает его."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()  # Отображение текущей прорисовки экрана.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
