#########################################
# File Name: doodlejump.py
# Description: This program will generate a game called doodle jump
# Author: Wesley Kim
# Date: 15/1/2018
#########################################

from math import sqrt
from random import randint

import pygame
pygame.init()

#set screen
WIDTH = 350
HEIGHT= 620
MAX = 310
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#define colours & fonts
LINE = (232,219,190)
GRID = (254,255,249)
BLACK = (  0,  0,  0)
font = pygame.font.SysFont("Arial",25)

#---import pictures---#

#doodler
doodler = pygame.image.load("doodler.png")
doodler = pygame.transform.scale(doodler,(50,50))

#platforms
greenPlatform = pygame.image.load("greenPlatform.png")
greenPlatform = pygame.transform.scale(greenPlatform,(60,15))
movingPlatform = pygame.image.load("movingPlatform.png")
movingPlatform = pygame.transform.scale(movingPlatform,(60,15))

#buttons
continueButton = pygame.image.load("continueButton.png")
continueButton = pygame.transform.scale(continueButton,(120,40))
controlsButton = pygame.image.load("controlsButton.png")
controlsButton = pygame.transform.scale(controlsButton,(120,40))
menuButton = pygame.image.load("menuButton.png")
menuButton = pygame.transform.scale(menuButton,(120,40))
playAgainButton = pygame.image.load("playAgainButton.png")
playAgainButton = pygame.transform.scale(playAgainButton,(120,40))
playButton = pygame.image.load("playButton.png")
playButton = pygame.transform.scale(playButton,(120,40))
scoreButton = pygame.image.load("scoreButton.png")
scoreButton = pygame.transform.scale(scoreButton,(50,50))

#titles
mainMenuTitle = pygame.image.load("doodleJumpTitle.png")
mainMenuTitle = pygame.transform.scale(mainMenuTitle,(330,75))
scoresTitle = pygame.image.load("doodleJumpScoresTitle.png")
scoresTitle = pygame.transform.scale(scoresTitle,(330,75))
scoresChart = pygame.image.load("scores.png")
scoresChart = pygame.transform.scale(scoresChart,(330,400))
informationTitle = pygame.image.load("doodleJumpInformationTitle.png")
informationTitle = pygame.transform.scale(informationTitle,(330,75))
info = pygame.image.load("information.png")
info = pygame.transform.scale(info,(330,400))
controlsTitle = pygame.image.load("doodleJumpControlsTitle.png")
controlsTitle = pygame.transform.scale(controlsTitle,(330,75))
controlsInfo = pygame.image.load("controls.png")
controlsInfo = pygame.transform.scale(controlsInfo,(330,330))
gameOverTitle = pygame.image.load("gameOverTitle.png")
gameOverTitle = pygame.transform.scale(gameOverTitle,(330,75))


#doodler variables
doodlerX = 150
doodlerY = 570
doodlerY2 = 620
doodlerShift = 15
doodlerH = doodler.get_height()
doodlerW = doodler.get_width()

doodlerXmenu = 35
doodlerYmenu = 410

GRAVITY = 2
doodlerSpeed = -30

#---------------------------------------#
# functions                             #
#---------------------------------------#

def grid():
    gameWindow.fill(GRID)
    for x in range(0,WIDTH,GRIDSIZE):
        pygame.draw.line(gameWindow, LINE, (x,0),(x,HEIGHT),1)
    for y in range(0,HEIGHT,GRIDSIZE):
        pygame.draw.line(gameWindow, LINE, (0,y),(WIDTH,y),1)

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def mainMenu():
    gameWindow.fill(GRID)
    for x in range(0,WIDTH,GRIDSIZE):
        pygame.draw.line(gameWindow, LINE, (x,0),(x,HEIGHT),1)
    for y in range(0,HEIGHT,GRIDSIZE):
        pygame.draw.line(gameWindow, LINE, (0,y),(WIDTH,y),1)
    gameWindow.blit(mainMenuTitle,(10,35))
    gameWindow.blit(greenPlatform,(30,460))
    gameWindow.blit(doodler,(doodlerXmenu,doodlerYmenu))
    gameWindow.blit(playButton,(175,175))
    gameWindow.blit(controlsButton,(200,300))
    gameWindow.blit(scoreButton,(250,500))
    pygame.display.update()
    pygame.time.delay(35)

