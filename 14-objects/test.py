# 测试题
# 01.在定义新的对象类型时应使用什么关键字？
# class

# 02.什么是属性？

# 03.什么是方法？
# 写在类里面，可以被直接调用。

# 04.如何区别类和实例？

# 05.实例引用通常在方法中如何命名？

# 06.什么是多态？

# 07.什么是继承？

# 动手试一试
# 01.定义一个BankAccount类，它有一些属性，包括账户名（一个字符串）、账号（一个字符串或整数）和余额（一个浮点数），另外还要有一些方法来显示余额，或者执行存取款操作。
class BankAccount:
    def __init__(self, account_name, account, balance):
        self.account_name = account_name
        self.account = account
        self.balance = balance

    def show_blance(self):
        print(self.account_name, "账号", self.account,"女士/先生","您的余额是", self.balance)

Bank = BankAccount("招行","二狗子", 10000000)
print(Bank.show_blance())

# 02.编写一个可以计算利息的类，名为InterestAccount，它应当是第一题中的BankAccount类的一个子类，所以会继承BankAccount类的属性和方法。InterestAccount类还应当有一个对应利率的属性和一个可以增加利息的方法。
# 为简单起见，假设我们每年都会调用一次addInterest()方法来计算利息并更新账户余额。这是涉及收集方式的最后一章内容了，前面已经介绍了列表、函数和对象，本章将介绍模块，第16章用一个叫作Pygame的模块开始绘制一些图形。