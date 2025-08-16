---
title: Hypermodern Python Toolbox 2023
description: Ten Python tools setting the standard in 2023.
date: 2023-02-25
competencies:
- Software Engineering

---

**Every Python developer is challenged by the size and velocity of the Python ecosystem** 😤

{{< img 
    src="/images/hypermodern-python-2023/hero.png"
    alt="Computer terminal in MC Escher style" 
    caption="{Prompt: 'a small computer terminal, in the style and layout of 'day and night' by of M.C. Escher, black and white', Seed: 4, Creator: Stable Diffusion 1}" 
>}}

This post provides clarity with the **Hypermodern Python Toolbox** - tools that are setting the standard for Python in 2023.

## Python 3.10

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
  File "/Users/adam/hypermodern-python/mistake.py", line 2, in <module>
    datas[0] = 2
NameError: name 'datas' is not defined. Did you mean: 'data'?
```

So much of programming is reading & responding error messages - these improvements are a great quality of life improvement for Python developers in 2023.

## pyenv & pyenv-virtualenv

The hardest thing about learning Python is learning to install & manage Python.  

Even senior developers can struggle with it, especially if Python is not their main language.

Working with Python requires being able to work both with different versions of Python and with different Python virtual environments.

![The xkcd classic commentary on the complex Python ecosystem.](/static/blog/hypermodern-python/python_environment_xkcd.png "The xkcd classic commentary on the complex Python ecosystem.")

**[pyenv](https://github.com/pyenv/pyenv) is a tool for managing different versions of Python**. It's an alternative to using miniconda or installing Python from a downloaded installer.

`$ pyenv versions` shows that three versions of Python are installed & managed by pyenv:

```shell-session
$ pyenv versions
3.7.9
3.8.13
3.10.5
```

Installing a specific version of Python is as simple as `$ pyenv install {version}`:

```shell-session
$ pyenv install 3.10.6
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Installing Python-3.10.6...
python-build: use tcl-tk from homebrew
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.10.6 to /Users/adam/.pyenv/versions/3.10.6
```

One trick with using pyenv is getting compiler flags correct - if you are having an trouble, take a look at this [installer script for Ubuntu](https://github.com/ADGEfficiency/dotfiles/blob/master/ubuntu/pyenv), [installer script for MacOS](https://github.com/ADGEfficiency/dotfiles/blob/master/macos/pyenv) and these [compiler flags](https://github.com/ADGEfficiency/dotfiles/blob/master/macos/pyenv-flags).


**[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is a tool for managing virtual environments in Python**. It's an alternative to venv or miniconda.  Virtual environments allow separate installations of Python to live side-by-side. 

pyenv-virtualenv plays well with our pyenv installations of Python. We can create a new virtual environment with `$ pyenv virtualenv {version} {name}`. 

Below we create a 3.10.6 Python virtual environment called `default`:

```shell-session
$ pyenv virtualenv 3.10.6 default
```

We now have a new virtual environment called `default` using Python version `3.10.6`:

```shell-session
$ pyenv versions
3.7.9
3.8.13
3.10.5
3.10.6
3.10.6/envs/default
```

*Tip - create a `.python-version` file to automatically switch to a pyenv-virtualenv virtual environment when you enter a directory.*

## Poetry

**[Poetry](https://python-poetry.org/docs/basic-usage/) is a tool for managing Python dependencies and packages**. It's an alternative to pip. Both pip and Poetry are used to install and upgrade third party packages.

There is not a one-to-one mapping between the files used by pip and Poetry.

Pip uses two files to manage a Python package:

1. `requirements.txt` - a list of Python dependencies,
2. `setup.py` - a Python script that describes our package.

Poetry uses two different files:

1. `pyproject.toml` to describe our Python package,
2. `poetry.lock` to define and lock all dependencies - similar to the output of `$ pip freeze`.

These two files are can be generated automatically - `poetry.lock` is only ever generated automatically.  

Poetry has two ways to start a new project:

1. `$ poetry new` - if you are starting from scratch,
2. `$ poetry init` - if you are adding Poetry to an existing project.

We can create a `pyproject.toml` for a project in an interactive way by first installing Poetry with pip, then running `$ poetry init` to create a `pyproject.toml`:

```shell-session
$ pip install -q poetry; poetry init
This command will guide you through creating your pyproject.toml config.

