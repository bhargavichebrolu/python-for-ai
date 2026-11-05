# Student score analysis using loops

student_scores = [82, 45, 91, 67, 38, 76]

total_score = 0
passed_count = 0
failed_count = 0

print("STUDENT SCORE ANALYSIS")
print("----------------------")

# Process each score
for score in student_scores:
    total_score += score

    if score >= 50:
        passed_count += 1
        print(f"{score}: Passed")
    else:
        failed_count += 1
        print(f"{score}: Failed")

# Calculate average
number_of_students = len(student_scores)
average_score = total_score / number_of_students

print("\nSUMMARY")
print("-------")
print(f"Number of students: {number_of_students}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

# Find the first score below 40
print("\nChecking for a score below 40:")

for score in student_scores:
    if score < 40:
        print(f"Found a score below 40: {score}")
        break

# Print numbers from 1 to 5 using while
print("\nCounting with while:")

count = 1

while count <= 5:
    print(count)
    count += 1