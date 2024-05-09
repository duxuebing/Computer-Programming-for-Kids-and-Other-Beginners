import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])  # 窗口的大小，宽为640像素，高为480像素
screen.fill([255,255,255])  # 用白色背景填充窗口
# pygame.draw.circle(screen,[255,0,0],[320,240], 30, 0)  # 画一个圆

# 画一个矩形 方式一
# pygame.draw.rect(screen, [255,0,0],[250,150,300,200],0)  # （或者使用下面2行的方式写）

# 画一个矩形 方式二
# my_list = [250, 150, 300, 200]
# pygame.draw.rect(screen, [255,0,0], my_list, 0)
# 又或者使用下面2行的方式写

# 画一个矩形 方式三
my_rect = pygame.Rect(250, 150, 300, 200)
pygame.draw.rect(screen, [255,0,0], my_rect, 0)

pygame.display.flip() #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()