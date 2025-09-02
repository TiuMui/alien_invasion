import sys

import pygame

from alian import Alian
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_size = (
            self.screen.get_rect().width,
            self.screen.get_rect().height
        )

        pygame.display.set_caption(self.settings.window_title)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alians = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры."""

        while True:
            self._tracking_events()
            self.ship.update()
            self._update_and_delete_bullet()
            self._update_screen()

    def _tracking_events(self):
        """Отслеживает события: нажатия клавишь, мышь."""

        current_iteration_event_list = pygame.event.get()
        for event in current_iteration_event_list:
            if event.type == pygame.QUIT:
                pygame.quit()  # Завершение работы Pygame.
                sys.exit()  # Завершение работы программы.  

            elif event.type == pygame.KEYDOWN:
                self._tracking_keydown(event)

            elif event.type == pygame.KEYUP:
                self._tracking_keyup(event)

    def _tracking_keydown(self, event):
        """Реакция на нажатие клавиш."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _tracking_keyup(self, event):
        """Реакция на отпускание клавиш."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создает новый снаряд и добавляет его в группу self.bullets."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_and_delete_bullet(self):
        """Обновляет позиции снярядов и удаляет вышедшие за пределы экрана."""

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Создает флот пришельцев."""

        alian = Alian(self)
        self.alians.add(alian)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает его."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alians.draw(self.screen)
        pygame.display.flip()  # Отображение текущей прорисовки экрана.


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
