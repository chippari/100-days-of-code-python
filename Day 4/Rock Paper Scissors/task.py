
# > Day 4 --------------------------------------------------------------------------------------------------------------
# > 5. Rock, Paper & Scissors Game -------------------------------------------------------------------------------------
# Import Random Module.
import random

print("> 5. Rock, Paper & Scissors Game:")
print("Welcome to the Rock, Paper & Scissors Game!")
print("How to play? At its core, Rock Paper Scissors is a hand game where each move defeats one and loses to another:"
      "\n-> Rock crushes Scissors."
      "\n-> Scissors cut Paper."
      "\n-> Paper covers Rock.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

wants_play = input("Would you like to play? (Y/N): ").upper()

if wants_play == "Y":
    # User Choice:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    user_choice = int(input(">> "))

    if user_choice == 0:
        print("User chose rock:")
        print(game_images[user_choice])
    elif user_choice == 1:
        print("User chose paper:")
        print(game_images[user_choice])
    elif user_choice == 2:
        print("User chose scissors:")
        print(game_images[user_choice])
    else:
        print("That's not a valid choice.")

    # Computer Choice:
    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        print("Computer chose rock:")
        print(game_images[computer_choice])
    elif computer_choice == 1:
        print("Computer chose paper:")
        print(game_images[computer_choice])
    elif computer_choice == 2:
        print("Computer chose scissors:")
        print(game_images[computer_choice])

    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    elif (user_choice == 0 and computer_choice == 0) or (user_choice == 1 and computer_choice == 1) or (user_choice == 2 and computer_choice == 2):
        print("It's a tie!")
    else:
        print("You lose! Computer wins.")

elif wants_play == "N":
    print("Ok, no problem. See you next time!")
else:
    print("That's not a valid choice.")

# ----------------------------------------------------------------------------------------------------------------------
