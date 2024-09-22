import pygame
import sys

pygame.init()

width = 800
height = 500
size = width,height
screen = pygame.display.set_mode(size)
bg = (200,120,180)

pygame.mixer.music.load('music/bgm.ogg')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

boom_sound = pygame.mixer.Sound('music/boom.wav')
bullet_sound = pygame.mixer.Sound('music/bullet.wav')

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                boom_sound.play()
            if event.button == 3:
                bullet_sound.play()

    screen.fill(bg)

    pygame.display.flip()
    clock.tick(10)