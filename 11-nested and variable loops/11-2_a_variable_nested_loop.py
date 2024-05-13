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