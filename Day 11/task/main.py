
# > Day 11 -------------------------------------------------------------------------------------------------------------
# > 1. Blackjack Project -----------------------------------------------------------------------------------------------

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_initial_cards(user_initial, computer_initial):
    # User get initial two cards.
    initial_two_cards = 0
    while initial_two_cards < 2:
        if len(user_initial) < 2:
            user_initial.append(random.choice(cards))
            initial_two_cards += 1
        else:
            break

    # Computer get initial card.
    if len(computer_initial) < 1:
        computer_initial.append(random.choice(cards))

def get_total_cards(player_cards):
    # User get your total cards.
    player_total = 0
    index = 0
    while index < len(player_cards):
        player_total += player_cards[index]
        index += 1
    return player_total

def get_more_cards(player):
    player.append(random.choice(cards))
    return player

def play_again():
    user_input = input('\nDo you want to play again? (Y/N): ').upper()

    if user_input == 'Y':
        blackjack_game()
    elif user_input == 'N':
        print('Thank you for playing!')
        game_loop = False

def blackjack_game():
    user_cards = []
    computer_cards = []
    user_total = 0
    computer_total = 0

    get_initial_cards(user_cards, computer_cards)
    user_total = get_total_cards(user_cards)

    game_loop = True
    while game_loop:
        print(f'Your cards: {user_cards}, current score: {user_total}')
        print(f'Computer cards: {computer_cards[0]}')

        ask_more_cards = input('Type (Y) to get another card, type (N) to pass: ').upper()
        if ask_more_cards == 'Y':
            get_more_cards(user_cards)
            user_total = get_total_cards(user_cards)

            if user_total == 21:
                print("You win!")
                play_again()
            elif user_total > 21:
                print("You went over. You lose!")
                play_again()

        elif ask_more_cards == 'N':
            while computer_total <= 16:
                get_more_cards(computer_cards)
                computer_total = get_total_cards(computer_cards)

            print(f'Your final hand: {user_cards}, final score: {user_total}')
            print(f'Computer final hand: {computer_cards}, final score: {computer_total}')

            if user_total > computer_total or computer_total > 21:
                print("You win!")
            elif user_total == computer_total:
                print("Draw!")
            else:
                print("You lose!")

            play_again()

blackjack_game()
# ----------------------------------------------------------------------------------------------------------------------
