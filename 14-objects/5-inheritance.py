class GameObject:
    def __init__(self, name):
        self.name = name
    def pickUp(self, player):
        pass  # pass关键字作为占位符
        # 在此处键入代码，将对象添加到玩家的物品集合中

class Coin(GameObject):
    def __init__(self, value):
        GameObject.__init__(self, "coin")
        self.value = value
    def spend(self, buyer, seller):
        pass  # pass关键字作为占位符
        # 在此处键入代码，从卖家的钱中扣除硬币
        # 将硬币添加到卖家的钱中