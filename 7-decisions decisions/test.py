# 测试题：
# 01.运行以下程序，你会得到什么样的输出？
# my_number = 7
# if my_number < 20:
#     print("Under 20")
# else:
#     print("20 or over")
#
# 答：输出Under 20

# 02.基于第一题中的程序，如果把my_number改为25，输出会是什么呢？
# 答：20 or over

# 03.如果要检查一个数是否大于30且不超过40，应该用哪一种if语句？
# if numbers > 30 and numbers <= 40
#     print("The number is between 30 and 40")

# 04.如果要检查用户输入的字母是大写还是小写（比如是Q还是q），应该使用哪一种if语句？
# 答：
# answer = input("请输入字母： ")
# if answer.isupper():
#     print("输入的是大写" + answer)
# elif answer.islower():
#     print("输入的是小写" + answer)
# else:
#     print("非字母" + answer)

# 参考答案：
# if answer == 'Q' or answer == 'q':
#     print("you typed a 'Q' ")


# 动手试一试
# 01.一家商店在降价促销：购买金额小于或等于10元享9折优惠，购买金额大于10元享8折优惠。编写一个程序，询问购买金额，然后显示优惠方案（9折或8折）和最终价格。
# 参考答案：
# 计算商店折扣的程序
# 小于或等于10元打九折，大于10元打8折
item_price = float(input('enter the price of the item: '))
if item_price <= 10.0:
    discount = item_price * 0.10
else:
    discount = item_price * 0.20
final_price = item_price - discount
print('You got',discount,'off, so your final price was', final_price)


# 02.一支少儿足球队在寻找年龄在10岁和12岁之间的女孩加入。编写一个程序，询问用户的年龄和性别（m表示男性，f表示女性），最后输出一条消息说明该用户是否可以加入球队。提示：要合理地编写程序，如果用户不是女孩，就不必再询问年龄。
gender = input("Enter your sex: ")
m = "男"
f = "女"
if gender == f:
    print("性别符合")
    age = int(input("Enter your age: "))
    if age in (10,11,12):
        print("年龄也符合要求")
    else:
        print("年龄不符合要求")
else:
    print("性别不符合，直接不符合")

# 参考答案：
gender = input("Are you male of female? ('m' or 'f') ")
if gender == 'f':
    age = int(input('What is your age? '))
    if age >= 10 and age <= 12:
        print('You can play on the team')
    else:
        print('You are not the right age.')
else:
    print('Only girls are allowed on this team.')

# 03.假设你正在开车长途旅行，这时刚到一个加油站，距离下一个加油站还有200千米。编写一个程序，判断是否应该在这里加油，换句话说，是否可以等到抵达下一个加油站再加油。这个程序应当询问下面几个问题。
# · 油箱有多大（单位是升）？
# · 现在油箱有多满（按百分比算，例如半满就是50%）？
# · 每升油可以走多少千米？
# 输出应该像这样：
"""
Size of tank: 60
percent full: 40
km per liter: 10
You can go another 240 km.
The next gas station is 200 km away.
You can wait for the next station.
"""
# 或者像这样
"""
Size of tank: 60
percent full: 30
km per liter: 8
You can go another 144 km.
The next gas station is 200 km away.
Get gas now!
"""
# 提示：在编写程序时要考虑留出5升的缓冲区，以防油表有误差。

# 参考答案：
tank_size = int(input('How big is your tank(liters)? '))
full = int(input('How full is your tank (eg. 50 for half full)? '))
mileage = int(input('What is your gas mileage (km per liter)? '))
range = tank_size * (full / 100) * mileage
print('You can go another', range, 'km.')
print('The next gas station is 200 km away.')
if range <= 200:
    print('Get gas now!')
else:
    print('You can wait for the next station.')

# 04.编写一个程序，用户必须输入正确的密码才能使用这个程序。你自己当然知道密码（你会将它写在代码中），不过，你的朋友要知道这个密码就必须向你求助或者直接猜密码，他也可以学习一定的Python知识，从而查看代码并找到密码。程序本身没什么特别要求，既可以是你已经编写过的程序，也可以是新编写的非常简单的程序，它必须在用户输入正确的密码时显示一条“You're in!”之类的消息。
pwd = int(input("Enter pwd: "))
pwds = 123456
if pwd == pwds:
    print("可以使用程序，You're in!")
else:
    print("不可以使用程序")

# 参考答案:
password = "bigsecret"
guess = input("Enter your password: ")
if guess == password:
    print("Password correct. Welcome")
    # 程序的其余部分代码放在这里
else:
    print("Password incorrect. Goodbye")
