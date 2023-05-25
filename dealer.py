import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Dealer:
    def __init__(self):
        self.cards = []

    def draw_card(self):
        self.cards.append(deck[random.randint(0, len(deck) - 1)])

    def print_first_card(self):
        print(f"Dealer's first card: {self.cards[0]}")

    def print_all_cards(self):
        print(f"Dealer's cards: {self.cards}, current score: {sum(self.cards)}")
