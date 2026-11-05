# Sets in Python

## 1. Introduction to Sets

A set is a built-in Python data structure used to store multiple unique elements in a single variable.

The most important characteristic of a set is that it does not allow duplicate elements.

Example:

```python
numbers = {10, 20, 30, 10, 20}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

Python automatically removes duplicate values when creating the set.

Sets are useful in:

- Removing duplicate records.
- Finding unique values in datasets.
- Comparing two collections.
- Finding common elements.
- Finding elements that exist in one collection but not another.
- Data cleaning and preprocessing.
- Membership checking.

## 2. Characteristics of Sets

Python sets have the following characteristics:

1. **Unique elements:** Duplicate elements are automatically removed.
2. **Mutable:** Elements can be added and removed.
3. **Unordered:** Sets do not guarantee insertion order.
4. **No indexing:** Elements cannot be accessed using numerical indexes.
5. **Heterogeneous:** Different hashable data types can be stored together.
6. **Dynamic:** Elements can be added or removed during execution.
7. **No mutable elements:** Lists, dictionaries and ordinary sets cannot be elements of another set because they are unhashable.

Example:

```python
data = {10, "Python", 20.5, True}

print(data)
```

A set can contain different hashable data types.

However, a list cannot be inserted directly into a set.

```python
# Invalid:
# data = {[10, 20], 30}
```

This raises a `TypeError` because lists are mutable and unhashable.

## 3. Creating Sets

Sets are normally created using curly brackets `{}`.

### Set containing integers

```python
numbers = {10, 20, 30, 40}
```

### Set containing strings

```python
languages = {"Python", "Java", "C++"}
```

### Set containing different data types

```python
data = {"Ammu", 23, 85.5, True}
```

### Set containing duplicates

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Duplicates are automatically removed.

### Creating an empty set

This is an important distinction:

```python
empty_set = set()
```

Using `{}` does not create an empty set.

```python
empty_dictionary = {}
```

Python interprets `{}` as an empty dictionary.

Therefore:

- `set()` creates an empty set.
- `{}` creates an empty dictionary.

### Using the set constructor

The `set()` constructor converts an iterable into a set.

```python
numbers = set([10, 20, 30, 10])

print(numbers)
```

Output:

```text
{10, 20, 30}
```

## 4. Unique Elements and Duplicate Removal

Sets automatically remove duplicates.

Example:

```python
student_records = [
    "Ammu",
    "Ravi",
    "John",
    "Ammu",
    "Ravi"
]

unique_students = set(student_records)

print(unique_students)
```

The resulting set contains each unique student name only once.

This is useful when processing datasets that contain repeated records.

Important: Converting a list to a set does not preserve the original list's ordering.

If order matters, a different deduplication approach may be required.

## 5. Unordered Property

Sets do not guarantee insertion order.

```python
numbers = {30, 10, 20}

print(numbers)
```

Do not rely on the displayed order of set elements.

Sets do not support positional indexing.

```python
numbers = {10, 20, 30}

# numbers[0]  # TypeError
```

If you need positional access, convert the set to a list:

```python
numbers_list = list(numbers)
```

However, the resulting list's order should not be treated as the original insertion order of the set.

## 6. Adding Elements to Sets

Python provides two commonly used methods for adding elements.

### 6.1 add()

`add()` inserts one element into the set.

```python
languages = {"Python", "Java"}

languages.add("C++")

print(languages)
```

If the element already exists, no duplicate is created.

```python
languages.add("Python")

print(languages)
```

The set remains unchanged.

### 6.2 update()

`update()` adds multiple elements from an iterable.

```python
languages = {"Python", "Java"}

languages.update(["C++", "JavaScript"])

print(languages)
```

The elements are inserted individually.

You can update a set using another set, a list or another iterable.

Example:

```python
first = {10, 20}
second = {30, 40}

first.update(second)

print(first)
```

### add() vs update()

| Method | Purpose |
|---|---|
| `add(x)` | Adds one element |
| `update(iterable)` | Adds multiple elements from an iterable |

## 7. Removing Elements from Sets

Python provides several methods to remove elements.

### 7.1 remove()

`remove()` deletes a specified element.

```python
languages = {"Python", "Java", "C++"}

