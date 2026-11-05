# Python Strings and String Formatting

## 1. What is a string?

A **string** (`str`) is a sequence of characters used to represent text.

```python name = *Python* message = 'Machine Learning' ```

Strings can be written using:
- Single quotes: `'Python'`
- Double quotes: `*Python*`
- Triple quotes: `""*Python*""` or `'''Python'''`

Triple-quoted strings can span multiple lines:

```python message = ""*This is a multi-line string.*"* ```

Check the type:

```python text = *Python" print(type(text))  # <class 'str'> ```

---

## 2. Indexing

**Indexing** retrieves one character from a string using its position.

Python uses **zero-based indexing**: the first character is at index `0`.

```python text = *PYTHON*

print(text[0])  # P print(text[1])  # Y print(text[3])  # H ```

### Positive indexing

| Character | P | Y | T | H | O | N |
|---|---:|---:|---:|---:|---:|---:|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

Syntax:

```python string[index] ```

### Negative indexing

Negative indexes count from the end.

| Character | P | Y | T | H | O | N |
|---|---:|---:|---:|---:|---:|---:|
| Index | -6 | -5 | -4 | -3 | -2 | -1 |

```python text = *PYTHON*

print(text[-1])  # N print(text[-2])  # O print(text[-6])  # P ```

### Invalid indexing

```python text = *PYTHON* print(text[6]) ```

This raises:

```text IndexError: string index out of range ```

The valid positive indexes are `0` through `5`.

**Remember:** Indexing retrieves one character. An invalid index raises `IndexError`.

---

## 3. Slicing

**Slicing** retrieves a section of a string.

Syntax:

```python string[start:stop] ```

The start index is included; the stop index is excluded.

```python text = *PYTHON*

print(text[0:3])  # **PYT** print(text[2:5])  # **THO** ```

For `text[2:5]`, Python includes indexes `2`, `3`, and `4`, but excludes index `5`.

### Why is the stop index excluded?

It makes the number of characters in a normal positive-step slice easy to calculate:

```python text = *PYTHON* result = text[1:4]

print(result)  # **YTH** ```

The slice contains:

```text 4 - 1 = 3 characters ```

It also allows adjacent slices to fit together:

```python text = *PYTHON*

print(text[0:3])  # **PYT** print(text[3:6])  # **HON** ```

### Omitting the start

```python text = *PYTHON*

print(text[:3])  # **PYT** ```

Omitting the start means begin at the beginning.

### Omitting the stop

```python text = *PYTHON*

print(text[2:])  # **THON** ```

Omitting the stop means continue to the end.

### Copying the whole string

```python text = *PYTHON*

print(text[:])  # **PYTHON** ```

### Slicing with negative indexes

```python text = *PYTHON*

print(text[-3:])    # **HON** print(text[:-1])    # **PYTHO** print(text[-4:-1])  # **THO** ```

### Slicing with a step

Full syntax:

```python string[start:stop:step] ```

The step controls how many positions Python moves between characters.

```python text = *PYTHON*

print(text[::1])   # **PYTHON** print(text[::2])   # **PTO** print(text[1::2])  # **YHN** ```

### Reversing a string

A negative step moves backwards.

```python text = *PYTHON*

print(text[::-1])  # **NOHTYP** ```

### Indexing versus slicing

| Operation | Result |
|---|---|
| `text[2]` | One character |
| `text[2:5]` | A substring |
| `text[100]` | Raises `IndexError` |
| `text[0:100]` | Returns the available string characters |

**Remember:** Indexing accesses one character. Slicing accesses a sequence of characters.

---

## 4. String immutability

Strings are **immutable**, meaning their characters cannot be changed in place after the string is created.

```python text = *Python* ```

This is not allowed:

```python text[0] = *J* ```

It raises a `TypeError`.

### String methods return new strings

```python text = *Python*

result = text.upper()

print(text)    # Python print(result)  # **PYTHON** ```

`.upper()` returns a new string. It does not modify the original.

