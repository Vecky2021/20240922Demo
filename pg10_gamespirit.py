import pygame
import sys
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite): # 定义一个Ball类，继承自pygame.sprite.Sprite类
    def __init__(self,image,position,speed,bg_size): # 定义Ball类的构造函数，参数包括（本类对象，图片，位置，移动速度）
        pygame.sprite.Sprite.__init__(self)  # 调用父类Sprite类的构造函数

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0], bg_size[1]

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.right <0:
            self.rect.left = self.width

        elif self.rect.left > self.width:
            self.rect.right = 0

        elif self.rect.top <0:
            self.rect.bottom = self.height

        elif self.rect.bottom > self.height:
            self.rect.top = 0

def main():
    pygame.init()

    ball_image = 'images2/golden.png'

    bg_image = 'images2/background.png'
    bg_size = width,height = 1370,706

    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('ball_game')

    background = pygame.image.load(bg_image).convert_alpha()

    balls = []

    for i in range(5):
        position = randint(0,width-120),randint(0,height-120)
        speed = [randint(-10,10), randint(-10,10)]
        ball = Ball(ball_image,position,speed,bg_size)

        balls.append(ball)

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.blit(background,(0,0))

        for each in balls:
            each.move()
            screen.blit(each.image,each.rect)


        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()




