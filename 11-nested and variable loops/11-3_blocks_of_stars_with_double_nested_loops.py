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

# How many blocks of stars do you want? 5
# How many lines in each block? 5
# How many stars per line? 5
# *****
# *****
# *****
# *****
# *****
#
# *****
# *****
# *****
# *****
# *****
#
# *****
# *****
# *****
# *****
# *****
#
# *****
# *****
# *****
# *****
# *****
#
# *****
# *****
# *****
# *****
# *****