def controls():
    gameWindow.blit(controlsTitle,(10,35))
    gameWindow.blit(controlsInfo,(10,120))
    gameWindow.blit(continueButton,(55/2,500))
    gameWindow.blit(menuButton,(175+55/2,500))
    pygame.display.update()

def information():
    gameWindow.blit(informationTitle,(10,35))
    gameWindow.blit(info,(10,120))
    gameWindow.blit(menuButton,(175+55/2,500))
    pygame.display.update()

def scores():
    gameWindow.blit(scoresTitle,(10,35))
    gameWindow.blit(scoresChart,(10,120))
    gameWindow.blit(menuButton,(175+55/2,500))
    pygame.display.update()

def drawMessages():
    scoreGraphics = font.render(str(score),1,BLACK)
    gameWindow.blit(scoreGraphics,(10,10))
    
def game():
    drawMessages()
    gameWindow.blit(doodler,(doodlerX,doodlerY))
    pygame.display.update()
    pygame.time.delay(35)

def gameOver():
    gameWindow.blit(gameOverTitle,(10,35))
    gameWindow.blit(playAgainButton,(55/2,400))
    gameWindow.blit(menuButton,(175+55/2,400))
    scoreGraphics = font.render("your score:",1,BLACK)
    finalScore = font.render(str(score),1,BLACK)
    gameWindow.blit(scoreGraphics,(80,200))
    gameWindow.blit(finalScore,(200,200))
    pygame.display.update()

#---------------------------------------#
#   the main program begins here        #
#---------------------------------------#

#declare variables
numPlatform = 10
score = 0
GRIDSIZE = 10

platformSpeed = 10

platformX = []
platformY = []
platformVisible = []
platformType = []

screen = 1

#platform colours
greenPlatformW = greenPlatform.get_width()
greenPlatformH = greenPlatform.get_height()
greenPlatformC = greenPlatform.get_at((greenPlatformW/2,greenPlatformH/3))

#generate platforms
for i in range(numPlatform):
    
    #platform location
    if i == 0:
        platformX.append(100)    #######
        platformY.append((HEIGHT - 55))        
    else:
        platformX.append(randint(0,WIDTH - 60))
        platformY.append((platformY[i-1] - 61))    ########
    platformVisible.append(True)

    #platform type
    if platformVisible[i]:
        platformVar = randint(1,100)
        if 1 <= platformVar <= 30:
            platformType.append(1) #movingPlatform
        elif 31 <= platformVar <= 100:
            platformType.append(4) #greenPlatform

