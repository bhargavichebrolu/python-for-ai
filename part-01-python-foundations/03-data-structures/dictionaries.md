# Dictionaries in Python

## 1. Introduction

A dictionary is a built-in Python data structure that stores information as **key-value pairs**.

Each item contains:
- A **key**: identifies the information.
- A **value**: stores the information associated with that key.

Example:

```python
student = {
    "name": "Ammu",
    "age": 23,
    "course": "Artificial Intelligence"
}
```

Here:
- `"name"` is a key.
- `"Ammu"` is its value.
- `"age"` is a key.
- `23` is its value.

Dictionaries are useful when information has labels or identifiers.

## 2. Characteristics of Dictionaries

| Characteristic | Explanation |
|---|---|
| Mutable | Items can be added, changed and removed |
| Insertion ordered | Preserves insertion order (guaranteed from Python 3.7) |
| Unique keys | A key can appear only once |
| Hashable keys | Keys must be hashable, such as strings, numbers or suitable tuples |
| Flexible values | Values can be strings, numbers, lists, tuples, sets or other dictionaries |
| Key-based access | Values are accessed using keys, not numerical positions |

Example:

```python
student = {"name": "Ammu", "age": 23}

student["age"] = 24  # Modify an existing value
student["city"] = "London"  # Add a new key-value pair
```

## 3. Creating Dictionaries

### Using curly braces

```python
student = {
    "name": "Ammu",
    "age": 23,
    "marks": 85
}
```

### Creating an empty dictionary

```python
student = {}
```

### Using dict()

```python
student = dict(name="Ammu", age=23, marks=85)
```

### Creating from pairs

```python
student = dict([
    ("name", "Ammu"),
    ("age", 23),
    ("marks", 85)
])
```

**Important:** `{}` creates an empty dictionary, not an empty set. Use `set()` for an empty set.

## 4. Accessing Dictionary Values

### Using square brackets

```python
student = {
    "name": "Ammu",
    "age": 23
}

print(student["name"])
print(student["age"])
```

If the key does not exist, square-bracket access raises a `KeyError`.

```python
print(student["city"])  # KeyError
```

### Using get()

`get()` safely retrieves a value. If the key is missing, it returns `None` by default.

```python
print(student.get("name"))
print(student.get("city"))
```

You can provide a default value:

```python
print(student.get("city", "Not available"))
```

**Difference:**

| Method | Missing key |
|---|---|
| `dictionary[key]` | Raises `KeyError` |
| `dictionary.get(key)` | Returns `None` by default |
| `dictionary.get(key, default)` | Returns the specified default |

## 5. Adding and Updating Items

Assigning a value to a new key adds an item.

```python
student = {"name": "Ammu", "age": 23}

student["city"] = "London"
```

Assigning to an existing key updates its value.

```python
student["age"] = 24
```

### Using update()

`update()` adds or modifies multiple key-value pairs.

```python
student.update({
    "age": 25,
    "course": "Artificial Intelligence"
})
```

It can also accept keyword arguments:

```python
student.update(city="Manchester", marks=90)
```

## 6. Removing Items

### pop()

Removes the specified key and returns its value.

```python
student = {"name": "Ammu", "age": 23, "city": "London"}

removed_value = student.pop("age")
print(removed_value)
```

A default can prevent a missing-key error:

```python
student.pop("course", "Not found")
```

### popitem()

Removes and returns the last inserted key-value pair.

```python
student.popitem()
```

### del

Deletes a particular key-value pair.

```python
del student["city"]
```

### clear()

Removes all items.

```python
student.clear()
```

## 7. Dictionary Methods: keys(), values(), items()

### keys()

Returns a view of all keys.

```python
student = {"name": "Ammu", "age": 23, "marks": 90}

print(student.keys())
```

### values()

Returns a view of all values.

```python
print(student.values())
```

### items()

Returns a view of key-value pairs.

```python
print(student.items())
```

These are dynamic dictionary views: they reflect changes made to the dictionary.

## 8. Iterating Through Dictionaries

### Iterating through keys

```python
student = {
    "name": "Ammu",
    "age": 23,
    "marks": 90
}

for key in student:
    print(key)
```

This is equivalent to:

```python
for key in student.keys():
    print(key)
```

### Iterating through values

```python
for value in student.values():
    print(value)
```

### Iterating through keys and values

Use `items()` when both are needed.

```python
for key, value in student.items():
    print(key, value)
```

## 9. Checking Whether a Key Exists

The `in` operator checks dictionary keys.

```python
student = {"name": "Ammu", "age": 23}

print("name" in student)  # True
print("city" in student)  # False
```

To check whether a value exists, use `values()`.

```python
print(23 in student.values())
```

**Important:** `in` checks keys by default, not values.

## 10. Dictionary Length

Use `len()` to count key-value pairs.

```python
student = {
    "name": "Ammu",
    "age": 23,
    "marks": 90
}

print(len(student))  # 3
```

## 11. Dictionary Comprehension

Dictionary comprehension creates a dictionary using a compact expression.

Syntax:

```python
new_dictionary = {key_expression: value_expression for item in iterable}
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Dictionary comprehension with a condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}
```

## 12. Nested Dictionaries

A dictionary can contain another dictionary as a value.

```python
students = {
    "student1": {
        "name": "Ammu",
        "marks": 90
    },
    "student2": {
        "name": "Ravi",
        "marks": 85
    }
}
```

Access nested values:

```python
print(students["student1"]["name"])
print(students["student2"]["marks"])
```

Update a nested value:

```python
students["student1"]["marks"] = 95
```

Nested dictionaries are useful for representing structured records.

## 13. Dictionary Keys and Hashability

