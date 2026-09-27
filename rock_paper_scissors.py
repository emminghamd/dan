# Rock, Paper, Scissors? (r/p/s):
# play vs pc that choses randomly, the inputs are r/p/s 
# uppercase get converted to lower case
# Invalid Choice! if the input is not r/p/s
# computer choice is random
# if you win print "You win!"
# if you lose print "You lose!"
# if it's a tie print "It's a tie!"
# after each game ask: Continue? (y/n):
# if the uses inputs y the game continues, if n the game ends with "Thanks for playing!"


import random

choice = ["r", "p", "s"]
user_choice = ""
comp_choice = random.choice(choice)
while True:
    print("Rock, Paper, Scissors? (r/p/s):")
    user_choice = input()
    user_choice = user_choice.lower()
    if user_choice not in choice:
        print("Invalid choice!")
        continue
    pc_choice = random.choice(choice)


    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "r" and comp_choice == "s") or (user_choice == "s" and comp_choice == "p") or (user_choice == "p" and comp_choice == "r"):
        print("You win!")
    else:
        print("You lose!")
    while True:
        print("continue? (y/n):")
        continue_choice = input().lower()
        if continue_choice == "y":
            break
        elif continue_choice == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice!")