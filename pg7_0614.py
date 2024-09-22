import pygame
import sys

pygame.init()
size = (1200,675)
screen = pygame.display.set_mode(size)
background = pygame.image.load('images/IMG_4712.jpg').convert()


mybird = pygame.image.load('images/bird1.png').convert()
position = mybird.get_rect()
position.center = (600,338)

# mybird.set_colorkey((255,255,255))
# mybird.set_alpha(200)
# print(mybird.get_at(position.center))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    screen.blit(mybird,position)

    pygame.display.flip()


