---
title: Data Science Project Checklist
description: Make your data science projects presentable, reproducible, accessible and extensible.
date_created: 2020-10-16
date_updated: 2020-10-16
competencies:
- Soft Skills
---

## Why a Checklist?

Checklists are used in a wide range of fields, from aviation and surgery to construction and finance. **They reduce errors, improve productivity and ensure consistency in complex tasks**. A list of steps to follow during surgical procedures leads to reduced complications and deaths.

Checklists are also useful in data science projects.  Following our checklist below, your projects will be:

- **Presentable**: Makes the difference between a project that forms a valuable part of your portfolio and a project that makes people question your ability.
- **Best practice software engineering techniques** are being followed.
- **Reproducible**: Others can run your code and get the same results.
- **Accessible**: Others can use your results and insights.
- **Extensible** Others can build on your work.

## Tested

Tests are a valuable software engineering practice that all data scientists should use.

Testing code has a number of benefits:

- **tell you if something breaks**,
- make you **write better code**,
- **help others understand** your code,
- **document expected behaviour** of your code.

A useful form of testing are in-line `assert` statements.  For example after splitting a dataset into test & train sets, we might want to check that our test set is smaller than our test set:

```python
te, tr = split_dataset(data)
assert te.shape[0] < tr.shape[0]
```

This will fail if the something is wrong - much better than a comment that sits silently and watches the world burn.

More extensive testing of behaviour can be done using a test suite. Seeing a test suite in a data science project helps improve the confidence that users have in your work. This isn't to say that testing can prove correctness (it can't), but tests are a sign that a data scientist has some level of software engineering education.

```python { title = "src.py" }
def my_complex_function():
    return super_secret_algorithm()
```

```python { title = "tests.py" }
from src import my_complex_function


def test_my_complex_function():
    assert my_complex_function() == expected_result
```

We can then run this test suite using:

```
$ pytest tests.py
```

## Styled

Part of making your code accessible is formatting in a style that people expect - for Python this means following PEP8.  Code style is somewhat arbitrary - this doesn't mean it's not important.  The fact that we drive on one side of the road is also arbitrary!

**Code style is important** - it allows your reader to quickly understand what your code is doing.  You introduce a lot of mental overhead if you format in inconsistent or unexpected ways.

Common mistakes we see from junior data scientists include:

```python
# space before and after assignment operator
# incorrect
var=int(42)
# correct
var = int(42)

# no space before & after default function arguments
# incorrect
def my_func(param = 10):
# correct
def my_func(param=10):
```

There are plenty more things to get right with Python code style - a useful resource is [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/) from Real Python.

You should not be manually formatting your code - use a code formatter like Ruff every time you save any Python script.

## Refactored

**A good predictor of a junior data scientist is a repository full Jupyter notebooks.**  Notebooks have their place in most data science projects, but not moving source code (definitions of functions and classes) out of notebooks into Python scripts (`.py` files) is a clear sign of someone inexperienced in doing data science professionally.

Moving of source code out of notebooks has multiple benefits:

- **allows version control** of the source code as `.py`,
- **reuse code** in multiple notebooks,
- **test code**.

A Jupyter Notebook is a big JSON file, with the JSON used to define where the cells are & the source Python code itself.

**This makes doing proper version control of notebooks almost impossible** - merging two notebooks that have diverged is possible, but it's dicey.

Moving source code out of notebooks allows multiple notebooks to all import the same function. Reuse of code is a basic lesson from software engineering that all data scientists should learn.  Duplication of code is inefficient at the best of times, dangerous at the worst.

Moving source code out of notebooks is not refactoring - refactoring is the process of restructuring code, without changing behaviour. This process of restructuring code is iterative - production code is likely to have gone through multiple refactors before it's used in the wild.

How many iterations of refactoring your source code should go through depends on the project - work spent refactoring research code that is thrown away may not be a good use of time.

We would expect the following steps to be taken in most projects:

- start out developing code inside notebooks,
- then move source code into Python scripts,
- finally one iteration of refactoring to improve code quality.

## Clean

Computer programs often generate hidden files when they run.  These files can be used as caches to speed up programs (such as Python's `.pyc` files) or used to backup the state of a program (such as Jupyter's `.ipynb_checkpoint`). `.pyc` files can be particularly dangerous - they can store information you do not want to share with the world, such as AWS credentials.

**A clean project should not contain any of these files - they are trash**.  Including them as part of a repository is messy at best, dangerous at worst.  Common trash files that make it into data science project repositories include:
- `__pycache__` directories & `.pyc` files
- `.ipynb_checkpoints`
- `.DS_Store`

The solution to not checking in these files is to use a `.gitignore` file - git will not allow you to check in files that match the patterns. A useful starter template for data science is:

```bash { title = ".gitignore" }
**/*.DS_Store
**/*.pyc
**/*.swp
**/*.ipynb_checkpoints
**/*.pyc
**/__pycache__
**/.pytest_cache
.egg
.egg-info
dist
```

You can also include in this `.gitignore` any project specific files or folders that are generated when code is executed - for example if your project creates a folder `data`, add this to the `.gitignore` so that you users don't accidentally check this in.

Another tip - it can be useful to setup a global `.gitignore`, that git will use in all your projects.  Below we tell git to also use the file `~/.gitignore`, on top of any local project `.gitignore`:

```
$ git config --global core.excludesfile ~/.gitignore
```

We would still recommend including a `.gitignore` with your project, for the benefit of users who don't have a global `.gitignore` setup, and to include project specific patterns to ignore.

