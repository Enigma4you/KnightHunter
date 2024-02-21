'''
Created on Aug 1, 2010

@author: OWNER
'''

from builtins import range
import pygame, Globals, MainMenuScreen, Pointer
pygame.init()

def title():
    
    #global score
    #global donePlaying
    #global titleScreen
    #global howToPlay
    #global mainGame
    #global gameOver
    #global creditScreen
    #global clearSprites
    
    Globals.screen.blit(Globals.background, (0, 0))
    
    menu = MainMenuScreen.MainMenuScreen()
    pointer = Pointer.Pointer()   
    allSprites = pygame.sprite.Group(menu, pointer)
    insFont = pygame.font.SysFont("None", 40)
    
    mainMenu = (
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
    " ",
    " ",
    " ",
    "       Start",
    "    Instructions",
    "      Credits",
    "       Quit", 
    " ",
    "  Last Score: %d " % Globals.score,
    )
    
    
    insLabels = []
    for line in mainMenu:
        tempLabel = insFont.render(line, 1, (255,255,0))
        insLabels.append(tempLabel)
    
    
    
    
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            
            if menu.state == 0:
                pointer.rect.center = (90, 405)
            elif menu.state == 1:
                pointer.rect.center = (75, 435)
            elif menu.state == 2:
                pointer.rect.center = (90, 460)
            elif menu.state == 3:
                pointer.rect.center = (95, 495)
                
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
                        #start game
                        Globals.donePlaying = False
                        Globals.mainGame = True
                        Globals.clearSprites = True
                    elif menu.state == 1:
                        #go to instructions
                        Globals.donePlaying = False
                        Globals.howToPlay = True
                        allSprites.empty()
                    elif menu.state == 2:
                        #show credits
                        Globals.donePlaying = False
                        Globals.creditScreen = True
                        allSprites.empty()
                    elif menu.state == 3:
                        #exit game
                        Globals.donePlaying = True
                        allSprites.empty()
                    keepGoing = False
                    Globals.titleScreen = False
       
            
        allSprites.clear(Globals.screen, Globals.background)            
        allSprites.update()
        allSprites.draw(Globals.screen)
        
        for i in range(len(insLabels)):
            Globals.screen.blit(insLabels[i], (50, 30*i))
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return Globals.donePlaying
