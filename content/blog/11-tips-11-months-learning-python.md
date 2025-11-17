---
title: Eleven tips from eleven months of learning Python
description: I've been learning Python for around eleven months - it's been a wonderful journey!
date_created: 2017-09-04
date_updated: 2025-11-03
competencies:
  - Software Engineering
  - Python
aliases:
- 2017-09-04-11-tips-11-months-learning-python
---

I've been learning Python for around eleven months - it's been a wonderful journey!

This post is a list of eleven things that I've learned in my first eleven months with the language.

## 1 - Python Environment Setup

**For many people the hardest thing about learning Python is getting it setup in the first place**! I recommend [using the Anaconda distribution of Python](https://www.anaconda.com/download/).

Regarding Python 2 vs Python 3 - **if you are starting out now it makes sense to learn Python 3**. It's worth knowing what the differences are between the two - once you've made some progress with Python 3.

The installation process is pretty straight forward - **you can check that Anaconda installed correctly by typing `$ python` into Terminal or Command Prompt**. You should see something like the following:

```bash
$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Becoming comfortable with using the Terminal is another step where people fail**. Understanding that the Terminal can be used to run programs (one at a time!) is a key paradigm that takes some time to get comfortable with.

Part of using a bash based terminal is learning commands such as:

- **`ls`**: List files in a directory
- **`cd some/directory`**: Move to another directory downstream
- **`cd ..`**: Move to a directory upstream
- **`pwd`**: Print the current directory

## 2 - Managing Packages with pip

**pip is a way to manage packages in Python**. pip is run from a Terminal. Below are the pip commands I use the most.

To install a package (Note that the `-U` argument forces pip to install the upgraded version of the package):

```bash
pip install pandas -U
```

To remove a package:

```bash
pip remove pandas
```

To print all installed packages:

```bash
pip freeze
```

Often projects will include a `requirements.txt` file that contains all the packages you need to run a project. **You can using this file to install packages with pip using**:

```bash
pip install -r requirements.txt
```

If you need to create one of these files (i.e. to setup an installation of Python on another machine) you can generate one using:

```bash
pip freeze > requirements.txt
```

## 3 - Using Virtual Environments

**Virtual environments are best practice for managing Python**. Different packages will require different sets of packages (called *dependencies*). By using one virtual environment per project you can ensure that the version of the package you are using is the one you want. This is especially true in the data science and machine learning world where packages are being rapidly developed (see TensorFlow, PyTorch etc).

**Combining virtual environments with a `requirements.txt` file also allow you to quickly setup a development environment on a remote machine** (i.e. on AWS or Google Cloud).

There are two main methods for managing virtual environments. Personally I use conda (as I always use the Anaconda distribution of Python). You could also use virtualenv to manage your environments.

On Unix based systems (Mac or Linux) you can activate virtual environments and then run scripts using that installation of Python:

```bash
source activate yourenv
```

## 4 - Running Python Scripts Interactively

**Running a script interactively can be very useful when you are learning Python** - both for debugging and getting and understanding of what is going on!

```bash
python -i script_name.py
```

After the script has run you will be left with an interactive console. **If Python encounters an error in the script then you will still end up in interactive mode** (at the point where the script broke).

Another way to run a script interactively is to use iPython (which Jupyter is built on top of):

```bash
$ ipython
```

You can then run a script using an iPython magic command:

```python
In [1]: %run script_name.py
```

**You can also use bash commands like `ls` or `cd` within an iPython session** - very cool!

## 5 - Iterate with enumerate

Often you want to loop over a list and keep information about the index of the current item in the list.

This can naively be done by:

```python
for item in a_list:
    other_list[idx] = item
    idx += idx
```

**Python offers a cleaner way to implement this**:

```python
for idx, item in enumerate(a_list):
    other_list[idx] = item
```

We can also start the index at a value other than zero:

```python
for idx, item in enumerate(a_list, 2):
    other_list[idx] = item
```

## 6 - Combine Lists with zip

Often we want to iterate over two lists together. A naive approach would be to:

```python
for idx, item_1 in enumerate(first_list):
    item_2 = second_list[idx]
    result = item_1 * item_2
```

**A better approach is to make use of zip** - part of the Python standard library:

```python
for item_1, item_2 in zip(first_list, second_list):
    result = item_1 * item_2
```

We can even combine zip with enumerate:

```python
for idx, (item_1, item_2) in zip(first_list, second_list):
    other_list[idx] = item_1 * item_2
```

## 7 - List Comprehensions

**List comprehensions are baffling at first**. They offer a much cleaner way to implement list creation.

A naive approach to making a list would be:

```python
new_list = []

for item in old_list:
    new_list.append(2 * item)
```

**List comprehensions offers a way to do this in a single line**:

```python
new_list = [item * 2 for item in old_list]
```

You can also create other iterables such as tuples or dictionaries using similar notation.

## 8 - Default Values for Functions

Often we create a function with inputs that only need to be changed rarely. **We can set a default value for a function by**:

```python
def my_function(input_1, input_2=10):
    return input_1 * input_2
```

We can run this function using:

```python
result = my_function(input_1=5)
# result = 50
```

If we wanted to change the value of the second input we could:

```python
result_2 = my_function(input_1=5, input_2=5)
# result = 25
```

## 9 - Version Control with git

**Like virtual environments git is a fundamental part of the workflow of anyone using Python**.

A full write up of how to use git is outside the scope of this article - these commands are useful to get started. Note that all of these commands should be entered in a Terminal that is inside the git repo.

To check the status of the repo:

```bash
git status
```

To add files to a commit and push to your master branch:

```bash
git add file_name
git commit -m 'commit message'
git push origin master
```

Note that you can do multiple commits in a single push.

We can also add multiple files at once. To add all files that are already tracked (i.e. part of the repo):

```bash
git add -u
```

To add all files (tracked & untracked):

```bash
git add *
```

Sometimes you will add files to your commit you didn't mean to - this allows you to undo them one by one (ie commit by commit):

```bash
git reset HEAD~
```

Sometimes you will want to undo your local changes to a file - you do this using:

```bash
git checkout file_to_reset
```

## 10 - Choosing a Text Editor

There are a range of text editors you can use to write Python:

- **Atom**: User-friendly editor with great Python support
- **vi**: Classic Unix text editor
- **vim**: Enhanced version of vi
- **spyder**: Comes with anaconda
- **Sublime Text**: Fast and customizable
- **Pycharm**: Full-featured IDE
- **notepad ++**: Windows text editor

All have their positives and negatives. **When you are starting out I recommend using whatever feels the most comfortable**.

Personally I started out using notepad ++, then went to spyder, then to Atom and vim.

**It's important to not focus too much on what editor you are using - more important to just write code**. If I was to recommend an editor to a beginner I would recommend Atom.

## 11 - Books & Resources

I can recommend the following resources for Python:

[Python Reddit](https://www.reddit.com/r/Python/)

[The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/)

[Python 3 Object Oriented Programming](https://www.amazon.co.uk/Python-3-Object-Oriented-Programming/dp/1849511268)

[Effective Python: 59 Specific Ways to Write Better Python](https://www.amazon.co.uk/Effective-Python-Specific-Software-Development/dp/0134034287)

[Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython](https://www.amazon.co.uk/Python-Data-Analysis-Wrangling-IPython/dp/1449319793)

[Python Machine Learning](https://www.amazon.co.uk/Python-Machine-Learning-Sebastian-Raschka/dp/1783555130)

[Automate the Boring Stuf with Python](https://automatetheboringstuff.com/)

I can also recommend the following for getting an understanding of git:

[Github For The Rest Of Us](https://www.youtube.com/watch?v=8_mHSdCkv3s)

[Understanding Git Conceptually](https://www.sbf5.com/~cduan/technical/git/)

## Summary

**Learning Python is a wonderful journey that requires mastering both the language and its ecosystem**.

Key takeaways:

- **Setup matters**: Use Anaconda and learn the terminal
- **Package management**: Master pip and virtual environments
- **Pythonic patterns**: Embrace enumerate, zip, and list comprehensions
- **Version control**: Git is essential for any Python developer
- **Tools**: Find an editor that works for you and stick with it
- **Keep learning**: Use the wealth of resources available in the Python community

Thanks for reading!
