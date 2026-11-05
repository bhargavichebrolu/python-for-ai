
"""
SETS IN PYTHON
--------------
This program demonstrates:

1. Creating sets
2. Empty sets
3. Duplicate removal
4. Unordered property
5. Adding elements: add(), update()
6. Removing elements: remove(), discard(), pop(), clear()
7. Union
8. Intersection
9. Difference
10. Symmetric difference
11. Membership checking
12. Subsets and supersets
13. Disjoint sets
14. Frozen sets
15. List and tuple conversions
16. Set comprehension
17. Copying sets
18. Practical student course analysis
"""


# =====================================================
# 1. CREATING SETS
# =====================================================

# Set containing integers
numbers = {10, 20, 30, 40}

# Set containing strings
languages = {"Python", "Java", "C++"}

# Set containing different data types
mixed_data = {"Ammu", 23, 85.5, True}

# Empty set
empty_set = set()

# Duplicate elements are automatically removed
duplicate_numbers = {10, 20, 10, 30, 20}

print("\n1. CREATING SETS")
print("----------------")
print("Numbers:", numbers)
print("Languages:", languages)
print("Mixed data:", mixed_data)
print("Empty set:", empty_set)
print("Duplicates removed:", duplicate_numbers)


# =====================================================
# 2. UNORDERED PROPERTY AND UNIQUENESS
# =====================================================

print("\n2. UNIQUENESS")
print("-------------")

student_records = [
    "Ammu",
    "Ravi",
    "John",
    "Ammu",
    "Ravi"
]

# Convert the list into a set to remove duplicates
unique_students = set(student_records)

print("Original records:", student_records)
print("Unique students:", unique_students)

# Sets do not support indexing.
# The following would raise TypeError:
#
# print(unique_students[0])


# =====================================================
# 3. ADDING ELEMENTS
# =====================================================

print("\n3. ADDING ELEMENTS")
print("------------------")

languages = {"Python", "Java"}

# add() inserts one element
languages.add("C++")

print("After add():", languages)

# Adding an existing element does not create a duplicate
languages.add("Python")

print("After adding duplicate:", languages)

# update() inserts multiple elements from an iterable
languages.update(["JavaScript", "SQL"])

print("After update():", languages)


# =====================================================
# 4. REMOVING ELEMENTS
# =====================================================

print("\n4. REMOVING ELEMENTS")
print("--------------------")

languages = {"Python", "Java", "C++", "SQL"}

# remove() removes an existing element
languages.remove("Java")

print("After remove():", languages)

# discard() safely handles a missing element
languages.discard("JavaScript")

print("After discard():", languages)

# pop() removes and returns an arbitrary element
removed = languages.pop()

print("Element removed by pop():", removed)
print("After pop():", languages)

# clear() removes every element
languages.clear()

print("After clear():", languages)


# =====================================================
# 5. SET OPERATIONS
# =====================================================

print("\n5. SET OPERATIONS")
print("-----------------")

python_students = {"Ammu", "Ravi", "John", "Priya"}

java_students = {"Ravi", "John", "David", "Kiran"}

# Union: all unique elements from both sets
all_students = python_students | java_students

print("Union:", all_students)

# Intersection: common elements
common_students = python_students & java_students

print("Intersection:", common_students)

# Difference: elements in Python but not Java
python_only = python_students - java_students

print("Python only:", python_only)

# Reverse difference: elements in Java but not Python
java_only = java_students - python_students

print("Java only:", java_only)

# Symmetric difference: elements that are not common
different_students = python_students ^ java_students

print("Symmetric difference:", different_students)


# =====================================================
# 6. SET METHODS FOR MATHEMATICAL OPERATIONS
# =====================================================

print("\n6. SET OPERATION METHODS")
print("------------------------")

a = {1, 2, 3}
b = {3, 4, 5}

# union() combines both sets
print("Union:", a.union(b))

# intersection() finds common elements
print("Intersection:", a.intersection(b))

# difference() finds elements in the first set only
print("Difference:", a.difference(b))

# symmetric_difference() finds non-common elements
print("Symmetric difference:", a.symmetric_difference(b))


# =====================================================
# 7. MEMBERSHIP CHECKING
# =====================================================

print("\n7. MEMBERSHIP")
print("-------------")

languages = {"Python", "Java", "C++"}

# Check whether Python exists
print("Python exists:", "Python" in languages)

# Check whether JavaScript is missing
print("JavaScript missing:", "JavaScript" not in languages)


