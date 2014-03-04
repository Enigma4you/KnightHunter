'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()

class GameOverScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets\Images\GameOver.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        
    def update(self):
        self.time = 0