---
title: Python
description: The default programming language for working with data.
date: 2024-12-07
competencies:
- "Software Engineering"
---

## Why Learn Python?

Learning Python will allow you to:

- **Industry standard** - Popular programming language for data work.
- **Powerful** - Rich ecosystem of data science tools like `pandas` and `scikit-learn`.
- **Mature** - Massive open-source community providing libraries, tools, and support.

## How to Run Python Code?

Running Python code requires two things - code and a Python interpreter.

Code is something you can write in a text file - often a `.py` file. The Python interpreter is something you need to install on your computer.

## Reading Python Code

Writing always requires reading. This means that writing code will require reading it.

Many development tasks involve more reading than writing code.

### How is Python Read?

Like English, Python is read from top to bottom, left to right. Code is executed line by line. 

When reading you should start at the top, and read downwards.

### Hello World

The traditional place to start when learning a new programming language is with a `Hello World` program:

```python
print("Hello World")
```

This program demonstrates features of the Python language:

- **the built-in function** `print`, which prints to the screen,
- **the string type** `str`, which is the sequence of characters `"Hello World"`,
- **function execution**, where we run the `print("Hello World")` function using our `str` as input.

## Built-in Functions

Built-in functions are always available in Python. We do not need to define built-in functions - we can just use them.

Common built-in functions include:
- `print` which will print to the screen,
- `sum`, which will add all the elements of an iterable, 
- `len` which will measure the length of an iterable.

### Refactoring Hello World

**Refactoring is rewriting a program without changing its functionality**.

The goal of refactor is improving code quality, without breaking it or changing what the code does.

We can refactor our program by assigning the string `Hello World` to a variable `message`:

```python
message = "Hello World"
print(message)
```

This refactor demonstrates an additional feature of the Python programming language - **variable assignment**, where we assign the string `Hello World` to the variable `message`.

Whether you think our refactored program is an improvement depends on your preferences as a developer.

## For Loops

**Looping is the process of running the same thing many times**.  

Looping is an example of iteration, and is a core programming concept.  Many programming languages support loops that can repeat logic on each of the things.

### Iterable Objects in Python

An iterable thing is a sequence of things. 

In Python, objects that can be iterated over are iterable. The `list`, `dict` and `str` are all iterable.

What things are in an iterable depends on the iterable.  For a `list`, the things are the items in the list.  For a `str`, the things are the characters in the string.

### For Loops in Python

In Python, we can iterate using a `for thing in things:` syntax. 

The length of the for loop is determined by the length of `things`.  

Its length will determine how many times our for loop runs:

```python
size = 4
for n in range(size):
    print(f"loop position {n} of {size}")
print("loop is done!")
```

This program demonstrates:

- **the built-in** `range()`, which to create an iterable to loop over,
- **iteration** of a `for` loop 4 times,
- **f-string formatting** of the string `f"{n} of {size}"`, which creates strings like `2 of 4`,
- **white space indentation**, which controls which code runs in each loop.

## Scope

**Scope is the context in which a line of code executes**.

Scope separates parts of a computer program, creating independent, isolated pockets of space.

These different pockets of space become areas where we can limit access to variables and data, allowing us to make parts of the program run without getting in the way of other parts.

The program below defines the variable `x` twice - once inside the `main` function and once outside the `main` function.

These two identically named variables `x` can exist alongside each other in the same program, but not at the same time. 

They exist in different scopes:

```python
def main():
    x = 20
    print(f"function main scope, {x=}")

x = 10
print(f"global scope, {x=}")
main()
```

The program above demonstrates:

- **function definition** `def`, which defines the `main()` function,
- **variable assignment** of `x` inside two different scopes,
- **f-string formatting** of the string `f"global scope, {x=}"`, which creates strings like `global scope, x=10`,
- **function execution** of the `main` function.

Scope is important in Python as it is how we define what code runs in for loops and inside functions.

## Whitespace Indentation

One of Python's defining features is the use of white space to manage scope.  

Other languages like C or Javascript use characters like `{ }` and `;` to control scope - Python uses whitespace.

### Both Space and Tab are Whitespace

Both the TAB and space key on your keyboard and the TAB or space characters in a text file are different characters, but they appear the same on your screen as blank, white space. In Python, both the space and tab characters are considered whitespace, and indentation levels are determined by the number of whitespace characters at the beginning of a line. It doesn't matter whether they are spaces or tabs, but they shouldn't be mixed.

