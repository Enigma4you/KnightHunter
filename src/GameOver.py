'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals
from GameOverScreen import *
#import pygame, Globals, GameOverScreen
pygame.init()

def gameover():
    
    gameoverscreen = GameOverScreen.GameOverScreen()   
    allSprites = pygame.sprite.Group(gameoverscreen)
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                keepGoing = False
                Globals.donePlaying = True
                
                
            elif event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    Globals.donePlaying = True
            
                if event.key == pygame.K_RETURN:
                    #return to main menu
                    Globals.currentWave = 1
                    Globals.lives = 3
                    Globals.meat = 0
                    Globals.growth = 1
                    Globals.gameOver = False
                    Globals.winScreen = False
                    Globals.donePlaying = False
                    Globals.titleScreen = True
                    Globals.mainGame = False
                    Globals.resume = False
                    clearSprites = True
                    Globals.startMenu = False
                    keepGoing = False
                
            
                                
        allSprites.update()
        allSprites.draw(Globals.screen)
        
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return Globals.donePlaying