'''
Created on Aug 1, 2010

@author: OWNER
'''
from __future__ import print_function

import pygame
pygame.init()
        
class Projectile(pygame.sprite.Sprite):
    def __init__(self, Fireball):
        pygame.sprite.Sprite.__init__(self, Fireball)
        self.x = 0
        self.y = 0
        
    def calcVector(self):
        if self.dir == 0:
            self.dx = 1
            self.dy = 0
        elif self.dir == 45:
            self.dx = .7
            self.dy = .7
        elif self.dir == 90:
            self.dx = 0
            self.dy = -1
        elif self.dir == 135:
            self.dx = -.7
            self.dy = -.7
        elif self.dir == 180:
            self.dx = -1
            self.dy = 0
        elif self.dir == 225:
            self.dx = -.7
            self.dy = .7
        elif self.dir == 270:
            self.dx = 0
            self.dy = 1
        elif self.dir == 315:
            self.dx = .7
            self.dy = .7
        else:
            print("something went wrong")