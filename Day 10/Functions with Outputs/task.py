
# > Day 10 -------------------------------------------------------------------------------------------------------------
# > 1. Functions with Outputs ------------------------------------------------------------------------------------------
print("\n> 1. Functions with Outputs")

# > 1.1. Creating Functions with Outputs -------------------------------------------------------------------------------
print("> 1.1. Creating Functions with Outputs")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Your Formated Name is: {formated_f_name} {formated_l_name}'

print("Welcome to Formated Name Program!")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print(format_name(f_name=first_name, l_name=last_name))

# ----------------------------------------------------------------------------------------------------------------------
