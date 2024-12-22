---
title: Hypermodern Python Toolbox - 2025
description: Python tools setting the standard in 2025.
date: 2024-12-05
tags:
- Python
- Hypermodern

---

**Every Python developer is challenged by the size and velocity of the Python ecosystem** 😤

![Prompt: 'a small computer terminal, in the style and layout of 'day and night' by of M.C. Escher, black and white'. Seed: 4.<br />Created with Stable Diffusion 1.](/static/blog/hypermodern-python/hero.png "Prompt: 'a small computer terminal, in the style and layout of 'day and night' by of M.C. Escher, black and white'. Seed: 4.<br />Created with Stable Diffusion 1.")

This post provides clarity with a **Hypermodern Python Toolbox** - tools that are setting the standard for Python in 2025.

## Python 3.11

Both 3.11 and 3.12 have brought performance improvements to Python. We choose 3.11 here because 3.12 is still a bit unstable with many popular libraries.

**Python 3.11 added better tracebacks** - the exact location of the error is pointed out.  This improves the information available to you during development and debugging.

The code below has a mistake. We want to assign a value to the first element of `data`, but the code refers to a non-existent variable `datas`:

```python { title = "mistake.py" }
data = [1, 4, 8]
# the variable datas does not exist!
datas[0] = 2
```

With pre 3.10 versions of Python, this results in an error traceback that points out that the variable `datas` doesn't exist:

```shell-session {shelldocwhatever}
$ uv run --python 3.9 --no-project mistake.py
```

```
Traceback (most recent call last):
  File "/Users/adamgreen/data-science-south-neu/mistake.py", line 3, in <module>
    datas[0] = 2
NameError: name 'datas' is not defined
```

Python 3.11 takes it's diagnosis two steps further and also offers a solution that the variable should be called `data` instead, and points out where on the line the error occurred:

```shell-session {shelldocwhatever}
$ uv run --python 3.11 --no-project mistake.py
```

```
Traceback (most recent call last):
  File "/Users/adamgreen/data-science-south-neu/mistake.py", line 3, in <module>
    datas[0] = 2
    ^^^^^
NameError: name 'datas' is not defined. Did you mean: 'data'?
```

So much of programming is reading & responding error messages - these improvements are a great quality of life improvement for Python developers in 2025.

## uv

The hardest thing about learning Python is learning to install & manage Python. Working with Python requires being able to work both with different versions of Python and with different Python virtual environments.

Even senior developers can struggle with the complexity of managing Python, especially if it is not their main language.

![The xkcd classic commentary on the complex Python ecosystem.](/images/hypermodern-2025/python_environment_xkcd.png)

**[uv]() is a tool for managing different versions of Python**. It's an alternative to using pyenv, miniconda or installing Python from a downloaded installer.

```shell-session
$ uv run --python 3.13 --no-project python -c "print('hello')"
hello
```

**uv is also a tool for managing virtual environments in Python**. It's an alternative to venv or miniconda.  Virtual environments allow separate installations of Python to live side-by-side.

```shell-session
$ uv venv --python 3.11
```

**uv is also a tool for managing Python dependencies and packages**. It's an alternative to pip. Both pip and Poetry are used to install and upgrade third party packages.

```toml {title = "pyproject.toml"}
[project]
name = "hypermodern"
version = "0.0.1"
requires-python = ">=3.11,<3.12"
dependencies = [
    "pandas>=2.0.0",
    "requests>=2.31.0"
]

[project.optional-dependencies]
test = ["pytest>=7.0.0"]
```

```shell-session
$ uv venv --python 3.11
```

```
warning: `VIRTUAL_ENV=/Users/adamgreen/.venv` does not match the project environment path `.venv` and will be ignored
Using CPython 3.11.9 interpreter at: /Users/adamgreen/.nix-profile/bin/python3.11
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

```shell-session
$ uv pip install -r pyproject.toml
Resolved 11 packages in 1.69s
Installed 11 packages in 61ms
 + certifi==2024.12.14
 + charset-normalizer==3.4.0
 + idna==3.10
 + numpy==2.2.0
 + pandas==2.2.3
 + python-dateutil==2.9.0.post0
 + pytz==2024.2
 + requests==2.32.3
 + six==1.17.0
 + tzdata==2024.2
 + urllib3==2.2.3
