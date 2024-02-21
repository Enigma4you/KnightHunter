'''
Created on Aug 1, 2010

@author: OWNER
'''
import pygame, Globals, random, SpawnSprites
from SmallMeat import *
from LargeMeat import *
from ExtraLife import *
from FlameCone import *
from SpearKnight import *
from AxeKnight import *
from Trees import *
from Boulders import *
#import pygame, SpawnSprites, SmallMeat, LargeMeat, ExtraLife, FlameCone, SpearKnight, AxeKnight, Trees, Boulders, random, Globals
pygame.init()

# waves

def spawnWave(currentWave):
    thisWave = currentWave
    if thisWave == 1:
        wave1()
    elif thisWave == 2:
        wave2()
    elif thisWave == 3:
        wave3()
    elif thisWave == 4:
        wave4()
    elif thisWave == 5:
        wave5()
    elif thisWave == 6:
        wave6()
    elif thisWave == 7:
        wave7()
    elif thisWave == 8:
        wave8()
    elif thisWave == 9:
        wave9()
    elif thisWave == 10:
        wave10()
    
    
    
def wave1():
    #SpawnSprites.spawnEnemy(SpearKnight.SpearKnight,5, 2)
    SpawnSprites.spawnEnemy(AxeKnight, 5, 2)
    SpawnSprites.spawnItem(FlameCone3, 1)
    SpawnSprites.spawnItem(FlameCone5, 1)
    SpawnSprites.spawnItem(SmallMeat, 3)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height(), 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height(), 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height(), 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
    
def wave2():
    SpawnSprites.spawnEnemy(SpearKnight,8,2)
    SpawnSprites.spawnItem(SmallMeat, 2)
    SpawnSprites.spawnItem(LargeMeat, 1)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
def wave3():
    SpawnSprites.spawnEnemy(SpearKnight,7,2)
    SpawnSprites.spawnEnemy(SpearKnight,3,4)
    SpawnSprites.spawnItem(SmallMeat, 1)
    SpawnSprites.spawnItem(LargeMeat, 3)
    SpawnSprites.spawnItem(ExtraLife, 1)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
def wave4():
    SpawnSprites.spawnEnemy(SpearKnight,10,2)
    SpawnSprites.spawnEnemy(SpearKnight,5,4)
    SpawnSprites.spawnItem(SmallMeat, 2)
    SpawnSprites.spawnItem(LargeMeat, 4)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
   
    
def wave5():
    SpawnSprites.spawnEnemy(SpearKnight,15,4)
    SpawnSprites.spawnItem(SmallMeat, 5)
    SpawnSprites.spawnItem(LargeMeat, 5)
    SpawnSprites.spawnItem(ExtraLife, 1)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
    
def wave6():
    SpawnSprites.spawnEnemy(SpearKnight,3,4)
    SpawnSprites.spawnItem(SmallMeat, 20)
    SpawnSprites.spawnItem(LargeMeat, 20)
    SpawnSprites.spawnItem(ExtraLife, 5)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))

    
def wave7():
    SpawnSprites.spawnEnemy(SpearKnight,10,4)
    SpawnSprites.spawnEnemy(SpearKnight,2,8)
    SpawnSprites.spawnItem(SmallMeat, 3)
    SpawnSprites.spawnItem(LargeMeat, 10)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
    
def wave8():
    SpawnSprites.spawnEnemy(SpearKnight,5,4)
    SpawnSprites.spawnEnemy(SpearKnight,5,8)
    SpawnSprites.spawnItem(SmallMeat, 1)
    SpawnSprites.spawnItem(LargeMeat, 20)
    SpawnSprites.spawnItem(ExtraLife, 3)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))

    
def wave9():
    SpawnSprites.spawnEnemy(SpearKnight,5,2)
    SpawnSprites.spawnEnemy(SpearKnight,5,4)
    SpawnSprites.spawnEnemy(SpearKnight,10,8)
    SpawnSprites.spawnItem(SmallMeat, 15)
    SpawnSprites.spawnItem(LargeMeat, 15)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    
def wave10():
    SpawnSprites.spawnEnemy(SpearKnight,10,2)
    SpawnSprites.spawnEnemy(SpearKnight,10,4)
    SpawnSprites.spawnEnemy(SpearKnight,10,8)
    SpawnSprites.spawnItem(SmallMeat, 10)
    SpawnSprites.spawnItem(LargeMeat, 10)
    SpawnSprites.spawnItem(ExtraLife, 5)
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Trees, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    SpawnSprites.spawnEnvironment(Boulders, random.randint(1,3), random.randrange(0,Globals.screen.get_height()-10, 25),  random.randrange(0,Globals.screen.get_height()-10, 25))
    