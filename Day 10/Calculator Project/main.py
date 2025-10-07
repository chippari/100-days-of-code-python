
# > Day 10 -------------------------------------------------------------------------------------------------------------
# > 4. Calculator Project ----------------------------------------------------------------------------------------------
print("\n> 4. Calculator Project")

import art

# >> 4.1. Mathematical Operation Functions and Dictionary --------------------------------------------------------------
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# >> 4.2. Calculation Function -----------------------------------------------------------------------------------------
def calculation(n1, operator, n2):
    if isinstance(n1, float) and isinstance(n2, float):
        if operator in math_operations:
            calculation_result = math_operations[operator](n1, n2)
            return calculation_result
        else:
            return "Invalid operator."
    else:
        return "This is not a valid number."

# >> 4.3. Calculator Function ------------------------------------------------------------------------------------------
def calculator():
    print(art.logo)
    print("Welcome to Calculator Project!")
    user_n1 = float(input("Enter first number: "))

    calculator_loop = True
    while calculator_loop:

        for symbol in math_operations:
            print(f'({symbol})', end=" ")

        user_operator = input("\nEnter operator: ")
        user_n2 = float(input("Enter second number: "))

        result = calculation(user_n1, user_operator, user_n2)
        print(f'{user_n1} {user_operator} {user_n2} = {result}')

        choice = input(f'\nType (Y) to continue calculating with {result}, or type (N) to start a '
                       f'new calculation, or type "quit": ').lower()

        if choice == 'y':
            user_n1 = result
        elif choice == 'n':
            calculator_loop = False
            print("\n" * 20)
            calculator()
        elif choice == 'quit':
            print("Thank you for using my calculator!")
            calculator_loop = False
        else:
            print("Invalid input.")

# >> 4.4. Calling the Calculator ---------------------------------------------------------------------------------------
calculator()

# ----------------------------------------------------------------------------------------------------------------------
