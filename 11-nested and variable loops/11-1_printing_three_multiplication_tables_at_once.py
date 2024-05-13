# multiplier = 5
# for i in range(1,11):
#     print(i, "x", multiplier, "=", i * multiplier)

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# 4 x 5 = 20
# 5 x 5 = 25
# 6 x 5 = 30
# 7 x 5 = 35
# 8 x 5 = 40
# 9 x 5 = 45
# 10 x 5 = 50

# 嵌套循环打印3张乘法表
# for multiplier in range(5,8): # （本行及以下3行） 外循环分别用值5，6，7 进行3次迭代
#     for i in range(1,11): # （本行及以下1行）内循环将打印1张乘法表
#         print(i, "x", multiplier, "=", i * multiplier)
#     print()

# 1 x 5 = 5
# 2 x 5 = 10
# 3 x 5 = 15
# 4 x 5 = 20
# 5 x 5 = 25
# 6 x 5 = 30
# 7 x 5 = 35
# 8 x 5 = 40
# 9 x 5 = 45
# 10 x 5 = 50
#
# 1 x 6 = 6
# 2 x 6 = 12
# 3 x 6 = 18
# 4 x 6 = 24
# 5 x 6 = 30
# 6 x 6 = 36
# 7 x 6 = 42
# 8 x 6 = 48
# 9 x 6 = 54
# 10 x 6 = 60
#
# 1 x 7 = 7
# 2 x 7 = 14
# 3 x 7 = 21
# 4 x 7 = 28
# 5 x 7 = 35
# 6 x 7 = 42
# 7 x 7 = 49
# 8 x 7 = 56
# 9 x 7 = 63
# 10 x 7 = 70

# 可变循环打印几个 *
numStars = int(input("How many stars do you want?"))
for i in range(1, numStars):
    print('*', end='')

# How many stars do you want?5
# ****

# 可变循环达到预期数量 *
numStars = int(input("How many stars do you want? "))
for i in range(1, numStars + 1): # 让numStars 加1，这样运行程序，就会得到预期数量的星号
    print('*', end='')
# How many stars do you want? 5
# *****

# 可变循环达到预期数量 *
numStars = int(input("How many stars do you want? "))
for i in range(0, numStars):
    print('*', end='')

# How many stars do you want? 5
# *****