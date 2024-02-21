'''
Created on Aug 1, 2010

@author: OWNER
'''
from __future__ import print_function

import pygame, Globals, SpawnSprites
pygame.init()              
                
class ScoreboardGUI(pygame.sprite.Sprite):
    def __init__(self):
        #global score
        #global lives
        #global currentWave
        pygame.sprite.Sprite.__init__(self)
        self.lives = Globals.lives
        self.score = Globals.score
        self.meat = Globals.meat
        self.wave = Globals.currentWave
        self.font = pygame.font.SysFont("None", 25)
        

        
    def update(self):
        self.text = "lives: %d  score: %d meat: %d  wave: %d" %(self.lives, self.score, self.meat, self.wave)
        self.image = self.font.render(self.text, 2,(200,50,0))
        self.rect = self.image.get_rect()
        self.wave = Globals.currentWave
        self.score = Globals.score
        self.lives = Globals.lives
        self.meat = Globals.meat
        
        
        
class GrowthBarGUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.loadImages()
        self.image = self.growthBarImages1[0]
        self.rect = self.image.get_rect()
        
        
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/KnightHunterspritesheet08.gif")
        imgMaster = imgMaster.convert()
        
        self.growthBarImages1 = []

        imgSize1 = (72, 21)
        offset1 = (15, 160)
        
        tmpImg = pygame.Surface(imgSize1)
        tmpImg.blit(imgMaster, (0, 0), (offset1, imgSize1))
        transColor = tmpImg.get_at((1, 1))
        tmpImg.set_colorkey(transColor)
        self.growthBarImages1.append(tmpImg)
        
        
    def update(self):
        self.rect.centerx = 40
        self.rect.centery = 26

  
        
class GrowthBarFillGUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.meat = Globals.meat
        
        self.loadImages()
        self.image = self.growthFillImages1[0]
        self.rect = self.image.get_rect()
        
        
    def loadImages(self):
        imgMaster = pygame.image.load("src/Assets/Images/KnightHunterspritesheet08.gif")
        imgMaster = imgMaster.convert()
        
        self.growthFillImages1 = []
        self.growthFillImages2 = []
        self.growthFillImages3 = []
        
        imgSize1 = (7, 7)
        #imgSize1 = (4, 4)
        offset1 = (14, 184)
        offset2 = (23, 184)
        offset3 = (32, 184)
        #offset1 = (4, 180)
        #offset2 = (10, 180)
        #offset3 = (16, 180)
        
        tmpImg = pygame.Surface(imgSize1)
        tmpImg.blit(imgMaster, (0, 0), (offset1, imgSize1))
        transColor = tmpImg.get_at((1, 1))
        tmpImg.set_colorkey(transColor)
        self.growthFillImages1.append(tmpImg)
   
        tmpImg = pygame.Surface(imgSize1)
        tmpImg.blit(imgMaster, (0, 0), (offset2, imgSize1))
        transColor = tmpImg.get_at((1, 1))
        tmpImg.set_colorkey(transColor)
        self.growthFillImages2.append(tmpImg)
        
        tmpImg = pygame.Surface(imgSize1)
        tmpImg.blit(imgMaster, (0, 0), (offset3, imgSize1))
        transColor = tmpImg.get_at((1, 1))
        tmpImg.set_colorkey(transColor)
        self.growthFillImages3.append(tmpImg)
   
    def checkMeat(self):
        print(self.meat%10)
        if self.meat%10 == 0:
            Globals.growthBar.empty()
            SpawnSprites.spawnGrowthBarFill(GrowthBarFillGUI,self.meat)
        elif self.meat%10 == 1:
            self.loadImages()
            self.image = self.growthFillImages1[0]
            self.rect = self.image.get_rect()
            SpawnSprites.spawnGrowthBarFill(GrowthBarFillGUI, self.meat)
        elif self.meat%10 == 9:
            self.loadImages()
            self.image = self.growthFillImages3[0]
            self.rect = self.image.get_rect()
            SpawnSprites.spawnGrowthBarFill(GrowthBarFillGUI, self.meat)
        else:
            self.loadImages()
            self.image = self.growthFillImages2[0]
            self.rect = self.image.get_rect()
            SpawnSprites.spawnGrowthBarFill(GrowthBarFillGUI, self.meat)
        
    def update(self):
        print("before meat is "+str(self.meat))
        self.meat = Globals.meat
        print("after meat is "+str(self.meat))
        self.checkMeat()

           
        #def spawnEnvironment(type, amount, startPosX, startPosY):
        #for i in range(amount):
            #acc = 1
            #startPosX = ((25*acc) + startPosX)
            #global obstacle
            #Globals.obstacle = str(type).lower
            #Globals.obstacle = type()
            #Globals.environment.add(Globals.obstacle)
            #Globals.obstacle.rect.center = (startPosX, startPosY)
            #acc += 1
        
class LivesGUI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)