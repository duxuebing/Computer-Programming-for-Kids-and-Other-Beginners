age = float(input("Enter your age: "))
grade = int(input("Enter your grade: "))
if age >= 8:
    if grade >= 3:
        print("You can play this game.")
    else:
        print("Sorry,you can't play the game.")
else:
    print("Sorry, you can't play the game.")


age = float(input("Enter your age: "))
grade = int(input("Enter your grade: "))
if age >= 8 and grade >= 3: # 使用and把条件结合
    print("You can play this game.")
else:
    print("Sorry, you can't play the game.")