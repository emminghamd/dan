import random
print("instructions:")
print("to get a randomly selected name")
#here we setup the initial instructions  
names_string = input("give me names each followed by a comma:\n")
# followed by split, to make sure that if any text is followed by a comma it gets split from the rest
names = names_string.split(",")

# here we get back the amount of different names the user inputs
name_amount = len(names)

# select a random name bethween 0 and the last index (-1 is set up because we start from 0 due to machine code)
random_choice = random.randint(0, name_amount -1)

#pick out a random name from the list of names using the random_choice

chosen_person = names[random_choice]
print(f"the randomly selected person is {chosen_person}")
