
# > Day 3 --------------------------------------------------------------------------------------------------------------
# > 3. Nesting and Elif ------------------------------------------------------------------------------------------------
print("> 3. Nesting and Elif")

# >> 3.1. Nesting and Elif (Exercise 1) --------------------------------------------------------------------------------
print(">> 3.1. Nesting and Elif (Exercise 1)")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster! :)")
    age = int(input("What is your age? "))

    if age <= 12:
        print("Please pay $5.00")
    elif age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry, you can't ride the rollercoaster! :(")

# ----------------------------------------------------------------------------------------------------------------------


