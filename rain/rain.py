import sys
import pygame
from settings import Settings
from drop import Drop


class Rain:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Rain")

        self.drops = pygame.sprite.Group()
        self._create_drops()

    def _create_drops(self):
        # Сначала создаем каплю и смотрим размеры
        drop = Drop(self, 0, 0)
        width, height = drop.rect.size
        available_space = self.screen_rect.width - width * 2
        drops_count = available_space // (width * 2)
        start_x = width + width / 2
        print(available_space)
        print(width)
        print(drops_count)
        print(start_x)
        for i in range(0, drops_count):
            self.drops.add(Drop(self, start_x, 0))
            start_x += width * 2

    def _update_drops(self):
        # print("Update Drops")
        self.drops.update()

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_drops()
            self._update_screen()

    def _update_screen(self):
        # print("update_screen()")
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    rain = Rain()
    rain.run_game()
