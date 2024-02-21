'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame
pygame.init()

class PauseMenuScreen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.RESUME = 0
        self.MAINMENU = 1
        self.CREDITS = 2
        self.QUIT = 3
        
        self.state = 0
        
        self.loadImages()
        self.image = self.menuImages[0]
        self.rect = self.image.get_rect()
        
        self.rect.center = (400,300)
        
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/StartMenu.gif")
        imgMaster = imgMaster.convert()
        
        self.menuImages = []
        
        imgSize = (800, 600)
        offset = (0, 0)
        
        
        tmpImg = pygame.Surface(imgSize)
        tmpImg.blit(imgMaster, (0, 0), (offset, imgSize))
        transColor = tmpImg.get_at(( 0, 0 ))
        tmpImg.set_colorkey(transColor)
        self.menuImages.append(tmpImg)
            
              
    def update(self):
        self.checkKeys()
            
        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]:
         #   if self.menudelay%10 == 0:
          #      self.moveDown()
           #     self.menudelay += 1
            #else:
               # self.menudelay += 1
        if keys[pygame.K_DOWN]:
            if self.menudelay%10 == 0:
                self.moveUp()
                self.menudelay += 1
            else:
                self.menudelay += 1
                
        else:
            self.menudelay = 0
            
                
    def moveUp(self):
        self.state += 1
        if self.state > 3:
            self.state = 0
        
    def moveDown(self):
        self.state -= 1
        if self.state < 0:
            self.state = 3