```


```shell-session
$ uv lock
```

```
Resolved 17 packages in 5ms
```


Running tools:

```shell-session
$ uv tool run --python 3.11 pytest 
```

```shell-session
$ uv tool run --python 3.12 pytest 
```

This will add programs that are available outside of a virtual environment:

```shell-session
$ which pytest
/Users/adamgreen/.local/bin/pytest
```

*Tip - create a `.envrc` with direnv to automatically switch to the correct Python version when you enter a directory.*

## ruff

**[Ruff]() is a tool to lint and format Python code** - it is an alternatives to tools like autopep8.

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

Recently Python has undergone a similar transition to the Javascript to Typescript transition, with static typing being improved in the standard library and with third party tooling.  Statically typed Python is the standard for many teams developing Python in 2025.

`mypy_error.py` has a problem - we attempt to divide a string by `10`:

```python { title = "mypy_error.py" }
def process(user):
    # line below causes an error
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

These first errors are because our code has no typing - let's add two type annotations:

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

*Tip - Use `reveal_type(variable)` in your code when debugging type issues. mypy will show you what type it thinks a variable has.*

## pydantic

TODO mention pydantic 2.0

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

```python { title = "pydantic_eg.py" }
import uuid
import pydantic

class User(pydantic.BaseModel):
    name: str
    id: str = None

    @pydantic.validator('id')
    def validate_id(cls, user_id:str ) -> str | None:
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

Here we use `$ uv init` to create a new project from scratch:

```shell-session
$ uv init --name typer-demo
$ uv venv
```

```shell-session
$ tree .
```

```
├── .python-version
├── .venv
│   ├── .gitignore
│   ├── bin
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── activate.nu
│   │   ├── activate.ps1
│   │   ├── activate_this.py
│   │   ├── deactivate.bat
│   │   ├── pydoc.bat
│   │   ├── python ⇒ /Users/adamgreen/.nix-profile/bin/python3.11
│   │   ├── python3 ⇒ python
│   │   └── python3.11 ⇒ python
│   ├── CACHEDIR.TAG
│   ├── lib
│   │   └── python3.11
│   │       └── site-packages
│   │           ├── _virtualenv.pth
│   │           └── _virtualenv.py
│   └── pyvenv.cfg
├── hello.py
├── pyproject.toml
└── README.md
```

```shell-session
$ uv add typer
Resolved 26 packages in 1.79s
Prepared 8 packages in 3.11s
Installed 8 packages in 14ms
 + click==8.1.7
 + markdown-it-py==3.0.0
 + mdurl==0.1.2
 + pygments==2.18.0
 + rich==13.9.4
 + shellingham==1.5.4
 + typer==0.15.1
 + typing-extensions==4.12.2
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
# TODO TODO
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
rich.print(f" :wave: rich printing\nuser {user}\n")
```

```
 normal printing
user {'name': 'omega', 'id': 'invalid'}

 👋 rich printing
user {'name': 'omega', 'id': 'invalid'}
```

If you are happy with Rich you can simplify your code by replacing the built-in print with the Rich print:

```python
from rich import print

print('this will be printed with rich :clap:')
```

```
this will be printed with rich 👏
```

*Tip - Rich offers much more than color and emojis - including displaying tabular data and better trackbacks of Python errors.*

## Polars

**Polars is a tool for fast data manipulation and analysis in Python** - it's an alternative to Pandas.

Built in Rust, Polars offers exceptional performance through query optimization and parallelization.

In eager-execution frameworks like Pandas, each data transformation is run without knowledge of what came before and after. By allowing data to be evaluated lazily, Polars can optimize across a series of data transformations.  

The example below shows query optimization with a toy dataset with three columns:

```python
import polars as pl

df = pl.DataFrame({
    'date': ['2025-01-01', '2025-01-02', '2025-01-03'],
    'sales': [1000, 1200, 950],
    'region': ['North', 'South', 'North']
})
```

We can then chain operations together and run them in one optimized query.  Below we chain together column creation and aggregation:

```python
result = (df
    # start lazy evaluation
    # Polars won't execute anything until .collect()
    .lazy()
    # with columns adds new columns
    .with_columns([
        # Parse string to date
        pl.col('date').str.strptime(pl.Date).alias('date'),
        # Add a new column with running total
        pl.col('sales').cum_sum().alias('cumulative_sales')
    ])
    .group_by('region')
    .agg([
        pl.col('sales').mean().alias('avg_sales'),
        pl.col('sales').count().alias('n_days')
    ])
    # run the optimized query
    .collect()
)

print(result)
```

```
shape: (2, 3)
┌────────┬───────────┬────────┐
│ region ┆ avg_sales ┆ n_days │
│ ---    ┆ ---       ┆ ---    │
│ str    ┆ f64       ┆ u32    │
╞════════╪═══════════╪════════╡
│ North  ┆ 975.0     ┆ 2      │
│ South  ┆ 1200.0    ┆ 1      │
└────────┴───────────┴────────┘
```

*Tip - Polars has powerful string operations with `pl.col("column").str`.*

## Pandera

Pandera is a tool for data validation and testing of Pandas and Polars - it's an alternative to Great Expectations or assert statements.

Pandera allows you to define schemas for your data, which can then be used to validate, clean, and transform your data. By defining schemas upfront, Pandera can catch data issues before they propagate through your analysis pipeline.

First let's create a schema for some sales data:

```python
import polars as pl
import pandera as pa
from pandera.polars import DataFrameSchema, Column