If the returned value is not stored, it is discarded:

```python text = *Python*

text.upper()

print(text)  # Python ```

To retain the result:

```python text = text.upper()

print(text)  # **PYTHON** ```

The variable now refers to the new string.

---

## 5. String methods

A **method** is a function associated with an object.

Syntax:

```python string.method() ```

When using a string method, ask:

## What does the method do?

## What type of value does it return? ## Does it modify the original string or return a new value?

Most string methods return a new value because strings are immutable.

### `.lower()`

Converts letters to lowercase.

```python text = *PyThOn*

print(text.lower())  # python ```

Returns: `str`

### `.upper()`

Converts letters to uppercase.

```python text = *PyThOn*

print(text.upper())  # **PYTHON** ```

Returns: `str`

### `.strip()`

Removes whitespace from both ends of a string.

```python text = *   Python AI   *

print(text.strip())  # Python AI ```

It does not remove spaces inside the string.

Returns: `str`

### `.lstrip()`

Removes whitespace from the left side.

```python text = *   Python   *

print(text.lstrip())  # Python ```

Returns: `str`

### `.rstrip()`

Removes whitespace from the right side.

```python text = *   Python   *

print(text.rstrip())  #    Python ```

Returns: `str`

### `.replace()`

Replaces occurrences of one substring with another.

```python text = *I like Java*

result = text.replace(*Java*, *Python*)

print(result)  # I like Python print(text)    # I like Java ```

You can limit the number of replacements:

```python text = *cat cat cat*

print(text.replace(*cat*, *dog*, 2))  # dog dog cat ```

Returns: `str`

### `.find()`

Returns the index of the first occurrence of a substring.

```python text = *Python Programming*

print(text.find(*P*))           # 0 print(text.find(*Programming*)) # 7 print(text.find(*z*))           # -1 ```

If the substring is not found, `.find()` returns `-1`.

Returns: `int`

### `.count()`

Counts how many times a substring appears.

```python text = *banana*

print(text.count(*a*))   # 3 print(text.count(*na*))  # 2 print(text.count(*z*))   # 0 ```

Returns: `int`

### `.startswith()`

Checks whether a string begins with a particular substring.

```python filename = *model.pkl*

print(filename.startswith(*model*))  # True ```

Returns: `bool`

### `.endswith()`

Checks whether a string ends with a particular substring.

```python filename = *model.pkl*

print(filename.endswith(*.pkl*))  # True print(filename.endswith(*.csv*))  # False ```

Returns: `bool`

### `.split()`

Divides a string into a list of strings.

```python text = *Python is useful*

words = text.split()

print(words)  # ['Python', 'is', 'useful'] ```

By default, `.split()` separates at whitespace.

You can specify a separator:

```python text = *python,java,c++*

languages = text.split(*,*)

print(languages)  # ['python', 'java', 'c++'] ```

Returns: `list`

Each element in the resulting list is a string.

### `.join()`

Combines strings from an iterable, usually a list.

```python languages = [*Python*, *Java*, *C++*]

result = * | *.join(languages)

print(result)  # Python | Java | C++ ```

The string before `.join()` is the separator.

Syntax:

```python *separator*.join(list_of_strings) ```

Returns: `str`

---

## 6. Method chaining

**Method chaining** means calling a method on the result of another method.

```python text = *   **PYTHON**,Java,C++   *

result = text.strip().lower().split(*,*)

print(result) ```

Output:

```python ['python', 'java', 'c++'] ```

Python evaluates the operations in order:

1. `.strip()` removes whitespace from both ends.
2. `.lower()` converts the resulting string to lowercase.
3. `.split(*,*)` divides the string at commas and returns a list.

The original `text` remains unchanged because the methods return new values and the result is not assigned back to `text`.

---

## 7. Concatenation

**Concatenation** means joining strings together.

The `+` operator concatenates strings.

```python first = *Machine* second = *Learning*

result = first + * * + second

print(result)  # Machine Learning ```

Python does not automatically add spaces:

