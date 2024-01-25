def play_blackjack():
    user_cards = []
    dealer_cards = []
    while play:
        choice = input("Welcome to Blackjack. Do you want to play?y/n")
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
