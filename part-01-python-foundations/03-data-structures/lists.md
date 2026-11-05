# Lists in Python

## 1. Introduction to Lists

A list is a built-in Python data structure used to store multiple values inside a single variable.

Instead of creating separate variables for every value, we can group related values together in a list.

Without a list:

```python student1 = *Ammu* student2 = *Ravi* student3 = *John* ```

Using a list:

```python students = [*Ammu*, *Ravi*, *John*] ```

Lists are useful for storing and processing collections of data.

They are extensively used in:
- Data processing
- Machine learning
- Data analysis
- Application development
- **API** responses
- Storing collections of records

## 2. Characteristics of Lists

Python lists have the following characteristics:

1. **Ordered:** Elements maintain their insertion order.
2. **Mutable:** Elements can be added, modified and removed after creation.
3. **Duplicates allowed:** A list can contain repeated values.
4. **Heterogeneous:** A list can contain different data types.
5. **Indexed:** Elements can be accessed using positive and negative indexes.
6. **Dynamic:** Lists can grow or shrink during program execution.
7. **Nested:** A list can contain other lists.

Example:

```python data = [*Python*, 23, 85.5, True, *Python*]

print(data) ```

The list contains strings, an integer, a float and a Boolean. It also contains a duplicate string.

## 3. Creating Lists

Lists are created using square brackets `[]`.

### List containing strings

```python languages = [*Python*, *Java*, *C++*] ```

### List containing integers

```python numbers = [10, 20, 30, 40] ```

### List containing different data types

```python student = [*Ammu*, 23, 85.5, True] ```

### Empty list

```python students = [] ```

An empty list is useful when data will be added later.

Another way to create a list is:

```python students = list() ```

### Using the list constructor

The `list()` constructor converts an iterable into a list.

```python numbers = list((10, 20, 30))

print(numbers) ```

Output:

```text [10, 20, 30] ```

## 4. Ordered Property

Lists preserve the order in which elements are inserted.

```python numbers = [30, 10, 20]

print(numbers) ```

Output:

```text [30, 10, 20] ```

Python does not automatically sort a list when elements are inserted.

## 5. Duplicate Elements

Lists allow duplicate values.

```python numbers = [10, 20, 10, 30, 20]

print(numbers) ```

Output:

```text [10, 20, 10, 30, 20] ```

Duplicates remain in the list unless explicitly removed.

## 6. Accessing List Elements Using Indexing

Python uses zero-based indexing.

This means the first element has index `0`, the second has index `1`, and so on.

```python languages = [*Python*, *Java*, *C++*, *SQL*]

print(languages[0])  # Python print(languages[1])  # Java print(languages[2])  # C++ print(languages[3])  # **SQL** ```

### Negative indexing

Negative indexing accesses elements from the end of the list.

```python languages = [*Python*, *Java*, *C++*, *SQL*]

print(languages[-1])  # **SQL** print(languages[-2])  # C++ print(languages[-3])  # Java print(languages[-4])  # Python ```

### IndexError

Accessing an index that does not exist raises an `IndexError`.

```python languages = [*Python*, *Java*, *C++*]

# This raises IndexError because index 5 does not exist.

print(languages[5]) ```

## 7. List Slicing

Slicing retrieves a portion of a list.

Syntax:

```python list_name[start:stop:step] ```

- `start`: Starting index, included.
- `stop`: Ending index, excluded.
- `step`: Number of positions to move between elements.

Example:

```python languages = [*Python*, *Java*, *C++*, *SQL*, *JavaScript*]

print(languages[1:4]) ```

Output:

```text ['Java', 'C++', '**SQL**'] ```

### Different slicing operations

```python languages = [*Python*, *Java*, *C++*, *SQL*, *JavaScript*]

print(languages[:3])    # First three elements print(languages[2:])    # From index 2 to the end print(languages[1:4])   # Indexes 1, 2 and 3 print(languages[::2])   # Every second element print(languages[::-1])  # Reversed copy ```

Slicing creates a new list and does not remove elements from the original list.

## 8. Lists Are Mutable

Mutable means an object can be modified after it has been created.

Lists are mutable.

### Modifying an element

```python languages = [*Python*, *Java*, *C++*]

languages[1] = *JavaScript*

print(languages) ```

Output:

```text ['Python', 'JavaScript', 'C++'] ```

The element at index `1` has been replaced.

### Difference between mutable and immutable

- Lists are mutable.
- Tuples are immutable.
- Strings are immutable.

A list allows individual elements to be reassigned, whereas a string does not allow individual characters to be reassigned.

## 9. Adding Elements to Lists

Python provides several methods to add elements.

### 9.1 append()

`append()` adds one element to the end of the list.

```python languages = [*Python*, *Java*]

languages.append(*C++*)

print(languages) ```

Output:

```text ['Python', 'Java', 'C++'] ```

Important: `append()` adds its argument as a single element.

Example:

```python numbers = [1, 2]

numbers.append([3, 4])

print(numbers) ```

Output:

```text [1, 2, [3, 4]] ```

The nested list `[3, 4]` becomes one element.

### 9.2 extend()

`extend()` adds individual elements from an iterable to the end of the list.

```python numbers = [1, 2]

numbers.extend([3, 4])

print(numbers) ```

Output:

```text [1, 2, 3, 4] ```

Unlike `append()`, `extend()` processes the supplied iterable and adds its elements individually.

### 9.3 insert()

`insert()` adds an element at a specified position.

Syntax:

```python list_name.insert(index, value) ```

Example:

```python languages = [*Python*, *Java*]

languages.insert(1, *C++*)

print(languages) ```

Output:

