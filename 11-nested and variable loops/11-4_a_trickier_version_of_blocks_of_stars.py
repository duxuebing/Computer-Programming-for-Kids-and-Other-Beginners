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