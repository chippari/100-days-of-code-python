
# > Day 5 --------------------------------------------------------------------------------------------------------------
# > 4. Password Generator Project --------------------------------------------------------------------------------------
print("\n> 4. Password Generator Project:")

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# >> 4.1. Password Generator Project (Easy Version) --------------------------------------------------------------------
print("\n>> 4.1. Password Generator Project (Easy Version):")

easy_generated_password = ""
if nr_letters > 0:
    for char in range(nr_letters):
        easy_generated_password += random.choice(letters)

if nr_numbers > 0:
    for number in range(nr_numbers):
        easy_generated_password += random.choice(numbers)

if nr_symbols > 0:
    for symbol in range(nr_symbols):
        easy_generated_password += random.choice(symbols)

print(f"Your Easy Generated Password: {easy_generated_password}")

# >> 4.2. Password Generator Project (Hard Version) --------------------------------------------------------------------
print("\n>> 4.2. Password Generator Project (Hard Version):")

hard_generated_password_list = []
if nr_letters > 0:
    for char in range(nr_letters):
        hard_generated_password_list.append(random.choice(letters))

if nr_numbers > 0:
    for number in range(nr_numbers):
        hard_generated_password_list.append(random.choice(numbers))

if nr_symbols > 0:
    for symbol in range(nr_symbols):
        hard_generated_password_list.append(random.choice(symbols))

random.shuffle(hard_generated_password_list)

hard_generated_password = ""
for char in hard_generated_password_list:
    hard_generated_password += char

print(f"Your Hard Generated Password: {hard_generated_password}")


# ----------------------------------------------------------------------------------------------------------------------
