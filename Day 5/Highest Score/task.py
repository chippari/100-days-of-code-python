
# > Day 5 --------------------------------------------------------------------------------------------------------------
# > 2. For Loops -------------------------------------------------------------------------------------------------------
print("\n> 2. For Loops")

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# >> 2.1. For Loops (Exercise 1) ---------------------------------------------------------------------------------------
print("\n>> 2.1. For Loops (Exercise 1):")

# In python, developers created a sum function to sum all the numbers and display the result, e.g.:
total_exam_score = sum(student_scores)
print(f"Total Student Scores (Built Sum Function): {total_exam_score}")

# But we can create the same idea using the for loops, e.g.:
sum_scores = 0
for score in student_scores:
    sum_scores += score

print(f"Total Student Scores (My For Loops): {sum_scores}")

# >> 2.2. For Loops (Exercise 2) ---------------------------------------------------------------------------------------
print("\n>> 2.2. For Loops (Exercise 2):")

# In python, developers created a max function to get the highest number and display it, e.g.:
highest_exam_score = max(student_scores)
print(f"Highest Student Score (Built Max Function): {highest_exam_score}")

# But we can create the same idea using the for loops, e.g.:
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Highest Score (My For Loops): {max_score}")

# ----------------------------------------------------------------------------------------------------------------------
