import sys

import pygame

from constants import DISPLAY_SIZE, WINDOW_TITLE


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""

        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

    def run_game(self):
        """Запуск основного цикла игры."""

        while True:
            current_iteration_event_list = pygame.event.get()
            for event in current_iteration_event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()  # Завершение работы Pygame.
                    sys.exit()  # Завершение работы программы.
            pygame.display.flip()  # Отображение текущей прорисовки экрана.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
