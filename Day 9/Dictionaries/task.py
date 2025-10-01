
# > Day 9 --------------------------------------------------------------------------------------------------------------
# > 1. Dictionaries ----------------------------------------------------------------------------------------------------
print("\n> 1. Dictionaries")

# >> 1.1. Creating a dictionary in Python  -----------------------------------------------------------------------------
print(">> 1.1. Creating a dictionary in Python:")

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(f'Print Function Definition: {programming_dictionary["Function"]}')

# >> 1.2. Adding new item to an existing dictionary  -------------------------------------------------------------------
print("\n>> 1.2. Adding new item to an existing dictionary:")

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# >> 1.3. Removing all items to an existing dictionary  ----------------------------------------------------------------
print("\n>> 1.3. Removing all items to an existing dictionary:")

programming_dictionary = {}
print(programming_dictionary)

# >> 1.4. Editing an item to an existing dictionary  -------------------------------------------------------------------
print("\n>> 1.4. Editing an item to an existing dictionary:")

programming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected."
programming_dictionary["Bug"] = "A modified version of Bug."
print(programming_dictionary)

# >> 1.5. Loop through a dictionary  -----------------------------------------------------------------------------------
print("\n>> 1.5. Loop through a dictionary:")

fruits = {
    "apple": "a round fruit with firm, white flesh and a green or red skin.",
    "banana": "a long, curved fruit with a yellow skin, soft and sweet.",
    "pineapple": "a large prickly fruit with stiff leaves and yellow flesh."
}

for key in fruits:
    print(f'{key}: {fruits[key]}')

# ----------------------------------------------------------------------------------------------------------------------
