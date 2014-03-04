'''
Created on Feb 27, 2013

@author: OWNER
'''

import pygame, Globals
from PowerUp import PowerUp
pygame.init()

class FlameCone5(PowerUp):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        
        self.WAITING = 0
        self.state = self.WAITING
        self.frame = 0
        self.delay = 2
        self.pause = 0
        
        self.loadImages()
        self.image = self.flameCone5Images[0]
        self.rect = self.image.get_rect()
        self.type = Globals.powerUpFlameCone5
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet05.gif")
        imgMaster = imgMaster.convert()
        
        self.flameCone5Images = []
        
        imgSize = (16, 16)
        offset = ((112, 48), (128, 48), (144, 48), (160, 48))
        
        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(transColor)
            self.flameCone5Images.append(tmpImg)
            
    def update(self):
        self.time = 0
        self.animation()
         
        
        
    def animation(self):
        flameCone5Center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = flameCone5Center
            
        
        #if self.state == self.WAITING:
        #    self.image = self.fireballImages[1]
        #else:
        self.pause += 1
        if self.pause > self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.flameCone5Images):
                self.frame = 0
                self.state = self.WAITING
                self.image = self.flameCone5Images[0]
            else:
                self.image = self.flameCone5Images[self.frame]
                

class FlameCone3(PowerUp):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.WAITING = 0
        self.state = self.WAITING
        self.frame = 0
        self.delay = 2
        self.pause = 0
                
        self.loadImages()
        self.image = self.flameCone3Images[0]
        self.rect = self.image.get_rect()
        self.type = Globals.powerUpFlameCone3
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet05.gif")
        imgMaster = imgMaster.convert()
        
        self.flameCone3Images = []
        
        imgSize = (16, 16)
        offset = ((112, 64), (128, 64), (144, 64), (160, 64))
        
        for i in range(4):
            tmpImg = pygame.Surface(imgSize)
            tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
            transColor = tmpImg.get_at((0, 0))
            tmpImg.set_colorkey(transColor)
            self.flameCone3Images.append(tmpImg)
            
    def update(self):
        self.time = 0
        self.animation()
         
        
        
    def animation(self):
        flameCone3Center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = flameCone3Center
            
        
        #if self.state == self.WAITING:
        #    self.image = self.fireballImages[1]
        #else:
        self.pause += 1
        if self.pause > self.delay:
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.flameCone3Images):
                self.frame = 0
                self.state = self.WAITING
                self.image = self.flameCone3Images[0]
            else:
                self.image = self.flameCone3Images[self.frame]
                