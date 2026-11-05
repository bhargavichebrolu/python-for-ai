
"""
LISTS IN PYTHON
---------------
This program demonstrates:
1. Creating lists
2. Accessing elements
3. Positive and negative indexing
4. Slicing
5. Mutability
6. append(), extend(), insert()
7. remove(), pop(), del, clear()
8. len(), min(), max(), sum()
9. sort(), sorted(), reverse()
10. Membership operators
11. Iteration and enumerate()
12. List comprehension
13. Nested lists
14. References and shallow/deep copying
15. A practical student score analysis
"""

import copy


# =====================================================
# 1. CREATING LISTS
# =====================================================

# List containing strings
languages = ["Python", "Java", "C++"]

# List containing integers
numbers = [10, 20, 30, 40]

# List containing different data types
student = ["Ammu", 23, 85.5, True]

# Empty list
empty_list = []

print("\n1. CREATING LISTS")
print("-----------------")
print("Languages:", languages)
print("Numbers:", numbers)
print("Mixed data:", student)
print("Empty list:", empty_list)


# =====================================================
# 2. INDEXING
# =====================================================

languages = ["Python", "Java", "C++", "SQL"]

print("\n2. LIST INDEXING")
print("----------------")

# Positive indexing starts at zero
print("First element:", languages[0])
print("Second element:", languages[1])

# Negative indexing starts from the end
print("Last element:", languages[-1])
print("Second last element:", languages[-2])


# =====================================================
# 3. SLICING
# =====================================================

print("\n3. LIST SLICING")
print("---------------")

# Retrieve elements from index 1 to 3
print("Index 1 to 3:", languages[1:4])

# Retrieve the first three elements
print("First three:", languages[:3])

# Retrieve elements from index 2 onwards
print("From index 2:", languages[2:])

# Retrieve every second element
print("Every second element:", languages[::2])

# Create a reversed copy
print("Reversed copy:", languages[::-1])


# =====================================================
# 4. MUTABILITY
# =====================================================

print("\n4. MUTABILITY")
print("-------------")

languages = ["Python", "Java", "C++"]

print("Before modification:", languages)

# Lists are mutable, so individual elements can be changed
languages[1] = "JavaScript"

print("After modification:", languages)


# =====================================================
# 5. ADDING ELEMENTS
# =====================================================

print("\n5. ADDING ELEMENTS")
print("------------------")

languages = ["Python", "Java"]

# append() adds one element at the end
languages.append("C++")
print("After append:", languages)

# extend() adds individual elements from an iterable
languages.extend(["JavaScript", "SQL"])
print("After extend:", languages)

# insert() adds an element at a specified position
languages.insert(1, "Go")
print("After insert:", languages)

# append() can also add a nested list as one element
numbers = [1, 2]
numbers.append([3, 4])
print("Append nested list:", numbers)

# extend() adds the elements individually
numbers = [1, 2]
numbers.extend([3, 4])
print("Extend list:", numbers)


# =====================================================
# 6. REMOVING ELEMENTS
# =====================================================

print("\n6. REMOVING ELEMENTS")
print("--------------------")

languages = ["Python", "Java", "C++", "Java"]

# remove() removes the first matching value
languages.remove("Java")
print("After remove:", languages)

# pop() removes and returns the last element
removed = languages.pop()
print("Popped element:", removed)
print("After pop:", languages)

# pop(index) removes an element at a specified index
removed = languages.pop(0)
print("Popped by index:", removed)
print("After indexed pop:", languages)

# del deletes an element using its index
languages = ["Python", "Java", "C++"]
del languages[1]
print("After del:", languages)

# clear() removes every element
languages.clear()
print("After clear:", languages)


# =====================================================
# 7. BUILT-IN LIST FUNCTIONS
# =====================================================

print("\n7. BUILT-IN FUNCTIONS")
print("---------------------")

scores = [82, 45, 91, 67, 38, 76]

# len() returns the number of elements
print("Number of scores:", len(scores))

# sum() calculates the total
print("Total score:", sum(scores))

# min() finds the smallest value
print("Lowest score:", min(scores))

# max() finds the largest value
print("Highest score:", max(scores))

# Calculate average
average = sum(scores) / len(scores)
print("Average score:", average)


# =====================================================
# 8. SORTING
# =====================================================

print("\n8. SORTING")
print("----------")

scores = [82, 45, 91, 67, 38]

# sorted() creates a new sorted list
ascending = sorted(scores)

print("Original list:", scores)
print("Sorted copy:", ascending)

