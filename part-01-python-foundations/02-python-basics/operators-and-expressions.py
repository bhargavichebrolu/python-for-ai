# Student performance analysis using Python operators

student_name = "Ammu"

python_score = 82
sql_score = 76
ml_score = 91

# 1. Arithmetic operators
total_score = python_score + sql_score + ml_score
average_score = total_score / 3
whole_number_average = total_score // 3
remainder = total_score % 3

print("STUDENT PERFORMANCE")
print("-------------------")
print(f"Student: {student_name}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Floor average: {whole_number_average}")
print(f"Remainder after dividing total by 3: {remainder}")

# 2. Comparison operators
passed = average_score >= 50
high_performer = average_score >= 80

print(f"\nPassed: {passed}")
print(f"High performer: {high_performer}")

# 3. Logical operators
all_modules_passed = (
    python_score >= 50
    and sql_score >= 50
    and ml_score >= 50
)

eligible_for_award = (
    average_score >= 80
    and all_modules_passed
)

print(f"All modules passed: {all_modules_passed}")
print(f"Eligible for award: {eligible_for_award}")

# 4. Assignment operators
bonus_points = 0
bonus_points += 5
bonus_points += 3

final_score = total_score
final_score += bonus_points

print(f"\nBonus points: {bonus_points}")
print(f"Final total after bonus: {final_score}")

# 5. Membership operators
modules = ["Python", "SQL", "Machine Learning"]

print(f"\nPython is a module: {'Python' in modules}")
print(f"Java is not a module: {'Java' not in modules}")

# 6. Identity operators
feedback = None

print(f"\nFeedback is missing: {feedback is None}")

# 7. Operator precedence
calculation = 10 + 5 * 2
calculation_with_parentheses = (10 + 5) * 2

print(f"\nWithout parentheses: {calculation}")
print(f"With parentheses: {calculation_with_parentheses}")