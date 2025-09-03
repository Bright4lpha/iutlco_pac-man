from __future__ import annotations
from typing import Tuple
import pygame

class SpriteSheet():
    def __init__(self, image: pygame.Surface):
        self.sheet = image
    
    def get_image(self, frame, size: Tuple[any], scale, colour) -> pygame.Surface:
        """_summary_

        Args:
            frame (_type_): _description_
            size (Tuple[int]): _description_
            scale (_type_): _description_
            colour (_type_): _description_

        Returns:
            pygame.Surface: _description_
        """
        image: pygame.Surface = pygame.Surface((size[0],size[1])).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * size[0]),0, size[0],size[1]))
        image = pygame.transform.scale(image, (size[0] * scale, size[1] * scale))
        image.set_colorkey(colour)
        
        return image