# =====================================================
# 8. SUBSETS AND SUPERSETS
# =====================================================

print("\n8. SUBSETS AND SUPERSETS")
print("------------------------")

a = {1, 2}
b = {1, 2, 3, 4}

# Check whether every element of a exists in b
print("a is subset of b:", a.issubset(b))

# Check whether b contains every element of a
print("b is superset of a:", b.issuperset(a))

# Equivalent operators
print("Subset using <=:", a <= b)
print("Superset using >=:", b >= a)


# =====================================================
# 9. DISJOINT SETS
# =====================================================

print("\n9. DISJOINT SETS")
print("----------------")

first = {1, 2, 3}
second = {4, 5, 6}

# Disjoint means there are no common elements
print("Are sets disjoint?", first.isdisjoint(second))


# =====================================================
# 10. FROZEN SETS
# =====================================================

print("\n10. FROZEN SETS")
print("---------------")

# Create an immutable set
fixed_numbers = frozenset([10, 20, 30, 10])

print("Frozen set:", fixed_numbers)

# Frozen sets support mathematical operations
other_numbers = frozenset([30, 40, 50])

print("Frozen set union:", fixed_numbers | other_numbers)

# The following operations are not supported:
#
# fixed_numbers.add(40)
# fixed_numbers.remove(10)
#
# Both would raise AttributeError.


# =====================================================
# 11. CONVERTING BETWEEN COLLECTIONS
# =====================================================

print("\n11. COLLECTION CONVERSIONS")
print("--------------------------")

# Convert list to set
numbers_list = [10, 20, 30, 10, 20]

numbers_set = set(numbers_list)

print("List:", numbers_list)
print("Set:", numbers_set)

# Convert set to list
numbers_again = list(numbers_set)

print("Converted list:", numbers_again)

# Convert tuple to set
numbers_tuple = (10, 20, 30, 10)

tuple_set = set(numbers_tuple)

print("Tuple:", numbers_tuple)
print("Tuple converted to set:", tuple_set)


# =====================================================
# 12. SET COMPREHENSION
# =====================================================

print("\n12. SET COMPREHENSION")
print("---------------------")

numbers = [1, 2, 3, 4, 5]

# Create a set containing squares
squares = {number ** 2 for number in numbers}

print("Squares:", squares)

# Filter even numbers
even_numbers = {
    number for number in numbers
    if number % 2 == 0
}

print("Even numbers:", even_numbers)

# Duplicate results are automatically removed
values = [1, 1, 2, 2, 3, 3]

unique_squares = {number ** 2 for number in values}

print("Unique squares:", unique_squares)


# =====================================================
# 13. COPYING SETS
# =====================================================

print("\n13. COPYING SETS")
print("----------------")

a = {10, 20, 30}

# Assignment creates another reference
b = a

b.add(40)

print("Original reference a:", a)
print("Reference b:", b)

# copy() creates a separate set object
a = {10, 20, 30}

b = a.copy()

b.add(40)

print("Original set:", a)
print("Copied set:", b)


# =====================================================
# 14. PRACTICAL APPLICATION:
# STUDENT COURSE ANALYSIS
# =====================================================

print("\n14. STUDENT COURSE ANALYSIS")
print("---------------------------")

# Students enrolled in Python
python_students = {
    "Ammu",
    "Ravi",
    "John",
    "Priya",
    "David"
}

# Students enrolled in Java
java_students = {
    "Ravi",
    "John",
    "David",
    "Kiran"
}

# Find all unique students
all_students = python_students | java_students

# Find students studying both courses
both_courses = python_students & java_students

# Find students studying only Python
python_only = python_students - java_students

# Find students studying only Java
java_only = java_students - python_students

# Find students studying exactly one of the courses
one_course_only = python_students ^ java_students

print("Python students:", python_students)
print("Java students:", java_students)

print("\nCOURSE SUMMARY")
print("--------------")
print("Total unique students:", len(all_students))
print("Students in both courses:", both_courses)
print("Only Python:", python_only)
print("Only Java:", java_only)
print("Exactly one course:", one_course_only)

# Add a new Python student
python_students.add("Sarah")

print("\nAfter adding Sarah:", python_students)

# Remove a student safely
python_students.discard("Unknown")

print("After safe removal:", python_students)

# Check membership
print("Is Ammu studying Python?", "Ammu" in python_students)


# =====================================================
# END OF PROGRAM
# =====================================================

print("\nSETS PROGRAM COMPLETED")
