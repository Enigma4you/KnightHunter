'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()

class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.loadImages()
        self.image = self.pointerImage[0]
        self.rect = self.image.get_rect()
        
        self.rect.center = (90, 405)
        
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.pointerImage = []
        
        imgSize = (20, 12)
        offset = (168, 28)
        
        
        tmpImg = pygame.Surface(imgSize)
        tmpImg.blit(imgMaster, (0, 0), (offset, imgSize))
        transColor = tmpImg.get_at(( 0, 0 ))
        tmpImg.set_colorkey(transColor)
        self.pointerImage.append(tmpImg)
        
    def update(self):
        self.time = 0

            
