import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
ploPoints = []
for x in range(0, 640):
    y = int(math.sin(x/640 * 4 * math.pi) * 200 + 200)  # 计算每个点的y坐标
    ploPoints.append([x,y])  # 将所有点添加到列表中
pygame.draw.lines(screen,[0,0,0],False,ploPoints,2) # 用draw.lines()方法画出整条曲线
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()