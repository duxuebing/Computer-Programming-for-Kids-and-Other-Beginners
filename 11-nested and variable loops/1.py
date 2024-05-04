multiplier = 5
for i in range(1,11):
    print(i, "x", multiplier, "=", i * multiplier)

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
for multiplier in range(5,8): # （本行及以下3行） 外循环分别用值5，6，7 进行3次迭代
    for i in range(1,11): # （本行及以下1行）内循环将打印1张乘法表
        print(i, "x", multiplier, "=", i * multiplier)
    print()

# 可变循环打印几个 *
numStars = int(input("How many stars do you want?"))
for i in range(1, numStars):
    print('*', end='')

# 可变循环达到预期数量 *
numStars = int(input("How many stars do you want? "))
for i in range(1, numStars + 1): # 让numStars 加1，这样运行程序，就会得到预期数量的星号
    print('*', end='')

# 可变循环达到预期数量 *
numStars = int(input("How many stars do you want? "))
for i in range(0, numStars):
    print('*', end='')