#game loop
inPlay = True
while inPlay:
    grid()
    
    #main menu
    if screen == 1:
        mainMenu()

        #jumping
        if doodlerYmenu + 50 == 460:
            doodlerSpeed = -25
        doodlerSpeed = doodlerSpeed + GRAVITY
        doodlerYmenu = doodlerYmenu + doodlerSpeed
        if doodlerYmenu + 50 > 460:
            doodlerYmenu = 460 - 50
            doodlerSpeed = 0

        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and (175<=mouseX<=295 and 175<=mouseY<=215):
                screen = 2

                #reset variables
                doodlerX = 150
                doodlerY = 570
                doodlerY2 = 620
                doodlerShift = 15
                doodlerH = doodler.get_height()
                doodlerW = doodler.get_width()

                GRAVITY = 2
                doodlerSpeed = -30

                score = 0
                
            elif event.type == pygame.MOUSEBUTTONDOWN and (200<=mouseX<=320 and 300<=mouseY<=340):
                screen = 3
            elif event.type == pygame.MOUSEBUTTONDOWN and (250<=mouseX<=300 and 500<=mouseY<=550):
                screen = 5

    #game
    elif screen == 2:

        #platforms
        for i in range (numPlatform):
            if platformType[i] == 1:
                gameWindow.blit(movingPlatform,(platformX[i],platformY[i]))
                platformX[i] = platformX[i] + platformSpeed
                if platformX[i] > 290 or platformX[i] < 0:
                    platformSpeed = -platformSpeed
            elif platformType[i] == 4:
                gameWindow.blit(greenPlatform,(platformX[i],platformY[i]))

        #game screen
        game()
        
        #keys
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            doodlerX -= doodlerShift
            if doodlerX < -50:
                doodlerX = 350
        if keys[pygame.K_RIGHT]:
            doodlerX += doodlerShift
            if doodlerX >350:
                doodlerX = -50         

        #jump
        if doodlerY + 50 == doodlerY2:
            doodlerSpeed = -25
        
        doodlerSpeed = doodlerSpeed + GRAVITY
        doodlerY = doodlerY + doodlerSpeed

        if doodlerY + 50 > doodlerY2:
            doodlerY = doodlerY2 - 50
            doodlerSpeed = 0
            
        for i in range (len(platformX)):
            if (platformX[i] <= doodlerX <= platformX[i] + greenPlatformW or \
               platformX[i] <= doodlerX + doodlerW <= platformX[i] + greenPlatformW) and \
               platformY[i] <= doodlerY + doodlerH-5 <= platformY[i] + greenPlatformH and \
               doodlerSpeed >= 0:
                
                doodlerY2 = platformY[i]

                #jump
                if doodlerY + 50 == doodlerY2:
                    doodlerSpeed = -25
                
                doodlerSpeed = doodlerSpeed + GRAVITY
                doodlerY = doodlerY + doodlerSpeed

                if doodlerY + 50 > doodlerY2:
                    doodlerY = doodlerY2 - 50
                    doodlerSpeed = 0

            elif ((doodlerX < platformX[i] or doodlerX > platformX[i] + greenPlatformW) or \
                  (doodlerX + doodlerW < platformX[i] or doodlerX > platformX[i] + greenPlatformW)) and \
                  platformY[i] <= doodlerY + doodlerH-5 <= platformY[i] + greenPlatformH and \
                  doodlerSpeed >= 0 and score > 0:
                
                doodlerY2 = 1000
        
        if doodlerY <= 310 and doodlerSpeed < 0:
            doodlerY = 310
            for i in range (len(platformX)):
                platformY[i] = platformY[i] - doodlerSpeed
                score = score + ((platformY[1] - doodlerSpeed)/10)
                score = int(round(score,1))
            if doodlerSpeed > 0:
                doodlerY = doodlerY + doodlerSpeed

        for i in range (numPlatform):
            if platformY[i] > 620:

                #generate platforms
                platformX[i] = randint(0,WIDTH - 60)
                platformY[i] = 16
                platformVisible.append(True)
                if platformVisible[i]:
                    platformVar = randint(1,100)
                    if 1 <= platformVar <= 30:
                        platformType.append(1) #movingPlatform
                    elif 31 <= platformVar <= 100:
                        platformType.append(4) #greenPlatform

        #game over
        if doodlerY > HEIGHT:
            screen = 6
        
    #controls
    elif screen == 3:
        controls()

        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and (55/2<=mouseX<=55/2+120 and 500<=mouseY<=540):
                screen = 4
            elif event.type == pygame.MOUSEBUTTONDOWN and (175+55/2<=mouseX<=175+55/2+120 and 500<=mouseY<=540):
                screen = 1

    #information
    elif screen == 4:
        information()

        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN and (175+55/2<=mouseX<=175+55/2+120 and 500<=mouseY<=540):
                screen = 1
                
    #scores
    elif screen == 5:
        scores()

        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN and (175+55/2<=mouseX<=175+55/2+120 and 500<=mouseY<=540):
                screen = 1

    #game over
    elif screen== 6:
        gameOver()
        
        #screen selection
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                (mouseX,mouseY) = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONDOWN and (175+55/2<=mouseX<=175+55/2+120 and 400<=mouseY<=440):
                screen = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and (55/2<=mouseX<=55/2+120 and 400<=mouseY<=440):
                screen = 2
                        
                #reset variables
                doodlerX = 150
                doodlerY = 570
                doodlerY2 = 620
                doodlerShift = 15
                doodlerH = doodler.get_height()
                doodlerW = doodler.get_width()

                GRAVITY = 2
                doodlerSpeed = -30

                score = 0

    #exit
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        
#---------------------------------------#
pygame.quit()
