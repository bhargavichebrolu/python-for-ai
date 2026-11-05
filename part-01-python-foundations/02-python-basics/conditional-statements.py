# Student result evaluation

student_name = "Ammu"

python_score = 82
sql_score = 76
ml_score = 91

total_score = python_score + sql_score + ml_score
average_score = total_score / 3

print("STUDENT RESULT")
print("--------------")
print(f"Student: {student_name}")
print(f"Average: {average_score:.2f}")

# 1. Determine pass or fail
if average_score >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")

# 2. Determine grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# 3. Check whether every module was passed
all_modules_passed = (
    python_score >= 50
    and sql_score >= 50
    and ml_score >= 50
)

if all_modules_passed:
    print("All modules passed")
else:
    print("At least one module was failed")

# 4. Determine award eligibility
if average_score >= 80 and all_modules_passed:
    print("Award status: Eligible")
else:
    print("Award status: Not eligible")

# 5. Check whether optional feedback was provided
feedback = ""

if feedback:
    print(f"Feedback: {feedback}")
else:
    print("No feedback provided")