# ask the user to make a choice
# if the choice is not valid return: Invalid choice!
# let the computer make a random choice aswell
# print choices (emojis)
# determine the winner
# ask the user if they want to continue, if not terminate the game

import random

emojis = {"r": "🪨", "s": "✂", "p": "📜"}
choices = ("r", "p", "s")

def get_user_choice():
  while True:
    user_choice  = input("rock, paper, scissors? (r/p/s): ").lower()
    if user_choice in choices:
        return user_choice
    else:
       print("Invalid choice!")

def display_choices(user_choice, computer_choice):
  print(f"you chose {emojis[user_choice]}")
  print(f"computer chose {emojis[computer_choice]}")

def determine_winnter(user_choice, computer_choice):
     if user_choice == computer_choice:
        print("Tie!")
     elif (
        (user_choice == "r" and computer_choice == "s") or 
        (user_choice == "s" and computer_choice == "p") or 
        (user_choice == "p" and computer_choice == "r")):
        print("You Win!")
     else:
       print("You lose")

def play_game():
   while True:
     user_choice = get_user_choice()

     computer_choice = random.choice(choices)  

     display_choices(user_choice, computer_choice)

     determine_winnter(user_choice, computer_choice)
   
     should_continue = input("Continue? (y/n): ").lower()
     if should_continue == "n":    
       break

play_game()
