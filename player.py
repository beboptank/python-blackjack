class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"Player {self.name}"

    def add_card(self, new_card):
        self.cards.append(new_card)
