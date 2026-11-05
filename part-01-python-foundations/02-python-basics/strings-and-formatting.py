# ==========================================
# PYTHON STRINGS: COMPLETE PRACTICE PROGRAM
# ==========================================

# 1. Creating strings
text = "Python Programming"

print("Original string:", text)


# 2. Indexing
print("\n--- Indexing ---")
print("First character:", text[0])
print("Fourth character:", text[3])
print("Last character:", text[-1])
print("Second-last character:", text[-2])


# 3. Slicing
print("\n--- Slicing ---")
print("First six characters:", text[:6])
print("Characters from index 7:", text[7:])
print("Indexes 0 to 5:", text[0:6])
print("Last three characters:", text[-3:])
print("Every second character:", text[::2])
print("Reversed string:", text[::-1])


# 4. String methods
print("\n--- String methods ---")

messy_text = "   Python Programming   "

print("lower():", text.lower())
print("upper():", text.upper())

print("strip():", messy_text.strip())
print("lstrip():", messy_text.lstrip())
print("rstrip():", messy_text.rstrip())

print("replace():", text.replace("Python", "AI"))
print("find():", text.find("Programming"))
print("count():", text.count("m"))

print("startswith():", text.startswith("Python"))
print("endswith():", text.endswith("Programming"))

words = text.split()
print("split():", words)

joined_text = " ".join(words)
print("join():", joined_text)


# 5. Strings are immutable
print("\n--- Immutability ---")

language = "Python"

language.upper()
print("After calling upper without assignment:", language)

language = language.upper()
print("After assigning the result:", language)


# 6. Concatenation
print("\n--- Concatenation ---")

first = "Machine"
second = "Learning"

combined = first + " " + second

print("Combined:", combined)


# 7. Repetition
print("\n--- Repetition ---")

print("Repeat:", "AI " * 3)
print("Separator:", "-" * 30)


# 8. Type conversion
print("\n--- Type conversion ---")

age = 25

message = "Age: " + str(age)
print(message)


# 9. f-strings
print("\n--- f-strings ---")

name = "Ammu"
score = 95.6789
accuracy = 0.9567
total = 1234567

print(f"My name is {name}.")
print(f"Score: {score:.2f}")
print(f"Accuracy: {accuracy:.2%}")
print(f"Total: {total:,}")
print(f"Calculation: {10} + {5} = {10 + 5}")


# 10. Formatting alignment
print("\n--- Alignment ---")

label = "Python"

print(f"|{label:<10}|")
print(f"|{label:>10}|")
print(f"|{label:^10}|")