Another source of problems is including spaces in file names - **file names should not contain spaces**.  Spaces in file names cause all sorts of issues, one being autocomplete on the command line. Instead of spaces consider using a `-` or `_` to separate words.

## Small

Text files are small - typical Python scripts are on the order of 10 KB.  A data science repository should also be small in size. **Cloning a data science repository should be fast** - if cloning your repository is slow, this is a sign that you have checked in large files in the past.

Key to keeping your repository size under control is to not check in large files - especially data, such as CSVs.  **Data should rarely be in a git repository**.  Remember that git works by keeping a copy of every file you ever check in - if you slightly adjust your 100 MB `data.csv` file three times, all of a sudden your git repository size has blown up from KB to almost half a GB!

If you do need to get data to your users (and you likely will to make your project reproducible), **it's better to provide a way for your users to download it themselves** - two options include a public S3 bucket (read only!) or a Google Drive download link.

## Reproducible

Reproducibility is the foundation of scientific progress - work that can't be repeated is discredited. Reproducibility of a data science project means that your users can access all of the following:

- data
- source code
- Python interpreter & package versions
- model training artifacts

Getting your users the data they need to run your code is one part of making your project reproducible.  As mentioned above, give your users the ability to download this themselves, so that you can keep data separate from source code.  Getting source code to your users is easy in the age of Github.

**Specifying the minimum Python version required is important if you are using a feature of Python that was recently introduced** (such as f-strings or assignment operators). You'll also want to tell your users this in the `README`, specifying the minimum Python version they'll need.

Next is to make sure they have the correct packages to run your code.  In Python, it's common to include a `requirements.txt` file that lists the packages you user will need.  You can automatically generate this file by writing the output of `pip freeze` into a file:

```
$ pip freeze > requirements.txt
```

This will copy all the packages in your current Python installation, which results in a large and rigid requirements file.  **An alternative is to manually create a human readable `requirements.txt`**, where you specify the versions of important packages, and let `pip` manage the dependencies for you.  More stable packages can be left without version numbers, but unstable packages should have a package number specified:

``` { title = "requirements.txt" }
tensorflow==2.3.0
pytest
```

When doing machine learning projects, you also want to consider what artifacts of your training process you want to share.  Users may want to train the model from scratch themselves, fine-tune your model or just use your model.   Sharing these artifacts can be done the same way as with data.

A final consideration with reproducibility is the operating system of your users.  Most data science projects are built to run on UNIX/POSIX systems, but many can also be run on Windows with some additional effort. No matter what your choice, you'll want to point out what assumptions you are making about the users operating system.

## Accessible

Accessibility & reproducibility are closely related.  Reproducibility is technical - that another data scientist could run your project and reproduce your results.

Accessibility is not technical - accessibility is about your users & audience being able to follow what you have done.  **Key to accessibility is thinking about who your users & audience are.**  If you users are only technical, a well documented Github repository is likely to suffice.

For a non-technical audience, a Github repository is not likely to be sufficient.  Better options for making your project accessible might include a blog post, or an interactive web app.

You don't need to go and start a full blog on your own domain. An easier option for blogging is posting directly to Medium.  If you are interested in starting a blog site on your own domain, a static site generator such as Jekyll or Hugo is the way to go.

For web apps - the heavier option is to build an app in a web development framework like Flask.  A more accessible option is to use a framework targeted at data science, such as Streamlit or Dash.

## Documented

**Documentation is a controversial topic in software engineering** - as with many simple questions there is not a simple answer to what & how much documentation your project needs.

It's not as simple as commenting everything - comments introduce additional maintenance cost, and the risk of code and comments contradicting each other.  Our advice for documentation is to:

- comment only what isn't obvious from the code,
- favour executable documentation, such as assert statements & test suites,
- use the `README` as the main source of documentation,
- write documentation on demand, as it's needed - don't try to guess what you'll need.

Common forms of executable documentation include in-line assert statements or full test suites (see the *Tested* section).  An important quality of executed documentation is less risk of getting out of sync with the rest of the code base.

There are however some documentation best practices everyone agrees on - the `README` is one.  Commonly this is a Markdown file called `README`.  Not every user of your project will look at all your source code - but all of them will read your `README`. A project without a `README` (either incomplete or missing) looks awful to experienced data scientists - make sure you include one!

In your `README` you want to communicate:

- what the project is,
- who it is for,
- how to set it up,
- how to use it.

A `README` template to get you started:

```markdown {title = README.md}
# Project Title

A one or two sentence introduction to what your project is.

## Setup

This project requires Python 3.X - setup by:

$ pip install -r requirements.txt

Download data using:

$ bash download_data.sh

## Use

Train a model:

$ python3 train.py

Use a pretrained model:

$ python3 pretrained.py
```

Other common forms of technical documentation include, tutorials, how-to guides, examples or full blown exhaustive reference material.  For a data science portfolio project, we suggest that a well written `README.md` and an example Jupyter notebook or two will be enough for most projects.

## Extensible

The final quality of a well presented data science project is extensibility. Software should be open for extension, but closed for modification.

This can range from a list of ideas for next steps, to a well engineered command line interface that makes doing experiments easy.

Ideas for improvements to the project can live inside the project `README`.  Another potential home for these is as Issues or Discussions on the GitHub page.

Writing a command-line interface that allows experimentation and extension is a valuable addition to most projects.  If you want people to try things, make it easy to do so!  You'll also find it's useful for your own work.
