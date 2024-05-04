import time
start = int(input('Countdown timer: How many seconds? '))
for i in range(start, 0, -1):
    print(i, end=' ')
    for star in range(i):
        print('*', end='')
        time.sleep(1)
print("BLAST OFF!")