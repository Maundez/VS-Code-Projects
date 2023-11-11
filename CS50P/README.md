# CS50P course files

A collection of Python scripts based on lessons and problems in CS50P

## 0. Functions, Variables

- `script1.py`: A tool for processing data from XYZ source.
- `module_a.py`: Contains functions related to ABC functionality.
- `utility.py`: General utility functions used across the project.
...
## 1. Conditionals


## 2. Loops
- `nutrition.py`: Prompts for a food name and matches a dict to find the calories
- `lists.py`: Loops through a dict to return students details


## 3. Exceptions
- `exceptions.py`: Explains the While True: loop and ValueError exception
- `outdated.py`: Checks a user entered date str against datetime format and returns a standardized date

## 4. Libraries
- `emojize.py` : imports an emoji library and outputs emoji based on inputted str.
- `figlet.py` : library import and error handling, command line arguments (argv), exception handling
- `adieu.py` : imports an inflect library to format string output https://pypi.org/project/inflect/
- `game.py` : uses the Radom library 

## 5. Unit Tests
- `test_twttr.py` : Tests strings
- `test_bank.py` : Tests int's being returned for conversion to a string in the orgiginal program
### `pytest` in the command line, not `python`
remember to use pytest when calling a pytest program and not python

### pytest unit test program syntax
`import pytest`
from `fuel` import `convert, gauge`: accesses the covert and the gauge functions from fuel.py program

### Pytest function syntax
`def` test_convert_fractions():
start the function name with `test`
then the name of the function you are testing `convert` - in this case
then a descriptor of the actual tests e.g. `fractions` in this case

### Notes on why you don't need to use a main() function ###
Automatic Discovery : pytest automatically discovers and runs tests based on certain naming conventions. Any file that starts or ends with test_ (like test_value.py) is considered a test file. Within these files, any function prefixed with test_ is considered a test function and will be run by pytest.

Execution Model: When you run pytest, it does the job of invoking the test functions for you. You don't need to explicitly call them as you would in a regular Python script. So, there's no need for a main() function to orchestrate the execution of the tests.

Isolation: Each test function should ideally be independent and not rely on the state set by other tests. This helps ensure that tests can run in any order and that the outcome of one test doesn't influence another. Therefore, there's no need for a main() function to manage the order in which tests are run.






## 6. File I/O
- `lines.py` : Opens a file and counts the number of lines of code. 
### 6.1 sys.argv 
The line `with open(sys.argv[1], 'r') as file:` opens `open` the file name in the second argument [1] in 'r' mode (read mode)
- `sys.argv[1]`: This is the first command-line argument passed to your Python script (excluding the script name itself, which is sys.argv[0]). In your case, it's expected to be the path to the Python file whose lines of code you want to count.
-`r`: This is the mode argument. It's optional and defaults to `r` if not specified, but it's often included for clarity. The mode can be '`r`' for reading, `w` for writing (which will overwrite the file if it already exists), '`a`' for appending (which will add to the end of the file if it exists, or create a new one if it doesn't), and '`r+`' for both reading and writing.
- `as file`: This part of the statement creates a context manager (using the with statement) and assigns the opened file to the variable file. Using a file with a context manager (the with statement) is considered good practice because it ensures that the file is properly closed after its suite finishes, even if an exception is raised. This is important for resource management and can prevent data corruption or leaks.
- `pizza.py`: Opens a csv file and uses tabulate to output the data in a tabular format
- `names.py`: Opens a csv file, mnipulates data and writes a new file


## 7. Regular Expressions

## 8. Object Oriented Programming


## 9. Et Cetera

## 10. Keywords
List of Python keywords along with brief descriptions:

1. **`and`**: Logical operator. Returns `True` if both operands are true.
2. **`as`**: Used in aliasing (renaming) while importing a module or with the `with` statement to bind the result.
3. **`assert`**: For debugging. Tests a condition and triggers an error if the condition is false.
4. **`async`**: Used for defining asynchronous functions.
5. **`await`**: Used in asynchronous programming to call asynchronous functions.
6. **`break`**: Exits the current loop prematurely.
7. **`class`**: Used to define a new class (object-oriented programming).
8. **`continue`**: Skips the current loop iteration and jumps to the next.
9. **`def`**: Used to define a function.
10. **`del`**: Used to delete an object or a variable.
11. **`elif`**: Used in conditional statements, same as "else if".
12. **`else`**: Used in conditional statements after `if` and `elif`.
13. **`except`**: Used in exception handling to catch errors.
14. **`False`**: Boolean value representing falsehood.
15. **`finally`**: Always executed, typically used to release resources in exception handling.
16. **`for`**: Used for looping, typically iterating over items.
17. **`from`**: Used with `import` to import specific parts of a module.
18. **`global`**: Declares a global variable.
19. **`if`**: Used for conditional statements.
20. **`import`**: Used to include a module into the current script.
21. **`in`**: Used to check if a value exists in a sequence or to loop through a sequence.
22. **`is`**: Checks if two variables refer to the same memory location.
23. **`lambda`**: Used to create an anonymous function.
24. **`None`**: Represents a null value.
25. **`nonlocal`**: Refers to a variable in the nearest enclosing scope that is not global.
26. **`not`**: Logical operator. Inverts the truth value.
27. **`or`**: Logical operator. Returns `True` if at least one operand is true.
28. **`pass`**: A null operation; a placeholder where code will eventually go.
29. **`raise`**: Raises an exception.
30. **`return`**: Exits the function and returns a value.
31. **`True`**: Boolean value representing truth.
32. **`try`**: Used for exception handling, to wrap potentially error-prone code.
33. **`while`**: Used for looping based on a condition.
34. **`with`**: Used for simplifying exception handling by wrapping code.
35. **`yield`**: Used in a function to turn it into a generator.

Note: This list is based on Python 3.8. Some keywords might be added or removed in future versions of Python. Always check the official documentation for the most updated list.