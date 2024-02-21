'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals

pygame.init()

# Enemy avatars
class Enemies(pygame.sprite.Sprite):
    def __init__(self, SpearKnight, AxeKnight):
        pygame.sprite.Sprite.__init__(self, SpearKnight, AxeKnight)
    
            
    def checkBounds(self):
        if self.rect.centerx > Globals.screen.get_width():
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = Globals.screen.get_width()
        if self.rect.centery > Globals.screen.get_height():
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = Globals.screen.get_height()
            