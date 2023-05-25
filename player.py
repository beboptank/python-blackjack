import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"Player {self.name}"

    def draw_card(self):
        self.cards.append(deck[random.randint(0, len(deck) - 1)])

    def print_player_cards(self):
        print(f"{self.name}'s cards: {self.cards}, current score: {sum(self.cards)}")

    def get_cards(self):
        return self.cards
