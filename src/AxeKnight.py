'''
Created on Jul 20, 2011

@author: Enigma4you
'''

import pygame, Globals
from Enemies import Enemies
pygame.init()


class AxeKnight(Enemies):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.STANDING = 0
        self.WALKING = 1
        
        self.loadImages()
        self.image = self.axeKnightImages[0]
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        
        self.type = Globals.enemyAxeKnight
         
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        
        self.state = self.WALKING
        
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.axeKnightImages = []
        
        imgSize = (16, 38)
        offset = ((192,4), (212, 4))
        
        for i in range(2):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(transColor)
            self.axeKnightImages.append(tmpImg)   
            
    def animation(self):
        if self.state == self.STANDING:
            self.image = pygame.transform.rotate(self.axeKnightImages[1], self.dir)
        else:
            self.pause += 1
            if self.pause > self.delay:
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.axeKnightImages):
                    self.frame = 0
                    self.state = self.WALKING
                    self.image = pygame.transform.rotate(self.axeKnightImages[0], self.dir)
                else:
                    self.image = pygame.transform.rotate(self.axeKnightImages[self.frame], self.dir)
        
    def update(self): 
        fireballCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = fireballCenter
        self.animation()
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        self.checkBounds()
        
class AxeKnightSlow(Enemies):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class AxeKnightMedium(Enemies):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
class AxeKnightFast(Enemies):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
