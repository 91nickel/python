import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.settings = ai_game.settings

        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load("f:/python/space/images/ship_white.png")
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль внизу в центре"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Обновляет позицию с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += float(self.settings.ship_speed_factor)
        if self.moving_left and self.rect.left > 0:
            self.x -= float(self.settings.ship_speed_factor)
        if self.moving_up and self.rect.top > 0:
            self.y -= float(self.settings.ship_speed_factor)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += float(self.settings.ship_speed_factor)
        self.rect.x = self.x
        self.rect.y = self.y
