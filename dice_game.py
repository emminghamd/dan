# need to put it all into a loop so that the user can keep rolling the dice until they want to stop
# ask: roll the dice?
# if user enters y
# generate two random numbers (2 dice rolls)
# print them
# if user enters n
# print "Thanks for playing" and exit the program
# if user enters another keyword
# print invalid choice and ask again

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
