class HotDog:  #(本行及以下25行) 定义HotDog类
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []
    def __str__(self): # (本行及以下8行) 定义新的__str__()方法
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with "
        for i in self.condiments:
            msg = msg+i+", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + "."
        return msg
    def cook(self, time):
        self.cooked_level=self.cooked_level+time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
    def addCondiment(self, condiment):  #(本行及以下1行) 定义新的addCondiment()方法
        self.condiments.append(condiment)
myDog = HotDog()  # <---- 创建HotDog类的实例
print(myDog)  # (本行及以下13行) 测试是否一切正常
print("Cooking hot dog for 4 minutes…")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 more minutes…")
myDog.cook(3)
print(myDog)
print("What happens if I cook it for 10 more minutes?")
myDog.cook(10)
print(myDog)
print("Now, I'm going to add some stuff on my hot dog.")
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print(myDog)
# myDog = HotDog()
# print(myDog.cooked_level)
# print(myDog.cooked_string)
# print(myDog.condiments)
# # 0  cooked_level 属性（烘烤时间）
# # Raw  cooked_string属性（烘烤程度）
# # []   condiments属性（配料）
#
# print("Now I'm going to cook the hot dog")
# myDog.cook(4)  # 把热狗烘烤4分钟
# print(myDog.cooked_level)  # (本行及以下1行) 查看新的属性值
# print(myDog.cooked_string)