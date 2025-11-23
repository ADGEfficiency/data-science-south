---
title: Customizing Jupyter Lab Shortcuts
description: How to setup custom keyboard shortcuts for Jupyter Lab.
date_created: 2020-12-06
date_updated: 2020-12-06
competencies:
- Software Engineering
---

Notebooks are a popular tool among data scientists - many data professionals write all their Python code in notebooks.

Jupyter Lab is a web application used by data scientists to run Jupyter Notebooks.  

This article shows **how to customize shortcuts in Jupyter Lab** and gives you a starter template for useful shortcuts.

We will setup custom shortcuts for:

- **restarting the iPython kernel**,
- **running all cells above this cell**,
- **opening a terminal**,
- **moving between tabs**.

## Why Customize Shortcuts?

The default shortcuts in Jupyter Lab are good (take a look at our [Jupyter Lab guide](https://www.data-science-south.com/blog/getting-the-most-jupyter-lab) for a list of the most important default shortcuts), but there are a few parts of the data science workflow that the default shortcuts don't cover.

Adding just a few custom shortcuts will lead to an increase in the speed & accuracy of your workflow.

## How to Customize Shortcuts in Jupyter Lab

You can access the *Keyboard Shortcuts* menu using:

1. *Menu Bar* -> **Settings**
2. *Settings* -> **Advanced Settings Editor**
3. *Advanced Settings Editor* -> **Keyboard Shortcuts**
4. *Keyboard Shortcuts* -> **User Preferences**

If you haven't edited your Jupyter Lab shortcuts before, you'll have nothing in the *User Preferences* section.  

![](/images/custom-jl-shortcuts/f1.png)

There are a few strategies for setting up *User Preferences*:

- copy all the *System Defaults* into *User Preferences*, and then modify the shortcuts you want to change
- only put the shortcuts we want to change into *User Preferences*, which is what we will do in this article

Either way, you'll benefit from having a copy of *System Defaults* open in a text editor, for easier searching (the Jupyter Lab search can leave a little wanting :).


## Restarting the Kernel & Running All Cells Above

The most important custom shortcuts are those that make restarting the kernel quicker.  Its something you do a lot when using notebooks.

Which shortcut is best for you depends on how you like to restart the kernel - we use *Restart Kernel & Run All* the most.  The full shortcuts we use for managing the kernel are:

- restart & run all -> `F6`,
- restart & clear -> `F7`,
- run all above -> `F8`.

Copying the JSON below directly into your *User Preferences* will give you these three custom shortcuts:

```json
{
    "shortcuts": [
        {
            "command": "runmenu:restart-and-run-all",
            "keys": [
                "F6"
            ],
            "selector": "[data-jp-code-runner]"
        },
        {
            "command": "kernelmenu:restart-and-clear",
            "keys": [
                "F7"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        },
        {
            "command": "kernelmenu:run-all-above",
            "keys": [
                "F8"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        }
    ]
}
```

You'll notice that we don't use `F5` - because this is often used as a *Refresh Page* shortcut in browsers.


## Open a Terminal

A good option here is `Alt T` (like on Ubuntu).

A common workflow for with this shortcut is:

- `Alt T` to open a terminal,
- do some work,
- `Alt ArrowUp` to switch back and forth with previous tab (usually a notebook),
- `Ctrl W` to close the terminal window.

`Alt ArrowUp` is a custom shortcut as well - see the *Move between tabs* section below.

```json
{
    "shortcuts": [
        {
            "command": "terminal:open",
            "keys": [
                "Alt T"
            ],
            "selector": "body"
        }
    ]
}
```

## Move Between Tabs

The final shortcuts are to make moving around between open tabs using `Alt` + arrow keys:

- `Alt ArrowUp` -> previously used,
- `Alt ArrowLeft` -> previous tab,
- `Alt ArrowRight` -> next tab.

```json
{
    "shortcuts": [
        {
            "command": "tabsmenu:activate-previously-used-tab",
            "keys": [
                "Alt ArrowUp"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-previous-tab",
            "keys": [
                "Alt ArrowLeft"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-next-tab",
            "keys": [
                "Alt ArrowRight"
            ],
            "selector": "body"
        }
    ]
}
```


## Full Custom Shortcuts JSON

Below is a copy of the full JSON we use to customize our shortcuts - you can copy this directly into *User Preferences*:

```json
{
    "shortcuts": [
        {
            "command": "sidebar:toggle",
            "keys": [
                "F9"
            ],
            "selector": ".jp-SideBar"
        },
        {
            "command": "runmenu:restart-and-run-all",
            "keys": [
                "F6"
            ],
            "selector": "[data-jp-code-runner]"
        },
        {
            "command": "kernelmenu:restart-and-clear",
            "keys": [
                "F7"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        },
        {
            "command": "kernelmenu:run-all-above",
            "keys": [
                "F8"
            ],
            "selector": "[data-jp-kernel-user]:focus"
        },
        {
            "command": "terminal:open",
            "keys": [
                "Alt T"
            ],
            "selector": "body"
        },
        {
            "command": "tabsmenu:activate-previously-used-tab",
            "keys": [
                "Alt ArrowUp"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-previous-tab",
            "keys": [
                "Alt ArrowLeft"
            ],
            "selector": "body"
        },
        {
            "command": "application:activate-next-tab",
            "keys": [
                "Alt ArrowRight"
            ],
            "selector": "body"
        },
        {
            "command": "notebook:change-cell-to-code",
            "keys": [
                "W"
            ],
            "selector": ".jp-Notebook:focus"
        },
        {
            "command": "notebook:change-cell-to-markdown",
            "keys": [
                "M"
            ],
            "selector": ".jp-Notebook:focus"
        }
    ]
}
```
