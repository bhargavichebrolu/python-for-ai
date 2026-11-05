# Tuples in Python

## 1. Introduction to Tuples

A tuple is a built-in Python data structure used to store multiple values in a single variable.

A tuple is similar to a list, but its most important characteristic is that it is immutable.

**Immutable** means that elements cannot be reassigned, added or removed after the tuple is created.

Example:

```python student = (*Ammu*, 23, *Artificial Intelligence*)

print(student) print(type(student)) ```

Output:

```text ('Ammu', 23, 'Artificial Intelligence') <class 'tuple'> ```

Tuples are useful when storing collections of values that should remain fixed.

Common applications include:

- Coordinates
- **RGB** colour values
- Fixed configuration settings
- Database-like records
- Returning multiple values from functions
- Representing fixed groups of related information

## 2. Characteristics of Tuples

Python tuples have the following characteristics:

1. **Ordered:** Elements maintain their insertion order.
2. **Immutable:** Individual elements cannot be reassigned.
3. **Duplicates allowed:** A tuple can contain repeated values.
4. **Heterogeneous:** Different data types can be stored together.
5. **Indexed:** Elements can be accessed using positive and negative indexes.
6. **Supports slicing:** A portion of a tuple can be retrieved.
7. **Nested:** A tuple can contain other tuples or other objects.

Example:

```python data = (*Python*, 23, 85.5, True, *Python*)

print(data) ```

The tuple contains multiple data types and a duplicate value.

## 3. Creating Tuples

Tuples are commonly created using parentheses `()`.

### Normal tuple

```python languages = (*Python*, *Java*, *C++*) ```

### Tuple containing integers

```python numbers = (10, 20, 30, 40) ```

### Tuple containing different data types

```python student = (*Ammu*, 23, 85.5, True) ```

### Empty tuple

```python empty_tuple = () ```

Alternatively:

```python empty_tuple = tuple() ```

### Tuple without parentheses

Python also supports tuple packing without parentheses.

```python numbers = 10, 20, 30, 40

print(type(numbers)) ```

The commas make this a tuple.

### Single-element tuple

A single-element tuple requires a trailing comma.

```python value = (10,)

print(type(value)) ```

Output:

```text <class 'tuple'> ```

Without the comma:

```python value = (10)

print(type(value)) ```

Output:

```text <class 'int'> ```

The parentheses alone do not create a tuple. The comma is what makes the value a tuple.

## 4. Ordered Property

Tuples preserve the order in which elements are inserted.

```python languages = (*Python*, *Java*, *C++*)

print(languages) ```

Output:

```text ('Python', 'Java', 'C++') ```

The order remains fixed because tuple elements cannot be reassigned.

## 5. Duplicate Elements

Tuples allow duplicate values.

```python numbers = (10, 20, 10, 30, 20)

print(numbers) ```

Output:

```text (10, 20, 10, 30, 20) ```

Unlike sets, tuples do not automatically remove duplicate elements.

## 6. Accessing Tuple Elements Using Indexing

Python uses zero-based indexing.

```python languages = (*Python*, *Java*, *C++*, *SQL*)

print(languages[0])  # Python print(languages[1])  # Java print(languages[2])  # C++ print(languages[3])  # **SQL** ```

### Negative indexing

Negative indexing accesses elements from the end.

```python languages = (*Python*, *Java*, *C++*, *SQL*)

print(languages[-1])  # **SQL** print(languages[-2])  # C++ print(languages[-3])  # Java print(languages[-4])  # Python ```

### IndexError

Accessing an index that does not exist raises an `IndexError`.

```python numbers = (10, 20, 30)

# numbers[5]  # IndexError

```

## 7. Tuple Slicing

Slicing retrieves a portion of a tuple.

Syntax:

```python tuple_name[start:stop:step] ```

- `start`: Starting index, included.
- `stop`: Ending index, excluded.
- `step`: Number of positions to move between elements.

Example:

```python languages = (*Python*, *Java*, *C++*, *SQL*, *JavaScript*)

print(languages[1:4]) ```

Output:

