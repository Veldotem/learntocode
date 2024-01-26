import random

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
user_cards = []
dealer_cards = []



def calculate_value(List):
    value = 0
    for card in List:
        value += cards[card]
    return value

def deal_card():
    card = random.choice(choices)
    return card

def end_of_game():
    choice = input("Would you like to play again?y/n\n")
    if choice == "y":
        play_game()
    else:
        print("Thanks for playing!")
        exit()

def check_for_blackjack(list):
    if calculate_value(user_cards) == 21 and len(list) == 2:
        print("Blackjack!")
        end_of_game()
    return
def check_winner(List1, List2):
    uservalue = calculate_value(List1)
    dealervalue = calculate_value(List2)
    if uservalue > dealervalue and uservalue <= 21:
        print("You won!")
        end_of_game()
    elif uservalue == dealervalue:
        print("Draw!")
        end_of_game()
    elif uservalue < dealervalue and dealervalue >= 21:
        print("You lost")
        end_of_game()