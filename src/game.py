from __future__ import annotations
import pygame
import sys
from src.scenes.main_menu import MainMenu
from src.constants import FPS, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
class Game():
    def __init__(self):
        self.fps = FPS
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.menu = MainMenu()

    def run(self):
        while True:
            self.screen.fill((20, 20, 20))
            self.menu.display_entity_view(self.screen)
            print(self.menu.current_button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            self.fps_clock.tick(self.fps)