```text ('Java', 'C++', '**SQL**') ```

### Different slicing operations

```python languages = (*Python*, *Java*, *C++*, *SQL*, *JavaScript*)

print(languages[:3])    # First three elements print(languages[2:])    # From index 2 to the end print(languages[1:4])   # Indexes 1, 2 and 3 print(languages[::2])   # Every second element print(languages[::-1])  # Reversed tuple copy ```

Slicing creates a new tuple. It does not modify the original tuple.

## 8. Tuples Are Immutable

Immutability is the most important property of tuples.

After a tuple is created, its elements cannot be reassigned.

Example:

```python numbers = (10, 20, 30)

# This raises TypeError:

# numbers[1] = 50 ```

Python raises:

```text TypeError: 'tuple' object does not support item assignment ```

You cannot directly:

- Change an individual element.
- Append an element.
- Insert an element.
- Remove an element.

However, you can create a new tuple using existing values.

```python numbers = (10, 20, 30)

new_numbers = numbers + (40, 50)

print(new_numbers) ```

Output:

```text (10, 20, 30, 40, 50) ```

The original tuple remains unchanged.

## 9. Tuple Methods

Tuples have only two main built-in methods because they cannot be modified.

### 9.1 count()

Returns the number of times a specified value appears.

```python scores = (80, 90, 80, 75, 80)

print(scores.count(80)) ```

Output:

```text 3 ```

### 9.2 index()

Returns the index of the first occurrence of a specified value.

```python languages = (*Python*, *Java*, *C++*, *Java*)

print(languages.index(*Java*)) ```

Output:

```text 1 ```

If the value does not exist, `index()` raises a `ValueError`.

## 10. Built-in Functions with Tuples

Several Python built-in functions work with tuples.

```python scores = (85, 90, 76, 88)

print(len(scores)) print(min(scores)) print(max(scores)) print(sum(scores)) ```

Output:

```text 4 76 90 **339** ```

| Function | Purpose |
|---|---|
| `len()` | Returns the number of elements |
| `min()` | Returns the smallest element |
| `max()` | Returns the largest element |
| `sum()` | Calculates the total of numeric elements |
| `sorted()` | Returns a new sorted list |

Important: `sorted()` returns a list, not a tuple.

Example:

```python numbers = (30, 10, 20)

result = sorted(numbers)

print(result) print(type(result)) ```

Output:

```text [10, 20, 30] <class 'list'> ```

To convert the result back into a tuple:

```python sorted_tuple = tuple(sorted(numbers)) ```

## 11. Membership Operators

Use `in` and `not in` to check whether an element exists.

```python languages = (*Python*, *Java*, *C++*)

print(*Python* in languages) print(*JavaScript* in languages) print(*JavaScript* not in languages) ```

Output:

```text True False True ```

## 12. Tuple Concatenation

The `+` operator combines tuples.

```python first = (10, 20) second = (30, 40)

combined = first + second

print(combined) ```

Output:

```text (10, 20, 30, 40) ```

Concatenation creates a new tuple. It does not modify either original tuple.

## 13. Tuple Repetition

The `*` operator repeats the elements of a tuple.

```python numbers = (1, 2)

result = numbers * 3

print(result) ```

Output:

```text (1, 2, 1, 2, 1, 2) ```

The original tuple remains unchanged.

## 14. Tuple Packing

Tuple packing means grouping multiple values into one tuple.

```python student = *Ammu*, 23, *Artificial Intelligence*

print(student) ```

Python automatically creates a tuple containing the three values.

## 15. Tuple Unpacking

Tuple unpacking assigns individual tuple elements to separate variables.

```python student = (*Ammu*, 23, *Artificial Intelligence*)

name, age, course = student

print(name) print(age) print(course) ```

Output:

```text Ammu 23 ### Artificial Intelligence ```

The number of target variables normally needs to match the number of tuple elements.

### Extended unpacking

The `*` operator can collect multiple elements into a list.

```python numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first) print(middle) print(last) ```

Output:

```text 10 [20, 30, 40] 50 ```

The middle values are collected into a list.

