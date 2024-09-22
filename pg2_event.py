import sys

import pygame

pygame.init()

width = 600
height = 400
size = width,height
speed = [2, 1]
bg = (0, 0, 0)



# 设置窗口尺寸
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption('my First game window')

# 实例化一个字体对象
font = pygame.font.Font(None,20) # 字体类型（默认字体），字体大小
screen.fill(bg)

position=0
line_height = font.get_linesize()

while True:
    # 用户的所有操作都会放在事件队列里面成为事件消息event
    # 检测到关闭（QUIT）事件时退出程序
    for event in pygame.event.get():
        print(str(event)+'\n')
        screen.blit(font.render(str(event),True,(0,255,0)),(0,position))  # true代表消除锯齿，（0，,255，0）rgb绿色
        position += line_height

        if position > height:
            position = 0
            screen.fill(bg)

        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
# 两个surface对象，（pygame中用来表示图像的对象）
# 一个是screen
# 一个是myPlaine
# 将一个图像绘制到另一个图像上
# 50行，blit()方法，把myPlaine绘制到screen上
# python实际上将screen对应位置的颜色改成myPlaine对应的颜色，打到覆盖的效果
# 移动的原理
# surface对象的position，以及帧率
# 帧代表一副图像
# 帧率代表1秒钟可以切换多少帧
# pygame支持40-200的帧率
# position调用move()方法，根据speed修改自身的位置（x坐标，y坐标）
# 控制飞机的移动速度
# time.delay()设置延迟10毫秒
# 也可使用
# clock = pygame.time.Clock()
# clock.tick(200)