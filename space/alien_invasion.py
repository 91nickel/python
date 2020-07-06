import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Назначение цвета фона
        pygame.display.set_caption("Alien Invasion")

        # Создание экземпляра статистики
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "RUN GAME")

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            # Переместить корабль вправо
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # Переместить корабль влево
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            # Переместить корабль вверх
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            # Переместить корабль вниз
            self.ship.moving_down = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_ships()

            # Очистка списка пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            # Скрыть указатель мыши
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды"""
        # Обновление позиций снарядов
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизийснарядов с пришельцами"""
        # Удаление снарядов и пришлеьцев, участвующих в коллизиях
        # Проверка попаданий в пришельцев
        # При обнаружении попадания удалить снаряд и пришельца
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_scores()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Увеличение уровня
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Создание флота вторжения"""
        # Создание пришельца
        # Интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens = available_space_x // (2 * alien_width)

        # Определяем кол-во рядов на экране
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height) // 2

        # Создание флота вторжения
        for row_number in range(0, number_rows):
            for alien_number in range(0, number_of_aliens):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """Проверяет достигли ли пришельцы нижней границы экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же самое, что и при столкновении с кораблем
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()
        # Проверка столкновение пришелец - корабль
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship Hit!")
            self._ship_hit()
        # Проверка достижения нижней границы экрана
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Обрабатывает столкновение пришельцев с кораблем"""
        # Уменьшение ships_left
        self.stats.ships_left -= 1
        self.sb.prep_ships()

        if self.stats.ships_left > 0:
            # Очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            # Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Вывод информации о счете
        self.sb.show_score()
        # Кнопка RUN GAME отобразится в том случае, если игра неактивна
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