```python print(*Python* + *Programming*)  # PythonProgramming ```

To add a space, include it explicitly:

```python print(*Python* + * * + *Programming*) ```

### Concatenating different types

This causes a `TypeError`:

```python age = 25

message = *Age: * + age ```

Python cannot directly concatenate a string and an integer.

Convert the integer:

```python message = *Age: * + str(age)

print(message)  # Age: 25 ```

An f-string is usually a cleaner alternative.

---

## 8. Repetition

The `*` operator repeats a string.

```python text = *Hi*

print(text * 3)  # HiHiHi ```

Repetition does not automatically add spaces:

```python print(*Python* * 3)  # PythonPythonPython ```

Include a space if needed:

```python print(*Python * * 3)  # Python Python Python ```

Repetition can also create separators:

```python print(*-* * 20) ```

Output:

## ```text

```

---

## 9. Type conversion with strings

Use `str()` to convert a value into a string.

```python age = 25

message = *Age: * + str(age)

print(message)  # Age: 25 ```

This is useful when combining strings with numbers.

Remember that `str()` converts a value to text. It does not change the original variable’s type.

---

## 10. f-strings

An **f-string** is a formatted string that allows variables and expressions to be inserted directly into a string.

Put `f` before the opening quote and place values inside `{}`.

```python name = *Ammu* age = 25

message = f*My name is {name} and I am {age} years old.*

print(message) ```

Output:

```text My name is Ammu and I am 25 years old. ```

### Expressions inside f-strings

You can insert expressions, not only variable names.

```python a = 10 b = 5

print(f*Total: {a + b}*)      # Total: 15 print(f*Is a bigger? {a > b}*) # Is a bigger? True ```

Python evaluates the expression inside `{}` and inserts its result.

### Formatting decimal places: `:.2f`

```python price = 12.**34567**

print(f*Price: £{price:.2f}*) ```

Output:

```text Price: £12.35 ```

Meaning:

- `:` begins the formatting instructions.
- `.2` means two digits after the decimal point.
- `f` means fixed-point decimal formatting.

The displayed value is rounded. The original variable is not necessarily changed.

### Formatting percentages: `:.2%`

```python accuracy = 0.**9567**

print(f*Accuracy: {accuracy:.2%}*) ```

Output:

```text Accuracy: 95.67% ```

Percentage formatting multiplies the displayed value by **100** and adds `%`.

### Formatting numbers with commas

```python population = **1234567**

print(f*Population: {population:,}*) ```

Output:

```text Population: 1,**234**,**567** ```

### Alignment

```python label = *Python*

print(f*|{label:<10}|*)  # Left-aligned print(f*|{label:>10}|*)  # Right-aligned print(f*|{label:^10}|*)  # Centred ```

- `<` means left-align.
- `>` means right-align.
- `^` means centre.

---

## 11. Complete practice program

