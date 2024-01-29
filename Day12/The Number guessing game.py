#choose difficulty
# hard = 5 attempts to guess the number
# easy = 10 attempts
# check answer
# give hint: higher lower
# if guess = wrong try again

import random
play = True
won = False
my_number = 1

def choose_difficulty():
    c_diff = input("What difficulty would you like to play?\ntype 'easy' for ten tries or 'hard' for five tries:\n ").lower()
    if c_diff == "easy":
        c_difficulty = 1
    elif c_diff == "hard":
        c_difficulty = 2
    return c_difficulty

def check_answer(n1):
    global winning
    if n1 == my_number:
        winning = True
        return (print("congratulations! You won!"))
    elif n1 < my_number:
        winning = False
        return (print("higher!"))
    elif n1 > my_number:
        winning = False
        return (print("lower!"))



def guess_number():
    guess_number = int(input("Guess a number between 1 and 100:\n"))
    check_answer(guess_number)

def play_again():
    choice = input("Do you want to play again?\n")
    if choice == "yes":
        play_game()
    elif choice == "no":
        exit("Thanks for playing!")
    else:
        print("\n\n!please enter yes or no!\n\n")
        play_again()
def play_game():
    print("Hello and welcome to 'Guess the Number'!\nThis Game works as follows. The game will choose a number between 1 and 100.\nAfter that you wil choose the difficulty and try to guess the number")
    while play:
        global my_number
        my_number = random.randint(1, 100)
        difficulty = choose_difficulty()
        if difficulty == 1:
            tries = 10
        elif difficulty == 2:
            tries = 5

        for i in range(tries):
            if i == 0:
                print(f"You have {tries} tries")
            elif i == tries-1:
                print("This is your last try!")
            else:
                print(f"You have {tries-i} tries!")
            guess_number()
            if winning == True:
                play_again()
            elif winning == False and i == tries-1:
                print("You lose!")

        play_again()

play_game()