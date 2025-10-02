
# > Day 9 --------------------------------------------------------------------------------------------------------------
# > 2. Nested Lists and Dictionaries -----------------------------------------------------------------------------------
print("\n> 2. Nested Lists and Dictionaries")

# >> 2.1. Creating a nested list in dictionary  ------------------------------------------------------------------------
print(">> 2.1. Creating a nested list in dictionary:")

travel = {
    "Brasil": ["Sao Paulo", "Campinas", "Rio de Janeiro"],
    "Italia": ["Venice", "Rome", "Sicily"]
}

# Print the city "Rome"
print(f'City Printed: {travel["Italia"][1]}')

# >> 2.2. Nesting Lists inside other Lists  ----------------------------------------------------------------------------
print(">> 2.2. Nesting Lists inside other Lists:")

nested_list = ["A", "B", ["C", "D"]]

# Print the letter "C"
print(f'Letter Printed: {nested_list[2][0]}')

# >> 2.3. Nesting Dictionary inside other Dictionary -------------------------------------------------------------------
print(">> 2.3. Nesting Dictionary inside other Dictionary:")

travel_log = {
    "Brasil": {
        "Times Visited": 8,
        "Cities": ["Sao Paulo", "Campinas", "Rio de Janeiro"]
    },
    "Italy": {
        "Times Visited": 3,
        "Cities": ["Venice", "Rome", "Sicily"]
    }
}

# Print how many times visited Italy and Venice:
print(f'How many times visited Italy: {travel_log["Italy"]["Times Visited"]}')
print(f'One cities visited in Italy: {travel_log["Italy"]["Cities"][0]}')

# ----------------------------------------------------------------------------------------------------------------------
