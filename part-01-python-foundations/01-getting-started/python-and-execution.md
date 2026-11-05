# Python and Program Execution

## 1. What is Python?

Python is a programming language used to write instructions that a computer can execute. It is commonly used for automation, data analysis, machine learning, AI development, web applications, and general software development.

## 2. What is VS Code?

Visual Studio Code (VS Code) is a code editor. It provides a workspace where developers can write, organise, debug, and run code in different programming languages.

VS Code does not itself execute Python code. It uses a Python interpreter installed on the computer.

## 3. What is a Python Interpreter?

A Python interpreter is software that executes Python code.

For example:

```python print(5 + 3) ```

The interpreter evaluates the expression `5 + 3` and executes the `print()` instruction. The output is:

```text 8 ```

## 4. What is a Python File?

A Python file normally uses the `.py` extension.

Example:

```text hello.py ```

The file contains Python instructions. The instructions execute when the file is run using a Python interpreter.

## 5. What is a Package?

A package is reusable Python code created to provide functionality that developers can use in their own programs.

Examples:

| Package | Common use |
|---|---|
| NumPy | Numerical computing |
| pandas | Data manipulation and analysis |
| Matplotlib | Data visualisation |
| scikit-learn | Traditional machine learning |
| PyTorch | Deep learning |

Packages save development time because developers can reuse existing functionality instead of implementing everything from scratch.

## 6. What is pip?

`pip` is a tool used to install Python packages.

Example:

```powershell pip install pandas ```

This installs the pandas package into the Python environment targeted by that `pip` command.

## 7. What does import mean?

The `import` statement makes a package or module available to the current Python program.

Example:

```python import pandas ```

The distinction is:

- `pip install pandas` installs pandas into an environment.
- `import pandas` makes pandas available in the current program.

## 8. What is a Virtual Environment?

A virtual environment is an isolated Python environment associated with a project.

It allows projects to maintain separate package installations and dependency versions.

For example:

```text project-a/ ├── .venv/ └── main.py

project-b/ ├── .venv/ └── main.py ```

Each project can have its own installed packages without interfering with the other project.

A virtual environment uses a Python interpreter selected when the environment is created. It does not automatically install every Python version.

Deleting `.venv` removes that environment and its installed packages, but does not delete the project's source code. The environment can be recreated and its dependencies reinstalled.

## 9. How a Python Program Runs

The general process is:

## The developer writes Python code in a `.py` file.

## VS Code uses the selected Python interpreter to run the file. ## The interpreter processes and executes the instructions. ## The program's output or errors appear in the terminal.

## 10. Practical Example

```python print(*Python is running.*) print(5 + 3) ```

Output:

```text Python is running. 8 ```

## Key Takeaways

- Python is a programming language.
- VS Code is a code editor.
- The Python interpreter executes Python code.
- A `.py` file stores Python instructions.
- Packages provide reusable functionality.
- `pip install` installs packages.
- `import` makes functionality available to a program.
- Virtual environments isolate project dependencies.