'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()
 
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, SmallMeat, LargeMeat, ExtraLife, FlameCone):
        pygame.sprite.Sprite.__init__(self, SmallMeat, LargeMeat, ExtraLife, FlameCone)
        self.type = ""