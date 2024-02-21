'''
Created on Aug 1, 2010

@author: OWNER
'''
import pygame, Globals
from PowerUp import PowerUp
pygame.init()
        
class LargeMeat(PowerUp):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.loadImages()
        self.image = self.largeMeatImages[0]
        self.rect = self.image.get_rect()
        self.type = Globals.powerUpLargeMeat
        
        
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.largeMeatImages = []
        
        imgSize = (21, 12)
        offset = ((144, 24))
        
        #for i in range(2):
        tmpImg = pygame.Surface(imgSize)
        tmpImg.blit(imgMaster, (0, 0), (offset, imgSize))
        transColor = tmpImg.get_at((0, 0))
        tmpImg.set_colorkey(transColor)
        self.largeMeatImages.append(tmpImg)
            
    def update(self):
        self.time = 0