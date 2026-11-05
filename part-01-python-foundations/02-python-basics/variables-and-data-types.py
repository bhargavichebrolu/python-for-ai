# ============================================================
# PYTHON VARIABLES AND DATA TYPES
# ============================================================

# 1. Assigning values to variables
student_name = "Ammu"
age = 25
height = 1.65
is_learning_python = True
middle_name = None

print("Student:", student_name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning_python)
print("Middle name:", middle_name)


# 2. Checking data types
print("\n--- Data Types ---")

print(type(student_name))
print(type(age))
print(type(height))
print(type(is_learning_python))
print(type(middle_name))


# 3. Dynamic typing
print("\n--- Dynamic Typing ---")

value = 100
print(value, type(value))

value = "Now I am a string"
print(value, type(value))


# 4. Reassigning variables
print("\n--- Reassignment ---")

score = 80
print("Original score:", score)

score = 95
print("Updated score:", score)


# 5. Variable naming
print("\n--- Variable Naming ---")

student_name = "Ammu"
total_marks = 450
model_accuracy = 0.95

print(student_name)
print(total_marks)
print(model_accuracy)


# 6. Type conversion
print("\n--- Type Conversion ---")

age_text = "25"
age_number = int(age_text)

price = 12
price_decimal = float(price)

number = 100
number_text = str(number)

print(age_text, type(age_text))
print(age_number, type(age_number))

print(price, type(price))
print(price_decimal, type(price_decimal))

print(number, type(number))
print(number_text, type(number_text))


# 7. Boolean conversion
print("\n--- Boolean Conversion ---")

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))


# 8. Checking types with isinstance()
print("\n--- Type Checking ---")

print(isinstance(age_number, int))
print(isinstance(student_name, str))
print(isinstance(model_accuracy, float))


# 9. Invalid conversion example
# Uncomment this line to see a ValueError:
# invalid_number = int("hello")