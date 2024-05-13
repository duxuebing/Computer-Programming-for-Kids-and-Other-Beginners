age = float(input("Enter your age: "))
grade = int(input("Enter your grade: "))
if age >= 8:
    if grade >= 3:
        print("You can play this game.")
    else:
        print("Sorry,you can't play the game.")
else:
    print("Sorry, you can't play the game.")

# Enter your age: 9
# Enter your grade: 3
# You can play this game.

age = float(input("Enter your age: "))
grade = int(input("Enter your grade: "))
if age >= 8 and grade >= 3: # 使用and把条件结合
    print("You can play this game.")
else:
    print("Sorry, you can't play the game.")

# Enter your age: 8
# Enter your grade: 2
# Sorry, you can't play the game.