import pygame
import sys

width = 800
height = 480
size = (width,height)
speed = [0,0]
bg = (100,100,100)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('移动飞机')
myPlane = pygame.image.load('images/me1.png')
position = myPlane.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = [-1,0]
            if event.key == pygame.K_RIGHT:
                speed = [1,0]
            if event.key == pygame.K_UP:
                speed = [0,-1]
            if event.key == pygame.K_DOWN:
                speed = [0,1]

        if event.type == pygame.KEYUP:
            speed = [0,0]

    position = position.move(speed)

    screen.fill(bg)
    screen.blit(myPlane,position)

    pygame.display.flip()