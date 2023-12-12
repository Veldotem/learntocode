import random
import target
import Words

backup = []
game_won = False
lives = 6

chosen_word = random.choice(Words.word_list)

print(chosen_word)

for letter in chosen_word:
    backup.append('_')

while not game_won and lives > 0:
    print(target.logo + "\n")
    print(target.stages[lives])
    print(f"You have {lives} tries left")
    display = "".join(backup)
    print(display)
    guess = input("Guess a letter:\n").lower()
    if guess not in backup:
        lives -= 1

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            backup[i] = guess

    if "_" not in display:
        game_won = True
        print("You Win!")
    elif lives == 0:
        print("You Lose!")
