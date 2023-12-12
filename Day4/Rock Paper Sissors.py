#import Modules
import random

#define variables/Lists
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

#code


#User Choice
user_choice = input("Please enter what you want to choose:\n")
print("\n\n")

random_int = random.randint(0,2)
opp_choice = choice[random_int]


if user_choice.casefold() == "rock":
    print(f"User chose Rock:\n\n{rock}")
    if random_int == 0:
        print(f"Opponent chose Rock:\n\n{rock}")
        print("\nIt is a draw!\n")

    elif random_int == 1:
        print(f"Opponent chose paper:\n\n{paper}")
        print("\nYou lost!\n")

    elif random_int == 2:
        print(f"Opponent chose scissors:\n\n{scissors}")
        print("\nYou win!\n")

elif user_choice.casefold() == "paper":
    print(f"User chose paper:\n\n{paper}")
    if random_int == 0:
        print(f"Opponent chose Rock:\n\n{rock}")
        print("\nYou win!\n")

    elif random_int == 1:
        print(f"Opponent chose paper:\n\n{paper}")
        print("\nIt is a draw!\n")

    elif random_int == 2:
        print(f"Opponent chose scissors:\n\n{scissors}")
        print("\nYou lost!\n")

elif user_choice.casefold() == "scissors":
    print(f"User chose sissors:\n\n{scissors}")
    if random_int == 0:
        print(f"Opponent chose Rock:\n\n{rock}")
        print("\nYou lost!\n")

    elif random_int == 1:
        print(f"Opponent chose paper:\n\n{paper}")
        print("\nYou win!\n")

    elif random_int == 2:
        print(f"Opponent chose scissors:\n\n{scissors}")
        print("\nIt is a draw!\n")