```python # ========================================== # PYTHON STRINGS: COMPLETE PRACTICE PROGRAM # ==========================================

# 1. Creating strings

text = *Python Programming*

print(*Original string:*, text)

# 2. Indexing

print(*\n--- Indexing ---*) print(*First character:*, text[0]) print(*Fourth character:*, text[3]) print(*Last character:*, text[-1]) print(*Second-last character:*, text[-2])

# 3. Slicing

print(*\n--- Slicing ---*) print(*First six characters:*, text[:6]) print(*Characters from index 7:*, text[7:]) print(*Indexes 0 to 5:*, text[0:6]) print(*Last three characters:*, text[-3:]) print(*Every second character:*, text[::2]) print(*Reversed string:*, text[::-1])

# 4. String methods

print(*\n--- String methods ---*)

messy_text = *   Python Programming   *

print(*lower():*, text.lower()) print(*upper():*, text.upper())

print(*strip():*, messy_text.strip()) print(*lstrip():*, messy_text.lstrip()) print(*rstrip():*, messy_text.rstrip())

print(*replace():*, text.replace(*Python*, *AI*)) print(*find():*, text.find(*Programming*)) print(*count():*, text.count(*m*))

print(*startswith():*, text.startswith(*Python*)) print(*endswith():*, text.endswith(*Programming*))

words = text.split() print(*split():*, words)

joined_text = * *.join(words) print(*join():*, joined_text)

# 5. Strings are immutable

print(*\n--- Immutability ---*)

language = *Python*

language.upper() print(*After calling upper without assignment:*, language)

language = language.upper() print(*After assigning the result:*, language)

# 6. Concatenation

print(*\n--- Concatenation ---*)

first = *Machine* second = *Learning*

combined = first + * * + second

print(*Combined:*, combined)

# 7. Repetition

print(*\n--- Repetition ---*)

print(*Repeat:*, *AI * * 3) print(*Separator:*, *-* * 30)

# 8. Type conversion

print(*\n--- Type conversion ---*)

age = 25

message = *Age: * + str(age) print(message)

# 9. f-strings

print(*\n--- f-strings ---*)

name = *Ammu* score = 95.**6789** accuracy = 0.**9567** total = **1234567**

print(f*My name is {name}.*) print(f*Score: {score:.2f}*) print(f*Accuracy: {accuracy:.2%}*) print(f*Total: {total:,}*) print(f*Calculation: {10} + {5} = {10 + 5}*)

# 10. Formatting alignment

print(*\n--- Alignment ---*)

label = *Python*

print(f*|{label:<10}|*) print(f*|{label:>10}|*) print(f*|{label:^10}|*) ```

---

## 12. Common mistakes

### Mistake 1: Forgetting zero-based indexing

```python text = *Python*

print(text[2])  # T, not H ```

### Mistake 2: Including the stop index

```python text = *Python*

print(text[1:4])  # yth, not ytho ```

### Mistake 3: Expecting a string method to modify the original

```python text = *Python*

text.upper()

print(text)  # Python ```

Store the returned value if you need it.

### Mistake 4: Mixing strings and numbers

```python age = 25

# *Age: * + age  # TypeError

```

Use `str(age)` or an f-string.

### Mistake 5: Confusing `.split()` and `.join()`

- `.split()` converts a string into a list.
- `.join()` combines strings from an iterable into one string.

### Mistake 6: Confusing `:.2f` and `:.2%`

- `:.2f` displays two decimal places.
- `:.2%` converts the displayed value to a percentage and displays two decimal places.

---

## 13. Interview questions

## What is a string in Python?

## Why does Python use zero-based indexing? ## What is the difference between indexing and slicing? ## Why is the stop index excluded in slicing? ## How do you reverse a string using slicing? ## What does it mean for strings to be immutable? ## What is the difference between `.find()` and indexing? ## What is the difference between `.split()` and `.join()`? ## What is method chaining? ## What is the difference between concatenation and repetition? ## Why can’t you concatenate a string and an integer directly? ## What is an f-string? ## What is the difference between `:.2f` and `:.2%`? ## What does `len()` return for a string? What does it return for a list?

---

## 14. Quick revision

| Concept | Meaning |
|---|---|
| `text[index]` | Retrieves one character |
| `text[start:stop]` | Retrieves a substring |
| `text[::-1]` | Reverses the string |
| `.lower()` | Returns lowercase string |
| `.upper()` | Returns uppercase string |
| `.strip()` | Removes whitespace from both ends |
| `.replace(old, new)` | Returns a string with replacements |
| `.find(value)` | Returns index or `-1` |
| `.count(value)` | Returns occurrence count |
| `.split(separator)` | Returns a list of strings |
| `.join(iterable)` | Returns one combined string |
| `+` | Concatenates strings |
| `*` | Repeats a string |
| `str(value)` | Converts a value to a string |
| `f*{value}*` | Inserts a value into a string |
| `:.2f` | Displays two decimal places |
| `:.2%` | Displays a percentage with two decimal places |

**Completion standard:** You should be able to explain every concept, predict the output of the practice program, and write a small string-processing program without copying the notes.