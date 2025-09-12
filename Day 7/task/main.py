
# > Day 7 --------------------------------------------------------------------------------------------------------------
# > 2. Hangman Game Project (Step 2) -----------------------------------------------------------------------------------
print("\n> 2. Hangman Game Project (Step 2)")

# Import Random Module:
import random

# Word List to be guessed:
word_list = ["aardvark", "baboon", "camel"]

# Chosen Word to be guessed:
word_chosen = random.choice(word_list)
print(f"The word chosen is: {word_chosen}")

# >> 2.1. Step 2 (TO-DO 1) ---------------------------------------------------------------------------------------------
print(">> 2.1. Step 1 (TO-DO 1):")
# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
word_length = len(word_chosen)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

user_guess = input("Guess a letter: ").lower()

# >> 2.2. Step 2 (TO-DO 2) ---------------------------------------------------------------------------------------------
print("\n>> 2.2. Step 1 (TO-DO 2):")
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""
for char in word_chosen:
    if char == user_guess:
        display += char
    else:
        display += "_"

print(display)
# ----------------------------------------------------------------------------------------------------------------------
