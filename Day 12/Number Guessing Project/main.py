
# > Day 12 -------------------------------------------------------------------------------------------------------------
# > 5. Number Guessing Project -----------------------------------------------------------------------------------------
print("\n> 5. Number Guessing Project")

import random

def play_again():
    again = input("Do you want to play again? (y/n): ").lower()

    if again == "y":
        return number_guessing_game()
    else:
        return "Thank you for playing!"

def number_guessing_game():
    attempts = 0
    number_chosen = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(number_chosen)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == number_chosen:
            print(f"You got it! The answer was {number_chosen}.")
            attempts = 0
        elif guess < number_chosen:
            print(f"Your guess is too low.")
        else:
            print(f"Your guess is too high.")

        attempts -= 1

        if attempts == 0:
            print("\nYou lose!")

    play_again()


number_guessing_game()

# ----------------------------------------------------------------------------------------------------------------------
