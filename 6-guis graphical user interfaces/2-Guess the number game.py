import random,easygui

secret = random.randint(1,100) # 选一个神秘数字
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret! It is a number from 1 to 100. I'll give you 6 tries.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?", upperbound = 100) # 得到玩家猜的数字
    if not guess: break # 本行及以下5行，最多允许猜6次
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 1 # 用掉一次机会

if guess == secret: # 本行及以下3行，游戏结束时打印消息
    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses! The number was " + str(secret))