class Dealer:
    def __init__(self):
        self.cards = []

    def add_card(self, new_card):
        self.cards.append(new_card)

    def print_first_card(self):
        print(f"Dealer's first card: {self.cards[0]}")
