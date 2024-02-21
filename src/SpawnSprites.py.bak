'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals, math, random, Fireball
from SpearKnight import  SpearKnight
from AxeKnight import AxeKnight

pygame.init()

def fire(CenterX, CenterY, Direction):
    global fireball
    fireball = Fireball.Fireball()
    Globals.fireballs.add(fireball)
    fireball.rect.center = (CenterX, CenterY)
    fireball.dir = (Direction)
    fireball.state = fireball.FIRING
    if Globals.growth == 1:
        growthScalar = 1
    elif Globals.growth == 2:
        growthScalar = 1.25
    elif Globals.growth == 3:
        growthScalar = 1.5
    #if Globals.growth == 1:
    if Direction == 0:
        fireball.y -= (8*growthScalar)
    elif Direction == 15:
        fireball.x -= (1.4*growthScalar)
        fireball.y -= (6.7*growthScalar)
    elif Direction == 30:
        fireball.x -= (2.7*growthScalar)
        fireball.y -= (5.4*growthScalar)
    elif Direction == 45:
        fireball.x -= (4*growthScalar)
        fireball.y -= (4*growthScalar)
    elif Direction == 60:
        fireball.x -= (5.4*growthScalar)
        fireball.y -= (2.7*growthScalar)
    elif Direction == 75:
        fireball.x -= (6.7*growthScalar)
        fireball.y -= (1.4*growthScalar)                                                      
    elif Direction == 90:
        fireball.x -= (8*growthScalar)
    elif Direction == 105:
        fireball.x -= (6.7*growthScalar)
        fireball.y += (1.4*growthScalar)
    elif Direction == 120:
        fireball.x -= (5.4*growthScalar)
        fireball.y += (2.7*growthScalar)
    elif Direction == 135:
        fireball.x -= (4*growthScalar)
        fireball.y += (4*growthScalar)
    elif Direction == 150:
        fireball.x -= (2.7*growthScalar)
        fireball.y += (5.4*growthScalar)
    elif Direction == 165:
        fireball.x -= (1.4*growthScalar)
        fireball.y += (6.7*growthScalar)
    elif Direction == 180:
        fireball.y += (8*growthScalar)
    elif Direction == 195:
        fireball.x += (1.4*growthScalar)
        fireball.y += (6.7*growthScalar)
    elif Direction == 210:
        fireball.x += (2.7*growthScalar)
        fireball.y += (5.4*growthScalar)
    elif Direction == 225:
        fireball.x += (4*growthScalar)
        fireball.y += (4*growthScalar)
    elif Direction == 240:
        fireball.x += (5.4*growthScalar)
        fireball.y += (2.7*growthScalar)
    elif Direction == 255:
        fireball.x += (6.7*growthScalar)
        fireball.y += (1.4*growthScalar)
    elif Direction == 270:
        fireball.x += (8*growthScalar)
    elif Direction == 285:
        fireball.x += (6.7*growthScalar)
        fireball.y -= (1.4*growthScalar)
    elif Direction == 300:
        fireball.x += (5.4*growthScalar)
        fireball.y -= (2.7*growthScalar)
    elif Direction == 315 or Direction == -45:
        fireball.x += (4*growthScalar)
        fireball.y -= (4*growthScalar)
    elif Direction == 330 or Direction == -30:
        fireball.x += (2.7*growthScalar)
        fireball.y -= (5.4*growthScalar)
    elif Direction == 345 or Direction == -15:
        fireball.x += (1.4*growthScalar)
        fireball.y -= (6.7*growthScalar)
    # y -= 8 is 0
    '''
    if Globals.growth == 2:
        if Direction == 0:
            fireball.y -= 10                                                                        
        elif Direction == 90:
            fireball.x -= 10
        elif Direction == 180:
            fireball.y += 10
        elif Direction == 270:
            fireball.x += 10
            
    if Globals.growth == 3:
        if Direction == 0:
            fireball.y -= 12                                                                       
        elif Direction == 90:
            fireball.x -= 12
        elif Direction == 180:
            fireball.y += 12
        elif Direction == 270:
            fireball.x += 12
    '''    
