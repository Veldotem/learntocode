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

def calculate_value(List)
    value = 0
    for card in List:
        value += cards[card]
    return value

def check_for_blackjack(list):
    if calculate_value(user_cards) == 21 and len(list) == 2:
        print("Blackjack!")
        end_game()
    return