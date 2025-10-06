
# > Day 10 -------------------------------------------------------------------------------------------------------------
# > 3. Docstrings ------------------------------------------------------------------------------------------------------
print("\n> 3. Docstrings")

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'Your Formated Name is: {formated_f_name} {formated_l_name}'

formatted_name = format_name(f_name="FABIO", l_name="ChiPpaRi")

length = len(formatted_name)

# ----------------------------------------------------------------------------------------------------------------------
