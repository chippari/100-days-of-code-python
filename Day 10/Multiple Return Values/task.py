
# > Day 10 -------------------------------------------------------------------------------------------------------------
# > 2. Multiple Return Value -------------------------------------------------------------------------------------------
print("\n> 2. Multiple Return Value")

# > 2.1. Creating Functions with Multiple Return Value -----------------------------------------------------------------
print("> 2.1. Creating Functions with Multiple Return Value")

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any values."

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Your Formated Name is: {formated_f_name} {formated_l_name}'

print("Welcome to Formated Name Program!")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print(format_name(f_name=first_name, l_name=last_name))

# ----------------------------------------------------------------------------------------------------------------------
