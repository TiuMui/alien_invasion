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
        self.aliens = pygame.sprite.Group()
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

        number_aliens_in_row, number_rows = self._calculate_fleet()

        for row_number in range(number_rows):
            for alian_number in range(number_aliens_in_row):
                self._create_alien(alian_number, row_number)

    def _calculate_fleet(self):
        """Рассчитывает количество пришельцев в одном ряду
        и количество рядов.
        """

        alien_for_calculate = Alian(self)
        alien_width, alian_height = alien_for_calculate.rect.size

        ship_height = self.ship.rect.height

        available_space_x = self.settings.screen_size[0] - (2 * alien_width)
        number_aliens_in_row = available_space_x // (2 * alien_width)

        available_space_y = (self.settings.screen_size[1] -
                             (3 * alian_height) - ship_height)
        number_rows = available_space_y // (2 * alian_height)

        return number_aliens_in_row, number_rows

    def _create_alien(self, alian_number, row_number):
        """Создает пришельца и размещает его в нужном ряду."""

        alien = Alian(self)
        alien_width, alian_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alian_number
        alien.rect.x = alien.x

        alien.y = alian_height + 2 * alian_height * row_number
        alien.rect.y = alien.y

        self.aliens.add(alien)

    def _update_screen(self):
        """Обновляет изображение на экране и отображает его."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
