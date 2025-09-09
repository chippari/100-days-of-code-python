
# > Day 4 --------------------------------------------------------------------------------------------------------------
# > 2. Lists -----------------------------------------------------------------------------------------------------------
print("> 2. Lists")
print(">> 2.1. Creating a List:")
# Lists are a simple collection of ordered items, and you create like this:
fruits = ["apple", "banana", "cherry"]
print(f"Full List of fruits: {fruits}")

print("\n>> 2.2. Accessing Items in List:")
# Accessing a Specific Item of the List:
print(f"First fruit of the list: {fruits[0]}")
print(f"Second fruit of the list: {fruits[1]}")

print("\n>> 2.3. Accessing Items Backwards in List:")
# Accessing a Specific Item of the List Backwards using Negative Indices:
print(f"Last fruit of the list: {fruits[-1]}")

print("\n>> 2.4. Modifying Items in List:")
fruits[0] = "pineapple"
print(f"Changed first fruit of the list: {fruits[0]}")

print("\n>> 2.5. Adding Items in List:")
# To add items to the end of a list using the append() function:
fruits.append("orange")
print(f"Full List of fruits: {fruits}")

# ----------------------------------------------------------------------------------------------------------------------
