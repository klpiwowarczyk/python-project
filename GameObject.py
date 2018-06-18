import pygame
import os

class GameObject(pygame.sprite.Sprite):
    def __init__(self,image_name):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Sprites',image_name))
        self.rect = self.image.get_rect()