It's best practice to use only spaces for indentation to maintain consistency across different editors and systems. Many text editors and integrated development environments (IDEs) can convert tabs to spaces automatically. You can also configure your TAB key to input space characters instead of a single TAB character, or set it to enter 4 spaces when pressed. The Python Style Guide (PEP 8) recommends four spaces per indentation level for readability and consistency.

The Python interpreter is strict about indentation and will raise an IndentationError if there's a mismatch in indentation levels. This can happen when mixing spaces and tabs, or when the number of spaces used for indentation is inconsistent. If your text editor is set up correctly, you won't need to worry about this, as pressing the TAB key will insert spaces.

## Conditional Logic

**Conditional logic gives computer programs the ability to branch**.

Branching a computer program means we can choose different things to happen based on the values of variables.

### Logical Conditions

In Python we can use the equality check `==` to compare two objects.

`==` resolves to the boolean `bool` type, which can be either `True` or `False`:

```python
print(1 == 1)
print(1 == 2)
```

We can do a few kinds of conditionals in Python:

- equalities with `==`,
- inequalities with `>`, `>=`, `<=`, `<`,
- `in` to check if something is in an iterable,
- `is` to check if one object is the same as another.

### If Statements

We can use this condition in an `if` statement:

```python
if True:
    print("condition is true")

if (2 == 2):
    print("condition is true")

if not (1 == 2):
    print("condition is not true")
```

### Truth versus Falsy

**Truthiness is a property of a Python object**. 

All Python objects are either truthy or falsy (but not both).

#### Truthy

A truthy object will act the same as the Boolean `True` object - it will evaluate to `True` in contexts like `if` statements:

```python
if True:
    print("the boolean True is truthy")

if [1, 2, 3]:
    print("a full list is truthy")

if 10:
    print("the integer 10 is truthy")

if "a string":
    print("`a string` is truthy")
```

#### Falsy

A falsy statement will not trigger an `if` condition:

```python

if None:
    print(f"this will never be printed")

if []:
    print(f"this will never be printed")

if 0:
    print(f"this will never be printed")

if "":
    print(f"this will never be printed")
```

Relying on truthiness in `if` statements can be a source of subtle errors, but results in clean, Pythonic code.

## While Loops

**A while loop combines iteration and conditional statements**.

A while loop runs and terminates based on a conditional:

```python
# initialize our counter at zero
counter = 0

# a while loop that runs until our counter is greater than 3
while counter < 3:
    # iterate up our counter
    counter += 1
    # print the counter
    print(f"counter: {counter}")
```

The state that the conditional relies upon (here the variable `counter`) is updated each time through the loop.  

**If the condition is never met, then the loop becomes an infinite loop**. 

An infinite loop is a bug where a program will never finish.

## Asserts

**Assert statements check for correctness in your code**.

An assert allows you to check a conditional expression (like `x == 10`), and raise an exception if the condition is not met.  An exception is an error.

An assert is a way to test something - it's similar to the idea of an `if` - like an `if`, an assert will evaluate based on a truthy or falsy conditional.

The basic syntax of an assert statement is:

```python
assert condition, "optional error message"
```

A useful feature of an assert is being able to print a custom message when it fails:

```python
assert 1 == 0, "this assert failed because 1 is not equal to 0"
```

### When to Use Assert Statements

Use assert statements when you want to check something in your code.  

Data science examples of using asserts include:

- checking that our train and test features have the same number of columns,
- asserting that our train set has more data than our test set,
- checking that a column is in a dataframe.

## Lists

### Lists are for Sequential Data

A data structure stores and organizes data in a computer program.  

**The list is an ordered data structure**. Each of the items in the list has a position relative to all the other items.  

Lists are good when we have data that is ordinal or sequential, where things come in a sequence, one after the other.

### Create a List

We can create an instance of a list using either `[]` or `list`:

```python
data = [0, 1, 2]
print(data)

data = list([4, 5, 6])
print(data)
```

### Add Elements to a List

We can add elements to our list - we can do this with `.append()`

```python
data = []
for n in range(3):
    data.append(n)
print(data)
```

`.append` adds data to the list **in-place** and returns `None`. 

If instead we assigned our variable `data` to the output of `.append`, we would lose our variable reference to the list - a common mistake:

```python
data = [0, 1, 2]
data = data.append(3)
print(data is None)
```

### Select Elements of a List

We can select elements of the list using the `[]` syntax.

We can use `[0]` to select the first element:

```python
data = [4, 40, 400]
assert data[0] == 4
assert data[1] == 40
assert data[2] == 400
```

