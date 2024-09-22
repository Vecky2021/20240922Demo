import pygame
import sys

# screen = pygame.display.set_mode(resolution=(0,0),flags=0,depth=0)
# 通过display模块的set_mode方法来创建一个surface对象
# 方法中有三个参数
# resolution是窗口分辨率,如果不制定参数，pygame会根据当前屏幕大小来设置窗口大小
# flags制定扩展选项
# depth用于制定颜色的位数，一般32位

width = 800
height = 480
size = (width,height)
speed = [0,0]
bg = (100,100,100)

full_screen = False

screen = pygame.display.set_mode(size,pygame.RESIZABLE)
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

            # 按下数字1键，切换全屏/非全屏
            if event.key == pygame.K_1:
                full_screen = not full_screen
                if full_screen:
                    # screen = pygame.display.set_mode((1280,800),pygame.FULLSCREEN)
                    # 可通过pygame.display.list_modes()获取当前系统支持的所有分辨率，
                    # 其中列表中的第一个元素代表当前支持的最高分辨率
                    best_size = pygame.display.list_modes()[0]
                    screen = pygame.display.set_mode(best_size,pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(size)




        if event.type == pygame.KEYUP:
            speed = [0,0]

    position = position.move(speed)

    screen.fill(bg)
    screen.blit(myPlane,position)

    pygame.display.flip()