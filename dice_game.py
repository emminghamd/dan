import random

while True:
    command = input("Roll the dice? (y/n)").lower()
    if command == "y":
        Dice1 = random.randint(1, 6)
        Dice2 = random.randint(1, 6)
        print(f"{Dice1}, {Dice2}")
    elif command == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid Choice!")
