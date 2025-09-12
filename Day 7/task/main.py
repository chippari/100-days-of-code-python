# > Day 7 --------------------------------------------------------------------------------------------------------------
# > 4. Hangman Game Project (Step 4) -----------------------------------------------------------------------------------
print("\n> 4. Hangman Game Project (Step 4)")

# Import Random Module:
import random

# Set Body Stages:
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Word List to be guessed:
word_list = ["aardvark", "baboon", "camel"]

# Chosen Word to be guessed:
word_chosen = random.choice(word_list)
print(f"The word chosen is: {word_chosen}")

# Create a Placeholder for the Chosen Word:
placeholder = ""
word_length = len(word_chosen)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

# >> 4.1. Step 4 (TO-DO 1, 2 & 3) --------------------------------------------------------------------------------------
print(">> 4.1. Step 4 (TO-DO 1, 2 & 3):")
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

lives = 6
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

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if user_guess not in word_chosen:
        lives -= 1

        if lives == 0:
            game_over = True
            print("\n********** You lose! **********")

    if "_" not in display:
        game_over = True
        print("\n********** You win! **********")

    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

# ----------------------------------------------------------------------------------------------------------------------
