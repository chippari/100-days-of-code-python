
# - Day 1 --------------------------------------------------------------------------------------------------------------
# - 5. Variable Naming -------------------------------------------------------------------------------------------------
# -- 5.1. Variable Naming Rules in Python:
# 1. Must start with a letter (a–z, A–Z) or underscore (_).
# 2. Can only contain letters, digits (0–9), and underscores (_).
# 3. Cannot start with a digit.
# 4. Case-sensitive (myVar != myvar).
# 5. Cannot be a Python keyword (e.g., if, for, class, etc.).
# 6. Constants are usually written in ALL CAPS (e.g., PI.)

# ✅ VALID VARIABLE NAMES
user_name = "Alice"
age = 25
_city = "New York"
firstName = "John"
last_name = "Doe"
value123 = 99
PI = 3.14159

print("Valid variables examples:")
print(user_name, age, _city, firstName, last_name, value123, PI)

# ❌ INVALID VARIABLE NAMES (these will cause errors if uncommented)
# 1variable = "Nope"         # ❌ Cannot start with a number.
# user name = "Nope"         # ❌ Spaces are not allowed.
# my-variable = "Nope"       # ❌ Hyphens are not allowed.
# class = "Nope"             # ❌ 'class' is a reserved keyword.
# for = "Nope"               # ❌ 'for' is a reserved keyword.
# def = "Nope"               # ❌ 'def' is a reserved keyword.
# @data = "Nope"             # ❌ '@' is not allowed.
# first$name = "Nope"        # ❌ '$' symbol not allowed.

# ----------------------------------------------------------------------------------------------------------------------
