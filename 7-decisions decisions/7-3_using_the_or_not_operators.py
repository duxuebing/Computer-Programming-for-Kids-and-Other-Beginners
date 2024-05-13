# or
color = input("Enter your favorite color: ")
if color == "red" or color == "blue" or color == "green":
    print("You are allowed to play this game.")
else:
    print("Sorry, you can't play the game.")


# not
age = float(input("Enter your age: "))
if not (age < 8):
    print("You are allowed to play this game.")
else:
    print("Sorry, you can't play the game.")