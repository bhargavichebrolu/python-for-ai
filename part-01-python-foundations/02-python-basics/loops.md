
# Loops in Python

## 1. What are loops?

Loops allow a program to execute a block of code repeatedly without writing the same statements multiple times.

Python provides two main loops:

- `for` loop
- `while` loop

## 2. The `for` loop

A `for` loop iterates over an iterable, such as a list, string, tuple, or range.

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

Output:

```text
Python
Java
C++
```

Python takes each item from the list, assigns it to the loop variable, and executes the indented block.

### Iterating over a string

Strings are iterable. A `for` loop can process one character at a time.

```python
word = "AI"

for character in word:
    print(character)
```

Output:

```text
A
I
```

## 3. The `range()` function

`range()` generates a sequence of integers. It is commonly used to control the number of loop iterations.

### `range(stop)`

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

The sequence starts at zero and excludes the stop value.

### `range(start, stop)`

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

The start value is included, while the stop value is excluded.

### `range(start, stop, step)`

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

The step determines the increment between values.

A negative step can generate values in descending order:

```python
for number in range(5, 0, -1):
    print(number)
```

Output:

```text
5
4
3
2
1
```

## 4. The `while` loop

A `while` loop repeats a block of code as long as its condition remains true.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

Python checks the condition before each iteration. When the condition becomes false, the loop terminates.

### Infinite loops

An infinite loop occurs when the stopping condition never becomes false.

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes, so the condition remains true.

Always ensure that a `while` loop has a valid stopping condition.

## 5. The `break` statement

`break` immediately terminates the nearest enclosing loop.

```python
for number in range(1, 10):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

When the number reaches five, the loop terminates.

## 6. The `continue` statement

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

The number three is skipped.

### Difference between `break` and `continue`

| Statement | Behaviour |
|---|---|
| `break` | Terminates the loop completely |
| `continue` | Skips only the current iteration |

## 7. Combining loops and conditional statements

Loops can process collections while conditional statements make decisions about each item.

```python
scores = [82, 45, 91, 67, 38]

for score in scores:
    if score >= 50:
        print(f"{score}: Passed")
    else:
        print(f"{score}: Failed")
```

Output:

```text
82: Passed
45: Failed
91: Passed
67: Passed
38: Failed
```

This is a fundamental pattern for processing datasets.

## 8. Complete example: Student score analysis

```python
student_scores = [82, 45, 91, 67, 38, 76]

total_score = 0
passed_count = 0
failed_count = 0

print("STUDENT SCORE ANALYSIS")
print("----------------------")

for score in student_scores:
    total_score += score

    if score >= 50:
        passed_count += 1
        print(f"{score}: Passed")
    else:
        failed_count += 1
        print(f"{score}: Failed")

number_of_students = len(student_scores)
average_score = total_score / number_of_students

print("\nSUMMARY")
print("-------")
print(f"Number of students: {number_of_students}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

print("\nChecking for a score below 40:")

for score in student_scores:
    if score < 40:
        print(f"Found a score below 40: {score}")
        break

print("\nCounting with while:")

count = 1

while count <= 5:
    print(count)
    count += 1
```

## 9. Key points

- `for` iterates over items in an iterable.
- `while` repeats while a condition is true.
- `range()` generates integer sequences.
- The stop value in `range()` is excluded.
- `break` terminates a loop.
- `continue` skips the current iteration.
- A `while` loop needs a stopping condition.
- Loops and conditions can be combined to process datasets.
