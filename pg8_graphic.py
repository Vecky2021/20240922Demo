import pygame
import sys

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

size = width,height = 800,500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    # rect()方法，绘制矩形。参数1：绘制的对象，参数2：矩形的颜色，参数3：绘制的位置、矩形的大小，参数4：矩形的边框大小
    pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)

    # polygon()方法，绘制多边形。参数1：绘制的对象，参数2：多边形的颜色，参数3：pointlist（多边形的各个点的坐标构成的列表），参数4：边框的大小
    points = [(200,75),(300,25),(400,75),(450,25),(450,125),(400,75),(300,125)]
    pygame.draw.polygon(screen,BLACK,points,5)

    # circle()方法，绘制圆形。参数1：绘制的对象，参数2：圆形的颜色，参数3：圆心坐标，参数4：半径，参数5：边框大小
    pygame.draw.circle(screen,BLACK,(300,300),20,3)

    # ellipse()方法，绘制椭圆形，参数1：绘制的对象，参数2：颜色，参数3：通过椭圆形得到的矩形的4个坐标，参数4：边框大小
    pygame.draw.ellipse(screen,BLACK,(200,200,100,50),5)


    pygame.display.flip()

    clock.tick(10) # 设置帧率，1秒钟绘制10次