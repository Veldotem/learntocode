import random

play = True
cards ={
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11
}

choices = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
r_choice = 0
add = 0
keep_playing = True

def over21(list):
    add = 0
    for element in list:
        add += cards[element]
    if add > 21:
        print("\n\nYour total is over 21, you lost\n\n")
        end_game()
    return


def check_winner(dealer_list, user_list):
    s_dealer = 0
    s_user = 0
    for card in dealer_list:
        s_dealer += cards[card]
    print(f"The Dealer has {s_dealer}!\n")
    for car in user_list:
        s_user += cards[car]
    print(f"You have {s_user}!\n")
    if s_dealer > s_user:
        print("\n\nThe Dealer Won!\n\n")
        end_game()
    elif s_dealer == s_user:
        print("\n\nIt is a draw!\n\n")
        end_game()
    elif s_dealer < s_user:
        print("\n\nYou have won!\n\n")
        end_game()

def end_game():
    p_again = "yes"
    p_again = input("\n\nDo You Want To play again?\n")
    if p_again.lower() == "yes":
        play_blackjack()
    if p_again.lower() == "no":
        exit("Thank you for playing")

def play_blackjack():
    user_cards = []
    dealer_cards = []
    choice = input("Welcome to Blackjack. Do you want to play?y/n\n")
    if choice == "y":
        print("\nDealing Cards!\n")
        user_cards.append(random.choice(choices))
        user_cards.append(random.choice(choices))
        dealer_cards.append(random.choice(choices))
        dealer_cards.append(random.choice(choices))
        print(f"\nThe Dealer's cards are:\n\n{dealer_cards[0]} plus a secret one")
        print(f"\nYour cards are:\n\n{user_cards}\n")
        new_card = input("do you want an additional card?y/n\n")
        while new_card == "y":
            user_cards.append(random.choice(choices))
            print(f"The Dealers Cards are:\n\n{dealer_cards[0]} plus a secret one.\nYour cards are:\n\n{user_cards}\n")
            over21(user_cards)
            new_card = input("do you want an additional card?y/n\n")
    check_winner(dealer_cards, user_cards)


play_blackjack()