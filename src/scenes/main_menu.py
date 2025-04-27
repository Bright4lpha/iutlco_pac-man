from __future__ import annotations
import sys
import pygame
from typing import List, Tuple
from src.constants import FONT, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from src.utils.renderable_interface import RenderableInterface

class Button():
    def __init__(self, x: int, y: int, width: int, height: int, button_label: str, on_click = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.on_click = on_click

        self.font = pygame.font.Font(FONT, 32)
        self.button_label = self.font.render(button_label, True, (255,0,0))
        self.button_rect = self.button_label.get_rect()
        self.button_rect.center = (self.x + (self.width // 2), self.y + (self.height // 4))
        #self.button_surf = self.font.render(button_label, True, (255,0,0))

    #def 

class MainMenu(RenderableInterface):
    def __init__(self):
        self.font = pygame.font.Font(FONT, 32)
        self.title = self.font.render(SCREEN_TITLE, True, (255,255,255))
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6)

        self.buttons: List[Tuple[int,Button,bool]] = [
            (1,Button(565,250,150,50,"Play",self.play),True),
            (2,Button(565,360,150,50,"Quit",self.quit),False),
            (3,Button(565,470,150,50,"Credits", self.credits),False)
        ]
        self.current_button: Tuple[int,Button,bool] = self.buttons[0]
        #self.current_button.button_label.fill((0,0,255))

    def play(self):
        print("play")

    def quit(self):
        print("quit")
        pygame.quit()
        sys.exit()

    def credits(self):
        print("credits")

    def update_entity_view(self):
        return super().update_entity_view()
    
    def display_entity_view(self, screen: pygame.Surface):
        screen.blit(self.title, self.title_rect)
        for button in self.buttons :
            #C'est le rectangle pour les boutons
            #pygame.draw.rect(screen,(255,255,255),button[1].button_rect)
            if button[2] == True:
                print("in the if")
                button[1].button_label = pygame.font.render(button[1].button_label, True, (255,255,0))
            screen.blit(button[1].button_label, button[1].button_rect)


if __name__=="__main__":
    
    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("IUTLCO - Pac-man")
    menu: MainMenu = MainMenu()
    
    while True:
        screen.fill((20, 20, 20))
        menu.display_entity_view(screen)
        print(menu.current_button)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        fpsClock.tick(fps)