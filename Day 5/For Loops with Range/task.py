
# > Day 5 --------------------------------------------------------------------------------------------------------------
# > 3. For Loops with Range --------------------------------------------------------------------------------------------
print("\n> 3. For Loops with Range")

# >> 3.1. For Loops with Range (How it works) --------------------------------------------------------------------------
print("\n>> 3.1. For Loops with Range (How it works):")

# The Range Function doesn't do anything by itself.
# But using in For Loops, this wills print out each of the numbers, starting at "a" and finishing at "b - 1". e.g.:
# If we put a range between 1 and 4, it will print this:
for number in range(1, 4):
    print(number)

# >> 3.2. For Loops with Range (Exercise 1) ----------------------------------------------------------------------------
print("\n>> 3.2. For Loops with Range (Exercise 1):")

# The Gauss Challenge:
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

total_number = 0
for number in range(1, 101):
    total_number += number

print(f"Total Number: {total_number}")

# ----------------------------------------------------------------------------------------------------------------------
