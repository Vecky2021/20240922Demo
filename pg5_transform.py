import pygame
import sys

width = 800
height = 500
size = width,height
screen = pygame.display.set_mode(size)
speed = [0,0]

# 原始飞机、原始位置
omyPlane = pygame.image.load('images/me1.png')
omyPlane_rect = omyPlane.get_rect()

# 变化的飞机，变化的位置
myPlane = omyPlane
position = myPlane_rect = omyPlane_rect

# 变化比率
ratio = 1.0

while True:
    # 监听关闭事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 监听键盘事件,移动
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed = [-2,0]
            if event.key == pygame.K_d:
                speed = [2,0]
            if event.key == pygame.K_w:
                speed = [0,-2]
            if event.key == pygame.K_s:
                speed = [0,2]

            # 监听放大缩小
            #放大=，缩小-，空格恢复原始尺寸
            if event.key == pygame.K_MINUS and ratio > 0.5:
                ratio = ratio - 0.1
            if event.key == pygame.K_EQUALS and ratio < 2:
                ratio = ratio + 0.1
            if event.key == pygame.K_SPACE:
                ratio = 1

            myPlane = pygame.transform.smoothscale(omyPlane,(int(omyPlane_rect.width*ratio),int(omyPlane_rect.height*ratio)))

        if event.type == pygame.KEYUP:
            speed = [0,0]

    # 改变飞机位置：
    position = position.move(speed)

    screen.fill(color=(100,100,100))

    screen.blit(myPlane,position)

    pygame.display.flip()

