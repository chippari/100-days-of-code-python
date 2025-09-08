
# - Day 2 --------------------------------------------------------------------------------------------------------------
# - 2. Type Error, Checking and Conversion -----------------------------------------------------------------------------
# -- 2.1. Fix the len() function:
print("-- 2.1. Type Error - Fix the len() function:")

# Before:
# "len(12345)" - len() function doesn't accept int.
# After:
print(len("12345"))

# -- 2.2. Type Checking:
# Description: You can check the data type of any value or variable in python using the type() function.
print("\n-- 2.2. Type Checking:")

# String Type Checking:
print("String Type Checking:", type("Hello"))

# Int Type Checking:
print("Int Type Checking:", type(123))

# Float Type Checking:
print("Float Type Checking:", type(12.34))

# Boolean Type Checking:
print("Boolean Type Checking:", type(True))

# -- 2.3. Type Conversion:
# Description: You can convert data into different data types using special functions (e.g., str(), int(), float(), bool()).
print("\n-- 2.3. Type Conversion:")

# Type Conversion - Convert a string to an int:
print("Convert a string to an int:", int("123"))

# Type Conversion - Convert an int to a string:
print("Convert an int to a string:", str(123))

# Type Conversion - Convert an int to a float:
print("Convert an int to a float:", float(123))

# Type Conversion - Convert a float to an int:
print("Convert an float to an int:", int(123.456))

# ----------------------------------------------------------------------------------------------------------------------