Package name [general]:  general
Version [0.1.0]:
Description []:
```

After running through the interactive session (where we specify our Python version and add the package mypy), we end up with a `pyproject.toml`:

```toml {title = "pyproject.toml"}
[tool.poetry]
name = "general"
version = "0.1.0"
authors = ["Adam Green <adam.green@adgefficiency.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
mypy = "^0.971"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

If we didn't add any dependencies we needed during the generation of `pyproject.toml`, we can add packages using:

```shell-session
$ poetry add mypy
```

At this point we have added but not installed our mypy dependency - we can do so with `poetry install`:

```shell-session
$ poetry install
Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file

Package operations: 4 installs, 0 updates, 0 removals

  • Installing mypy-extensions (0.4.3)
  • Installing tomli (2.0.1)
  • Installing typing-extensions (4.3.0)
  • Installing mypy (0.971)
```

The install operation also creates a `poetry.lock` file:

```shell-session
$ head -n 12 poetry.lock
[[package]]
name = "mypy"
version = "0.971"
description = "Optional static typing for Python"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
mypy-extensions = ">=0.4.3"
tomli = {version = ">=1.1.0", markers = "python_version < \"3.11\""}
typing-extensions = ">=3.10"
```

While Poetry is great, we still need pip. Poetry itself needs to be installed with pip.

Poetry and pip play well together - we can export our dependencies to a pip compatible `requirements.txt`:

```shell-session
$ poetry export -f requirements.txt > requirements.txt
```

*Watch out for - Poetry has the ability to create it's own virtual environments. It's common to turn this off in some environments - such as inside Docker images, where you want to use the default installation of Python.*

## Black & isort

**[Black](https://github.com/psf/black) & [isort](https://github.com/PyCQA/isort) are tools to format Python code** - they are alternatives to tools like autopep8.

The code below in `bad_format.py` is poorly formatted:

```python { title = "bad_format.py" }
data=[1, 4, 8]
data[0] = 2
```

We can run Black from a terminal, pointing it at `bad_format.py`:

```shell-session
$ black bad_format.py
reformatted test.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

The result is that our `bad_format.py` now has nicely formatted Python code:

```python { title = "bad_format.py" }
data = [1, 4, 8]
data[0] = 2
```

The code below in `bad_imports.py` has imports that are out of order alphabetically and grouped incorrectly:

```python { title = "bad_imports.py" }}
import pandas as pd
import random
import collections
data = [1, 4, 8]
data[0] = 2
```

We can use isort to fix these imports:

```shell-session
$ isort bad_imports.py
Fixing /Users/adam/dss/notes/content/ideas/temp/test.py
```

Our fixed file has nicely formatted imports:

```python { title = "bad_imports.py" }}
import collections
import random

import pandas as pd

data = [1, 4, 8]
data[0] = 2
```

*Tip - it's common to run these formatters on file save or in continuous integration - consider adding a format on save to your text editor.*

## Ruff

**[Ruff](https://github.com/charliermarsh/ruff) is a Python linter** - it's alternative to Flake8.  Ruff will check code based on rules - it will not format code like Black and isort.

Ruff's big thing is being written in Rust - this makes it fast.  When used with Black to ensure consistent code style, Ruff covers much of the Flake8 rule set, along with other rules such as isort.

A great way to use Ruff is with the defaults and check everything.  

The code below has three problems - we use an undefined variable `datas`, it has imports in the wrong place and imports something we don't use:

```python { title = "ruff.py" }
data = datas[0]
import collections
```

Running Ruff in the same directory points out the issues:

```shell-session
$ ruff check .
ruff.py:1:8: F821 Undefined name `datas`
ruff.py:2:1: E402 Module level import not at top of file
ruff.py:2:8: F401 [*] `collections` imported but unused
Found 3 errors.
[*] 1 potentially fixable with the --fix option.
```

*Tip - Ruff is quick enough to run on file save during development - your text editor will allow this somehow!*

## mypy

**[mypy](http://www.mypy-lang.org/) is a tool for enforcing type safety in Python** - it's an alternative to type declarations remaining as only unexecuted documentation.

Recently Python has undergone a similar transition to the Javascript to Typescript transition, with static typing being improved in the standard library and with third party tooling.  Statically typed Python is the standard for many teams developing Python in 2023.

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

## zxpy

**[zxpy](https://github.com/tusharsadhwani/zxpy) is a tool for running shell commands inside Python**.  

We will use the [Github CLI](https://cli.github.com/manual/) as a source of shell commands - it is a nice way to get data about your code on Github. 

Below we get all the issues for the mypy repository on Github:

```shell-session
$ gh search issues --repo python/mypy --json title | jq > issues.json
$ head -n 7 issues.json
[
  {
    "title": "Not evaluating Union[X, Y] from Type[Union[X, Y]] over (Type[T]) -> T function"
  },
  {
    "title": "Detect `Any` used as a metaclass"
  },
```

This JSON array (or list of dictionaries in Python) is data we want to work on in Python. We could read the `issues.json` file in Python - this would involve running the shell command and Python interpreter separately.

With zxpy we can run the shell command right in Python - using the `~"shell-command"` syntax:

```python {title = "zxpy_eg.py"}
import json

issues = json.loads(~"gh search issues --repo python/mypy --json title")
print(f"{len(issues)} issues")
print(f" first {issues[0]}")
print(" last {issues[-1]}")
```

We can then run this script using the zxpy interperter:

```shell-session
$ zxpy zxpy_eg.py
30 issues
 first {'title': 'Cannot infer type of generic attributes in `match` statements when inheritance is involved'}
 last {'title': 'Parent modules are added as a dependency'}
```

*Tip* - f-strings in zxpy are written `~f"gh search issues --repo {repo}`.


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
