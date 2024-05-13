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