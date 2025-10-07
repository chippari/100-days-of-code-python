
# > Day 12 -------------------------------------------------------------------------------------------------------------
# > 1. Namespaces, Global & Local Scope --------------------------------------------------------------------------------
print("\n> 1. Namespaces, Global & Local Scope")

# This variable is Global Scope, because we can access everywhere on the code.
enemy = 1

def increase_enemies():
    # This variable is Local Scope, because we can access only inside this function.
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemy}")

# ----------------------------------------------------------------------------------------------------------------------
