'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals
pygame.init()


def instructions():
    global donePlaying
    global titleScreen
    global howToPlay
    
    Globals.screen.blit(Globals.background, (0, 0))
    
    allSprites = pygame.sprite.Group()
    insFont = pygame.font.SysFont("None", 40)
    
    instructions = (
    " ",
    " ",
    "Knight Hunter.",
    "Objective: You are an innocent dragon" ,
    "defending yourself against the violent",
    "knights threatening your existence." 
    " " ,
    "How to Play:" ,
    "Defeat each wave of enemies using your" ,
    "fireballs." ,
    " ",
    "arrow keys - move your dragon" ,
    "z - fireballs" ,
    "p - pause menu" ,
    " " ,
    "Pick up the meat to grow bigger" ,
    "Pick up the flashing emblems for extra lives" ,
    "Just burninate everything!",
    " ",          
    "Press Enter to go back..."
    )
    
    insLabels = []
    for line in instructions:
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
                    allSprites.empty()
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    Globals.donePlaying = True
                    allSprites.empty()
                    
                if event.key == pygame.K_RETURN:
                    #return to main menu
                    Globals.howToPlay = False
                    Globals.titleScreen = True
                    keepGoing = False
                    allSprites.empty()
                    
                
        allSprites.clear(Globals.screen, Globals.background)      
        allSprites.update()
        allSprites.draw(Globals.screen)
        
        for i in range(len(insLabels)):
            Globals.screen.blit(insLabels[i], (50, 30*i))
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return Globals.donePlaying