import random
secret = random.randint(1,100)
guess = 0 # 选一个神秘数字
tries = 0
print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 100. I'll give you 6 tries.")

while guess != secret and tries < 6:
    guess = int(input("What's yer guess? ")) # 得到玩家猜的数字（本行及以下4行）最多允许猜6次
    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")
    tries = tries + 1 

if guess == secret: # 用掉一次机会（本行及以下4行）当游戏结束时打印消息
    print("AVAST! Ye got it! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was", secret)