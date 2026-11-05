# Python Data Structures: Lists vs Tuples vs Sets vs Dictionaries

## 1. Introduction

Python provides four important built-in data structures:

1. List
2. Tuple
3. Set
4. Dictionary

They all store collections of data, but they have different characteristics and use cases.

Choosing the correct data structure affects how you store, access, modify and process information.

---

## 2. Main Comparison Table

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `{}` or `set()` | `{key: value}` |
| Stores | Elements | Elements | Unique elements | Key-value pairs |
| Ordered | Yes | Yes | No guaranteed order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys cannot duplicate |
| Indexing | Yes | Yes | No | Access by key |
| Slicing | Yes | Yes | No | No positional slicing |
| Membership | Checks elements | Checks elements | Checks elements | Checks keys by default |
| Empty structure | `[]` | `()` | `set()` | `{}` |
| Typical use | Changeable collections | Fixed collections | Unique values | Labelled data and mappings |

**Important:** Dictionaries preserve insertion order in Python 3.7 and later. Sets do not guarantee a meaningful iteration order.

---

## 3. Lists

A list stores multiple elements in an ordered, mutable collection.

Example:

```python
skills = ["Python", "Java", "SQL"]

skills.append("Machine Learning")

print(skills)
```

Output:

```text
['Python', 'Java', 'SQL', 'Machine Learning']
```

### Key characteristics

- Ordered collection.
- Mutable: elements can be changed.
- Allows duplicate elements.
- Supports indexing and slicing.
- Can store different data types.

### When should you use a list?

Use a list when:
- You need to maintain an ordered collection.
- You need to add or remove elements.
- Duplicate values are acceptable.
- You need to access elements using positions.

### Practical applications

- Dataset records.
- Model predictions.
- Training examples.
- Lists of filenames.
- Batch processing.

---

## 4. Tuples

A tuple stores multiple elements in an ordered, immutable collection.

Example:

```python
coordinates = (10, 20)

print(coordinates[0])
```

Output:

```text
10
```

### Key characteristics

- Ordered collection.
- Immutable: elements cannot be reassigned or removed.
- Allows duplicate elements.
- Supports indexing and slicing.
- Can store different data types.

### When should you use a tuple?

Use a tuple when:
- The collection should not be structurally changed.
- You need to represent a fixed group of related values.
- You want to return multiple values from a function.
- You need a hashable collection of values for use as a dictionary key or set element (provided all contained elements are hashable).

### Practical applications

- Coordinates.
- RGB colour values.
- Fixed configuration values.
- Returning multiple values from functions.
- Fixed records.

**Important:** A tuple is immutable, but if it contains a mutable object such as a list, that nested object can still be modified.

---

## 5. Sets

A set stores unique elements.

Example:

```python
numbers = {10, 20, 30, 20, 10}

print(numbers)
```

Output contains only:

```text
{10, 20, 30}
```

The displayed order may differ.

### Key characteristics

- No guaranteed iteration order.
- Mutable.
- Does not allow duplicate elements.
- Does not support indexing or slicing.
- Elements must be hashable.
- Supports mathematical set operations.

### Important operations

```python
first = {1, 2, 3, 4}
second = {3, 4, 5, 6}

# Union: all unique elements
print(first | second)

# Intersection: common elements
print(first & second)

# Difference: elements in first but not second
print(first - second)

# Symmetric difference: elements in either set, but not both
print(first ^ second)
```

### When should you use a set?

Use a set when:
- You need unique values.
- You want to remove duplicates.
- You need to find common elements.
- You need to compare two collections.
- You need efficient average-case membership checks.

### Practical applications

- Removing duplicate records.
- Finding common users.
- Comparing dataset categories.
- Tracking unique words.
- Identifying unique labels.

---

## 6. Dictionaries

A dictionary stores information as key-value pairs.

Example:

```python
student = {
    "name": "Ammu",
    "age": 23,
    "course": "Artificial Intelligence"
}

print(student["name"])
```

Output:

```text
Ammu
```

### Key characteristics

- Preserves insertion order.
- Mutable.
- Keys must be unique.
- Keys must be hashable.
- Values can be any data type.
- Values are accessed using keys.

### When should you use a dictionary?

Use a dictionary when:
- Data has meaningful labels.
- You need to map one value to another.
- You need to retrieve information using an identifier.
- You need to represent structured records.
- You are working with JSON or API responses.

### Practical applications

- Student records.
- Employee information.
- API responses.
- Machine learning configuration.
- Model evaluation metrics.
- Word-frequency counting.

---

## 7. Understanding Mutability

Mutability means whether an object can be changed after it has been created.

