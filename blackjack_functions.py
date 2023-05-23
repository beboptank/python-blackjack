import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game(player, dealer):
    player.add_card(cards[random.randint(0, len(cards) - 1)])
    player.add_card(cards[random.randint(0, len(cards) - 1)])
    player.print_player_cards()
    dealer.add_card(cards[random.randint(0, len(cards) - 1)])
    dealer.add_card(cards[random.randint(0, len(cards) - 1)])
    dealer.print_first_card()


def get_card_total(card_array):
    return sum(card_array)


def draw_card(player):
    player.draw_card(cards[random.randint(0, len(cards) - 1)])


def draw_card(dealer):
    dealer.draw_card(cards[random.randint(0, len(cards) - 1)])
