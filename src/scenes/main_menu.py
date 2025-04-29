from __future__ import annotations
import sys
import pygame
from src import constants as const
from src.scenes.credits import Credits
from itertools import count
from src.utils.renderable_interface import RenderableInterface
from typing import List

class Button():
    newid = (count(start=0,step=1))
    def __init__(self, x: int, y: int, width: int, height: int, button_label: str, is_selected: bool, on_click = None):
        self.index = next(self.newid)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_selected = is_selected
        self.on_click = on_click

        self.font = pygame.freetype.Font(const.FONT, 32)
        self.label = button_label
        self.button_label = self.font.render(button_label, True, (255,0,0))
        self.button_rect = self.button_label[0].get_rect()
        self.button_rect.center = (self.x + (self.width // 2), self.y + (self.height // 4))

class MainMenu(RenderableInterface):
    def __init__(self):
        self.font = pygame.freetype.Font(const.FONT, 32)
        self.title = self.font.render(const.SCREEN_TITLE,const.BLACK)
        self.title_rect = self.title[0].get_rect()
        self.title_rect.center = (const.SCREEN_WIDTH // 2, const.SCREEN_HEIGHT // 6)

        self.buttons: List[Button] = [
            Button(565,250,150,50,"Play",True,self.play),
            Button(565,360,150,50,"Quit",False,self.quit),
            Button(565,470,150,50,"Credits",False, self.credits)
        ]
        self.current_button_index: int = 0

    def play(self):
        print("play")

    def quit(self):
        print("quit")
        pygame.quit()
        sys.exit()

    def credits(self, screen: pygame.Surface):
        credits_scene = Credits()
        credits_scene.display_entity_view(screen)
        print("credits")
        
    def select_button(self):
        keys = pygame.key.get_pressed()
        step = 1
        if keys[pygame.K_DOWN]:
            if self.current_button_index == 2:
                #set the older current button to False
                self.buttons[self.current_button_index].is_selected = False
                #update index button
                self.current_button_index = 0
                #set the new current button to True
                self.buttons[self.current_button_index].is_selected = True
            else:
                self.buttons[self.current_button_index].is_selected = False
                
                self.current_button_index += step
                self.buttons[self.current_button_index].is_selected = True

            print("Down key is pressed")
        elif keys[pygame.K_UP]:
            step = -1
            if self.current_button_index == 0:
                #set the older current button to False
                self.buttons[self.current_button_index].is_selected = False
                #update index button
                self.current_button_index = 2
                #set the new current button to True
                self.buttons[self.current_button_index].is_selected = True
            else:
                self.buttons[self.current_button_index].is_selected = False
                
                self.current_button_index += step
                self.buttons[self.current_button_index].is_selected = True
            print("Up key is pressed")
        

    def update_entity_view(self):
        return super().update_entity_view()
    
    def display_entity_view(self, screen: pygame.Surface):
        screen.blit(self.title[0], self.title_rect)
        for button in self.buttons :
            #C'est le rectangle pour les boutons
            #pygame.draw.rect(screen,(255,255,255),button[1].button_rect)
            print(f"button : {button.is_selected}")
            if button.is_selected == True:
                button.button_label = self.font.render(button.label, const.YELLOW)
            else:
                button.button_label = self.font.render(button.label, const.WHITE)
            screen.blit(button.button_label[0], button.button_rect)


if __name__=="__main__":
    
    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = const.SCREEN_WIDTH, const.SCREEN_HEIGHT
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