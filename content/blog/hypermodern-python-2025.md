---
title: Hypermodern Python Toolbox
description: Python tools setting the standard in 2025.
date: 2024-12-05
tags:
- Python
- Hypermodern

---

**Every Python developer is challenged by the size and velocity of the Python ecosystem** 😤

![Prompt: 'a small computer terminal, in the style and layout of 'day and night' by of M.C. Escher, black and white'. Seed: 4.<br />Created with Stable Diffusion 1.](/static/blog/hypermodern-python/hero.png "Prompt: 'a small computer terminal, in the style and layout of 'day and night' by of M.C. Escher, black and white'. Seed: 4.<br />Created with Stable Diffusion 1.")

This post provides clarity with the **Hypermodern Python Toolbox** - tools that are setting the standard for Python in 2025.

## Python 3.12

Both 3.11 and 3.12 have brought performance improvements to Python.

- better debugging?
- better tracebacks
- Self for type hinting

---

**Python 3.10 added better error messages** - improving the information available for developers during development and debugging.

The code below has a mistake. We want to assign a value to the first element of `data`, but the code refers to a non-existent variable `datas`:

```python { title = "mistake.py" }
data = [1, 4, 8]
#  the variable datas does not exist!
datas[0] = 2
```

With older versions of Python, this results in an error traceback that points out that the variable `datas` doesn't exist:

```shell-session
$ python --version
3.8.13

$ python mistake.py
Traceback (most recent call last):
  File "mistake.py", line 2, in <module>
    datas[0] = 2
NameError: name 'datas' is not defined
```

Python 3.10 takes it's diagnosis one step further and also offers a solution that the variable should be called `data` instead:

```shell-session
$ python --version
3.10.6

$ python mistake.py
Traceback (most recent call last):
  File "/Users/adam/hypermodern-python-2022/mistake.py", line 2, in <module>
    datas[0] = 2
NameError: name 'datas' is not defined. Did you mean: 'data'?
```

So much of programming is reading & responding error messages - these improvements are a great quality of life improvement for Python developers in 2025.

## uv

The hardest thing about learning Python is learning to install & manage Python.  

Even senior developers can struggle with it, especially if Python is not their main language.

Working with Python requires being able to work both with different versions of Python and with different Python virtual environments.

![The xkcd classic commentary on the complex Python ecosystem.](/static/blog/hypermodern-python/python_environment_xkcd.png "The xkcd classic commentary on the complex Python ecosystem.")

**[uv]() is a tool for managing different versions of Python**. It's an alternative to using pyenv, miniconda or installing Python from a downloaded installer.

**uv is also a tool for managing virtual environments in Python**. It's an alternative to venv or miniconda.  Virtual environments allow separate installations of Python to live side-by-side.

**uv is also a tool for managing Python dependencies and packages**. It's an alternative to pip. Both pip and Poetry are used to install and upgrade third party packages.

*Tip - create a `.python-version` file to automatically switch to a pyenv-virtualenv virtual environment when you enter a directory.*

## ruff

**[Ruff]() is a tool to lint and format Python code** - it is an alternatives to tools like autopep8.



*Tip - Ruff is quick enough to run on file save during development - your text editor will allow this somehow!*

## mypy

