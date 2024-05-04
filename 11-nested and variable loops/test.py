# 测试题
# 01.如何在Python中创建可变循环？
# 答： 循环的参数使用变量
# 参考答案：
# for i in range(numberOfLoops)
# for i in range(1, some Number)

# 02.如何在Python中创建嵌套循环？
# 答：使用2个及以上的for循环
# 参考答案：
for i in range(5):
    for j in range(8):
        print("hi", end=" ")
    print()

# 03.键入并运行下面的代码，总共会打印出多少个星号？
for i in range(5):
    for j in range(3):
        print('* ', end='')
    print()
# 答： 打印15个星号

# 04.运行第3题中的代码，会得到什么样的输出结果？
# 答:
# * * *
# * * *
# * * *
# * * *
# * * *

# 05.如果一棵决策树有4层，每层有两个选择，那么一共有多少种选择（决策树有多少条路径）？
# 参考答案： 对4层决策树来说，一共会有2的4次方种选择，也就是16种选择，或者说决策树有16条可选路径。

# 动手试一试
# 01.还记得在第8章中编写的倒计时定时器程序吗？下面的代码可以帮助你回想起来：
import time
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!")
# 请用一个可变循环来修改这个程序，询问用户从哪个数开始倒计时，举例如下。
# 答：
import time
number = int(input('Countdown timer: How many seconds? '))
for i in range(number, 0, -1):
    print(i)
    time.sleep(1)
print("BLAST OFF!")
# Countdown timer: How many seconds? 4
# 4
# 3
# 2
# 1
# BLAST OFF!

# 02.修改第1题中的程序，除了打印每个数字，还要打印出一行星号，如下所示。
import time
number = int(input('Countdown timer: How many seconds? '))
for i in range(number, 0, -1):
    for star in range(0, i):
        print('* ', end='')
    print(i)
print("BLAST OFF!")
# Countdown timer: How many seconds? 4
# 4 * * * *
# 3 * * *
# 2 * *
# 1 *
# BLAST OFF!
# （提示：可以用嵌套循环来实现，也可以尝试其他方式。）

# 参考答案
import time
start = int(input('Countdown timer: How many seconds? '))
for i in range(start, 0, -1):
    print(i, end=' ')
    for star in range(i):
        print('*', end='')
        time.sleep(1)
print("BLAST OFF!")

import time
start = int(input('Countdown timer: How many seconds? '))
for i in range(start, 0, -1):
    print(i, '*' * i)
    time.sleep(1)
print("BLAST OFF!")