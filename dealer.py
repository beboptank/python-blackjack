class Dealer:
    def __init__(self):
        self.cards = []

    def draw_card(self, new_card):
        self.cards.append(new_card)

    def print_first_card(self):
        print(f"Dealer's first card: {self.cards[0]}")

    def print_all_cards(self):
        print(f"Dealer's cards: {self.cards}, current score: {sum(self.cards)}")