languages.remove("Java")

print(languages)
```

If the element does not exist, Python raises a `KeyError`.

### 7.2 discard()

`discard()` also removes a specified element.

```python
languages = {"Python", "Java", "C++"}

languages.discard("JavaScript")

print(languages)
```

Unlike `remove()`, `discard()` does not raise an error if the element is missing.

### 7.3 pop()

`pop()` removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
```

Do not assume which element will be removed.

### 7.4 clear()

`clear()` removes all elements.

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

Output:

```text
set()
```

### Removal comparison

| Method | Behaviour |
|---|---|
| `remove(x)` | Removes x; raises `KeyError` if missing |
| `discard(x)` | Removes x; does nothing if missing |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |

## 8. Set Operations

Set operations are one of the most important features of Python sets.

They are based on mathematical set theory.

Suppose we have two sets:

```python
python_students = {"Ammu", "Ravi", "John", "Priya"}

java_students = {"Ravi", "John", "David", "Kiran"}
```

We can compare the two collections using set operations.

### 8.1 Union

Union combines all unique elements from both sets.

Operator: `|`

```python
python_students = {"Ammu", "Ravi", "John"}

java_students = {"Ravi", "John", "David"}

all_students = python_students | java_students

print(all_students)
```

Conceptual result:

```text
{'Ammu', 'Ravi', 'John', 'David'}
```

Equivalent method:

```python
all_students = python_students.union(java_students)
```

Union removes duplicates automatically.

### 8.2 Intersection

Intersection returns only the elements that exist in both sets.

Operator: `&`

```python
common_students = python_students & java_students

print(common_students)
```

Conceptual result:

```text
{'Ravi', 'John'}
```

Equivalent method:

```python
common_students = python_students.intersection(java_students)
```

### 8.3 Difference

Difference returns elements that exist in the first set but not the second.

Operator: `-`

```python
python_only = python_students - java_students

print(python_only)
```

Conceptual result:

```text
{'Ammu'}
```

Equivalent method:

```python
python_only = python_students.difference(java_students)
```

The order matters.

```python
java_only = java_students - python_students
```

Conceptual result:

```text
{'David'}
```

`A - B` and `B - A` can produce different results.

### 8.4 Symmetric Difference

Symmetric difference returns elements that exist in either set but not in both.

Operator: `^`

```python
different_students = python_students ^ java_students

print(different_students)
```

Conceptual result:

```text
{'Ammu', 'David'}
```

Equivalent method:

```python
different_students = python_students.symmetric_difference(java_students)
```

### Set operations comparison

| Operation | Operator | Purpose |
|---|---|---|
| Union | `\|` | All unique elements from both sets |
| Intersection | `&` | Common elements |
| Difference | `-` | Elements in first set but not second |
| Symmetric difference | `^` | Elements that are not common |

## 9. Membership Operators

Use `in` and `not in` to check whether an element exists.

```python
languages = {"Python", "Java", "C++"}

print("Python" in languages)
print("JavaScript" in languages)
print("JavaScript" not in languages)
```

Output:

```text
True
False
True
```

Membership checking is generally efficient with sets, particularly for larger collections.

## 10. Set Relationships

Python provides methods to check relationships between sets.

### 10.1 issubset()

Checks whether every element of one set exists in another set.

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

Output:

```text
True
```

Equivalent operator: `<=`

```python
print(a <= b)
```

### 10.2 issuperset()

Checks whether one set contains every element of another set.

```python
print(b.issuperset(a))
```

Output:

```text
True
```

Equivalent operator: `>=`

```python
print(b >= a)
```

### 10.3 isdisjoint()

Checks whether two sets have no elements in common.

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

Output:

```text
True
```

## 11. Frozen Sets

A `frozenset` is an immutable version of a set.

Example:

```python
numbers = frozenset([10, 20, 30, 10])

print(numbers)
```

Duplicate elements are removed automatically.

However, elements cannot be added or removed after creation.

```python
numbers = frozenset([10, 20, 30])

# numbers.add(40)  # AttributeError
```

