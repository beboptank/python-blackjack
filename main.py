import blackjack_functions
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
    dealer_one = dealer.Dealer()
    start_game(player_one, dealer_one)
    player_one_cards = player_one.get_cards()
    dealer_one_cards = dealer_one.get_cards()
else:
    print("Okay, maybe later!")

while is_playing:

    if get_card_total(player_one_cards) == 21:
        print("Blackjack! You win!")
        is_playing = False
        break
    elif get_card_total(player_one_cards) > 21:
        ace_index = player_one_cards.index(11)
        player_one_cards[ace_index] = 1

    if get_card_total(player_one_cards) > 21:
        print("You bust. Game over.")
        is_playing = False
        break

    draw = input("Would you like to hit (draw another card) or stay (keep your current hand)? Type 'y' or 'n' and press Enter. ")
    if draw == 'y':
        player_one.draw_card()
        player_one_cards = player_one.get_cards()
        dealer_one_cards = dealer_one.get_cards()
        player_one.print_player_cards()
        dealer_one.print_all_cards()
    else:
        print(f"Final score - {player_one.name}: {blackjack_functions.get_card_total(player_one_cards)}, Dealer: {blackjack_functions.get_card_total(dealer_one_cards)}")
        if blackjack_functions.get_card_total(player_one_cards) > blackjack_functions.get_card_total(dealer_one_cards):
            print("You win!")
        elif blackjack_functions.get_card_total(player_one_cards) == blackjack_functions.get_card_total(dealer_one_cards):
            print("Push. The dealer wins.")
        else:
            print("You lose, the dealer wins.")

    is_playing = False