## 16. Swapping Variables Using Tuple Unpacking

Python allows two variables to be swapped without using a temporary variable.

```python a = 10 b = 20

a, b = b, a

print(a) print(b) ```

Output:

```text 20 10 ```

Python evaluates the right-hand side and then assigns the values to the left-hand variables.

## 17. Nested Tuples

A tuple can contain other tuples.

```python
students = (
    (*Ammu*, 85),
    (*Ravi*, 90),
    (*John*, 76)
)
```

Access nested elements:

```python print(students[0]) print(students[0][0]) print(students[0][1]) ```

Output:

```text ('Ammu', 85) Ammu 85 ```

The first index selects the inner tuple. The second index selects an element within that tuple.

## 18. Mutable Objects Inside Tuples

A tuple is immutable, but it can contain a mutable object such as a list.

```python data = ([10, 20], 30)

data[0].append(40)

print(data) ```

Output:

```text ([10, 20, 40], 30) ```

Why does this work?

The tuple's references cannot be reassigned, but the list referenced by the first element is mutable.

This distinction is important:

- `data[0] = [10, 20, 40]` is not allowed.
- `data[0].append(40)` is allowed because it modifies the contained list.

Tuple immutability is not automatically recursive.

## 19. Tuple References and Identity

Assigning a tuple to another variable creates another reference to the same tuple object.

```python a = (10, 20, 30)

b = a

print(a is b) ```

Output:

```text True ```

Both variables refer to the same object.

Because tuples are immutable, sharing the same tuple is generally safe from accidental element modification.

## 20. Converting Between Lists and Tuples

Python allows conversion between lists and tuples.

### Tuple to list

```python numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list) ```

Output:

```text [10, 20, 30] ```

The resulting list is mutable.

### List to tuple

```python numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

print(numbers_tuple) ```

Output:

```text (10, 20, 30) ```

The resulting tuple is immutable.

These conversions are useful when data needs to be modified temporarily or represented as a fixed collection.

## 21. Why Use Tuples?

Tuples are useful when values should be grouped together and should not be individually reassigned.

### Coordinates

```python location = (51.**5072**, -0.**1276**) ```

### RGB colour values

```python red = (**255**, 0, 0) ```

### Fixed employee records

```python employee = (**101**, *John*, *Software Engineer*) ```

### Image dimensions

```python image_size = (**224**, **224**) ```

### Returning multiple values from functions

```python
def calculate_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)

    return total, average

result = calculate_statistics([10, 20, 30])

print(result) ```

The function returns a tuple containing the total and average.

## 22. When Not to Use Tuples

Avoid tuples when:

- You need to add or remove elements frequently.
- You need to update individual elements.
- The collection changes regularly.
- You need key-based access to meaningful values.

In those situations, lists or dictionaries may be more suitable.

## 23. Complete Practical Program

See the companion file `tuples.py` for a fully commented executable program covering:

- Tuple creation
- Empty and single-element tuples
- Indexing and negative indexing
- Slicing
- Immutability
- Tuple methods
- Built-in functions
- Membership
- Concatenation and repetition
- Packing and unpacking
- Extended unpacking
- Swapping variables
- Nested tuples
- Mutable objects inside tuples
- Tuple references
- List and tuple conversions
- Student record analysis

## 24. Summary

| Concept | Important detail |
|---|---|
| Tuple syntax | `()` |
| Mutable | No |
| Ordered | Yes |
| Duplicates | Allowed |
| Indexing | Supported |
| Slicing | Supported |
| Add elements | No direct modification |
| Remove elements | No direct modification |
| Main methods | `count()`, `index()` |
| Packing | Group values into a tuple |
| Unpacking | Assign tuple elements to variables |
| Concatenation | `+` |
| Repetition | `*` |
| Convert to list | `list()` |
| Convert from list | `tuple()` |
| Nested tuples | Supported |
| Single-element tuple | Requires a trailing comma |

Tuples are important when representing fixed collections of related values. Understanding immutability, tuple packing, unpacking and the difference between tuples and lists is essential for writing reliable Python programs.