Frozen sets support mathematical set operations, but not mutation methods.

### Why use frozenset?

Frozen sets are useful when:

- A collection must remain unchanged.
- A set needs to be used as a dictionary key.
- A set needs to be stored inside another set.
- Immutable collections are required.

Example:

```python
permissions = frozenset(["read", "write"])

# Can be used as a dictionary key.
roles = {
    permissions: "editor"
}
```

## 12. Converting Between Lists and Sets

Python allows conversion between lists and sets.

### List to set

```python
numbers = [10, 20, 30, 10, 20]

numbers_set = set(numbers)

print(numbers_set)
```

Duplicate elements are removed.

### Set to list

```python
numbers = {10, 20, 30}

numbers_list = list(numbers)

print(numbers_list)
```

The resulting list does not guarantee the original insertion order of the set.

### Tuple to set

```python
numbers = (10, 20, 30, 10)

numbers_set = set(numbers)

print(numbers_set)
```

The duplicate element is removed.

## 13. Set Comprehension

Set comprehension provides a concise way to create sets.

Normal approach:

```python
numbers = [1, 2, 3, 4, 5]

squares = set()

for number in numbers:
    squares.add(number ** 2)

print(squares)
```

Using set comprehension:

```python
numbers = [1, 2, 3, 4, 5]

squares = {number ** 2 for number in numbers}

print(squares)
```

Set comprehension uses curly brackets.

It automatically stores unique results.

Example with a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number for number in numbers
    if number % 2 == 0
}

print(even_numbers)
```

Output:

```text
{2, 4, 6}
```

## 14. Copying Sets

Assignment creates another reference to the same set object.

```python
a = {10, 20, 30}

b = a

b.add(40)

print(a)
print(b)
```

Both variables show the updated set because they reference the same object.

### Shallow copy

Use `copy()` to create a separate set object.

```python
a = {10, 20, 30}

b = a.copy()

b.add(40)

print(a)
print(b)
```

The original set remains unchanged.

Because ordinary sets cannot contain mutable elements, a shallow copy is sufficient for the usual set use cases.

## 15. Applications of Sets in AI and Data Science

Sets are useful in:

- Removing duplicate records.
- Extracting unique labels.
- Comparing datasets.
- Finding common categories.
- Detecting differences between data sources.
- Checking whether records have already been processed.
- Comparing vocabulary or token collections.
- Data preprocessing.

Example:

```python
training_labels = {"positive", "negative"}

testing_labels = {"positive", "negative", "neutral"}

new_labels = testing_labels - training_labels

print(new_labels)
```

Output:

```text
{'neutral'}
```

This identifies a label that exists in the testing data but not in the training data.

## 16. Complete Practical Program

See the companion file `sets.py` for a fully commented executable program covering:

- Set creation
- Empty sets
- Duplicate removal
- Adding elements
- Removing elements
- Union
- Intersection
- Difference
- Symmetric difference
- Membership
- Subset and superset
- Disjoint sets
- Frozen sets
- List and tuple conversions
- Set comprehension
- Copying sets
- Student course analysis

## 17. Summary

| Concept | Important detail |
|---|---|
| Set syntax | `{}` |
| Empty set | `set()` |
| Mutable | Yes |
| Ordered | No guaranteed order |
| Duplicates | Not allowed |
| Indexing | Not supported |
| Add one element | `add()` |
| Add multiple elements | `update()` |
| Remove and raise if missing | `remove()` |
| Remove safely if missing | `discard()` |
| Remove arbitrary element | `pop()` |
| Remove everything | `clear()` |
| Union | `\|` |
| Intersection | `&` |
| Difference | `-` |
| Symmetric difference | `^` |
| Subset | `issubset()` |
| Superset | `issuperset()` |
| Disjoint | `isdisjoint()` |
| Immutable set | `frozenset()` |
| Set comprehension | `{expression for item in iterable}` |
| Copy | `copy()` |

Sets are essential when working with unique values and comparing collections. Understanding their uniqueness, unordered nature, membership operations and mathematical set operations is important for data processing and AI applications.