Dictionary keys must be hashable.

Common valid keys:

```python
data = {
    "name": "Ammu",
    10: "Ten",
    3.14: "Pi",
    (1, 2): "Coordinate"
}
```

Common invalid keys:

```python
# These raise TypeError because lists and sets are mutable and unhashable.

# data = {[1, 2]: "value"}
# data = {{1, 2}: "value"}
```

Values do not have this restriction:

```python
data = {
    "numbers": [1, 2, 3],
    "details": {"city": "London"},
    "tags": {"python", "AI"}
}
```

## 14. Duplicate Keys

Dictionary keys must be unique.

If the same key is written more than once, the later value replaces the earlier value.

```python
student = {
    "name": "Ammu",
    "age": 22,
    "age": 23
}

print(student["age"])  # 23
```

## 15. Copying Dictionaries

### Assignment creates another reference

```python
original = {"name": "Ammu"}
reference = original

reference["name"] = "Ravi"

print(original)  # Also changes
```

Both variables refer to the same dictionary.

### copy() creates a shallow copy

```python
original = {"name": "Ammu", "marks": [80, 90]}

copied = original.copy()
copied["name"] = "Ravi"
```

The top-level dictionaries are separate, but nested mutable objects are still shared.

### Deep copy

Use `copy.deepcopy()` when nested mutable objects must also be copied.

```python
import copy

original = {"name": "Ammu", "marks": [80, 90]}

copied = copy.deepcopy(original)
copied["marks"].append(95)

print(original["marks"])  # [80, 90]
print(copied["marks"])    # [80, 90, 95]
```

## 16. Useful Dictionary Methods

| Method | Purpose |
|---|---|
| `get(key)` | Safely retrieves a value |
| `keys()` | Returns keys |
| `values()` | Returns values |
| `items()` | Returns key-value pairs |
| `update()` | Adds or updates items |
| `pop(key)` | Removes a specified key |
| `popitem()` | Removes the last inserted pair |
| `clear()` | Removes all items |
| `copy()` | Creates a shallow copy |
| `setdefault()` | Returns a value, inserting a default if the key is missing |
| `fromkeys()` | Creates a dictionary from an iterable of keys |

### setdefault()

```python
student = {"name": "Ammu"}

student.setdefault("age", 23)
student.setdefault("name", "Ravi")

print(student)
```

`setdefault()` inserts the default only if the key is absent. It does not overwrite an existing value.

### fromkeys()

```python
subjects = ["Python", "Java", "SQL"]

subject_status = dict.fromkeys(subjects, "Not started")
```

Be careful when using a mutable default value with `fromkeys()`: all keys will refer to the same object.

## 17. Merging Dictionaries

### Using update()

```python
first = {"name": "Ammu", "age": 23}
second = {"city": "London", "course": "AI"}

first.update(second)
```

This modifies `first`.

### Using the union operator

Python 3.9 and later support `|` for dictionary merging.

```python
first = {"name": "Ammu", "age": 23}
second = {"city": "London"}

combined = first | second
```

This creates a new dictionary. If both dictionaries contain the same key, the value from the right-hand dictionary wins.

## 18. Dictionary Applications in AI and Data Science

Dictionaries are frequently used for:

1. **Data records:** representing students, employees, products and customers.
2. **JSON data:** JSON objects are commonly represented as Python dictionaries when parsed.
3. **API responses:** storing structured data returned by web APIs.
4. **Frequency counting:** counting words, labels or categories.
5. **Machine learning:** storing configuration parameters and evaluation metrics.
6. **Data preprocessing:** mapping category names to numerical values.
7. **Model outputs:** storing predictions, confidence scores and metadata.

Example: counting word frequency.

```python
words = ["AI", "Python", "AI", "ML", "Python", "AI"]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
```

Output:

```text
{'AI': 3, 'Python': 2, 'ML': 1}
```

## 19. Common Mistakes

### Mistake 1: Accessing a missing key

```python
# Raises KeyError
# print(student["city"])

# Safer
print(student.get("city", "Unknown"))
```

### Mistake 2: Assuming in checks values

```python
student = {"name": "Ammu"}

print("Ammu" in student)  # False
print("Ammu" in student.values())  # True
```

### Mistake 3: Using mutable keys

Lists and sets cannot be dictionary keys because they are unhashable.

### Mistake 4: Assuming dictionaries use positional indexing

```python
student = {"name": "Ammu", "age": 23}

# student[0] is not positional access.
# It tries to find the key 0.
```

### Mistake 5: Confusing assignment and copying

```python
second = first        # Same object
second = first.copy() # Shallow copy
```

## 20. When Should You Use a Dictionary?

Use a dictionary when:
- Data has identifiable labels.
- You need to retrieve values using keys.
- You need to map one value to another.
- You need to represent structured records.
- You need efficient average-case key lookup.

Example:

```python
employee = {
    "id": 101,
    "name": "Ammu",
    "department": "AI",
    "salary": 35000
}
```

The dictionary is a natural choice because each value has a meaningful label.

---

## Final Summary

A dictionary stores information using key-value pairs.

Remember these essential points:

- Dictionaries are mutable.
- They preserve insertion order in modern Python.
- Keys must be unique and hashable.
- Values can be of any type.
- `dictionary[key]` accesses a value but raises `KeyError` for missing keys.
- `get()` provides safer access.
- `keys()`, `values()` and `items()` provide views of dictionary contents.
- `update()` adds or modifies multiple items.
- Dictionary comprehension creates dictionaries from iterables.
- Nested dictionaries represent structured data.
- Dictionaries are widely used in APIs, JSON, data processing and machine learning.
