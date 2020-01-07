import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

RED = (255, 0, 0)
scrollbgimg = pygame.image.load('background.png')
catImg = pygame.image.load('cat.png')
weaponImg = pygame.image.load('weapon.png')
catx = 0
caty = 50
weaponx = 0
weapony = 0
scrollbgx = 0
weaponFlag = False
direction = ''

while True: # the main game loop
    DISPLAYSURF.fill(RED)

    if direction == 'right' and catx < 750:
        catx += 5       
    elif direction == 'down' and caty < 550:
        caty += 5        
    elif direction == 'left' and catx > 0:
        catx -= 5        
    elif direction == 'up' and caty > 0:
        caty -= 5

   
    #배경 스크롤 이미지 출력
    if scrollbgx > -1200:
        scrollbgx -= 1
    else:
        scrollbgx = 0
    DISPLAYSURF.blit(scrollbgimg, (scrollbgx, 0)) 

    #고양이 이미지 출력
    DISPLAYSURF.blit(catImg, (catx, caty)) 

    #무기 이미지 출력
    if weaponFlag == True:
        weaponx += 5;
        DISPLAYSURF.blit(weaponImg, (weaponx+50, weapony))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'up'
            if event.key == pygame.K_DOWN:
                direction = 'down'
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            if event.key == pygame.K_SPACE:
                weaponFlag = True;
                weaponx = catx;
                weapony = caty;
                

    pygame.display.update()
    fpsClock.tick(FPS)