schema = DataFrameSchema(
    {
        "date": Column(pa.DateTime, nullable=False, coerce=True, title="Date of sale"),
        "sales": Column(
            float,
            checks=[pa.Check.greater_than(0), pa.Check.less_than(10000)],
            title="Daily sales amount",
        ),
        "region": Column(
            str,
            checks=[pa.Check.isin(["North", "South", "East", "West"])],
            title="Sales region",
        ),
    }
)
```

We can now validate data using this schema, which will check data types. along with our checks on the `sales` and the `region` columns:

```python
data = pl.DataFrame({
    "date": ["2025-01-01", "2025-01-02", "2025-01-03"],
    "sales": [-1000, 1200, 950],
    "region": ["North", "South", "East"]
})

print(schema(data))
```

```
shape: (3, 3)
┌────────────┬────────┬────────┐
│ date       ┆ sales  ┆ region │
│ ---        ┆ ---    ┆ ---    │
│ datetime   ┆ f64    ┆ str    │
╞════════════╪════════╪════════╡
│ 2025-01-01 ┆ 1000.0 ┆ North  │
│ 2025-01-02 ┆ 1200.0 ┆ South  │
│ 2025-01-03 ┆ 950.0  ┆ North  │
└────────────┴────────┴────────┘
```

*Tip - Use Pandera's check decorators to add custom validation logic beyond simple range and type checks. Custom checks can validate complex business rules or statistical properties of your data.*

## DuckDB

**DuckDB is database for fast analytical SQL querying** - it's an alternative to SQLite, Polars and Pandas.

Like SQLite, DuckDB is a single-file database. While SQLite are optimized for transactional workloads, DuckDB is specifically designed for analytical queries on structured data.

Let's create some sample data using both CSV and Parquet formats:

```python
import duckdb
import polars as pl

sales = pl.DataFrame(
    {
        "date": ["2025-01-01", "2025-01-02", "2025-01-03"],
        "product_id": [1, 2, 1],
        "amount": [100, 150, 200],
    }
).to_csv("sales.csv", index=False)

products = pl.DataFrame(
    {"product_id": [1, 2], "name": ["Widget", "Gadget"], "category": ["A", "B"]}
).to_parquet("products.parquet")
```

Below we run a SQL query across both formats:

```python
con = duckdb.connect()

print(
    con.execute(
        """
    WITH daily_sales AS (
        SELECT 
            date,
            product_id,
            SUM(amount) as daily_total
        FROM 'sales.csv'
        GROUP BY date, product_id
    )
    SELECT 
        s.date,
        p.name as product_name,
        p.category,
        s.daily_total
    FROM daily_sales s
    JOIN 'products.parquet' p ON s.product_id = p.product_id
    ORDER BY s.date, p.name
"""
    ).df()
)
```

```
         date product_name category  daily_total
0  2025-01-01      Widget        A         100
1  2025-01-02      Gadget        B         150
2  2025-01-03      Widget        A         200
```

DuckDB shines when working with larger than memory datasets. It can efficiently query Parquet files directly without loading them into memory first.

*Tip - Use DuckDB's EXPLAIN command to understand query execution plans and optimize your queries. For example, `con.execute("EXPLAIN SELECT * FROM 'sales.csv'")` shows how DuckDB will process your query.*

## Loguru

**[Loguru](https://github.com/Delgan/loguru) is a tool for adding logging to Python applications** - it's an alternative to the standard library's logging module and structlog.

Loguru's central idea is that there is only one `logger`. In a great example of the unintuitive value of constraints - having less `logger` objects is actually better than being able to create many.

Let's see how Loguru simplifies logging. First, a basic example:

Logging with Loguru is as simple as `from loguru import logger`:

```python
from loguru import logger

logger.info("Hello, Loguru!")
```

Configuring the logger is all done through a single `logger.add` call.

We can configure how we log to `std.out`:

```python
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
    level="INFO"
)
```

The code below configures logging to a file:

```python
logger.add(
    "log.txt",
    format="{time} {level} {message}",
    level="DEBUG"
)
```

*Tip - Use `@logger.catch` decorators liberally on your main functions - it will catch and log any exceptions with rich tracebacks while allowing your application to continue running. This is especially useful during development and debugging.*

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

