from __future__ import annotations
import pygame
import pygame.freetype
import sys
from scenes.main_menu import MainMenu
import constants as const
class Game():
    def __init__(self):
        pygame.init()
        pygame.freetype.init()
        self.fps = const.FPS
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.SCREEN_TITLE)
        self.menu = MainMenu()

    def run(self):
        while True:
            print(f"current button index : {self.menu.current_button_index}")
            self.screen.fill(const.BLACK_2)
            self.menu.display_entity_view(self.screen)
            print(self.menu.buttons[self.menu.current_button_index].label)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.menu.current_button_index == 2:
                        self.menu.credits(self.screen)
                self.menu.select_button()
            pygame.display.flip()
            self.fps_clock.tick(self.fps)

