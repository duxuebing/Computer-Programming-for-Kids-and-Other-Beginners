# 可变嵌套循环打印星号
numLines = int(input('How many lines of stars do you want? '))
numStars = int(input('How many stars per line? '))
for line in range(0, numLines):
    for star in range(0, numStars):
        print('* ', end='')
    print()

# How many lines of stars do you want? 5
# How many stars per line? 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# 利用双重嵌套循环打印星号块
numBlocks = int(input('How many blocks of stars do you want? '))
numLines = int(input('How many lines in each block? '))
numStars = int(input('How many stars per line? '))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print('*', end='')
        print()
    print()

# How many blocks of stars do you want? 2
# How many lines in each block? 2
# How many stars per line? 2
# **
# **
#
# **
# **


# 更为复杂的星号块打印程序
numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    for line in range(1, block * 2): # (本行及以下1行) 关于行数和星号数的公式
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print()
    print()

# How many blocks of stars do you want? 3
# * * *
#
# * * * * *
# * * * * * * *
# * * * * * * * * *
#
# * * * * * * *
# * * * * * * * * *
# * * * * * * * * * * *
# * * * * * * * * * * * * *
# * * * * * * * * * * * * * * *


numBlocks = int(input('How many blocks of stars do you want? '))
for block in range(1, numBlocks + 1):
    print('block =', block) # 显示变量
    for line in range(1, block * 2):
        for star in range(1, (block + line) * 2):
            print('* ', end='')
        print(' line =', line, 'star =', star) # 显示变量
    print()

# How many blocks of stars do you want? 3
# block = 1
# * * *  line = 1 star = 3
#
# block = 2
# * * * * *  line = 1 star = 5
# * * * * * * *  line = 2 star = 7
# * * * * * * * * *  line = 3 star = 9
#
# block = 3
# * * * * * * *  line = 1 star = 7
# * * * * * * * * *  line = 2 star = 9
# * * * * * * * * * * *  line = 3 star = 11
# * * * * * * * * * * * * *  line = 4 star = 13
# * * * * * * * * * * * * * * *  line = 5 star = 15





















