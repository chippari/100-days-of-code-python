
# > Day 3 --------------------------------------------------------------------------------------------------------------
# > 7. Treasure Island Project -----------------------------------------------------------------------------------------

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First User Decision:
print("\nYou're at a cross road. Where do you want to go? Type 'left' or 'right':")
user_choice_1 = input(">> ").lower()

if user_choice_1 == "left":
    print("\nYou come to a lake. There's an island in the middle of the lake.")
    # Second User Decision:
    print("Type 'wait' to wait for a boat or 'swim' to swim across:")
    user_choice_2 = input(">> ").lower()

    if user_choice_2 == "wait":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors: one red, one yellow and one blue.")
        # Third User Decision:
        print("Which color do you choose?")
        user_choice_3 = input(">> ").lower()

        if user_choice_3 == "red":
            print("\n========== Game Over ==========")
            print("You open the red door and flames burst out. The heat is unbearable. "
                  "You are burned by fire. Game Over.")
        elif user_choice_3 == "blue":
            print("\n========== Game Over ==========")
            print("You open the blue door and hear growls in the dark. "
                  "Suddenly, wild beasts leap at you. You are eaten alive.")
        elif user_choice_3 == "yellow":
            print("\n========== You Win! ==========")
            print("You open the yellow door, and golden light fills the room. "
                  "You have found the hidden treasure!")
        else:
            print("\n========== Game Over ==========")
            print("Confused, you open a door that wasn’t really there. "
                  "The walls collapse and you are trapped forever.")
    elif user_choice_2 == "swim":
        print("\n========== Game Over ==========")
        print("You dive into the water, but the current is strong. "
              "Suddenly, a group of trout swarm you. You are attacked and dragged under.")
    else:
        print("\n========== Game Over ==========")
        print("You wander around the lake, unsure what to do. "
              "Night falls, and strange creatures emerge from the shadows. "
              "You never make it to the island...")
elif user_choice_1 == "right":
    print("\n========== Game Over ==========")
    print("You take the right path and the ground beneath you crumbles. "
          "You fall into a dark, endless hole.")
else:
    print("\n========== Game Over ==========")
    print("You stand frozen, unable to decide. "
          "The forest grows darker around you until all light fades, and you vanish into the night...")

# ----------------------------------------------------------------------------------------------------------------------
