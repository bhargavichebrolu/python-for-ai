
# ============================================================
# PYTHON DICTIONARIES
# Complete practical reference program
# ============================================================


# ------------------------------------------------------------
# 1. CREATING DICTIONARIES
# ------------------------------------------------------------

student = {
    "name": "Ammu",
    "age": 23,
    "course": "Artificial Intelligence",
    "marks": 90
}

print("1. ORIGINAL DICTIONARY")
print(student)

# Creating an empty dictionary
empty_dictionary = {}

# Creating a dictionary using dict()
employee = dict(name="Ravi", age=25, department="IT")

print(empty_dictionary)
print(employee)


# ------------------------------------------------------------
# 2. ACCESSING VALUES
# ------------------------------------------------------------

print("\n2. ACCESSING VALUES")

print("Name:", student["name"])
print("Age:", student.get("age"))

# get() returns a default if the key does not exist
print("City:", student.get("city", "Not available"))

# Square brackets with a missing key would raise KeyError.
# print(student["city"])


# ------------------------------------------------------------
# 3. ADDING AND UPDATING ITEMS
# ------------------------------------------------------------

print("\n3. ADDING AND UPDATING")

# Add a new key-value pair
student["city"] = "London"

# Update an existing value
student["marks"] = 95

# Update multiple items
student.update({
    "age": 24,
    "university": "UEL"
})

print(student)


# ------------------------------------------------------------
# 4. REMOVING ITEMS
# ------------------------------------------------------------

print("\n4. REMOVING ITEMS")

temporary_data = {
    "name": "Ravi",
    "age": 25,
    "city": "London"
}

# pop() removes a specified key and returns its value
removed_age = temporary_data.pop("age")
print("Removed age:", removed_age)

# popitem() removes the last inserted key-value pair
removed_pair = temporary_data.popitem()
print("Removed pair:", removed_pair)

# del removes a specified item
del temporary_data["name"]

print("After removals:", temporary_data)

# clear() removes all items
temporary_data.clear()
print("After clear:", temporary_data)


# ------------------------------------------------------------
# 5. KEYS, VALUES AND ITEMS
# ------------------------------------------------------------

print("\n5. KEYS, VALUES AND ITEMS")

