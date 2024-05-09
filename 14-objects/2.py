class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
    def __str__(self): # (本行及以下2行) 这里是__str__() 方法
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg
myBall = Ball("red", "small", "down")
print(myBall)