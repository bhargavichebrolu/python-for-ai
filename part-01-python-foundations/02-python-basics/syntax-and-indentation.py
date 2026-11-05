# ============================================================
# PYTHON SYNTAX, INDENTATION, AND COMMENTS
# ============================================================

# 1. Python is case-sensitive
print("Python uses lowercase print()")

language = "Python"
Language = "Java"

print("language:", language)
print("Language:", Language)


# 2. Statements and expressions
result = 10 + 5
print("10 + 5 =", result)


# 3. Indentation defines code blocks
if result > 10:
    print("The result is greater than 10")
    print("This line belongs to the same if block")

    if result == 15:
        print("This is a nested if block")
        print("It uses another indentation level")

print("This line is outside both if blocks")


# 4. Multiple statements
first_name = "Ammu"
topic = "Python syntax"

print("Name:", first_name)
print("Topic:", topic)


# 5. Comments
# This is a single-line comment.
# Python ignores comments when executing the program.

print("Comments do not appear in the output")


# 6. Continuation across multiple lines
total = (
    10
    + 20
    + 30
)

print("Total:", total)


# 7. Common syntax conventions
# Use meaningful variable names.
student_name = "Ammu"

# Use consistent indentation: 4 spaces per level.
if student_name:
    print("Student name is available")


# 8. A syntax error example — uncomment to test
# print("This line has a missing closing parenthesis"

# 9. An indentation error example — uncomment to test
# if 10 > 5:
# print("This line should be indented")