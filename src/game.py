from __future__ import annotations
import pygame
import pygame.freetype
import sys
import os
from src.scenes.main_menu import MainMenu
from src import constants as const
class Game():
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.freetype.init()
        self.fps = const.FPS
        self.fps_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        pygame.display.set_caption(const.SCREEN_TITLE)
        self.menu = MainMenu()
        self.status = const.GameStatus(2).name

    def run(self):
        while True:

            if self.status == const.GameStatus(2).name and self.menu.current_page == const.MenuState(1).name:
                self.screen.fill(const.BLACK_2)
                self.menu.display_entity_view(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu.quit()
                  
                if event.type == pygame.KEYDOWN and self.status == const.GameStatus(2).name:
                    if event.key == pygame.K_RETURN:
                        if self.menu.current_button_index == 2:
                            self.menu.current_page = const.MenuState(2).name
                            self.menu.clean_entity_view(self.screen)
                            self.menu.credits(self.screen)
                            
                        elif self.menu.current_button_index == 1:
                            self.menu.quit()
                            
                        else:
                            self.status = const.GameStatus(1).name
                            self.menu.play()
                            

                    elif event.key == pygame.K_ESCAPE and self.status == const.GameStatus(2).name and self.menu.current_page == const.MenuState(1).name:
                        self.menu.quit()
                    if event.key == pygame.K_ESCAPE and self.menu.current_page == const.MenuState(2).name:
                        self.menu.current_page = const.MenuState(1).name
                        
                self.menu.select_button()
            pygame.display.flip()
            self.fps_clock.tick(self.fps)

