# class Ghost():
#     def __init__(self):
#         pass
    
# if __name__ == "__main__":
#     import pygame
#     from src.utils.sprite_sheet import SpriteSheet
#     import src.constants as const
    
#     pygame.init()

#     SCREEN_WIDTH = 500
#     SCREEN_HEIGHT = 500
    
#     BG = (50, 50, 50)
#     BLACK = (0, 0, 0)

#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
#     sprite_sheet_image = pygame.image.load(const.BLUE_GHOST).convert_alpha()
#     sprite_sheet = SpriteSheet(sprite_sheet_image)
    
#     sprite_sheet_image_2 = pygame.image.load(const.RED_GHOST).convert_alpha()
#     sprite_sheet_2 = SpriteSheet(sprite_sheet_image_2)
    
#     sprite_sheet_image_3 = pygame.image.load(const.ORANGE_GHOST).convert_alpha()
#     sprite_sheet_3 = SpriteSheet(sprite_sheet_image_3)
    
#     sprite_sheet_image_4 = pygame.image.load(const.GREEN_GHOST).convert_alpha()
#     sprite_sheet_4 = SpriteSheet(sprite_sheet_image_4)
    
#     animation_list = []
#     animation_list_2 = []
#     animation_list_3 = []
#     animation_list_4 = []
#     animation_steps = 8
#     dx = 0.5
#     dy = 0.5
    
#     last_update = pygame.time.get_ticks()
#     animation_cooldown = 200
#     frame = 0
    
#     for x in range(animation_steps):
#         animation_list.append(sprite_sheet.get_image(x, (16, 15), 3, BLACK))
#         animation_list_2.append(sprite_sheet_2.get_image(x, (16, 15), 3, BLACK))
#         animation_list_3.append(sprite_sheet_3.get_image(x, (16, 15), 3, BLACK))
#         animation_list_4.append(sprite_sheet_4.get_image(x, (16, 15), 3, BLACK))


    
    
#     run = True
#     while run:


#         screen.fill(BG)
        
#         current_time = pygame.time.get_ticks()
        
#         if current_time - last_update >= animation_cooldown:
#             frame += 1
#             last_update = current_time
#             if frame >= len(animation_list):
#                 frame = 0

#         for x in range(animation_steps):
#             screen.blit(animation_list[frame], (0, 0))
#             screen.blit(animation_list_2[frame], (450, 0))
#             screen.blit(animation_list_3[frame], (0, 450))
#             screen.blit(animation_list_4[frame], (450, 450))
       

#         #event handler
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#         pygame.display.update()

#     pygame.quit()

import pygame
import os
from src.utils.sprite_sheet import SpriteSheet
import src.constants as const

import pygame, sys
from pytmx.util_pygame import load_pygame
from src import constants as const

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=pos)

class Ghost():
    def __init__(self, x, y, animation_list, clockwise=True):
        self.x = x
        self.y = y
        self.speed = 5
        self.clockwise = clockwise
        self.animations = animation_list
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.cooldown = 200
        self.dir_index = 0  # 0:right, 1:down, 2:left, 3:up
        self.directions = self.get_directions(clockwise)

    def get_directions(self, clockwise):
        if clockwise:
            return [(1, 0), (0, 1), (-1, 0), (0, -1)]
        else:
            return [(0, 1), (-1, 0), (0, -1), (1, 0)]

    def move(self):
        dx, dy = self.directions[self.dir_index]
        self.x += dx * self.speed
        self.y += dy * self.speed

        # Changement de direction au centre (limites du carré)
        if self.x >= 250 and dx > 0: self.dir_index = (self.dir_index + 1) % 4
        if self.y >= 250 and dy > 0: self.dir_index = (self.dir_index + 1) % 4
        if self.x <= 0 and dx < 0: self.dir_index = (self.dir_index + 1) % 4
        if self.y <= 0 and dy < 0: self.dir_index = (self.dir_index + 1) % 4

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.cooldown:
            self.frame = (self.frame + 1) % len(self.animations)
            self.last_update = current_time

    def draw(self, screen):
        screen.blit(self.animations[self.frame], (self.x, self.y))

    def update(self, screen):
        self.move()
        self.update_animation()
        self.draw(screen)



os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1024

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = (50, 50, 50)
BLACK = (0, 0, 0)


def load_ghost_animation(path):
    sheet = SpriteSheet(pygame.image.load(path).convert_alpha())
    return [sheet.get_image(x, (16, 15), 3, BLACK) for x in range(8)]

blue_ghost = load_ghost_animation(const.BLUE_GHOST)
red_ghost = load_ghost_animation(const.RED_GHOST)
orange_ghost = load_ghost_animation(const.ORANGE_GHOST)
green_ghost = load_ghost_animation(const.GREEN_GHOST)

ghosts = [
    Ghost(0, 0, blue_ghost, clockwise=True),
    Ghost(450, 0, red_ghost, clockwise=False),
    Ghost(0, 450, orange_ghost, clockwise=False),
    Ghost(450, 450, green_ghost, clockwise=True),
]

sprite_group = pygame.sprite.Group()

tmx_data = load_pygame(const.MAP_BACKGROUND)

for layer in tmx_data.visible_layers:
    print(layer)
    if hasattr(layer, 'data'):
        for x,y,surf in layer.tiles():
            print(x,y,surf)
            pos = (x*32, y*32)
            Tile(pos=pos, surf=surf, groups=sprite_group)

run = True
clock = pygame.time.Clock()

while run:
    screen.fill(BG)
    sprite_group.draw(screen)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for ghost in ghosts:
        ghost.update(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