| Data structure | Mutable? |
|---|---|
| List | Yes |
| Tuple | No |
| Set | Yes |
| Dictionary | Yes |

Example:

```python
# List: modification is allowed
numbers = [10, 20, 30]
numbers[0] = 100

# Tuple: reassignment of an element is not allowed
coordinates = (10, 20)
# coordinates[0] = 100  # TypeError

# Set: adding elements is allowed
unique_numbers = {10, 20, 30}
unique_numbers.add(40)

# Dictionary: updating values is allowed
student = {"name": "Ammu"}
student["name"] = "Ravi"
```

---

## 8. Understanding Ordering and Duplicates

| Data structure | Ordering | Duplicates |
|---|---|---|
| List | Preserved | Allowed |
| Tuple | Preserved | Allowed |
| Set | No guaranteed order | Not allowed |
| Dictionary | Insertion order preserved | Keys cannot duplicate |

Example:

```python
numbers_list = [1, 2, 2, 3]
numbers_tuple = (1, 2, 2, 3)
numbers_set = {1, 2, 2, 3}

student = {
    "name": "Ammu",
    "age": 23,
    "age": 24
}

print(numbers_list)
print(numbers_tuple)
print(numbers_set)
print(student)
```

The duplicate `age` key is replaced by its later value.

---

## 9. Indexing and Access

| Data structure | How to access |
|---|---|
| List | `numbers[0]` |
| Tuple | `coordinates[0]` |
| Set | No indexing |
| Dictionary | `student["name"]` |

Example:

```python
numbers = [10, 20, 30]
coordinates = (10, 20)
unique_numbers = {10, 20, 30}

student = {
    "name": "Ammu",
    "age": 23
}

print(numbers[0])
print(coordinates[0])
print(student["name"])

# unique_numbers[0] is invalid
```

---

## 10. Choosing the Correct Data Structure

Use this decision guide:

| Requirement | Recommended structure |
|---|---|
| Ordered collection that changes | List |
| Ordered collection that should remain fixed | Tuple |
| Unique values only | Set |
| Key-value mapping | Dictionary |
| Remove duplicates from a collection | Set |
| Access information using labels | Dictionary |
| Store coordinates | Tuple |
| Store a sequence of model predictions | List |
| Find common values between collections | Set |
| Store configuration settings | Dictionary |

---

## 11. Practical AI and Data Science Examples

### List: model predictions

```python
predictions = [0, 1, 1, 0, 1]
```

A list can preserve the sequence of predictions.

### Tuple: image dimensions

```python
image_dimensions = (224, 224, 3)
```

A tuple can represent fixed image dimensions: height, width and channels.

### Set: unique labels

```python
labels = {"spam", "ham", "spam", "ham"}

print(labels)
```

A set stores each unique label once.

### Dictionary: model configuration

```python
model_config = {
    "model": "BERT",
    "learning_rate": 0.00002,
    "batch_size": 16,
    "epochs": 5
}
```

A dictionary makes configuration values accessible through descriptive keys.

---

## 12. Performance Considerations

The following are typical average-case expectations for Python's built-in implementations. Actual performance depends on the data, operation and implementation details.

| Operation | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Access by index | O(1) | O(1) | Not supported | Not positional |
| Access by key | Not applicable | Not applicable | Not applicable | Average O(1) |
| Membership check | O(n) | O(n) | Average O(1) | Average O(1) for keys |
| Append/add item | Amortized O(1) | Not supported | Average O(1) | Average O(1) for insertion |
| Remove a known value | O(n) | Not supported | Average O(1) | Average O(1) for known key |

Complexity describes how an operation scales with the number of elements; it is not a direct measurement of execution time.

---

## 13. Common Mistakes

1. Using `{}` when intending to create an empty set. Use `set()`.
2. Trying to modify a tuple element.
3. Expecting a set to preserve insertion order.
4. Trying to access a set using an index.
5. Assuming `in` checks dictionary values. It checks keys by default.
6. Using a list or set as a dictionary key.
7. Forgetting that duplicate dictionary keys overwrite earlier values.
8. Assuming a shallow copy also duplicates nested lists and dictionaries.

---

## 14. Final Selection Rule

Remember these four rules:

- **List:** ordered and changeable collection.
- **Tuple:** ordered collection that cannot be structurally changed.
- **Set:** collection of unique elements.
- **Dictionary:** collection of key-value pairs.

Do not choose a data structure just because its syntax looks familiar. Choose it based on how the data needs to be stored, accessed and modified.

These four structures are foundational to Python programming and are used throughout data analysis, machine learning, deep learning and generative AI development.