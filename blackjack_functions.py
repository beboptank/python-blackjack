def start_game(player, dealer):
    player.draw_card()
    player.draw_card()
    player.print_player_cards()
    dealer.draw_card()
    dealer.draw_card()
    dealer.print_first_card()


def get_card_total(card_array):
    return sum(card_array)
