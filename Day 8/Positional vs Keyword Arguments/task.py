
# > Day 8 --------------------------------------------------------------------------------------------------------------
# > 2. Positional vs Keyword Arguments ---------------------------------------------------------------------------------
print("\n> 2. Positional vs Keyword Arguments")

def greet_with(name, location):
    print(f"-> Hello {name}, it's a pleasure to meet you!")
    print(f"-> You live in {location}.")

# >> 2.1. Creating a Function with Multiple Inputs (Positional Argument) -----------------------------------------------
print(">> 2.1. Creating a Function with Multiple Inputs (Positional Argument):")

# By default, when you create a function in Python, it will keep the order of arguments in the function definition, and
# this is called Positional Argument.

greet_with("Fabio", "Sao Paulo")

# >> 2.2. Creating a Function with Multiple Inputs (Keyword Argument) --------------------------------------------------
print("\n>> 2.2. Creating a Function with Multiple Inputs (Keyword Argument):")

# You can use keywords when you provide the arguments when you call a function so that there is less confusion which
# value is assigned to which input parameter.

greet_with(location="Sao Paulo", name="Fabio")

# ----------------------------------------------------------------------------------------------------------------------
