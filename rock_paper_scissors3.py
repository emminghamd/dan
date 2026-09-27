# ask the user to make a choice
# if the choice is not valid return: Invalid choice!
# let the computer make a random choice aswell
# print choices (emojis)
# determine the winner
# ask the user if they want to continue, if not terminate the game

import random

ROCK = "r"
SCISSORS = "s"
PAPER = "p"
emojis = {ROCK: "🪨", SCISSORS: "✂", PAPER: "📜"}
choices = tuple(emojis.keys())

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
        (user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == SCISSORS and computer_choice == PAPER) or 
        (user_choice == PAPER and computer_choice == ROCK)):
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
