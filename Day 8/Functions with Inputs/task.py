
# > Day 8 --------------------------------------------------------------------------------------------------------------
# > 1. Functions with Inputs -------------------------------------------------------------------------------------------
print("\n> 1. Functions with Inputs")

# >> 1.1. Review how to create a Function  -----------------------------------------------------------------------------
print(">> 1.1. Review how to create a Function:")

# Creating a Greet Function:
def greet():
    print(">> Hello!")
    print(">> It's a pleasure to meet you!")
    print(">> Let's program something together?")

# Calling the Greet Function:
greet()

# >> 1.2. Creating a Function with Input  ------------------------------------------------------------------------------
print("\n>> 1.2. Creating a Function with Input:")

# Creating a Greet Function that allows Input:
def greet_with_name(name):
    print(f">> Hello {name}!")
    print(f">> It's a pleasure to meet you, {name}!")
    print(f">> Let's program something together {name}?")

# Calling the Greet Function and Insert an Input:
greet_with_name("Fabio")

# ----------------------------------------------------------------------------------------------------------------------
