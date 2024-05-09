# 多态的例子，这两个类都使用了方法名getArea()，但是在不同形状中，它的计算方法是不同的，这就是多态的一个例子。
class Triangle:  #(本行及以下7行) 这是Trigangle类（三角形）
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):  # 它们都有一个名为getArea() 的方法
        area = self.width * self.height / 2.0
        return area

class Square:  #(本行及以下6行) 这是Square类（正方形）
    def __init__(self, size):
        self.size = size

    def getArea(self):  # 它们都有一个名为getArea() 的方法
        area = self.size * self.size
        return area


# 假设又这两个类的实例
myTriangle = Triangle(4,5)
print(myTriangle.getArea())

mySquare = Square(7)
print(mySquare.getArea())