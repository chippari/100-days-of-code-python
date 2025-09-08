
# - Day 2 --------------------------------------------------------------------------------------------------------------
# - 4. Number Manipulation ---------------------------------------------------------------------------------------------
print("- 4. Number Manipulation")

# -- 4.1. Flooring a Number:
print("-- 4.1. Flooring a Number:")
print("Without Flooring a Number: ", (5 / 3))
print("With Flooring a Number: ", int(5 / 3))

# -- 4.2. Rounding a Number:
print("\n-- 4.2. Rounding a Number:")
print("Without Rounding a Number:", (5 / 3))
print("With Rounding a Number:", round(5 / 3))
print("With Rounding a Number and Two Decimals:", round(5 / 3, 2))

# -- 4.3. Assignment Operators:
print("\n-- 4.3. Assignment Operators:")
score = 2

# --- 4.3.1. Assignment Addition Operation:
print("--- 4.3.1. Assignment Addition Operation:")
print("score =", score)
score += 1
print("score += 1 -> result =", score)

# --- 4.3.2. Assignment Subtraction Operation:
print("--- 4.3.2. Assignment Subtraction Operation:")
print("score =", score)
score -= 1
print("score -= 1 -> result =", score)

# --- 4.3.3. Assignment Multiple Operation:
print("--- 4.3.3. Assignment Multiple Operation:")
print("score =", score)
score *= 2
print("score *= 2 -> result =", score)

# --- 4.3.4. Assignment Division Operation:
print("--- 4.3.4. Assignment Division Operation:")
print("score =", score)
score /= 2
print("score /= 2 -> result =", score)

# -- 4.4. f-Strings:
print("\n-- 4.4. f-Strings:")

name = "Lucas"
age = 23
height = 1.70

print(f"Your name is {name}, and your age is {age} years old. Your height is {height} meters.")


# ----------------------------------------------------------------------------------------------------------------------
