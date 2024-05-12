import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
x_speed = 10 # 这是speed变量
y_speed = 10 # 加入y_speed相关代码（垂直运动）
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255],[x,y,90,90],0) # （本行及以下5行）把显示沙滩的代码放在这里，也就是whild循环内部
    x = x + x_speed  # 这里是speed变量
    y = y + y_speed  # 加入y_speed 的相关代码（垂直运动）
    if x > screen.get_width() - 90 or x < 0: # 判断沙球是否碰到窗口的任意边界
        x_speed = - x_speed
    if y > screen.get_height() - 90 or y < 0: # (本行及以下1行)让沙滩球在窗口的上边界和下边界之间反弹
        y_speed = - y_speed
    screen.blit(my_ball, [x,y])
    pygame.display.flip()
pygame.quit()