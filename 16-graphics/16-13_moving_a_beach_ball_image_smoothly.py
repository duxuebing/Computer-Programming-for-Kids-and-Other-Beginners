import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x = 50  # （本行及以下1行）增加这两行代码
y = 50
screen.blit(my_ball,[x,y])
pygame.display.flip()
for looper in range(1,200): # 开始for循环
    pygame.time.delay(20)  # 把time.delay() 的值从2000改为20
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)  # （本行及以下2行）使用x和y（而不是数字）
    x = x + 5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()