class Ball: # 这里告诉python，我们在创建一个类
    def bounce(self): # (本行及以下2行) 这是一个方法
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()  # 创建Ball类的实例
myBall.direction = "down"  # (本行及以下2行) 设置一些属性
myBall.color = "red"
myBall.size = "small"

print("I just created a ball.")  # (本行及以下3行) 打印对象的属性
print("My ball is", myBall.size)
print("My ball is", myBall.color)
print("My ball't direction is",myBall.direction)
print("Now I'm going to bounce the ball")
print()
myBall.bounce()
print("Now the ball's direction is",myBall.direction)  # 使用方法