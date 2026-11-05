
# Conditional Statements in Python

## 1. What are conditional statements?

Conditional statements allow a program to make decisions based on whether a condition evaluates to `True` or `False`.

For example:

```python
score = 72

if score >= 50:
    print("Passed")
```

Python evaluates `score >= 50`. Since the expression is `True`, Python executes the indented block.

## 2. The `if` statement

Syntax:

```python
if condition:
    # code executes when condition is True
```

Example:

```python
temperature = 28

if temperature > 25:
    print("It is warm")
```

The condition is evaluated first. If it is true, the indented statements execute. If false, Python skips the block.

### Indentation

Indentation defines which statements belong to a conditional block.

```python
if temperature > 25:
    print("It is warm")
    print("Wear light clothing")

print("Program finished")
```

The first two `print()` statements belong to the `if` block. The final statement is outside it and executes regardless of the condition.

Python conventionally uses four spaces for each indentation level.

## 3. The `else` statement

`else` executes when the preceding `if` condition is false.

```python
score = 42

if score >= 50:
    print("Passed")
else:
    print("Failed")
```

Python executes one of the two blocks.

## 4. The `elif` statement

`elif` means “else if.” It allows multiple conditions to be checked in order.

```python
score = 82

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade below C")
```

Python evaluates conditions from top to bottom. Once one condition is true, its block executes and the remaining branches are skipped.

### Condition order matters

Incorrect ordering:

```python
score = 95

if score >= 70:
    print("Grade C")
elif score >= 80:
    print("Grade B")
elif score >= 90:
    print("Grade A")
```

This prints `Grade C`, because `95 >= 70` is already true.

For this grading example, check the highest threshold first.

## 5. Combining conditions with logical operators

### `and`

Both conditions must be true.

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

If either condition is false, the combined expression is false.

### `or`

At least one condition must be true.

```python
is_student = False
has_discount_code = True

if is_student or has_discount_code:
    print("Discount available")
```

### `not`

Reverses a Boolean condition.

```python
is_blocked = False

if not is_blocked:
    print("Account access allowed")
```

Since `not False` is `True`, the block executes.

## 6. Truthy and falsy values

Python can evaluate values directly in conditions without an explicit comparison.

Common falsy values include:

```python
False
None
0
0.0
""
[]
{}
set()
```

Most other values are truthy, including non-empty strings and collections.

Example:

```python
username = ""

if username:
    print("Username provided")
else:
    print("Username is empty")
```

An empty string is falsy, so the `else` block executes.

A non-empty list is truthy:

```python
items = ["Python", "SQL"]

if items:
    print("There are items")
```

## 7. Complete example: Student result evaluation

```python
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

# Determine pass or fail
if average_score >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")

# Determine grade
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

# Check whether every module was passed
all_modules_passed = (
    python_score >= 50
    and sql_score >= 50
    and ml_score >= 50
)

if all_modules_passed:
    print("All modules passed")
else:
    print("At least one module was failed")

# Determine award eligibility
if average_score >= 80 and all_modules_passed:
    print("Award status: Eligible")
else:
    print("Award status: Not eligible")

# Check whether optional feedback was provided
feedback = ""

if feedback:
    print(f"Feedback: {feedback}")
else:
    print("No feedback provided")
```

## Key points

- `if` executes a block when its condition is true.
- `else` handles the false case.
- `elif` checks another condition if previous conditions were false.
- Python checks conditional branches from top to bottom.
- Indentation determines which statements belong to a block.
- `and` requires every condition to be true.
- `or` requires at least one condition to be true.
- `not` reverses a Boolean value.
- Empty strings and empty collections are falsy.
- Non-empty strings and collections are truthy.
