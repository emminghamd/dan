# generate a code that:
# accepts only numbers
# if any other value is given it returns:
# please enter a valid number
# sends back in a loop the message:
# Guess the number bethween 1 and 100;
# if the given number is too high it returns:
# Too high!
# if the number is too low it returns:
# Too low!
# if the number is right it returns:
# Congratulations! That's the number!

import random
number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! That's the number!")
            break        
    except ValueError:
        print("please enter a valid number")


# alternative way of doing it:
#import random
#guess = ""
#random_number = random.randint(1, 100)
#while guess != random_number:
#        guess = input("Guess the number between 1 and 100: ")
#        if not guess.isnumeric():
#            print("please enter a valid number")
#            continue
#        guess = int(guess)
#        if guess < 1 or guess > 100:
#            print("please enter a number between 1 and 100")
#            continue
#        if guess < random_number:
#            print("Too low!")
#        elif guess > random_number:
#            print("Too high!")
#        else:
#            print("Congratulations! That's the number!")
#            break


  