**[mypy](http://www.mypy-lang.org/) is a tool for enforcing type safety in Python** - it's an alternative to type declarations remaining as only unexecuted documentation.

Recently Python has undergone a similar transition to the Javascript to Typescript transition, with static typing being improved in the standard library and with third party tooling.  Statically typed Python is the standard for many teams developing Python in 2025.

The code below in `mypy_error.py` has a problem - we attempt to divide a string by `10`:

```python { title = "mypy_error.py" }
def process(user):
    #  line below causes an error
    user['name'] / 10

user = {'name': 'alpha'}
process(user)
```

We can catch this error by running mypy - catching the error without actually executing the Python code:

```shell-session
$ mypy --strict mypy_error.py
mypy_error.py:1: error: Function is missing a type annotation
mypy_error.py:5: error: Call to untyped function "process" in typed context
Found 2 errors in 1 file (checked 1 source file)
```

These first errors are because our Python code has zero typing - let's add two type annotations:

1. `user: dict[str,str]` - `user` is a dictionary with strings as keys and values,
2. `-> None:` - the `process` function returns None.

```python { title = "mypy_intermediate.py"}
def process(user: dict[str,str]) -> None:
    user['name'] / 10

user = {'name': 'alpha'}
process(user)
```

Running mypy on `mypy_intermediate.py`, mypy points out the error in our code:

```shell-session
$ mypy --strict mypy_intermediate.py
mypy_fixed.py:2: error: Unsupported operand types for / ("str" and "int")
Found 1 error in 1 file (checked 1 source file)
```

This is a test we can run without writing any specific test logic - very cool!

Static type checking will catch some bugs that many unit test suites won't.  Static typing will check more paths than a single unit test often does - catching edge cases that would otherwise only occur in production.

*Tip - add mypy as an additional layer of testing to your test suite.*

## pydantic

**[pydantic](https://pydantic-docs.helpmanual.io/) is a tool for organizing and validating data in Python** - it's an alternative to using dictionaries or dataclasses.

pydantic is part of Python's typing revolution - pydantic's ability to create custom types makes writing typed Python a joy.

pydantic uses Python type hints to define data types. Imagine we want a user with a `name` and `id`:

```python
import uuid

users = [
    {'name': 'alpha', 'id': str(uuid.uuid4())},
    {'name': 'beta'},
    {'name': 'omega', 'id': 'invalid'}
]
```

We could model this with pydantic - introducing a class that inherits from `pydantic.BaseModel`:

```python
import uuid
import pydantic

class User(pydantic.BaseModel):
    name: str
    id: str = None

users = [
    User(name='alpha', 'id'= str(uuid.uuid4())),
    User(name='beta'),
    User(name='omega', id='invalid'),
]
```

A strength of pydantic is validation - we can introduce some validation of our user ids - below checking that the `id` is a valid GUID - otherwise setting to `None`:

```python
import uuid
import pydantic

class User(pydantic.BaseModel):
    name: str
    id: str = None

    @pydantic.validator('id')
    def validate_id(cls, user_id):
        try:
            user_id = uuid.UUID(user_id, version=4)
            print(f"{user_id} is valid")
            return user_id
        except ValueError:
            print(f"{user_id} is invalid")
            return None

users = [
    User(name='alpha', id= str(uuid.uuid4())),
    User(name='beta'),
    User(name='omega', id='invalid'),
]
[print(user) for user in users]
```

Running the code above, our pydantic model has rejected one of our ids - our `omega` has had it's original ID of `invalid` rejected and ends up with an `id=None`:

```shell-session
$ python pydantic_eg.py
45f3c126-1f50-48bf-933f-cfb268dca39a is valid
invalid is invalid
name='alpha' id=UUID('45f3c126-1f50-48bf-933f-cfb268dca39a')
name='beta' id=None
name='omega' id=None
```

These pydantic types can become the primitive data structures in your Python programs (instead of dictionaries) - making it eaiser for other developers to understand what is going on.

*Tip - you can generate Typescript types from pydantic models - making it possible to share the same data structures with your Typescript frontend and Python backend.*

## Typer

**[Typer](https://typer.tiangolo.com/) is a tool for building command line interfaces (CLIs) using type hints in Python** - it's an alternative to sys.argv or argparse.

We can build a Python CLI with Poetry and Typer by first creating a Python package with Poetry, adding `typer` as a dependency).

Here we use `$ poetry new` to create a new Poetry project from scratch:

```shell-session
$ poetry new general
$ tree
.
└── general
    ├── README.md
    ├── general
    │   └── __init__.py
    ├── pyproject.toml
    └── tests
        └── __init__.py
```

We then add a Python file `./general/cli.py` with our Typer CLI:

```python { title = "./general/cli.py" }
import typer

def main(name: str) -> None:
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)
```

We can now run this CLI by running `python ./general/cli.py`:

```shell-session
$ python ./general/cli.py omega
Hello omega
```

Typer gives us a `--help` flag for free:

```shell-session
$ python general/cli.py --help
Usage: cli.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.
```

We can take this one step further, by adding a script to our `pyproject.toml`. `general-cli` will now point towards the `main` function in `general.cli`:

```toml {title = "pyproject.toml"}
[tool.poetry.scripts]
general-cli = "general.cli:main"
```

This then allows us to run our Typer CLI using `$ poetry run general-cli`:

```shell-session
$ poetry run general-cli zeta
hello zeta
```

*Tip - you can create nested CLI groups using commands and command groups.*

## Rich

**[Rich](https://rich.readthedocs.io/en/stable/) is a tool for printing pretty text to a terminal** - it's an alternative to the monotone terminal output of most Python programs.

One of Rich's most useful features is pretty printing of color and emojis:

```python
import rich

user = {'name': 'omega', 'id': 'invalid'}
print(f" normal printing\nuser {user}\n")
rich.print(f" :wave: [bold blue]rich[/] [green]printing[/]\nuser {user}\n")
```

![](/static/blog/hypermodern-python/rich.png)

If you are happy with Rich you can simplify your code by replacing the built-in print with the Rich print:

```python
from rich import print
print('this will be printed with rich :clap:')
```

![](/static/blog/hypermodern-python/rich2.png)

*Tip - Rich offers much more than color and emojis - including displaying tabular data and better trackbacks of Python errors.*

## Polars

## Pandera

## DuckDB

## Streamlit

## HTMX

## The Toolbox

The **Hypermodern Python Toolbox** is:

- [**Python 3.10**](https://www.python.org/downloads/release/python-3100/) for better error messages,
- [**pyenv**](https://github.com/pyenv/pyenv) & [**pyenv-virtualenv**](https://github.com/pyenv/pyenv-virtualenv) for managing Python versions and virtual environments,
- [**Poetry**](https://python-poetry.org/docs/) for managing Python packages & dependencies,
- [**Black**](https://black.readthedocs.io/en/stable/) & [**isort**](https://pycqa.github.io/isort/) for formatting Python code,
- [**Ruff**](https://github.com/antonmedv/ruff) for linting Python code,
- [**mypy**](http://mypy-lang.org/) for static type checking,
- [**pydantic**](https://pydantic-docs.helpmanual.io/) for organizing & validating data,
- [**Typer**](https://typer.tiangolo.com/) for typed CLIs,
- [**zxpy**](https://github.com/tusharsadhwani/zxpy) for running shell commands inside Python,
- [**Rich**](https://rich.readthedocs.io/en/stable/) for pretty printing to the terminal.
