import sys

import pygame

# pygame.init()

width = 600
height = 400
size = width,height
speed = [2, 1]
bg = (255, 255, 255)


# 设置窗口尺寸
screen = pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption('my First game window')

# 加载主角图片
myPlaine = pygame.image.load('images/me1.png')

# 获取主角位置矩形
position = myPlaine.get_rect()

# 在循环中编写图片移动事件
while True:
    # 用户的所有操作都会放在事件队列里面成为事件消息event
    # 检测到关闭（QUIT）事件时退出程序
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)

    if position.left <0 or position.right >width:
        # 反转图像，第一个true表示水平反转为真，第二个false代表垂直反转为假
        myPlaine = pygame.transform.flip(myPlaine,True,False)

        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        myPlaine = pygame.transform.flip(myPlaine, False, True)
        speed[1] = -speed[1]

    # 填充背景
    # 可以通过rgb三元组来设置三原色的明度
    screen.fill(color='green')

    # 把飞机画到screen上面去
    screen.blit(myPlaine,position)

    # 更新界面
    # 将画面缓冲到显示器上
    # 加快绘图速度，减少闪烁情况
    pygame.display.flip()

    # 设置延迟10毫秒
    pygame.time.delay(10)

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