student = {
    "name": "Ammu",
    "age": 23,
    "marks": 95
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# ------------------------------------------------------------
# 6. ITERATING THROUGH A DICTIONARY
# ------------------------------------------------------------

print("\n6. ITERATING")

# Iterating through keys
for key in student:
    print("Key:", key)

# Iterating through values
for value in student.values():
    print("Value:", value)

# Iterating through both keys and values
for key, value in student.items():
    print(key, "=", value)


# ------------------------------------------------------------
# 7. CHECKING KEY AND VALUE EXISTENCE
# ------------------------------------------------------------

print("\n7. MEMBERSHIP")

print("name" in student)  # Checks keys
print("city" in student)

print(95 in student.values())  # Checks values


# ------------------------------------------------------------
# 8. DICTIONARY LENGTH
# ------------------------------------------------------------

print("\n8. LENGTH")

print("Number of items:", len(student))


# ------------------------------------------------------------
# 9. DICTIONARY COMPREHENSION
# ------------------------------------------------------------

print("\n9. DICTIONARY COMPREHENSION")

numbers = [1, 2, 3, 4, 5, 6]

# Create a dictionary of numbers and their squares
squares = {
    number: number ** 2
    for number in numbers
}

print("Squares:", squares)

# Create a dictionary containing only even numbers
even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# ------------------------------------------------------------
# 10. NESTED DICTIONARIES
# ------------------------------------------------------------

print("\n10. NESTED DICTIONARIES")

students = {
    "student1": {
        "name": "Ammu",
        "marks": 95
    },
    "student2": {
        "name": "Ravi",
        "marks": 85
    }
}

# Access nested values
print(students["student1"]["name"])
print(students["student2"]["marks"])

# Update a nested value
students["student1"]["marks"] = 98

print(students)


# ------------------------------------------------------------
# 11. DUPLICATE KEYS
# ------------------------------------------------------------

print("\n11. DUPLICATE KEYS")

duplicate_example = {
    "name": "Ammu",
    "age": 22,
    "age": 23
}

# The later value replaces the earlier value.
print(duplicate_example)


# ------------------------------------------------------------
# 12. DICTIONARY COPYING
# ------------------------------------------------------------

print("\n12. COPYING DICTIONARIES")

original = {
    "name": "Ammu",
    "marks": [80, 90]
}

# Assignment creates another reference to the same object.
reference = original

reference["name"] = "Ravi"

print("Original after reference modification:", original)

# copy() creates a shallow copy.
shallow_copy = original.copy()

shallow_copy["name"] = "Kiran"

print("Original:", original)
print("Shallow copy:", shallow_copy)

# Nested lists are still shared in a shallow copy.
shallow_copy["marks"].append(95)

print("Original nested list:", original["marks"])
print("Shallow copy nested list:", shallow_copy["marks"])

# deepcopy() also copies nested mutable objects.
import copy

deep_copy = copy.deepcopy(original)

deep_copy["marks"].append(100)

print("Original after deep copy modification:", original["marks"])
print("Deep copy nested list:", deep_copy["marks"])


# ------------------------------------------------------------
# 13. SETDEFAULT
# ------------------------------------------------------------

print("\n13. SETDEFAULT")

profile = {"name": "Ammu"}

# Inserts age because the key does not exist.
profile.setdefault("age", 23)

# Does not replace name because it already exists.
profile.setdefault("name", "Ravi")

print(profile)


# ------------------------------------------------------------
# 14. FROMKEYS
# ------------------------------------------------------------

print("\n14. FROMKEYS")

subjects = ["Python", "Java", "SQL"]

subject_status = dict.fromkeys(subjects, "Not started")

print(subject_status)


# ------------------------------------------------------------
# 15. MERGING DICTIONARIES
# ------------------------------------------------------------

print("\n15. MERGING")

personal_details = {
    "name": "Ammu",
    "age": 23
}

academic_details = {
    "course": "Artificial Intelligence",
    "university": "UEL"
}

# update() modifies the first dictionary.
merged_using_update = personal_details.copy()
merged_using_update.update(academic_details)

print("Using update():", merged_using_update)

# | creates a new merged dictionary (Python 3.9+).
merged_using_operator = personal_details | academic_details

print("Using |:", merged_using_operator)


# ------------------------------------------------------------
# 16. PRACTICAL EXAMPLE: WORD FREQUENCY
# ------------------------------------------------------------

print("\n16. WORD FREQUENCY")

words = [
    "AI",
    "Python",
    "AI",
    "Machine Learning",
    "Python",
    "AI"
]

frequency = {}

for word in words:
    # get() returns 0 if the word is not already present.
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)


# ------------------------------------------------------------
# 17. PRACTICAL EXAMPLE: STUDENT MARKS ANALYSIS
# ------------------------------------------------------------

print("\n17. STUDENT MARKS ANALYSIS")

student_marks = {
    "Ammu": 92,
    "Ravi": 85,
    "Kiran": 78,
    "Priya": 96
}

# Calculate the average mark.
total_marks = sum(student_marks.values())
number_of_students = len(student_marks)

average = total_marks / number_of_students

print("Average marks:", average)

# Find the student with the highest marks.
top_student = max(student_marks, key=student_marks.get)

print("Top student:", top_student)
print("Highest marks:", student_marks[top_student])

# Identify students who scored at least 90.
high_scorers = {
    name: marks
    for name, marks in student_marks.items()
    if marks >= 90
}

print("High scorers:", high_scorers)


# ============================================================
# END OF DICTIONARIES PROGRAM
# ============================================================
