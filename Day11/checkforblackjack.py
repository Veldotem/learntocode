import calculatevalue
import BlackJack
def check_for_blackjack(list):
    if calculatevalue.calculate_value(BlackJack.user_cards) == 21 and len(list) == 2:
        print("Blackjack!")
    return