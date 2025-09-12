
# > Day 7 --------------------------------------------------------------------------------------------------------------
# > 3. Hangman Game Project (Step 3) -----------------------------------------------------------------------------------
print("\n> 3. Hangman Game Project (Step 3)")

# Import Random Module:
import random

# Word List to be guessed:
word_list = ["aardvark", "baboon", "camel"]

# Chosen Word to be guessed:
word_chosen = random.choice(word_list)
print(f"The word chosen is: {word_chosen}")

# >> 3.1. Step 3 (TO-DO 1 & 2) -----------------------------------------------------------------------------------------
print(">> 3.1. Step 1 (TO-DO 1 & 2):")
# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.

placeholder = ""
word_length = len(word_chosen)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_chars = []

while not game_over:
    user_guess = input("Guess a letter: ").lower()

    display = ""
    for char in word_chosen:
        if char == user_guess:
            display += char
            correct_chars.append(user_guess)
        elif char in correct_chars:
            display += char
        else:
            display += "_"
    
    print(display)
    
    if "_" not in display:
        game_over = True
        print("You win!")
# ----------------------------------------------------------------------------------------------------------------------
