
# > Day 4 --------------------------------------------------------------------------------------------------------------
# > 1. Random Module ---------------------------------------------------------------------------------------------------
print("> 1. Random Module")
# First Import Random Library:
import random

# >> 1.1. Random Number Between 0.0 and 1.0 ----------------------------------------------------------------------------
print(">> 1.1. Random Number Between 0.0 and 1.:")
# Generate a Random Number between 0.0 and 1.0 using random.random()
# This return the next random floating-point number in the range 0.0 <= X < 1.0
rand_num_0_to_1 = random.random()
print(f"My Random Number between 0.0 and 1.0 is: {rand_num_0_to_1}")

# You can multiply the random.random() to extend the range, for example:
# Multiply by 10 to extend the range between 0.0 and 10.0
rand_num = random.random() * 10
print(f"My Random Number multiplied by 10 and between 0.0 and 10.0 is: {rand_num}")

# >> 1.2. Random Integer Number ----------------------------------------------------------------------------------------
print("\n>> 1.2. Random Integer Number:")
# Generate a Random Integer Number using random.randint(a, b)
# This return a random integer N such that a <= N <= b
rand_int = random.randint(1, 10)
print(f"My Random Integer Number between 1 and 10 is: {rand_int}")

# >> 1.3. Random Floating Number ---------------------------------------------------------------------------------------
print("\n>> 1.3. Random Floating Number:")
# Generate a Random Floating Number using random.uniform(a, b)
# This return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a
rand_float = random.uniform(1, 10)
print(f"My Random Floating Number between 1.0 and 10.0 is: {rand_float}")

# >> 1.4. Create Coin Flip Program -------------------------------------------------------------------------------------
print("\n>> 1.4. Create Coin Flip Program:")
coin_flip = random.randint(0, 1)

if coin_flip == 0:
    print("Heads")
else:
    print("Tails")

# ----------------------------------------------------------------------------------------------------------------------
