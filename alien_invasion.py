import sys
from time import sleep

import pygame

from alian import Alian
from bullet import Bullet
from button import Button
from constants import (ALIEN_KILL_BY_BULLET, BULLET_KILL_BY_ALIEN, FPS,
                       FULL_SCREEN_MODE, GAME_PAUSE)
from game_statistics import GameStatistics
from settings import Settings
from ship import Ship


class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""

        pygame.init()

        self.settings = Settings()

        if FULL_SCREEN_MODE:
            self.screen = pygame.display.set_mode(
                (0, 0),
                pygame.FULLSCREEN | pygame.DOUBLEBUF
            )
            self.settings.screen_size = (
                self.screen.get_rect().width,
                self.screen.get_rect().height
            )
        else:
            self.screen = pygame.display.set_mode(
                self.settings.screen_size,
                pygame.DOUBLEBUF
            )

        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.window_title)
        self.statistics = GameStatistics(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Запуск основного цикла игры."""

        clock = pygame.time.Clock()
        while True:
            self._tracking_events()

            if self.statistics.game_active:
                self.ship.update()
                self._update_and_delete_bullet()

                self._check_bullets_and_aliens_collision()

                self._update_aliens_in_fleet()

            self._update_screen()

            clock.tick(FPS)

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

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._tracking_play_button(event)

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

    def _tracking_play_button(self, event):
        """Реакция на нажатие кнопки 'Play' мышью - запускает
        новую игру."""

        mouse_position = pygame.mouse.get_pos()
        button_clicked = self.play_button.rect.collidepoint(mouse_position)

        if button_clicked and not self.statistics.game_active:
            self.statistics.reset_statistics()
            self.statistics.game_active = True
            pygame.mouse.set_visible(False)

            self._aliens_and_bullets_empty()
            self.ship.move_to_the_center()

            self._create_fleet()

    def _fire_bullet(self):
        """Создает новый снаряд и добавляет его в группу self.bullets."""

        if (
            len(self.bullets) < self.settings.bullets_allowed and
            self.statistics.game_active
        ):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_and_delete_bullet(self):
        """Обновляет позиции снярядов и удаляет вышедшие за пределы экрана."""

        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullets_and_aliens_collision(self):
        """Фиксирует и обрабатывает столкновения снарядов и пришельцев."""

        pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            BULLET_KILL_BY_ALIEN,
            ALIEN_KILL_BY_BULLET
        )

        if not self.aliens:
            self.bullets.empty()
            sleep(GAME_PAUSE)
            self._create_fleet()

    def _ship_and_alien_collision(self):
        """Обрабатывает столкновение корабля с пришельцем."""

        self.statistics.ships_left -= 1
        self._aliens_and_bullets_empty()
        self.ship.move_to_the_center()
        sleep(GAME_PAUSE)

        if self.statistics.ships_left <= 0:
            self.statistics.game_active = False
            pygame.mouse.set_visible(True)

        else:
            self._create_fleet()

    def _aliens_and_bullets_empty(self):
        """Удаляет всех пришельцев и снаряды."""

        self.aliens.empty()
        self.bullets.empty()

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

    def _update_aliens_in_fleet(self):
        """Обновляет позиции всех пришельцев во флоте, фиксирует столкновение
        любого пришельца с кораблем или нижним краем."""

        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_and_alien_collision()

        self._check_fleet_bottom()

    def _check_fleet_edges(self):
        """Фиксирует достижение любым пришельцем края экрана."""

        for alien in self.aliens.sprites():
            if (alien.rect.left <= 0 or
               alien.rect.right >= self.screen_rect.right):
                self._change_fleet_direction()
                break

    def _check_fleet_bottom(self):
        """Фиксирует достижение любым пришельцем нижнего края."""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._ship_and_alien_collision()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление его движения."""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_down_speed
        self.settings.alien_speed *= -1

    def _update_screen(self):
        """Обновляет изображение на экране и отображает его."""

        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.statistics.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
