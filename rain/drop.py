import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Создание капли
        self.image = pygame.image.load("f:/python/rain/drop.png")
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self):
        if self.rect.bottom == self.screen_rect.height:
            self.rect.y = 0
        else:
            self.rect.y = self.rect.y + 1