def spawnEnemy(type, amount, speed):
    for i in range(amount):
        Globals.enemy = str(type).lower        
        Globals.enemy = type()
        thisEnemy = type
        Globals.enemySprites.add(Globals.enemy) 
        
        sideOrTopSpawn = random.randint(0,3)
        if sideOrTopSpawn == 0:
            stagger = random.randint(1,10)
            Globals.enemy.rect.centery = ( random.randrange(8, Globals.screen.get_height()) )
            Globals.enemy.centerx = 0
            while stagger%5 != 0:
                stagger += 1
            else:
                Globals.enemy.dir = 270
                if thisEnemy == Globals.enemySpearKnight:
                    print "this is a spear knight"
                    Globals.enemy.dx += speed
                    Globals.enemy.y = 0
                elif thisEnemy == Globals.enemyAxeKnight:
                    print "this is an axe knight"
                    Globals.enemy.dx += speed
                    Globals.enemy.y = speed#math.sin(speed)
                else:
                    print type
                    print "the enemy is " + str(Globals.enemy)
                    print "a spear knight looks like this " + str(Globals.enemySpearKnight)
                    print "an axe knight looks like this " + str(Globals.enemyAxeKnight)
                    print "thisEnemy looks like this " + str(thisEnemy)
                    print "unknown enemy type"
                
            
        if sideOrTopSpawn == 1:
            stagger = random.randint(1,10)
            Globals.enemy.rect.centerx = ( random.randrange(8, Globals.screen.get_width()) )
            Globals.enemy.rect.centery = 0
            Globals.enemy.x = 0
            while stagger%5 != 0:
                stagger += 1
            else:
                Globals.enemy.dy += speed
            Globals.enemy.dir = 180
            
        if sideOrTopSpawn == 2:
            stagger = random.randint(1,10)
            Globals.enemy.rect.centery = ( random.randrange(8, Globals.screen.get_height()) )
            Globals.enemy.rect.centerx = Globals.screen.get_width()
            while stagger%5 != 0:
                stagger += 1
            else:
                Globals.enemy.dx -= speed
            Globals.enemy.y = 0
            Globals.enemy.dir = 90
            
        if sideOrTopSpawn == 3:
            stagger = random.randint(1,10)
            Globals.enemy.rect.centerx = ( random.randrange(8, Globals.screen.get_width()) )
            Globals.enemy.rect.centery = Globals.screen.get_height()
            Globals.enemy.x = 0
            while stagger%5 != 0:
                stagger += 1
            else:
                Globals.enemy.dy -= speed
            Globals.enemy.dir = 0
    
    print stagger
    print len(Globals.enemySprites) 
    print "%d after stagger" %(amount) 
            
def spawnItem(type, amount):
    for i in range(amount):
        #global item
        Globals.item = str(type).lower
        Globals.item = type()
        Globals.powerups.add(Globals.item)
        Globals.item.rect.center = (random.randrange(0, Globals.screen.get_width()),random.randrange(0, Globals.screen.get_height()))
        
def spawnIten(type, amount, posX, posY):
    for i in range(amount):
        #global item
        Globals.item = str(type).lower
        Globals.item = type()
        Globals.powerups.add(Globals.item)
        Globals.item.rect.center = (posX, posY)
  

def spawnEnvironment(type, amount, startPosX, startPosY):
    for i in range(amount):
        acc = 1
        startPosX = ((25*acc) + startPosX)
        #print type
        #print Globals.obstacle
        #print type()
        Globals.obstacle = str(type).lower
        #print "type is called"
        #print type
        #print Globals.obstacle
        #print type()
        Globals.obstacle = type()
        Globals.environment.add(Globals.obstacle)
        Globals.obstacle.rect.center = (startPosX, startPosY)
        acc += 1
        
def spawnGrowthBarFill(type, thisMeat):
        #thisMeat = Globals.meat
        if Globals.meat%10 == 0:
            Globals.growthBar.clear(Globals.screen,Globals.background)
        else:
            acc = Globals.meat%10
            startPosX = 50
            startPosY = 30
            for i in range(acc):
                print "growth is at"+str(acc)
                startPosX = ((4*acc) + 50)
                Globals.growthBarFill = str(type).lower
                Globals.growthBarFill = type()
                Globals.growthBar.add(Globals.growthBarFill)
                Globals.growthBarFill.rect.center = (startPosX, startPosY)
                acc += 1
            
        