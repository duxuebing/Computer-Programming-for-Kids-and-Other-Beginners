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


class Ball:
    def __init__(self, color, size, direction):  # （本行及以下3行）这里是 __init__() 方法的定义。init 前后各又2条下划线，共有4条下划线
        self.color = color
        self.size = size
        self.direction = direction
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
myBall = Ball("red", "small", "down")  # 属性为 __init__() 方法的参数传入
print("I just created a ball.")  # (本行及以下3行) 打印对象的属性
print("My ball is", myBall.size)
print("My ball is", myBall.color)
print("My ball't direction is",myBall.direction)
print("Now I'm going to bounce the ball")
print()
myBall.bounce()
print("Now the ball's direction is",myBall.direction)  # 使用方法
# print(myBall)





