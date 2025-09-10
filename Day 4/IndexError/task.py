
# > Day 4 --------------------------------------------------------------------------------------------------------------
# > 4. Index Error -----------------------------------------------------------------------------------------------------
print("> 4. Index Error")

# >> 4.1. Index Error (Example) ----------------------------------------------------------------------------------------
print(">> 4.1. Index Error (Example):")
# When you try to access an item that is not in the range of the List, you will get an IndexError. E.g:
fruits = ["apple", "banana", "orange", "apple"]

# This fruits list has in total four fruits, but you can access the last item by 4 - 1 = 3,
# Because the lists starts at zero, containing the first fruit.
print(f'Total of items in fruits list: {len(fruits)}')

# If you try this: fruits[4] you will get an Index Error, because is not in the range of the list.
# Instead, you get the last item of fruits list typing like this:
print(f'Last item in fruits list: {fruits[4 - 1]}')

# >> 4.2. Nested Lists -------------------------------------------------------------------------------------------------
print("\n>> 4.2. Nested Lists:")
# You can put Lists inside other Lists, this becomes something called a "Nested List".

fruits = ["apple", "banana", "orange"]
vegetables = ["carrot", "potatoes", "spinach"]

fruits_and_vegetables = [fruits, vegetables]
print(f"fruits List: {fruits}")
print(f"vegetables List: {vegetables}")
print(f"Fruits & Vegetables List: {fruits_and_vegetables}")

# ----------------------------------------------------------------------------------------------------------------------
