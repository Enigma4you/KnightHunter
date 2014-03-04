'''
Created on Jul 31, 2010

@author: OWNER
'''
import pygame, math
pygame.init()


screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((150, 150, 150))

powerUpSmallMeat = "smallMeat"
powerUpLargeMeat = "largeMeat"
powerUpExtraLife = "extraLife"
powerUpFlameCone3 = "flameCone3"
powerUpFlameCone5 = "flameCone5"
enemySpearKnight = "spearKnight"
enemyAxeKnight = "axeKnight"
enemySwordKnight = "swordKnight"
environmentTree = "tree"
environmentBoulder = "boulder"

growthBar = pygame.sprite.Group()
gameGUI = pygame.sprite.Group(growthBar)
fireballs = pygame.sprite.Group()
enemySprites = pygame.sprite.Group()
smallMeatSprites = pygame.sprite.Group()
largeMeatSprites = pygame.sprite.Group()
extraLifeSprites = pygame.sprite.Group()
treeSprites = pygame.sprite.Group()
boulderSprites = pygame.sprite.Group()
environment = pygame.sprite.Group(treeSprites, boulderSprites)
powerups = pygame.sprite.Group(smallMeatSprites, largeMeatSprites, extraLifeSprites)

dragonCenterX = 400
dragonCenterY = 300
dragonDirection = 0
theta = dragonDirection * math.pi/180

donePlaying = False
titleScreen = True
howToPlay = False
gameOver = False
winScreen = False
mainGame = False
pauseMenu = False
creditScreen = False
resume = False
clearSprites = False
bonusLevel = False
waveDisplay = False

score = 0
lives = 3
meat = 0
growth = 1
currentWave = 1
growthBarFill = ""
enemy = ""
item = ""
obstacle = ""