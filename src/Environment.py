'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()

class Environment(pygame.sprite.Sprite):
    def __init__(self, Trees, Boulders):
        pygame.sprite.Sprite.__init__(self)
        