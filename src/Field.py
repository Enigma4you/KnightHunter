'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()

# Environment
class Field(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/Assets/Images/FieldBackGround.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    
        
    def update(self):
        self.time = 0
        
        