# > Day 7 --------------------------------------------------------------------------------------------------------------
# > 5. Hangman Game Project (Final Step) -------------------------------------------------------------------------------
print("\n> 5. Hangman Game Project (Final Step)")

# Import Random Module, Hangman Words and Hangman Art:
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py (Checked)
# Import word_list from hangman_words:
from hangman_words import word_list

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game. (Checked)
# Import stages & logo from hangman_art:
from hangman_art import stages, logo
print(f"{logo}\n")

# Chosen Word to be guessed:
word_chosen = random.choice(word_list)

# -> Attention: Only remove this comment for testing and debugging purpose!
# print(f"The word chosen is: {word_chosen}")

# Create a Placeholder for the Chosen Word:
placeholder = ""
word_length = len(word_chosen)
for position in range(word_length):
    placeholder += "_"

lives = 6
game_over = False
correct_chars = []

while not game_over:
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"Attention! You have {lives} lives left.")

    # User Guess Input:
    user_guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if user_guess in correct_chars:
        print(f">> You've already guessed this letter: '{user_guess}'. Try another letter...")

    display = ""
    for char in word_chosen:
        if char == user_guess:
            display += char
            correct_chars.append(user_guess)
        elif char in correct_chars:
            display += char
        elif char != user_guess:
            display += "_"

    print(f"\nWord to guess: {display}")

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.
    if user_guess not in word_chosen:
        print(f">> Sorry, this letter is not in the word: '{user_guess}'. You lose a life! Try again...")
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print("\n>>>>>>>>>> You lose! <<<<<<<<<<")
            print(f"The word was: {word_chosen} ")

    if "_" not in display:
        game_over = True
        print("\n>>>>>>>>>> You win! <<<<<<<<<<")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])

# ----------------------------------------------------------------------------------------------------------------------
