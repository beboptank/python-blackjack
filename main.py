import player
import dealer
from blackjack_functions import start_game
from blackjack_functions import get_card_total

# Blackjack / 21 Rules:
# - Played using cards
# - Don't go over 21 (a bust)
# - Cards 2 to 10 count as face value
# - Cards J, Q, and K count as 10
# - An Ace counts as 1 or 11
# - If your score and the dealer's score are the same, you draw
# - If the dealer ends up with a hand that is smaller than 17, they must draw

is_playing = False

player_input = input("Would you like to play a game of blackjack? Type 'y' or 'n' and press Enter: ")

if player_input == 'y':
    is_playing = True
    player_name = input("Please enter your name and press Enter: ")
    player_one = player.Player(player_name)
    dealer = dealer.Dealer()

while is_playing:
    start_game(player_one, dealer)
    player_one_cards = player_one.get_cards()

    if get_card_total(player_one_cards) == 21:
        print("Blackjack! You win!")
    elif get_card_total(player_one_cards) > 21:
        ace_index = player_one_cards.index(11)
        player_one_cards[ace_index] = 1
    is_playing = False
