
# > Day 13 -------------------------------------------------------------------------------------------------------------
# > 4. Fix the errors --------------------------------------------------------------------------------------------------
print("\n> 4. Fix the errors")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have type in an invalid number. Please try again with a numerical response such as '15'.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")


# ----------------------------------------------------------------------------------------------------------------------
