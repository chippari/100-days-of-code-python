
# > Day 3 --------------------------------------------------------------------------------------------------------------
# > 5. Python Pizza ----------------------------------------------------------------------------------------------------
print("> 5. Python Pizza")

# >> 5.1. Python Pizza (Exercise 1) ------------------------------------------------------------------------------------
print("\n>> 5.1. Python Pizza (Exercise 1)")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

if size == "S":
    bill += 15
    print(f"Small Pizza cost ${bill}")
elif size == "M":
    bill += 20
    print(f"Medium Pizza cost ${bill}")
elif size == "L":
    bill += 25
    print(f"Large Pizza cost ${bill}")
else:
    print("You typed something wrong!")

if pepperoni == "Y":
    if size == "S":
        pepperoni_price = 2
    else:
        pepperoni_price = 3

    bill += pepperoni_price
    print(f"Peperoni Additional cost ${pepperoni_price}")

if extra_cheese == "Y":
    extra_cheese_price = 1
    bill += 1
    print(f"Extra Cheese cost ${extra_cheese_price}")

print(f"Your final bill is: ${bill}")

# ----------------------------------------------------------------------------------------------------------------------
