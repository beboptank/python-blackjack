import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game(player, dealer):
    player.add_card(cards[random.randint(0, len(cards) - 1)])
    player.add_card(cards[random.randint(0, len(cards) - 1)])
    player.print_player_cards()
