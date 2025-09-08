
# > Day 3 --------------------------------------------------------------------------------------------------------------
# > 4. Multiple If Statements ------------------------------------------------------------------------------------------
print("> 4. Multiple If Statements")

# >> 4.1. Multiple If Statements (Exercise 1) --------------------------------------------------------------------------
print(">> 4.1. Multiple If Statements (Exercise 1)")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster! :)")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5.0
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7.0
        print(f"Youth tickets are ${bill}")
    else:
        bill = 12.0
        print(f"Adults tickets are ${bill}")

    wants_photo = input("Would you like to take a photo? (y/n): ")
    if wants_photo == "y":
        # Add $3 to their bill.
        bill += 3.0

    print(f"Your final bill is: ${bill}")
else:
    print("Sorry, you can't ride the rollercoaster! :(")

# ----------------------------------------------------------------------------------------------------------------------

