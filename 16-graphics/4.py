# 正弦曲线
import pygame,sys
import math  # 导入数学函数，包括sin()
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255, 255, 255])
for x in range(0, 640):  # 从左到右循环（X 的取值范围是0~639）
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 240)  # 计算每个点的y坐标（垂直坐标）
    pygame.draw.rect(screen, [0,0,0],[x,y,1,1])  # 使用小矩形来画点
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
