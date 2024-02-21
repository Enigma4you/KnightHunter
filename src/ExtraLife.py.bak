'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals
from PowerUp import PowerUp
pygame.init()

class ExtraLife(PowerUp):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.WAITING = 0
        self.state = self.WAITING
        self.frame = 0
        self.delay = 2
        self.pause = 0
        
        self.loadImages()
        self.image = self.extraLifeImages[0]
        self.rect = self.image.get_rect()
        self.type = Globals.powerUpExtraLife
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.extraLifeImages = []
        
        imgSize = (16, 10)
        offset = ((168,4), (168, 16))
        
        for i in range(2):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(transColor)
            self.extraLifeImages.append(tmpImg)
          
    def update(self):
        
        self.animation()
         
        
        
    def animation(self):
        extraLifeCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = extraLifeCenter
            
        
        #if self.state == self.WAITING:
        #    self.image = self.fireballImages[1]
        #else:
        self.pause += 1
        if self.pause > self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.extraLifeImages):
                self.frame = 0
                self.state = self.WAITING
                self.image = self.extraLifeImages[0]
            else:
                self.image = self.extraLifeImages[self.frame]
                