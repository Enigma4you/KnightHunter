'''
Created on Aug 1, 2010

@author: OWNER
'''

from builtins import range
import pygame, Globals, PauseMenuScreen, Pointer
pygame.init()

def pausemenu():
        
    #global donePlaying
    #global titleScreen
    #global startMenu
    #global mainGame
    #global creditScreen
    #global resume
    #global clearSprites
    #global lives
    #global currentWave
    
    menu = PauseMenuScreen.PauseMenuScreen()
    pointer = Pointer.Pointer()   
    allSprites = pygame.sprite.Group(menu, pointer)
    insFont = pygame.font.SysFont("None", 40)
    
    pointer.rect.center = ( 340, 314 )
    startMenu = (
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "                                      Resume",
    "                                    Start Menu",
    "                                      Credits",
    "                                        Quit", 
    " ",
    "                                      Score: %d " % Globals.score,
    "                                      Lives: %d " % Globals.lives,
    )
    
    insLabels = []
    for line in startMenu:
        tempLabel = insFont.render(line, 1, (255,255,0))
        insLabels.append(tempLabel)
        
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():

            
            if menu.state == 0:
                pointer.rect.center = (340, 314)
            elif menu.state == 1:
                pointer.rect.center = (325, 344)
            elif menu.state == 2:
                pointer.rect.center = (340, 375)
            elif menu.state == 3:
                pointer.rect.center = (355, 405)
            
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
                
                
            elif event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
            
                if event.key == pygame.K_RETURN:
                    if menu.state == 0:
                        #resume game
                        Globals.donePlaying = False
                        Globals.titleScreen = False
                        Globals.mainGame = True
                        Globals.resume = True
                        Globals.clearSprites = False
                    elif menu.state == 1:
                        #go to main menu
                        Globals.donePlaying = False
                        Globals.titleScreen = True
                        Globals.creditScreen = False
                        Globals.resume = False
                        allSprites.empty()
                        Globals.lives = 3
                        Globals.growth = 1
                        Globals.meat = 0
                        Globals.currentWave = 1
                        
                    elif menu.state == 2:
                        #go to credits
                        Globals.donePlaying = False
                        Globals.titleScreen = False
                        Globals.creditScreen = True
                        Globals.pauseMenu = False
                        Globals.resume = False
                        allSprites.empty()
                        Globals.lives = 3
                        Globals.currentWave = 1
                        
                    elif menu.state == 3:
                        #quit
                        Globals.donePlaying = True
                        allSprites.empty()
                
                    
                    Globals.startMenu = False
                    keepGoing = False
                
            
                    
        allSprites.clear(Globals.screen, Globals.background)             
        allSprites.update()
        allSprites.draw(Globals.screen)
        
        for i in range(len(insLabels)):
            Globals.screen.blit(insLabels[i], (50, 30*i))
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return Globals.donePlaying
