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
        if event.type == pygame.MOUSEMOTION:
            # print(event)
            print(event.pos)
            position.center = event.pos


    screen.fill(color=bg)
    screen.blit(myPlane,position)

    pygame.display.flip()