# Descending order using sorted()
descending = sorted(scores, reverse=True)
print("Descending copy:", descending)

# sort() modifies the original list
scores.sort()
print("After sort():", scores)

# Reverse sorting in place
scores.sort(reverse=True)
print("After descending sort():", scores)


# =====================================================
# 9. REVERSING
# =====================================================

print("\n9. REVERSING")
print("------------")

numbers = [10, 20, 30, 40]

# reverse() modifies the original list
numbers.reverse()

print("After reverse():", numbers)

# Slicing creates a reversed copy
reversed_numbers = numbers[::-1]

print("Reversed copy:", reversed_numbers)


# =====================================================
# 10. MEMBERSHIP CHECKING
# =====================================================

print("\n10. MEMBERSHIP")
print("--------------")

languages = ["Python", "Java", "C++"]

# in checks whether an element exists
print("Python exists:", "Python" in languages)

# not in checks whether an element does not exist
print("JavaScript missing:", "JavaScript" not in languages)


# =====================================================
# 11. ITERATION
# =====================================================

print("\n11. ITERATION")
print("-------------")

languages = ["Python", "Java", "C++"]

# Process every element using a for loop
for language in languages:
    print("Language:", language)

# enumerate() provides both index and element
for index, language in enumerate(languages):
    print(index, language)

# enumerate() can start counting from one
for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")


# =====================================================
# 12. LIST COMPREHENSION
# =====================================================

print("\n12. LIST COMPREHENSION")
print("----------------------")

numbers = [1, 2, 3, 4, 5]

# Create a new list containing squares
squares = [number ** 2 for number in numbers]

print("Squares:", squares)

# Filter only even numbers
even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print("Even numbers:", even_numbers)


# =====================================================
# 13. NESTED LISTS
# =====================================================

print("\n13. NESTED LISTS")
print("----------------")

students = [
    ["Ammu", 85],
    ["Ravi", 90],
    ["John", 76]
]

# Access the first inner list
print("First student:", students[0])

# Access individual values inside the first inner list
print("Student name:", students[0][0])
print("Student score:", students[0][1])

# Iterate through nested lists
for student_record in students:
    name = student_record[0]
    score = student_record[1]

    print(f"{name}: {score}")


# =====================================================
# 14. REFERENCES AND COPYING
# =====================================================

print("\n14. REFERENCES AND COPYING")
print("--------------------------")

# Both variables refer to the same list object
a = [1, 2, 3]
b = a

b.append(4)

print("Original reference a:", a)
print("Reference b:", b)

# copy() creates a shallow copy
a = [1, 2, 3]
b = a.copy()

b.append(4)

print("Original a after shallow copy:", a)
print("Copied b:", b)

# Demonstrate shallow copying with nested lists
a = [[1, 2], [3, 4]]
b = a.copy()

# The inner list is shared
b[0].append(99)

print("Original after shallow nested modification:", a)
print("Shallow copy:", b)

# deepcopy() creates independent nested objects
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)

print("Original after deep copy modification:", a)
print("Deep copy:", b)


# =====================================================
# 15. PRACTICAL APPLICATION:
# STUDENT SCORE ANALYSIS
# =====================================================

print("\n15. STUDENT SCORE ANALYSIS")
print("--------------------------")

# Store student scores in a list
student_scores = [82, 45, 91, 67, 38, 76]

# Initialise counters and total
total_score = 0
passed = []
failed = []

# Process every score
for score in student_scores:

    # Add the current score to the running total
    total_score += score

    # Classify the score
    if score >= 50:
        passed.append(score)
    else:
        failed.append(score)

# Calculate statistics
number_of_students = len(student_scores)
average_score = total_score / number_of_students

print("All scores:", student_scores)
print("Total score:", total_score)
print(f"Average score: {average_score:.2f}")
print("Highest score:", max(student_scores))
print("Lowest score:", min(student_scores))

# Display passed and failed scores
print("Passed scores:", passed)
print("Failed scores:", failed)

# Sort scores without changing the original list
sorted_scores = sorted(student_scores)

print("Sorted scores:", sorted_scores)

# Add a new score
student_scores.append(88)

print("After adding a score:", student_scores)

# Remove a score
student_scores.remove(45)

print("After removing 45:", student_scores)

# Check whether a score exists
print("Is 91 present?", 91 in student_scores)


# =====================================================
# END OF PROGRAM
# =====================================================

print("\nLISTS PROGRAM COMPLETED")
