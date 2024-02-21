'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals


def credits():
    #global donePlaying
    #global titleScreen
    #global credtiScreen
    
    Globals.screen.blit(Globals.background, (0, 0))
    
    allSprites = pygame.sprite.Group()
    insFont = pygame.font.SysFont("None", 40)
    
    creditList = (
    " " ,
    " " ,
    " " ,
    "                              Producer",
    "                        Engamin Sanchez" ,
    " " ,
    "                            Sound Effects",
    "                        Engamin Sanchez" ,
    " ",
    "                            Art and Design",
    "                        Engamin Sanchez" ,
    " " ,
    "                           Special Thanks",
    "                             David Nelson" ,
    " " ,
    )   
    
    insLabels = []
    for line in creditList:
        tempLabel = insFont.render(line, 1, (255,255,0))
        insLabels.append(tempLabel)
    
    
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
                if event.key == pygame.K_UP:
                    #return to main menu
                    Globals.donePlaying = False
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    Globals.donePlaying = True
                    
                if event.key == pygame.K_RETURN:
                    #return to main menu
                    Globals.creditScreen = False
                    Globals.titleScreen = True
                    keepGoing = False
                    allSprites.empty()
                
                    
        allSprites.update()
        allSprites.draw(Globals.screen)
        
        for i in range(len(insLabels)):
            Globals.screen.blit(insLabels[i], (50, 30*i))
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return Globals.donePlaying