And `[-1]` to select the last element:

```python
data = [4, 40, 400]
assert data[-1] == 400
assert data[-2] == 40
assert data[-3] == 4
```

### Measuring the Length of a List

Other common list operations include measuring the length (the number of elements in the list) using the Python built-in `len`:

```python
data = [0, 1, 2]
assert len(data) == 3
```

## Dictionaries

### Dictionaries are for Named Data

A data structure stores and organizes data in a computer program.  

The dictionary is a data structure that refers to data by name. Each **value** (data) in the dictionary has a **key** (name).

### Creating a Dictionary

We can instantiate a dictionary using either `dict` or `{}`:

```python
data = {"message": "hello"}
print(data)
```

### Selecting Data from a Dictionary

We can select values of our dictionary by key using `[]`:

```python
data = {"message": "hello"}
print(data["message"])
```

### Adding Data to a Dictionary

We can add elements to our dictionary by assigning a key to a value:

```python
data = {
  "message": "hello",
  "status": "priority"
}
assert data["status"] == "priority"
print(data)
```

### Iterating over a Dictionary

We can iterate over the keys and values in a dictionary with `.items()`:

```python
data = {
  "message": "hello",
  "status": "priority"
}
for key, value in data.items():
    print(f"{key}: {value}")
```

You can also just iterate over the keys using `.keys()` or the values using `.values()`.

The dictionary has no order - you should never rely on the order of iteration when iterating over the keys, values or items in a dictionary.  If you want a particular order, use a list.

## Sets 

### Sets are for Unique Data

A data structure stores and organizes data in a computer program.  

The set is a data structure that holds unique values - each value only occurs once in the set.

### Creating a Set

Below we create a set using a list of four items - but as two are duplicates, our set only has three:

```python
data = set([0, 1, 2, 2])
assert len(data) == 3
print(data)
```

### Using a Set to Check Uniqueness

Sets are useful when we want to do anything around unique values.

We can check that there are no unique values in a list by comparing it's length with a set:

```python
data = [0, 1, 2, 2]
assert len(data) != len(set(data))

data = [0, 1, 2, 3]
assert len(data) == len(set(data))
print("all passed ^^")
```

## Functions

Functions are a tool used to organize and reuse code. They make code modular, reusable, and maintainable.

Functions allow us to organize, manage and structure the functionality of a computer program.

### Functions Can Be Reused

**A killer-feature of the function is that we can re-use it**.  

Executing a function many times allow us to write code once and use it many times. 

Good function design will avoid duplicated code. Duplicated code is bad because we need to update multiple places in a code base when we want to change only one thing.

We can define a function in Python by using the `def` keyword to **define the function name** `f` and inputs `x`, using **whitespace indentation** to define the scope of our function and using the `return` keyword to define **what our function returns**:

```python
def f(x):
    return x * x
```

The function `f(x)` is defined at the moment this code is executed, but it's not executed yet, it's just defined. 

We can execute this function using `function_name(inputs)`:

```python
def f(x):
    return x * x

print(f(2))
assert f(2) == 4
assert f(3) == 9
```

We can use a different name for our function by changing the word after the `def` keyword - below we write a function called `g` that performs the same task as `f`.

```python
def g(x):
    return x * x

print(g(2))
assert g(2) == 4
assert g(3) == 9
```

### Functions Can Take Multiple Inputs

Functions can also take multiple inputs, which can be defined in the parenthses after the function name:

```python
def add(a, b):
    return a + b
print(add(2, 3))
assert add(2, 3) == 5
```

### Function Inputs Can Have Default Values

Functions can also have default values for inputs, which means that the input does not have to be provided when the function is called. For example:

```python
def add(a, b=0):
    return a + b

print(add(2))
assert add(2) == 2
```

### Functions Can Return Multiple Outputs

Functions can also return multiple values, which can be done by separating the values with a comma. For example, a function could return the result of a calculation and a string message indicating the status of the calculation:

```python
def calculate_result(a, b):
    result = a + b
    message = "Calculation successful"
    return result, message

print(calculate_result(2, 3))
```

Or it could return a dictionary containing different pieces of information:

```python
def gather_data(a, b):
    data = {"result": a*b, "status": "success"}
    return data

print(gather_data(2,3))
```

## Classes

Classes are a tool used to organize and reuse code. 

Like a function, a Python class allows us to organize functionality.  **In addition to organizing functionality, a class also allows organizing data**.

