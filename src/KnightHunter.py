'''
Created on May 12, 2010

@author: Engamin Sanchez

---    A game where the player controls a dragon and destroys
---    the enemy waves of monsters to clear each round.
---    Obstacles and power ups make the game more interesting.
'''
from __future__ import print_function
import pygame, Globals, Credits, Game, GameOver, Instructions, Title, PauseMenu, Win
pygame.init()



# ---------------------------------------------------------------------------------

def main():
    
    #global donePlaying 
    #global titleScreen
    #global howToPlay
    #global mainGame
    #global gameOver
    #global creditScreen
    #global startMenu
    #global menu
    #global clearSprites
    
    while Globals.donePlaying != True:
        print(str(Globals.donePlaying))
        if Globals.titleScreen == True:
            Title.title()
        elif Globals.howToPlay == True:
            Instructions.instructions()
        elif Globals.mainGame == True:
            Game.game()
        elif Globals.pauseMenu == True:
            PauseMenu.pausemenu()
        elif Globals.gameOver == True:
            GameOver.gameover()
        elif Globals.creditScreen == True:
            Credits.credits()
        elif Globals.winScreen == True:
            Win.win()
            
        


# --------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------
