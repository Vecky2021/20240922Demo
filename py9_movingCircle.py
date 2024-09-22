import pygame
import sys

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

size = width,height = 800,500
screen = pygame.display.set_mode(size)

position = size[0]//2,size[1]//2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            print("anle")
            position = event.pos

    pygame.draw.circle(screen,RED,position,10,5)
    pygame.draw.circle(screen,GREEN,position,15,5)
    pygame.draw.circle(screen,BLUE,position,20,5)

    screen.fill(WHITE)
    pygame.display.flip()

    clock.tick(10)