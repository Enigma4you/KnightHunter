'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals
from Environment import Environment
pygame.init()

class Trees(Environment):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.loadImages()
        self.image = self.treeImages[0]
        self.rect = self.image.get_rect()
        self.type = Globals.environmentTree
        
    
       
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.treeImages = []
        
        imgSize = (25, 25)
        offset = ((240, 4))
        
        tmpImg = pygame.Surface(imgSize)
        tmpImg.blit(imgMaster, (0, 0), (offset, imgSize))
        transColor = tmpImg.get_at((0, 0))
        tmpImg.set_colorkey(transColor)
        self.treeImages.append(tmpImg)
            
    def update(self):
        self.time = 0