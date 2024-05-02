for looper in [1,2,3,4,5]:
    print("hello")

# hello
# hello
# hello
# hello
# hello

for looper in [1,2,3,4,5]:
    print(looper)

# 1
# 2
# 3
# 4
# 5

for looper in [1,2,3,4,5]:
    print(looper, "items 8 =", looper * 8)

# 1 items 8 = 8
# 2 items 8 = 16
# 3 items 8 = 24
# 4 items 8 = 32
# 5 items 8 = 40

for looper in range(1,5):
    print(looper, "items 8 =",looper * 8)

# 1 items 8 = 8
# 2 items 8 = 16
# 3 items 8 = 24
# 4 items 8 = 32

for looper in range(1,11):
    print(looper, "times 8 =", looper * 8)

# 1 times 8 = 8
# 2 times 8 = 16
# 3 times 8 = 24
# 4 times 8 = 32
# 5 times 8 = 40
# 6 times 8 = 48
# 7 times 8 = 56
# 8 times 8 = 64
# 9 times 8 = 72
# 10 times 8 = 80

for i in range(1, 10, 2):
    print(i)
# 1
# 3
# 5
# 7
# 9

for i in range(5, 26, 5):
    print(i)
# 5
# 10
# 15
# 20
# 25

for i in range(10, 1, -1):
    print(i)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2

import time
for i in range(10, 0, -1): # 反向倒计时
    print(i)
    time.sleep(1) # 等待1秒
print("BLAST OFF!")

for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
    print(cool_guy, "is the coolest guy ever!")

# Spongebob is the coolest guy ever!
# Spiderman is the coolest guy ever!
# Justin Timberlake is the coolest guy ever!
# My Dad is the coolest guy ever!

# 条件循环 --- whild循环
print("Type 3 to continue, anything else to quit.")
someInput = input()
while someInput == '3': # 只要someInput的值为3，就一直执行循环体
    print("Thank you for the 3. Very kind of you.")
    print("Type 3 to continue, anything else to quit.")
    someInput = input()
print("That's not 3, so I'm quitting now.")

# 提前跳转 ---- continue 语句
for i in range(1,6):
    print()
    print('i =', i, ' ', end='')
    print('Hello, how ', end='')
    if i == 3:
        continue
    print('are you to day?', end='')
print()

# i = 1  Hello, how are you to day?
# i = 2  Hello, how are you to day?
# i = 3  Hello, how
# i = 4  Hello, how are you to day?
# i = 5  Hello, how are you to day?

# 跳出循环 --- break语句
for i in range(1,6):
    print()
    print('i =', i, ' ', end='')
    print('Hello, how ', end='')
    if i == 3:
        break
    print('are you to day?', end='')
print()

# i = 1  Hello, how are you to day?
# i = 2  Hello, how are you to day?
# i = 3  Hello, how










