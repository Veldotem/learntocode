import random
from GameData import data
from Art import logo


current_value: ""
new_value: ""
max_id = len(data)
play = True

def game_end():
    new_game = input("do you want to play again? (y/n)")
    if new_game == "y":
        play_game()
    else:
        exit("thanks for playing")


def play_game():
    global current_value
    global new_value
    print(logo)
    current_value = random.choice(data)
    while play:
        new_value = random.choice(data)
        while new_value == current_value:
            new_value = random.choice(data)
        cur_fol = current_value.get('follower_count')
        new_fol = new_value.get('follower_count')
        choice = int(input(f"Who has more followers?\n\n1:{current_value.get('name')}, a {current_value.get('description')}from {current_value.get('country')}\nor\n2:{new_value.get('name')}, a {new_value.get('description')} from {new_value.get('country')}?\n"))
        if choice == 1:
            if cur_fol > new_fol:
                print("You guessed correctly")
            elif cur_fol < new_fol:
                print("You guessed wrong")
                game_end()
        elif choice == 2:
            if cur_fol > new_fol:
                print("You guessed wrong")
                game_end()
            elif cur_fol < new_fol:
                print("You guessed correctly")
                current_value = new_value


play_game()