```text ['Python', 'C++', 'Java'] ```

The original elements are shifted to make room.

### append() vs extend() vs insert()

| Method | Purpose |
|---|---|
| `append(x)` | Adds one element at the end |
| `extend(iterable)` | Adds elements from an iterable |
| `insert(i, x)` | Adds an element at a specified index |

## 10. Removing Elements from Lists

Python provides several ways to remove elements.

### 10.1 remove()

`remove()` removes the first matching value.

```python languages = [*Python*, *Java*, *C++*, *Java*]

languages.remove(*Java*)

print(languages) ```

Output:

```text ['Python', 'C++', 'Java'] ```

Only the first occurrence is removed.

If the value does not exist, Python raises a `ValueError`.

### 10.2 pop()

`pop()` removes and returns an element.

Without an argument, it removes the last element.

```python languages = [*Python*, *Java*, *C++*]

removed = languages.pop()

print(removed) print(languages) ```

Output:

```text C++ ['Python', 'Java'] ```

You can also specify an index.

```python languages = [*Python*, *Java*, *C++*]

removed = languages.pop(1)

print(removed)   # Java print(languages) # ['Python', 'C++'] ```

### 10.3 del

The `del` statement deletes an element using its index.

```python languages = [*Python*, *Java*, *C++*]

del languages[1]

print(languages) ```

Output:

```text ['Python', 'C++'] ```

It can also delete a slice.

```python numbers = [10, 20, 30, 40, 50]

del numbers[1:3]

print(numbers) ```

Output:

```text [10, 40, 50] ```

### 10.4 clear()

`clear()` removes every element from the list.

```python languages = [*Python*, *Java*, *C++*]

languages.clear()

print(languages) ```

Output:

```text [] ```

The list still exists, but it is empty.

### Removal comparison

| Operation | Behaviour |
|---|---|
| `remove(value)` | Removes the first matching value |
| `pop(index)` | Removes and returns an element |
| `pop()` | Removes and returns the last element |
| `del` | Deletes by index or slice |
| `clear()` | Removes all elements |

## 11. Useful List Functions

Python provides built-in functions that work with lists.

```python scores = [82, 45, 91, 67, 38, 76]

print(len(scores)) print(min(scores)) print(max(scores)) print(sum(scores)) ```

Output:

```text 6 38 91 **399** ```

| Function | Purpose |
|---|---|
| `len()` | Returns the number of elements |
| `min()` | Returns the smallest element |
| `max()` | Returns the largest element |
| `sum()` | Returns the sum of numeric elements |
| `sorted()` | Returns a new sorted list |

Note: `sum()`, `min()` and `max()` require compatible values. They cannot perform meaningful numerical operations on arbitrary mixed data types.

## 12. Sorting Lists

Python provides `sort()` and `sorted()`.

### 12.1 sort()

`sort()` modifies the original list.

```python scores = [82, 45, 91, 67, 38]

scores.sort()

print(scores) ```

Output:

```text [38, 45, 67, 82, 91] ```

Descending order:

```python scores.sort(reverse=True)

print(scores) ```

Output:

```text [91, 82, 67, 45, 38] ```

Important: `sort()` modifies the list in place and returns `None`.

### 12.2 sorted()

`sorted()` returns a new sorted list without modifying the original.

```python scores = [82, 45, 91, 67, 38]

result = sorted(scores)

print(result) print(scores) ```

Output:

```text [38, 45, 67, 82, 91] [82, 45, 91, 67, 38] ```

Descending order:

```python result = sorted(scores, reverse=True) ```

### sort() vs sorted()

| Feature | `sort()` | `sorted()` |
|---|---|---|
| Modifies original list | Yes | No |
| Returns sorted list | No, returns `None` | Yes |
| Reverse sorting | Supported | Supported |
| Works with other iterables | No, list method | Yes |

## 13. Reversing Lists

The `reverse()` method reverses the list in place.

```python numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers) ```

Output:

```text [40, 30, 20, 10] ```

It does not sort the values. It simply reverses their current order.

You can also use slicing:

```python numbers = [10, 20, 30, 40]

reversed_numbers = numbers[::-1]

print(reversed_numbers) ```

This creates a reversed copy.

## 14. Membership Operators

Use `in` and `not in` to check whether an element exists.

```python languages = [*Python*, *Java*, *C++*]

print(*Python* in languages) print(*JavaScript* in languages) print(*JavaScript* not in languages) ```

Output:

```text True False True ```

Membership checks are useful when validating whether a value exists before processing it.

## 15. Iterating Through Lists

A `for` loop can process every element in a list.

```python languages = [*Python*, *Java*, *C++*]

for language in languages:
    print(language)
```

You can also use indexes:

```python languages = [*Python*, *Java*, *C++*]

for index in range(len(languages)):
    print(index, languages[index])
```

### enumerate()

`enumerate()` provides both the index and the element during iteration.

```python languages = [*Python*, *Java*, *C++*]

for index, language in enumerate(languages):
    print(index, language)
```

You can specify a starting index:

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

This is often cleaner than manually maintaining a counter.

## 16. List Comprehension

List comprehension provides a concise way to create a new list from an iterable.

Normal approach:

```python numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares) ```

Using list comprehension:

```python numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares) ```

Output:

```text [1, 4, 9, 16, 25] ```

### List comprehension with conditions

```python numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print(even_numbers) ```

Output:

```text [2, 4, 6] ```

The condition filters which elements are included in the resulting list.

## 17. Nested Lists

A nested list is a list containing other lists.

```python
students = [
    [*Ammu*, 85],
    [*Ravi*, 90],
    [*John*, 76]
]
```

Each inner