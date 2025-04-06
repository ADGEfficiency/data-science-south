---
title: Getting the most out of Jupyter Lab 
description: A guide to the next generation of notebook tooling.
date: '2020-11-05'
competencies:
- Software Engineering

---

Notebooks are a common tool among data scientists - many data professionals write all their code in notebooks.

Jupyter Lab is a web application used by data scientists to run Jupyter Notebooks. Historically the only way to work with notebooks was using Jupyter Notebook - **in 2017 we were given Jupyter Lab**.

Jupyter Lab offers a superior development experience to Jupyter Notebook, with improvements such as:

- a file browser
- a text editor
- terminal access
- split views

**This post is aimed at showing off what Jupyter Lab can do.** 


## Notebook 101

### Installation & Use

Install without a space:

```bash
$ pip install jupyterlab
```

Start a server with a space:

```bash
$ jupyter lab
```

You can then point your browser to `http://localhost:8888/lab`, and you'll see the *Launcher* screen, shown below with the *File Browser* open in the sidebar:

![](/images/getting-most-jupyter/f1.png)

Unlike Jupyter Notebook, you can have multiple tabs open side by side - you can also keep track of your kernels by selecting *Running Terminals & Kernels* in the sidebar:

![](/images/getting-most-jupyter/f2.png)


### Notebooks vs. Jupyter Notebook vs. Jupyter Lab

Something that can be confusing is the difference between the `.ipynb` notebook file, Jupyter Notebook & Jupyter Lab:

- a notebook file (`.ipynb`) is a **JSON text file** that defines the structure & code of a notebook
- Jupyter Notebook & Jupyter Lab are **programs** that allow you to run & edit notebook files

Both Jupyter Notebook & Jupyter Lab can be used to run any `.ipynb` notebook file.


### Kernels & virtual environments

Another area for confusion is what exactly a *kernel* is.  **A kernel is just a running Python interpreter**, usually connected to a notebook.  It is possible swap kernels after they are running, but it's not something we do a lot.

Kernels can be managed from the menu bar - restarting kernels is something that is done a lot.  Unfortunately there are no default shortcuts setup for kernel management - see our post on [Customizing Jupyter Lab Shortcuts](https://www.climate-code.com/blog/customizing-jupyter-lab-shortcuts) to see how to set these up.

In order to control which virtual environment you are using in the notebook, it's best to activate the environment before you install Jupyter Lab or start the server.  For example, if you are using `conda` to manage virtual environments:

```bash
$ conda activate base
$ jupyter lab
```

You'll also want to make sure you activated this environment before installing Jupyter Lab.


## Modal editor

When editing notebooks, Jupyter Lab becomes a modal editor with two modes - *Command* and *Edit*: 
- Command Mode for operating on cells
- Edit Mode for operating on text

A modal editor will operate differently depending on the mode - the same key will do different things based on what mode you are in.  You can see what mode you are in on the status bar.

You can move between modes using:

- `Enter` to move from Command Mode to Edit Mode
- `Escape` to move from Edit Mode to Command Mode

Cells can be run using `Shift Enter` in either mode, ending up in Command Mode.


### Cells

A notebook is composed of cells - blocks that contain text.  The text inside a cell can either be code, Markdown or raw text.  The ability to have mix executable code and Markdown documentation is a key feature of notebooks.

You can change the cell type using a dropdown:

![](/images/getting-most-jupyter/f3.png)

You can change cell types using the following shortcuts in Command mode:

- `m` = change cell to Markdown 
- `y` = change cell to code

Three other useful Command Mode shortcuts for operating on cells are:

- `a` = insert cell above
- `b` = insert cell below
- `dd` = delete cell

Mastering these five shortcuts will allow you to work with cells as efficiently as you work with text.


## Tooltip

Pressing `Shift-Tab` will show a tooltip for the function or class your cursor is on:

![](/images/getting-most-jupyter/f4.png)


## Contextual help

Similar to the tooltip, except it's always there.  You can have this help always shown in a separate pane by opening a *Show Contextual Help* window from the Launcher:

![](/images/getting-most-jupyter/f7.png)


## Consoles

Consoles are another way to interact with a running kernel - a cool trick is to connect a console to a Python script (`.py`):

![](/images/getting-most-jupyter/f5.png)


## Markdown preview

No more committing `README.md` changes just to see the updates:

![](/images/getting-most-jupyter/f6.png)


## `?` and `??`

These are actually `iPython` features, and will also work in an `iPython` kernel:

- a single `?` to see the docstring
- a double `??` to see the source code

![](/images/getting-most-jupyter/f8.png)


## Running shell commands

Another `iPython` feature - running shell commands inside a notebook:

![](/images/getting-most-jupyter/f9.png)

You can use this to automatically install packages in the first cell of a notebook - make sure to use the `-q` flag to hide the output:

![](/images/getting-most-jupyter/f10.png)

## `%%autoreload`

Autoreload helps deal with problem of source code outside the notebook not being reimported when it's changed.  This is only a problem when the source code changes after you start the kernel - essentially only when you are writing code yourself, external to the notebook.

Putting these two commands at the top of your notebook will mean that if you make changes to source code outside of the notebook, you can get these changes without having to restart the kernel.

```python
%load_ext autoreload
%autoreload 2
```

## Theme

The most important tip of all - a dark theme:

![](/images/getting-most-jupyter/f11.png)

## Useful Keyboard Shortcuts 

Below is a list of the most useful keyboard shortcuts in Jupyter Lab:

- `Cmd B` = toggle sidebar
- `Alt W` = close tab 
- `Enter`= to move from Command to Edit 
- `Escape` = to move from Edit to Command 
- `Shift Enter` = run cell

### Command Mode

- `a` = insert cell above
- `b` = insert cell below
- `dd` = delete cell
- `z` = undo cell
- `shift z` = redo cell 

- `m` = change cell to Markdown
- `y` = change cell to code 

### Text mode

- `Cmd Z` = undo text 
- `Shift Cmd Z` = redo text 
