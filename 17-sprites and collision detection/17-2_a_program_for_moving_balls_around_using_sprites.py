import sys,pygame
from random import choice

class Ball(pygame.sprite.Sprite):  # （本行及以下5行）定义Ball类的子类
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵
        self.image = pygame.image.load(image_file) # 在动画精灵中加载图像文件
        self.rect = self.image.get_rect() # 得到定义图像边界的矩形
        self.rect.left,self.rect.top = location # 设置球的初始位置
        self.speed = speed # 给Ball类增加speed属性
    def move(self):  # （本行及以下6行）加入这个方法来移动球
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width: # (本行及以下1行) 检查是否碰到了窗口的左边界或右边界，如果碰到了，就让球向水平方向上的另一个边界移动
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height: # （本行及以下1行） 检查是否碰到了窗口的上边界或下边界，如果碰到了，就让球向垂直方向上的另一个边界移动
            self.speed[1] = -self.speed[1]

size = width,height = 640,480 #(本行及以下2行)设置窗口大小
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "beach_ball.png"
balls = []
for row in range(0,3):  # 创建列表跟踪这些球
    for column in range(0,3):
        location = [column * 180 + 10, row * 180 + 10]  # 每次循环时都有一个不同的位置
        speed = [choice([-2,2]), choice([-2,2])]
        ball = Ball(img_file, location, speed)  # 在这个位置上创建一个球
        balls.append(ball)  # 把这些球收集到一个列表中 # 在创建Ball类的实例时把这些球加到列表中

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    screen.fill([255,255,255])  # （本行及以下5行）重绘屏幕
    for ball in balls:
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
pygame.quit()