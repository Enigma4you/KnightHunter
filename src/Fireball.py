'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals, Dragon
from Projectile import Projectile
pygame.init()

class Fireball(Projectile):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.FIRING = 0
        self.SPREAD = 1
        self.RAPID = 2
        
        self.loadImages()
        self.image = self.fireballImages1[0]
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
         
        self.growth = 1
        
        self.frame = 0
        self.delay = 3
        self.pause = 0
        self.dir = 0
        self.x = 0
        self.y = 0
        
        self.state = self.FIRING
        
    
          
    def update(self):
        fireballCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = fireballCenter
        self.sound()
        self.animation()
        self.checkBounds()
        self.calcVector()
        self.checkGrowth()
        self.rect.center = (self.rect.centerx, self.rect.centery)
        
        
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.fireballImages1 = []
        self.fireballImages2 = []
        self.fireballImages3 = []
        
        imgSize1 = (8, 12)
        imgSize2 = (18, 14)
        imgSize3 = (22, 16)
        offset1 = ((90, 4), (90, 18))
        offset2 = ((100, 4), (100, 20))
        offset3 = ((120, 4), (120, 24))
        
        
        for i in range(2):
            tmpImg = pygame.Surface(imgSize1)
            tmpImg.blit(imgMaster, (0, 0), (offset1[i], imgSize1))
            transColor = tmpImg.get_at((0, 1))
            tmpImg.set_colorkey(transColor)
            self.fireballImages1.append(tmpImg)
            
        for i in range(2):
            tmpImg = pygame.Surface(imgSize2)
            tmpImg.blit(imgMaster, (0, 0), (offset2[i], imgSize2))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.fireballImages2.append(tmpImg)
            
        for i in range(2):
            tmpImg = pygame.Surface(imgSize3)
            tmpImg.blit(imgMaster, (0, 0), (offset3[i], imgSize3))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.fireballImages3.append(tmpImg)   
    
    def sound(self):
        if not pygame.mixer:
            print "problem with sound"
        else:
            pygame.mixer.init()
            self.sndKill = pygame.mixer.Sound("C:\Users\OWNER\Desktop\Assignment\QTR 8\Intermediate Scripting Languages\KnightHunter\src\Assets\Sound\spritedie.ogg")

    def checkGrowth(self):
        if Globals.growth == 1:
            self.growth = 1
        elif Globals.growth == 2:
            self.growth = 2
        elif Globals.growth == 3:
            self.growth = 3
        else:
            print "something is wrong with the fireball growth"

    
    def animation(self):
        fireballCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = fireballCenter
        
        self.pause += 1
        if self.growth == 1:
            if self.pause > self.delay:
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.fireballImages1):
                    self.frame = 0
                    self.state = self.FIRING
                    self.image = pygame.transform.rotate(self.fireballImages1[0], self.dir)
                else:
                    self.image = pygame.transform.rotate(self.fireballImages1[self.frame], self.dir)
                    
        if self.growth == 2:
            if self.pause > self.delay:
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.fireballImages2):
                    self.frame = 0
                    self.state = self.FIRING
                    self.image = pygame.transform.rotate(self.fireballImages2[0], self.dir)
                else:
                    self.image = pygame.transform.rotate(self.fireballImages2[self.frame], self.dir)
                    
                    
        if self.growth == 3:
            if self.pause > self.delay:
                self.pause = 0
                self.frame += 1
                if self.frame >= len(self.fireballImages3):
                    self.frame = 0
                    self.state = self.FIRING
                    self.image = pygame.transform.rotate(self.fireballImages3[0], self.dir)
                else:
                    self.image = pygame.transform.rotate(self.fireballImages3[self.frame], self.dir)
            
    def calcVector(self):
        self.rect.centerx += self.x
        self.rect.centery += self.y
        
    def checkBounds(self):
        if self.rect.centerx > Globals.screen.get_width():
            self.kill()
        if self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > Globals.screen.get_height():
            self.kill()
        if self.rect.centery < 0:
            self.kill()   
            