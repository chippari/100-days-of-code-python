
# > Day 13 -------------------------------------------------------------------------------------------------------------
# > 1. Describe the Problem --------------------------------------------------------------------------------------------
print("\n> 1. Describe the Problem")

def my_function():
    for i in range(1, 20):
        print(i)
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# Answer: The loop is running in a range from 1 to 20, but the last number will be 19, because range in a loop behave
# like this.

# 2. When is the function meant to print "You got it"?
# Answer: When the loop achieves at 20, but the range need to be (1, 21) to work.

# 3. What are your assumptions about the value of i?
# Answer: It starts at 1, after will be 2, and so on until achieve the last number minus 1.

# ----------------------------------------------------------------------------------------------------------------------