A class can have both **attributes** (data) and **methods** (functionality).

Class attributes are often lower level data structures like strings, dictionaries or lists.

### Class Instances

**An instance of a class is an individual object created from that class, which has its own unique set of attributes and methods**. 

It can be thought of as a specific occurrence or realization of the general structure defined by the class.

Each instance can have its own state, behavior, and identity, and can be manipulated independently of other instances of the same class. Classes define the blueprint for objects, and instances are the actual objects created from that blueprint.

### Defining a Class

We can define a class using `class MathRobot` to define the class name, `def __init__(self, name)` as the method that runs when the class is created and `def method(self, argument)` to defines a custom method.

```python
class MathRobot:
    def __init__(self, name):
        self.name = name
        print(f"new instance of the MathRobot class called {self.name} created")

    def hello(self):
        print(f"hello from {self.name}")

    def add(self, x, y):
        return x + y

robot = MathRobot("issac")
```

After creating an instance of the class (here called `robot`), we can access the attributes of the class using the `.` syntax:

```python
print(robot.name)
```

We can also access the methods of the class in the same way that we call functions:

```python
robot.hello()
```

Additionally, classes can create and use class variables and class methods. Class variables are variables that are shared among all instances of a class, while instance variables are unique to each instance of a class.

```python
class MathRobot:
    robot_count = 0

    def __init__(self, name):
        self.name = name
        MathRobot.robot_count += 1
        print(f"new instance of the MathRobot class called {self.name} created")

    def hello(self):
        print(f"hello from {self.name}")

    def add(self, x, y):
        return x + y
    
    @classmethod
    def get_robot_count(cls):
        return cls.robot_count

robot1 = MathRobot("issac")
robot2 = MathRobot("robot2")
print(MathRobot.get_robot_count())
```

## Files

`pathlib` is part of the Python standard library.  It provides an object-oriented way of working with file and directory paths, and is available in Python 3.4.

The `pathlib.Path` object represents a file system path. This can be for either a file or a directory.

### Creating a `pathlib.Path` Object

You can create a `pathlib.Path` object by instantiating it with a string:

```python
from pathlib import Path

path = Path("./intro-to-python/main.py")
print(path)
```

### Check if a Path Exists

You can check if a path exists using `pathlib.Path.exists`:

```python
from pathlib import Path

if not Path("./intro-to-python/main.py").exists():
    print("main-fake.py doesn't exist")
```

### Separating Out a Path into Parts

One of the strengths of `pathlib` is the ability to separate out parts of the path as attributes of the `pathlib.Path` object:

```python
from pathlib import Path

path = Path("./intro-to-python/main.py")
assert path.name == "main.py"
assert path.stem == "main"
assert path.suffix == ".py"
assert path.parent == Path("./intro-to-python")
print(path)
```

### Joining Paths

Paths can be joined using the `/` syntax:

```python
from pathlib import Path

path = Path("./intro-to-python")
fi = path / "main.py"
assert fi.name == "main.py"
print(fi)
```

### Listing Files and Directories

We can use `pathlib` to list the files and directories in a given directory.  

The `pathlib.Path` object has a method called `iterdir()` which returns a list of `Path` objects for each file and directory in the given directory:

```python
from pathlib import Path

print(list(Path(".").iterdir()))
```

### Creating Directories

To create a new directory, you can use the `Path.mkdir()` which creates a new directory with the given name:

```python
from pathlib import Path

folder = Path("example_directory")
folder.mkdir()
print(list(Path(".").iterdir()))
```

## JSON

JSON (JavaScript Object Notation) is a human-readable data format written in text.

JSON is commonly used for data exchange, for example between a web application and a server.

A JSON object is represented in key-value pairs, where the keys are strings and the values can be of any data type, such as numbers, strings, booleans, arrays, and other objects:

```json
{
    "name": "John Smith",
    "age": 30,
    "isStudent": false,
    "courses": ["math", "history", "science"]
}
```

The `json` Python library provides `json.dumps()` to convert a Python object to a JSON string, and `json.loads()` to convert a JSON string to a Python object.

The suffix `s` in `json.loads` and `json.dumps` means string - that we are either loading from a string with `json.loads`, or transforming into a string with `json.dumps`, which dumps the object into a string.  

### Writing JSON Files

`json.dumps()` function is used to convert a Python object into a JSON string, and `Path.write_text()` method writes this string into a file.

