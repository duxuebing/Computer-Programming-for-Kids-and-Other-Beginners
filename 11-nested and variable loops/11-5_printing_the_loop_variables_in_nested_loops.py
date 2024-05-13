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