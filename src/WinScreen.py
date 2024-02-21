'''
Created on Aug 3, 2010

@author: student
'''
import pygame, Globals
pygame.init()

class WinScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.loadImages()
        if Globals.growth == 1:
            self.image = self.WinScreenImages1[0]
        elif Globals.growth == 2:
            self.image = self.WinScreenImages2[0]
        elif Globals.growth == 3:
            self.image = self.WinScreenImages3[0]
        self.rect = self.image.get_rect()
        
    def update(self):
        self.time = 0
        
    def loadImages(self):
        imgMaster1 = pygame.image.load("src/Assets/Images/WinScreen1.gif")
        imgMaster1 = imgMaster1.convert()
        imgMaster2 = pygame.image.load("src/Assets/Images/WinScreen2.gif")
        imgMaster2 = imgMaster2.convert()
        imgMaster3 = pygame.image.load("src/Assets/Images/WinScreen3.gif")
        imgMaster3 = imgMaster3.convert()
        
        self.WinScreenImages1 = []
        self.WinScreenImages2 = []
        self.WinScreenImages3 = []
        
        imgSize = (800, 600)
        offset = (0,0)
        
        tmpImg1 = pygame.Surface(imgSize)
        tmpImg1.blit(imgMaster1, (0, 0), (offset, imgSize))
        transColor = tmpImg1.get_at((0, 0))
        tmpImg1.set_colorkey(0,0)
        self.WinScreenImages1.append(tmpImg1)
        
        tmpImg2 = pygame.Surface(imgSize)
        tmpImg2.blit(imgMaster2, (0, 0), (offset, imgSize))
        transColor = tmpImg2.get_at((0, 0))
        tmpImg2.set_colorkey(0,0)
        self.WinScreenImages2.append(tmpImg2)
        
        tmpImg3 = pygame.Surface(imgSize)
        tmpImg3.blit(imgMaster3, (0, 0), (offset, imgSize))
        transColor = tmpImg3.get_at((0, 0))
        tmpImg3.set_colorkey(0,0)
        self.WinScreenImages3.append(tmpImg3)
        

            