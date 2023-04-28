import player
import dealer

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
    print(player_one)
    print(dealer)
    is_playing = False
