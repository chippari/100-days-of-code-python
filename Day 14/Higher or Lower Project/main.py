
# > Day 14 -------------------------------------------------------------------------------------------------------------
# > 1. Higher or Lower Project -----------------------------------------------------------------------------------------

import random
from art import logo, vs
from game_data import data

def play_again():
    again = input("\nDo you want to play again? (Y/N): ").upper()

    if again == 'Y':
        return higher_or_lower_game()
    else:
        return print("Thank you for playing. See you later!")

def higher_or_lower_game():
    user_score = 0
    data_a = random.choice(data)
    data_b = random.choice(data)

    game_loop = True
    while game_loop:
        print(f"\nCurrent Score: {user_score}")
        print(logo)
        print(f"Compare A: {data_a['name']}, a {data_a['description']}, from {data_a['country']}.")
        print(vs)
        print(f"Against B: {data_b['name']}, a {data_b['description']}, from {data_b['country']}.")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A':
            if data_a['follower_count'] > data_b['follower_count']:
                print(f"You're right!")
                user_score += 1
                data_a = data_b
                data_b = random.choice(data)
            else:
                print(f"Sorry, that's wrong. Final Score: {user_score}")
                game_loop = False
        elif user_choice == 'B':
            if data_b['follower_count'] > data_a['follower_count']:
                print(f"You're right!")
                user_score += 1
                data_a = data_b
                data_b = random.choice(data)
            else:
                print(f"Sorry, that's wrong. Final Score: {user_score}")
                game_loop = False

    play_again()

higher_or_lower_game()

# ----------------------------------------------------------------------------------------------------------------------
