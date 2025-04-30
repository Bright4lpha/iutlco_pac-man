import pygame
import sys
from src.utils.renderable_interface import RenderableInterface
from src import constants as const

class Credits(RenderableInterface):
    def __init__(self):
        self.font = pygame.freetype.Font(const.FONT, 32)
        self.title = self.font.render("Crédits",const.BLACK)
        self.title_rect = self.title[0].get_rect()
        self.title_rect.center = (const.SCREEN_WIDTH // 2, const.SCREEN_HEIGHT // 6)
        
    def display_entity_view(self, screen):
        screen.blit(self.title[0], self.title_rect)
    
    def update_entity_view(self):
        return super().update_entity_view()
    
    def clean_entity_view(self):
        return super().clean_entity_view()
        
if __name__=="__main__":
    
    pygame.init()
    fps = 60
    fpsClock = pygame.time.Clock()
    width, height = const.SCREEN_WIDTH, const.SCREEN_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("IUTLCO - Pac-man")
    credits: Credits = Credits()
    
    while True:
        screen.fill((20, 20, 20))
        credits.display_entity_view(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        fpsClock.tick(fps)