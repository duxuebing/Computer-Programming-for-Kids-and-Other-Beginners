# 测试题：
# 01.下面的循环会运行多少次？
for i in range(1, 6):
    print('Hi, Warren')
# 答：运行五次

# 02.下面的循环会运行多少次？在每次循环时，i的值是什么？
for i in range(1, 6, 2):
    print('Hi, Warren')
# 答：运行3此，每次循环i值分别是1，3，5

# 03.range(1, 8)会列出哪些数字？
# 答：1,2,3,4,5,6,7

# 04.range(8)会列出哪些数字？
# 答：0,1,2,3,4,5,6,7

# 05.range(2, 9, 2)会列出哪些数字？
# 答：2,4,6,8

# 06.range(10, 0, -2)会列出哪些数字？
# 答： 10,8,6,4,2

# 07.使用哪个关键字可以停止当前的迭代循环，提前跳到下一次循环？
# 答：continue

# 08.while循环什么时候结束？
# 当测试条件为False时，whild循环便会结束

# 动手试一试
# 01.编写一个程序，显示一张乘法表。在开始时要询问用户想显示哪个数字的乘法表，输出结果应该如下所示。
"""
Which multiplication table would you like?
5
Here is your table:
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
"""
# 答：
number = int(input("Which multiplication table would you like?"))
print("Here is your table:")
for i in range(1,11):
    print(number,"*",i,"=", number * i)

# 02.在编写第1题中的程序时，你可能使用了for循环（大多数人会这么做），现在再用while循环来编写这个程序。（如果已经使用了while循环，可以试着用for循环来编写。）
number = int(input("Which multiplication table would you like?"))
print("Here is your table:")
count = 0
while (count < 10):
    count = count + 1
    print(number, "*", count, "=", number * count)

# 参考答案：
number = int(input("Which multiplication table would you like?"))
print('Here is your table:')
i = 1
while i <= 10:
    print(number, 'times', i, '=', number * i)
    i = i + 1

# 03.向上面的乘法表程序中再加些代码，在询问用户想显示哪个数字的乘法表之后，再问问用户希望最大乘到哪个数字。输出结果应该如下所示：
"""
Which multiplication table would you like?
7
How high do you want to go?
12
Here is your table:
7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
7 × 4 = 28
7 × 5 = 35
7 × 6 = 42
7 × 7 = 49
7 × 8 = 56
7 × 9 = 63
7 × 10 = 70
7 × 11 = 77
7 × 12 = 84
"""
# 任选for循环或者while循环来完成，或者两种做法都试试看。
# 使用for循环实现
number = int(input("Which multiplication table would you like?"))
high_num = int(input("How high do you want to go?"))
print("Here is your table:")
for i in range(1,high_num+1):
    print(number,"*",i,"=", number * i)


# 使用while
number = int(input("Which multiplication table would you like?"))
high_num = int(input("How high do you want to go?"))
print("Here is your table:")
count = 0
while (count < high_num):
    count = count + 1
    print(number, "*", count, "=", number * count)



# 参考答案
number = int(input('Which multiplication table would you like?'))
limit = int(input("How high do you want to go?"))
print('Here is your table:')
for i in range(1, limit + 1):
    print(number, 'times', i, '=', number * i)







