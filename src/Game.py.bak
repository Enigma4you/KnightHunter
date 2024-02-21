'''
Created on Aug 1, 2010

@author: OWNER
'''

import pygame, Globals, Dragon, Boulders, ExtraLife, Field, Fireball, LargeMeat, SmallMeat, FlameCone, ScoreboardGUI
import SpawnSprites, Waves, SpearKnight, AxeKnight
pygame.init()

def game():
    
    if Globals.clearSprites == True:
        Globals.environment.empty()
        Globals.powerups.empty()
        Globals.fireballs.empty()
        Globals.enemySprites.empty()
        Globals.gameGUI.empty()
        

    pygame.display.set_caption("Knight Hunter - Defend against the vicious knights")

    Globals.screen.blit(Globals.background, (0, 0))
    
    field = Field.Field()
    dragon = Dragon.Dragon()
    growthBarOutline = ScoreboardGUI.GrowthBarGUI()
    scoreboard = ScoreboardGUI.ScoreboardGUI()
    fieldSprite = pygame.sprite.Group(field)
    friendlySprites = pygame.sprite.Group(dragon)
    scoreSprites = pygame.sprite.Group(scoreboard, growthBarOutline)

    
    if Globals.resume == False:
        Globals.score = 0
        Waves.spawnWave(Globals.currentWave)
       # SpawnSprites.spawnGrowthBarFill(Globals.meat)
        Globals.clearSprites = False
        
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            
            #clearing sprites without leaving the game() function
            #if Globals.clearSprites == True:
                #Globals.environment.empty()
                #Globals.powerups.empty()
                #Globals.fireballs.empty()
                #Globals.enemySprites.empty()
                #Globals.gameGUI.empty()
            
            print Globals.growthBar
            print len(Globals.growthBar)
            print Globals.growthBarFill
            
                      
            if scoreboard.lives <= -1:
                Globals.gameOver = True
                Globals.resume = False
                Globals.clearSprites = True
                Globals.mainGame = False
                keepGoing = False
            
            if event.type == pygame.QUIT:
                Globals.donePlaying = True
                keepGoing = False
                
                
            elif event.type == pygame.KEYDOWN:
                keyName = pygame.key.name(event.key)
                if event.key == pygame.K_ESCAPE:
                    Globals.donePlaying = True
                    keepGoing = False
                    
                if event.key == pygame.K_p:
                    keepGoing = False
                    Globals.pauseMenu = True
                    Globals.mainGame = False
                    Globals.resume = True
                    Globals.clearSprites = False
                         
         
         
        hitEnvironment = pygame.sprite.spritecollide(dragon, Globals.environment, False)
        for theEnvironment in hitEnvironment:
            if theEnvironment.type == Globals.environmentTree:  
                dragon.state = dragon.STANDING
                dragon.dx = 0
                dragon.dy = 0
            elif theEnvironment.type == Globals.environmentBoulder:
                dragon.dx = 0
                dragon.dy = 0
                
        hitPowerUp = pygame.sprite.spritecollide(dragon, Globals.powerups, True)
        for powerUps in hitPowerUp: 
            print powerUps.type
            if powerUps.type == Globals.powerUpSmallMeat:
                print Globals.growth
                #dragon.sndEat.play()
                Globals.score += 500
                Globals.meat += 1
                #SpawnSprites.spawnGrowthBarFill(Globals.meat)
                if Globals.meat >= 30:
                    Globals.meat = 30
                scoreboard.score = Globals.score
                        
            elif powerUps.type == Globals.powerUpLargeMeat:
                print Globals.growth
                #dragon.sndEat.play()   
                Globals.score += 1250
                Globals.meat += 2
                if Globals.meat >= 30:
                    Globals.meat = 30
                scoreboard.score = Globals.score
                    
            elif powerUps.type == Globals.powerUpExtraLife:
                #dragon.sndExtraLife.play()
                Globals.score += 75
                Globals.lives += 1
                scoreboard.lives = Globals.lives
                scoreboard.score = Globals.score
                
            elif powerUps.type == Globals.powerUpFlameCone3:
                # this will give score, destroy the sprite, and start counting
                # down the timer for the flame cone
                Globals.score += 150
                dragon.powerupactive = dragon.FLAMECONE3
                
            elif powerUps.type == Globals.powerUpFlameCone5:
                # this will give score, destroy the sprite, and start counting
                # down the timer for the flame cone
                Globals.score += 350
                dragon.powerupactive = dragon.FLAMECONE5
                
            else:
                print "got a power up type I don't understand"
                        
        
        bounceEnemies = pygame.sprite.groupcollide(Globals.environment, Globals.enemySprites, False, False)
        if bounceEnemies:
            for theEnemyBounce in bounceEnemies:
                if theEnemyBounce.type == Globals.enemySpearKnight:
                    theEnemyBounce.dx *= -1
                    theEnemyBounce.dy *= -1
                    
       
 
        hitEnemies = pygame.sprite.spritecollide(dragon, Globals.enemySprites, True)
        if hitEnemies:
            for theEnemyHit in hitEnemies:
                if theEnemyHit.type == Globals.enemySpearKnight:
                    SpawnSprites.spawnEnemy(SpearKnight.SpearKnight, 1, 2)
                #elif theEnemyHit == SpearKnightMedium:
                    #SpawnSprites.spawnEnemy(SpearKnight.SpearKnight, 1, 4, SpawnSprites)
                #elif theEnemyHit == SpearKnightFast:
                    #SpawnSprites.spawnEnemy(SpearKnight.SpearKnight, 1, 8, SpawnSprites)
                else:
                    print theEnemyHit
                    print theEnemyHit.type
                    print "enemy spawn error"
                    
                Globals.lives -= 1
                Globals.meat /= 2
                scoreboard.lives = Globals.lives
                dragon.reset()
        
        for fireball in Globals.fireballs:        
            burnEnemies = pygame.sprite.spritecollide(fireball, Globals.enemySprites, True)
            if burnEnemies:
                for enemyBurned in burnEnemies:
                    Globals.score += 3000
                    scoreboard.score = Globals.score
                    #fireball.sndKill.play()
                    fireball.kill()
                    SpawnSprites.spawnIten(SmallMeat.SmallMeat, 1, enemyBurned.x, enemyBurned.y)
                    #SpawnSprites.spawnItem(SmallMeat.SmallMeat, 1, enemyBurned.x, enemyBurned.y)
                    
        for fireball in Globals.fireballs:        
            burnEnvironment = pygame.sprite.spritecollide(fireball, Globals.environment, False)
            for theEnvironment in burnEnvironment: 
                if theEnvironment.type == Globals.environmentTree:
                    theEnvironment.kill()
                    Globals.score += 50
                    scoreboard.score = Globals.score
                    #fireball.sndKill.play()
                    fireball.kill()
                elif theEnvironment.type == Globals.environmentBoulder:
                    fireball.kill()
                
        
        if len(Globals.enemySprites) == 0:
            if Globals.currentWave > 10:
                Globals.winScreen = True
                Globals.resume = False
                Globals.clearSprites = True
                Globals.mainGame = False
                keepGoing = False
            else: 
                Globals.currentWave += 1
                dragon.reset()
                Globals.clearSprites = True
                Globals.resume = True
                Waves.spawnWave(Globals.currentWave)
            
        
        SpawnSprites.spawnGrowthBarFill(ScoreboardGUI.GrowthBarFillGUI, Globals.meat)
        fieldSprite.update()
        Globals.fireballs.update()
        Globals.environment.update()
        Globals.enemySprites.update()
        Globals.gameGUI.update()
        friendlySprites.update()
        scoreSprites.update()
        
        fieldSprite.draw(Globals.screen)
        Globals.fireballs.draw(Globals.screen)
        Globals.powerups.draw(Globals.screen)
        Globals.environment.draw(Globals.screen)
        Globals.enemySprites.draw(Globals.screen)
        friendlySprites.draw(Globals.screen)
        Globals.gameGUI.draw(Globals.screen)
        scoreSprites.draw(Globals.screen)
        Globals.powerups.update()
        
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
