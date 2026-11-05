
"""
TUPLES IN PYTHON
----------------
This program demonstrates:

1. Creating tuples
2. Empty and single-element tuples
3. Indexing and negative indexing
4. Slicing
5. Immutability
6. Tuple methods: count() and index()
7. Built-in functions
8. Membership operators
9. Concatenation and repetition
10. Tuple packing and unpacking
11. Extended unpacking
12. Swapping variables
13. Nested tuples
14. Mutable objects inside tuples
15. Tuple references
16. List and tuple conversions
17. Practical student record analysis
"""


# =====================================================
# 1. CREATING TUPLES
# =====================================================

# Tuple containing strings
languages = ("Python", "Java", "C++")

# Tuple containing integers
numbers = (10, 20, 30, 40)

# Tuple containing different data types
student = ("Ammu", 23, 85.5, True)

# Empty tuple
empty_tuple = ()

# Single-element tuple requires a trailing comma
single_element_tuple = (10,)

# Tuple without parentheses: tuple packing
packed_tuple = 10, 20, 30

print("\n1. CREATING TUPLES")
print("------------------")
print("Languages:", languages)
print("Numbers:", numbers)
print("Mixed data:", student)
print("Empty tuple:", empty_tuple)
print("Single-element tuple:", single_element_tuple)
print("Packed tuple:", packed_tuple)


# =====================================================
# 2. INDEXING
# =====================================================

languages = ("Python", "Java", "C++", "SQL")

print("\n2. TUPLE INDEXING")
print("-----------------")

# Positive indexing starts at zero
print("First element:", languages[0])
print("Second element:", languages[1])

# Negative indexing starts from the end
print("Last element:", languages[-1])
print("Second last element:", languages[-2])


# =====================================================
# 3. SLICING
# =====================================================

print("\n3. TUPLE SLICING")
print("----------------")

languages = ("Python", "Java", "C++", "SQL", "JavaScript")

# Retrieve elements between indexes 1 and 3
print("Index 1 to 3:", languages[1:4])

# Retrieve the first three elements
print("First three:", languages[:3])

# Retrieve elements from index 2 onwards
print("From index 2:", languages[2:])

# Retrieve every second element
print("Every second element:", languages[::2])

# Create a reversed tuple
print("Reversed tuple:", languages[::-1])


# =====================================================
# 4. IMMUTABILITY
# =====================================================

print("\n4. IMMUTABILITY")
print("---------------")

numbers = (10, 20, 30)

print("Original tuple:", numbers)

# Tuple elements cannot be reassigned.
# The following statement raises TypeError:
#
# numbers[1] = 50

# We can create a new tuple instead.
new_numbers = numbers + (40, 50)

print("Original tuple remains:", numbers)
print("New tuple:", new_numbers)


# =====================================================
# 5. TUPLE METHODS
# =====================================================

print("\n5. TUPLE METHODS")
print("----------------")

scores = (80, 90, 80, 75, 80)

# count() returns the number of occurrences
print("Number of 80s:", scores.count(80))

# index() returns the first occurrence's index
print("Index of 90:", scores.index(90))


# =====================================================
# 6. BUILT-IN FUNCTIONS
# =====================================================

print("\n6. BUILT-IN FUNCTIONS")
print("---------------------")

scores = (85, 90, 76, 88)

# Count the number of elements
print("Number of scores:", len(scores))

# Calculate total
print("Total:", sum(scores))

# Find smallest value
print("Minimum:", min(scores))

# Find largest value
print("Maximum:", max(scores))

# sorted() returns a list, not a tuple
sorted_scores = sorted(scores)

print("Sorted list:", sorted_scores)

# Convert sorted result back to a tuple
sorted_tuple = tuple(sorted_scores)

print("Sorted tuple:", sorted_tuple)


# =====================================================
# 7. MEMBERSHIP
# =====================================================

print("\n7. MEMBERSHIP")
print("-------------")

languages = ("Python", "Java", "C++")

print("Python exists:", "Python" in languages)
print("JavaScript missing:", "JavaScript" not in languages)


# =====================================================
# 8. CONCATENATION AND REPETITION
# =====================================================

print("\n8. CONCATENATION AND REPETITION")
print("--------------------------------")

first = (10, 20)
second = (30, 40)

