
# > Day 12 -------------------------------------------------------------------------------------------------------------
# > 3. Global Vars -----------------------------------------------------------------------------------------------------
print("\n> 3. Global Vars")

# >> 3.1. Modifying Global Scope (Bad Practice) ------------------------------------------------------------------------
print(">> 3.1. Modifying Global Scope (Bad Practice)")
# It's not recommended to use, because can make bugs, it's confusing sometimes, and it's not considered a best practice.

enemies = 1

def increase_enemies():
    # It can modify and use the Global Variable if you insert this code:
    global enemies
    print(f"enemies inside function: {enemies}") # 1 enemies
    enemies += 1

increase_enemies()
print(f"enemies outside function: {enemies}") # 2 enemies

# >> 3.2. Modifying Global Scope (Best Practice) -----------------------------------------------------------------------
print("\n>> 3.2. Modifying Global Scope (Best Practice)")
# Instead, it's considered a best practice if you use Return Values on your function.

def new_increase_enemies(enemy):
    print(f"enemies inside function: {enemy}") # 2 enemies
    return enemy + 1

enemies = new_increase_enemies(enemies)
print(f"enemies outside function: {enemies}") # 3 enemies

# ----------------------------------------------------------------------------------------------------------------------
