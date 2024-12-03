---
title: Python Libraries
summary: Install Python libraries with pip and import them into your code.
---

## Libraries in Python

**A library is a collection of pre-written code that can be used to perform specific tasks**. 

Libraries can be imported and used to add functionality to the program without having to write the code from scratch.  

Python has a large ecosystem of libraries.

## Modules, Packages and Libraries

**A Python library is formed of modules and packages**:

- A library is a collection of Python packages.
- A package is a collection of Python modules.
- A module is Python code written and saved into a `lang:shell-session:.py` file.

Consider this Python project that has:

- an entrypoint `lang:shell-session:main.py` script,
- a library `lang:shell-session:neulibrary`,
- two packages `lang:shell-session:package_one` and `lang:shell-session:package_two`,
- two modules `lang:shell-session:math` and `lang:shell-session:database`,
- two `lang:shell-session:__init__.py` to tell Python that our two directories are packages.

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


## Importing Modules in Python

### Importing an Entire Library

Libraries can be imported in a Python script by `import {library}`:

```pyrepl
import pathlib

print(pathlib)
```

### Import Objects from a Library

We can also import specific objects from a library.  

These objects can be Python classes, functions or variables that point to lower level objects like strings or lists.

We can import objects using `from {library} import {thing}`:

```pyrepl
from pathlib import Path

print(Path)
```

### Aliasing Objects on Import

A common pattern is to alias when importing - a library, module or object can be aliased on import using `import {library} as {alias}`:

```pyrepl
from pathlib import Path as PathObject

print(PathObject)
```

## Using the Standard Library

**The standard library in Python is a collection of libraries that are included with the Python programming language**. 

It includes a wide range of libraries that are available for use without the need for additional installation or setup. 

**Python's standard library is why Python is known as a batteries included programming language**.  Python includes a lot of functionality out of the box.

## What Standard Library Modules Should I Know?

Important standard library libraries to know include:

- `pathlib` - working with files and directories,
- `os` - working with the operating system,
- `json` - working with JSON data,
- `math` - mathematical operations,
- `random` - random number generation,
- `datetime` - working with dates and times.

Don't feel the need to go and study these libraries - just being aware of them and using them as you need is fine.

## Using Third Party Libraries

**Third party libraries are libraries that are not included by default**. They need to be installed before they can be used.

`pandas` is an open source, third party Python library - it's foundational for data professionals.  We will use it as an example third party library.

## Installing Third Party Libraries

Installing third party Python libraries is usually done with `lang:shell-session:pip`.  `lang:shell-session:pip` is a Python package manager that integrates with `PyPI` - an index of Python packages.

If you have installed Python locally, then you can access `lang:shell-session:pip` from a terminal as as shell program:

```shell-session
#  install pandas using pip
$ pip install pandas
```

If you are in a notebook environment (or anything running iPython), you can use the `!` prefix (which will run a shell command inside your notebook):

```ipython
#  install pandas using pip in an iPython notebook
!pip install pandas
```

This `!` prefix syntax is very useful within any environment running iPython (like a notebook) - you can also use it for any other shell command (not only `lang:shell-session:pip install`).

## Using Third Party Libraries

We can import a third party library the same as one from the standard library:

```pyrepl
import pandas

#  print the pandas version
print(pandas.__version__)
```

A common pattern is to alias when importing - `pandas` is often aliased to `pd` on import using `import {module} as {alias}`:

The code below imports the `pandas` library, aliases it to a variable `pd`, and uses the built-in `dir` to show what we can do with our `pandas` module:

```pyrepl
import pandas as pd

#  print the attributes of the pandas module
print(dir(pd))
```

`dir` is a useful function when you want to understand what you can do with any Python object - very useful when you want to explore what you can do with a third party library like `pandas` or `pandas.DataFrame`:

```pyrepl
import pandas as pd

#  print the attributes of the pandas DataFrame object
print(dir(pd.DataFrame))
```