```python
import json
from pathlib import Path

# define a Python object - a list of dictionaries
data = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]

# convert the Python object to a JSON formatted string
data_json = json.dumps(data)

# write the JSON string to a file using the Path object
file = Path("example.json")
file.write_text(data_json)
```

### Reading JSON Files

The `Path.read_text()` method is used to read the contents of a file as a string, and `json.loads()` function converts this string back into a Python object.

```python
import json
from pathlib import Path

# read the JSON string to a Python string
file_contents = file.read_text()

# convert the JSON string back into list of dictionaries
data_from_file = json.loads(file_contents)
print(data_from_file)
```

## Libraries

**A library is a collection of pre-written code that can be used to perform specific tasks**. 

Libraries can be imported and used to add functionality to the program without having to write the code from scratch.  

Python has a large ecosystem of libraries, available both from the standard library and from third-parties.

### Libraries in Python

**A Python library is formed of modules and packages**:

- A library is a collection of Python packages.
- A package is a collection of Python modules.
- A module is Python code written and saved into a `.py` file.

Consider this Python project that has:

- an entrypoint `main.py` script,
- a library `neulibrary`,
- two packages `package_one` and `package_two`,
- two modules `math` and `database`,
- two `__init__.py` to tell Python that our two directories are packages.

```shell-session
$ tree .
.
├── main.py
└── neulibrary
   ├── package_one
   │  ├── __init__.py
   │  └── math.py
   └── package_two
      ├── __init__.py
      └── database.py
```


{{< highlight shell-session >}}
$ tree .
.
├── main.py
└── neulibrary
   ├── package_one
   │  ├── __init__.py
   │  └── math.py
   └── package_two
      ├── __init__.py
      └── database.py
{{< / highlight >}}


### Importing Modules in Python

#### Importing an Entire Library

Libraries can be imported in a Python script by `import {library}`:

```python
import pathlib

print(pathlib)
```

#### Import Objects from a Library

We can also import specific objects from a library.  

These objects can be Python classes, functions or variables that point to lower level objects like strings or lists.

We can import objects using `from {library} import {thing}`:

```python
from pathlib import Path

print(Path)
```

#### Aliasing Objects on Import

A common pattern is to alias when importing - a library, module or object can be aliased on import using `import {library} as {alias}`:

```python
from pathlib import Path as PathObject

print(PathObject)
```

### The Standard Library

**The standard library in Python is a collection of libraries that are included with the Python programming language**. 

It includes a wide range of libraries that are available for use without the need for additional installation or setup. 

**Python's standard library is why Python is known as a batteries included programming language**.  Python includes a lot of functionality out of the box.

### What Standard Library Modules Should I Know?

Important standard library libraries to know include:

- `pathlib` - working with files and directories,
- `os` - working with the operating system,
- `json` - working with JSON data,
- `math` - mathematical operations,
- `random` - random number generation,
- `datetime` - working with dates and times.

Don't feel the need to go and study these libraries - just being aware of them and using them as you need is fine.

### Third Party Libraries

**Third party libraries are libraries that are not included by default**. They need to be installed before they can be used.

`pandas` is an open source, third party Python library - it's foundational for data professionals.  We will use it as an example third party library.

### Installing Third Party Libraries

Installing third party Python libraries is usually done with `pip`.  `pip` is a Python package manager that integrates with `PyPI` - an index of Python packages.

If you have installed Python locally, then you can access `pip` from a terminal as as shell program:

```shell-session
# install pandas using pip
$ pip install pandas
```

If you are in a notebook environment (or anything running iPython), you can use the `!` prefix (which will run a shell command inside your notebook):

```ipython
# install pandas using pip in an iPython notebook
!pip install pandas
```

This `!` prefix syntax is very useful within any environment running iPython (like a notebook) - you can also use it for any other shell command (not only `pip install`).

### Using Third Party Libraries

We can import a third party library the same as one from the standard library:

```python
import pandas

# print the pandas version
print(pandas.__version__)
```

A common pattern is to alias when importing - `pandas` is often aliased to `pd` on import using `import {module} as {alias}`:

The code below imports the `pandas` library, aliases it to a variable `pd`, and uses the built-in `dir` to show what we can do with our `pandas` module:

```python
import pandas as pd

# print the attributes of the pandas module
print(dir(pd))
```

`dir` is a useful function when you want to understand what you can do with any Python object - very useful when you want to explore what you can do with a third party library like `pandas` or `pandas.DataFrame`:

```python
import pandas as pd

# print the attributes of the pandas.DataFrame object
print(dir(pd.DataFrame))
```
