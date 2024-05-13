# 条件循环 --- whild循环
print("Type 3 to continue, anything else to quit.")
someInput = input()
while someInput == '3': # 只要someInput的值为3，就一直执行循环体
    print("Thank you for the 3. Very kind of you.")
    print("Type 3 to continue, anything else to quit.")
    someInput = input()
print("That's not 3, so I'm quitting now.")