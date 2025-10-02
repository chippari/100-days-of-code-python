
# > Day 9 --------------------------------------------------------------------------------------------------------------
# > 3. Blind Auction Project -------------------------------------------------------------------------------------------
print("\n> 3. Blind Auction Project")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the Blind Auction Project!")

dictionary_bids = {}

loop = True
while loop:
    name = input("\nWhat is your name? ")
    bid = int(input("What is your bid? $"))

    dictionary_bids[name] = bid

    other_bid = input("Are there any other bids? (y/n): ").lower()
    if other_bid == "n":
        loop = False

winner_bid = max(dictionary_bids.values())
winner_name = max(dictionary_bids.keys())
print(f'The winner {winner_name} is with a bid of {winner_bid}')

# ----------------------------------------------------------------------------------------------------------------------
