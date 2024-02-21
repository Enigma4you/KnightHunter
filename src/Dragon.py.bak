'''
Created on Jul 31, 2010

@author: OWNER
'''

import pygame, Globals, SpawnSprites
pygame.init()

class Dragon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.STANDING = 0
        self.WALKING = 1
        
        self.UP = 0
        self.RIGHT = 1
        self.DOWN = 2
        self.LEFT = 3
        
        self.NORMAL = 0
        self.FLAMECONE3 = 1
        self.FLAMECONE5 = 2
        self.INVINCIBLE = 3
        
        self.loadImages()
        self.image = self.dragonImages1[0]
        self.rect = self.image.get_rect()
        
        self.rect.center = (Globals.dragonCenterX, Globals.dragonCenterY)
        
        Globals.growth = 1
        
        self.dx = 0
        self.dy = 0
        
        self.frame = 0
        self.delay = 4
        self.pause = 0
        self.firedelay = 0
        
        self.dir = Globals.dragonDirection
        
        self.state = self.STANDING
        self.move = self.UP
        self.powerupactive = self.NORMAL

              
    def loadImages(self):
        imgMaster = pygame.image.load("Assets\Images\KnightHunterspritesheet04.gif")
        imgMaster = imgMaster.convert()
        
        self.dragonImages1 = []
        self.dragonImages2 = []
        self.dragonImages3 = []
        
        imgSize1 = (40, 38)
        imgSize2 = (50, 48)
        imgSize3 = (60, 58)
        offset1 = ((4, 4), (48, 4))
        offset2 = ((4, 47), (58, 47))
        offset3 = ((4, 100), (68, 100))
        
        
        for i in range(2):
            tmpImg = pygame.Surface(imgSize1)
            tmpImg.blit(imgMaster, (0, 0), (offset1[i], imgSize1))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.dragonImages1.append(tmpImg)
            
        for i in range(2):
            tmpImg = pygame.Surface(imgSize2)
            tmpImg.blit(imgMaster, (0, 0), (offset2[i], imgSize2))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.dragonImages2.append(tmpImg)
            
        for i in range(2):
            tmpImg = pygame.Surface(imgSize3)
            tmpImg.blit(imgMaster, (0, 0), (offset3[i], imgSize3))
            transColor = tmpImg.get_at((1, 1))
            tmpImg.set_colorkey(transColor)
            self.dragonImages3.append(tmpImg)
            
              
    def update(self):
        
        #self.calcVector()
        self.checkGrowth()
        self.animation()
        self.checkBounds()
        self.checkKeys()
        self.sound()
        
    def sound(self):
        if not pygame.mixer:
            print "problem with sound"
        else:
            pygame.mixer.init()
            #self.sndEat = pygame.mixer.Sound("C:\Users\OWNER\Desktop\Assignment\QTR 8\Intermediate Scripting Languages\KnightHunter\src\Assets\Sound\eat1.ogg")
            #self.sndFootstep = pygame.mixer.Sound("C:\Users\OWNER\Desktop\Assignment\QTR 8\Intermediate Scripting Languages\KnightHunter\src\Assets\Sound\footstep.ogg")
            #self.sndFireball = pygame.mixer.Sound("C:\Users\OWNER\Desktop\Assignment\QTR 8\Intermediate Scripting Languages\KnightHunter\src\Assets\Sound\fireball.ogg")
            self.sndExtraLife = pygame.mixer.Sound("C:\Users\OWNER\Desktop\Assignment\QTR 8\Intermediate Scripting Languages\KnightHunter\src\Assets\Sound\extralife.ogg")
            
    def checkGrowth(self):
        #check growth to change sprite
        if Globals.meat < 10:
            Globals.growth = 1
        elif Globals.meat < 20:
            Globals.growth = 2
        elif Globals.meat >= 20:
            Globals.growth = 3
    

    def deathAnimation(self):
        self.time = 0
            
    def animation(self):
        dragonCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = dragonCenter
        
        if Globals.growth == 1:
            if self.state == self.STANDING:
                self.image = pygame.transform.rotate(self.dragonImages1[0], self.dir)
            else: 
                self.pause += 1
                if self.pause > self.delay:
                    self.pause = 0
                    #self.sndFootstep.play() 
                    self.frame += 1
                    if self.frame >= len(self.dragonImages1):
                        self.frame = 0
                        self.state = self.STANDING
                        self.image = pygame.transform.rotate(self.dragonImages1[0], self.dir)
                    else:
                        
                        self.image = pygame.transform.rotate(self.dragonImages1[self.frame], self.dir)
                        
        elif Globals.growth == 2:  
            if self.state == self.STANDING:
                self.image = pygame.transform.rotate(self.dragonImages2[0], self.dir)
                self.rect = self.image.get_rect()
                self.rect.center = (Globals.dragonCenterX, Globals.dragonCenterY)
            else: 
                self.pause += 1
                if self.pause > self.delay:
                    self.pause = 0
                    #self.sndFootstep.play() 
                    self.frame += 1
                    if self.frame >= len(self.dragonImages2):
                        self.frame = 0
                        self.state = self.STANDING
                        self.image = pygame.transform.rotate(self.dragonImages2[0], self.dir)
                    else:
                        
                        self.image = pygame.transform.rotate(self.dragonImages2[self.frame], self.dir)
                        
        elif Globals.growth == 3:
            if self.state == self.STANDING:
                self.image = pygame.transform.rotate(self.dragonImages3[0], self.dir)
            else: 
                self.pause += 1
                if self.pause > self.delay:
                    self.pause = 0
                    #self.sndFootstep.play() 
                    self.frame += 1
                    if self.frame >= len(self.dragonImages3):
                        self.frame = 0
                        self.state = self.STANDING
                        self.image = pygame.transform.rotate(self.dragonImages3[0], self.dir)
                    else:
                        
                        self.image = pygame.transform.rotate(self.dragonImages3[self.frame], self.dir)
            
            
                    
        
        
        self.rect.center = (self.rect.centerx,self.rect.centery )
        
    def reset(self):
        Globals.dragonCenterX = 400
        Globals.dragonCenterY = 300
        Globals.dragonDirection = 0
        self.rect.center = (Globals.dragonCenterX, Globals.dragonCenterY)
        
            
    def calcVector(self):
        if self.dir == 0:
            self.dx = 1
            self.dy = 0
        elif self.dir == 45:
            self.dx = .7
            self.dy = .7
        elif self.dir == 90:
            self.dx = 0
            self.dy = -1
        elif self.dir == 135:
            self.dx = -.7
            self.dy = -.7
        elif self.dir == 180:
            self.dx = -1
            self.dy = 0
        elif self.dir == 225:
            self.dx = -.7
            self.dy = .7
        elif self.dir == 270:
            self.dx = 0
            self.dy = 1
        elif self.dir == 315:
            self.dx = .7
            self.dy = .7
        else:
            print "something went wrong"
        
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.moveUp()
            self.state = self.WALKING
        if keys[pygame.K_DOWN]:
            self.moveDown()
            self.state = self.WALKING
        if keys[pygame.K_LEFT]:
            self.moveLeft()
            self.state = self.WALKING
        if keys[pygame.K_RIGHT]:
            self.moveRight()
            self.state = self.WALKING
        if keys[pygame.K_z]:
            self.dragonFire()
        else:
            self.firedelay = 0
            #self.dx = 0
            #self.dy = 0
            
            
    def stop(self):
        self.state = self.STANDING 
        
    def dragonFire(self): 
        if self.firedelay%10 == 0:
            #self.sndFireball.play()
            if self.powerupactive == self.NORMAL:
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, Globals.dragonDirection)
            if self.powerupactive == self.FLAMECONE3:
                tempDir1 = Globals.dragonDirection + 30
                tempDir2 = Globals.dragonDirection - 30
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, Globals.dragonDirection)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir1)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir2)
                print tempDir1
            if self.powerupactive == self.FLAMECONE5:
                tempDir1 = Globals.dragonDirection + 45
                tempDir2 = Globals.dragonDirection + 30
                tempDir3 = Globals.dragonDirection + 15
                tempDir4 = Globals.dragonDirection - 15
                tempDir5 = Globals.dragonDirection - 30
                tempDir6 = Globals.dragonDirection - 45
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, Globals.dragonDirection)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir1)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir2)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir3)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir4)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir5)
                SpawnSprites.fire(Globals.dragonCenterX, Globals.dragonCenterY, tempDir6)
                print tempDir1
                print tempDir2
                print tempDir3
                print tempDir4
                print tempDir5
                print tempDir6
                
            self.firedelay += 1
        else:
            self.firedelay += 1 
    
    def moveUp(self):
        if self.move == self.DOWN:
            self.dy = 0
        elif self.dy >= -4:
            self.dy -= 2
        else:
            self.dy = -4
        self.rect.centery += self.dy
        Globals.dragonCenterY += self.dy
        Globals.dragonDirection = 0
        self.dir = Globals.dragonDirection
        self.move = self.UP
        
    def moveDown(self):
        if self.move == self.UP:
            self.dy = 0
        elif self.dy <= 4:
            self.dy += 2
        else:
            self.dy = +4
        self.rect.centery += self.dy
        Globals.dragonCenterY += self.dy
        Globals.dragonDirection = 180
        self.dir = Globals.dragonDirection
        self.move = self.DOWN
        
    def moveLeft(self):
        if self.move == self.RIGHT:
            self.dx = 0
        elif self.dx >= -4:
            self.dx += -2
        else:
            self.dx = -4
        self.rect.centerx += self.dx
        Globals.dragonCenterX += self.dx
        Globals.dragonDirection = 90
        self.dir = Globals.dragonDirection
        self.move = self.LEFT
               
    def moveRight(self):
        if self.move == self.LEFT:
            self.dx = 0
        elif self.dx <= 4:
            self.dx += 2
        else:
            self.dx = +4
        self.rect.centerx += self.dx
        Globals.dragonCenterX += self.dx
        Globals.dragonDirection = 270
        self.dir = Globals.dragonDirection
        self.move = self.RIGHT
        
    def moveNW(self):
        Globals.dragonCenterX -= 2
        Globals.dragonCenterY -= 2
        Globals.dragonDirection = 45
        self.rect.centerx -= 2
        self.rect.centery -= 2
        self.dir = Globals.dragonDirection
        
    def moveSW(self):
        Globals.dragonCenterX -= 2
        Globals.dragonCenterY += 2
        Globals.dragonDirection = 135
        self.rect.centerx -= 2
        self.rect.centery += 2
        self.dir = Globals.dragonDirection
        
    def moveSE(self):
        Globals.dragonCenterX += 2
        Globals.dragonCenterY += 2
        Globals.dragonDirection = 225
        self.rect.centerx += 2
        self.rect.centery += 2
        self.dir = Globals.dragonDirection
        
    def moveNE(self):
        Globals.dragonCenterX += 2
        Globals.dragonCenterY -= 2
        Globals.dragonDirection = 315
        self.rect.centerx += 2
        self.rect.centery -= 2
        self.dir = Globals.dragonDirection
        
    def checkBounds(self):
        if self.rect.centerx > Globals.screen.get_width():
            Globals.dragonCenterX = 0
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            Globals.dragonCenterX = Globals.screen.get_width()
            self.rect.centerx = Globals.screen.get_width()
        if self.rect.centery > Globals.screen.get_height():
            Globals.dragonCenterY = 0
            self.rect.centery = 0
        if self.rect.centery < 0:
            Globals.dragonCenterY = Globals.screen.get_height()
            self.rect.centery = Globals.screen.get_height()
            
