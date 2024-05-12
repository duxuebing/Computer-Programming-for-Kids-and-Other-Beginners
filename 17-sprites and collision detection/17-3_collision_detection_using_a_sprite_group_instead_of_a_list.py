import sys, pygame
from random import choice
class Ball(pygame.sprite.Sprite):  #(本行及以下13行) Ball类的定义
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
def animate(group):  #(本行及以下12行) 新的animate()函数
    screen.fill([255,255,255])
    for ball in group:
        group.remove(ball)  # <---- 从动画精灵组中删除动画精灵
        if pygame.sprite.spritecollide(ball, group, False): # <---- 检查动画精灵与动画精灵组之间的碰撞情况
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)  # <---- 将球添加到原来的动画精灵组中
        ball.move()
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)
size = width, height = 640, 480  # <---- 主程序从这里开始
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "beach_ball.png"
group = pygame.sprite.Group()  # <---- 创建动画精灵组
for row in range (0, 2):  # (本行及以下2行) 这一次只生成4个球
    for column in range (0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-2, 2]), choice([-2, 2])]
        ball = Ball(img_file, location, speed)
        group.add(ball)  # <---- 将每个球添加到动画精灵组中
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate(group)  #<---- 调用animate()函数并传入动画精灵组
pygame.quit()