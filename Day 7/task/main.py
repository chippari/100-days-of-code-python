
# > Day 7 --------------------------------------------------------------------------------------------------------------
# > 1. Hangman Game Project (Step 1) -----------------------------------------------------------------------------------
print("\n> 1. Hangman Game Project (Step 1)")

# Import Random Module:
import random

# Word List to be guessed:
word_list = ["aardvark", "baboon", "camel"]

# >> 1.1. Step 1 (TO-DO 1) ---------------------------------------------------------------------------------------------
print(">> 1.1. Step 1 (TO-DO 1):")
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

word_chosen = random.choice(word_list)
print(f"The word chosen is: {word_chosen}")

# >> 1.2. Step 1 (TO-DO 2) ---------------------------------------------------------------------------------------------
print("\n>> 1.2. Step 1 (TO-DO 2):")
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

user_guess = input("Guess a letter: ").lower()

# >> 1.3. Step 1 (TO-DO 3) ---------------------------------------------------------------------------------------------
print("\n>> 1.3. Step 1 (TO-DO 3):")
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

for char in word_chosen:
    if char == user_guess:
        print("Right")
    else:
        print("Wrong")

# ----------------------------------------------------------------------------------------------------------------------