# Combine two tuples
combined = first + second

print("Combined tuple:", combined)

# Repeat tuple elements
numbers = (1, 2)

repeated = numbers * 3

print("Repeated tuple:", repeated)


# =====================================================
# 9. TUPLE PACKING AND UNPACKING
# =====================================================

print("\n9. PACKING AND UNPACKING")
print("------------------------")

# Packing: group multiple values into a tuple
student = ("Ammu", 23, "Artificial Intelligence")

print("Packed tuple:", student)

# Unpacking: assign tuple elements to variables
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# =====================================================
# 10. EXTENDED UNPACKING
# =====================================================

print("\n10. EXTENDED UNPACKING")
print("----------------------")

numbers = (10, 20, 30, 40, 50)

# The * operator collects remaining elements into a list
first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# =====================================================
# 11. SWAPPING VARIABLES
# =====================================================

print("\n11. SWAPPING VARIABLES")
print("----------------------")

a = 10
b = 20

print("Before swapping:", a, b)

# Tuple unpacking swaps the values
a, b = b, a

print("After swapping:", a, b)


# =====================================================
# 12. NESTED TUPLES
# =====================================================

print("\n12. NESTED TUPLES")
print("-----------------")

students = (
    ("Ammu", 85),
    ("Ravi", 90),
    ("John", 76)
)

# Access the first inner tuple
print("First student:", students[0])

# Access individual values
print("First student name:", students[0][0])
print("First student score:", students[0][1])

# Iterate through nested tuples
for name, score in students:
    print(f"{name}: {score}")


# =====================================================
# 13. MUTABLE OBJECTS INSIDE TUPLES
# =====================================================

print("\n13. MUTABLE OBJECTS INSIDE TUPLES")
print("---------------------------------")

# The tuple is immutable, but it contains a mutable list
data = ([10, 20], 30)

print("Before modifying inner list:", data)

# This is allowed because the inner list is mutable
data[0].append(40)

print("After modifying inner list:", data)

# Reassigning the tuple element itself is not allowed.
# data[0] = [100, 200]  # TypeError


# =====================================================
# 14. TUPLE REFERENCES
# =====================================================

print("\n14. TUPLE REFERENCES")
print("--------------------")

a = (10, 20, 30)

# b refers to the same tuple object
b = a

print("Tuple a:", a)
print("Tuple b:", b)

# is checks whether both variables refer to the same object
print("Same object:", a is b)


# =====================================================
# 15. CONVERTING BETWEEN LISTS AND TUPLES
# =====================================================

print("\n15. LIST AND TUPLE CONVERSION")
print("-----------------------------")

# Convert tuple to list
numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

print("Converted list:", numbers_list)

# Modify the list because lists are mutable
numbers_list.append(40)

print("Modified list:", numbers_list)

# Convert list back to tuple
new_tuple = tuple(numbers_list)

print("Converted tuple:", new_tuple)


# =====================================================
# 16. PRACTICAL APPLICATION:
# STUDENT RECORD ANALYSIS
# =====================================================

print("\n16. STUDENT RECORD ANALYSIS")
print("---------------------------")

# Each student record is represented as an immutable tuple
student_records = (
    ("Ammu", 85),
    ("Ravi", 90),
    ("John", 76),
    ("Priya", 92),
    ("David", 68)
)

# Initialise variables for analysis
total_score = 0
highest_score = 0
lowest_score = float("inf")

# Process each student record
for name, score in student_records:

    # Add the current score to the total
    total_score += score

    # Update the highest score
    if score > highest_score:
        highest_score = score

    # Update the lowest score
    if score < lowest_score:
        lowest_score = score

    # Display individual student information
    print(f"Student: {name}, Score: {score}")

# Calculate the average
number_of_students = len(student_records)
average_score = total_score / number_of_students

print("\nSTUDENT SUMMARY")
print("----------------")
print("Number of students:", number_of_students)
print("Total score:", total_score)
print(f"Average score: {average_score:.2f}")
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)

# Extract only the student names into a new tuple
student_names = tuple(
    name for name, score in student_records
)

print("Student names:", student_names)


# =====================================================
# END OF PROGRAM
# =====================================================

print("\nTUPLES PROGRAM COMPLETED")
