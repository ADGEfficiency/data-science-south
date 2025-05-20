---
title: Bash Shell
summary: Learn how to use a shell, write shell scripts, and configure your shell environment.
competencies:
- "Software Engineering"
---

## What is Bash?

Bash is a shell.  Shells are computer programs that do a few different things:

**Run programs**: Execute other programs on your computer:

```shell-session
$ python script.py
```

**Compose & run pipelines**: Chain programs together to process data:

```shell-session
$ cat file.txt | sort > sorted.txt
```

**Scripting**: Automate tasks with shell scripts:

```bash
#!/usr/bin/env bash
echo "hello from a script"
```

### This Lesson

- **What is Bash**: A shell program that runs other programs, enabling command execution, pipelines, scripting, and history features
- **Terminal vs shell vs command line**: Understanding the differences between these related but distinct components
- **Shell configuration**: Customizing your shell environment with `.bashrc`, `.zshrc`, and other configuration files
- **Environment variables**: Using and configuring your shell environment with variables like `$PATH`
- **Navigation**: Moving around the filesystem with commands like `cd`, `pwd`, and using keyboard shortcuts like tab completion and CTRL-R
- **File operations**: Creating, viewing, moving, and deleting files and directories with `touch`, `cat`, `mv`, `rm` and more
- **Redirection and pipes**: Connecting programs together using `|`, `>`, `>>`, and `<` to build powerful command pipelines
- **Shell scripting**: Writing reusable scripts with commands, variables, command-line arguments, and functions

These skills form the foundation for many data science workflows, enabling everything from automated data processing to CI/CD pipelines and Docker deployments.

### Resources

Recommended resources to learn Bash:

- **Survival guide for Unix newbies**: A short guide on Unix [matt.might.net](https://matt.might.net/articles/basic-unix/)
- **Effective Shell**: A book of essentials on how to use the shell [effective-shell.com](https://effective-shell.com/)
- **BashGuide**: A guide on Bash and Bash scripting [mywiki.wooledge.org](https://mywiki.wooledge.org/BashGuide)
- **Missing semester**: Proficiency with tools, including shell, shell scripting and the command line [missing.csail.mit.edu](https://missing.csail.mit.edu/)

### Notation

`$` indicates a command is run interactively in a Bash shell -- you don't need to write this leading `$` when you are typing in the shell.

For example, in the code below, to run this on your own machine, you need to type `ls`, then `Enter` to run the command in the REPL:

```shell-session
$ ls
archetypes                      data-science-south.excalidraw   log.py                          public                          temp
assets                          data.txt                        main.py                         pyproject.toml                  temp.py
CLAUDE.md                       hugo.toml                       Makefile                        README.md                       temp.sh
content                         i18n                            mistake.py                      resources                       tests
data                            layouts                         out.xml                         static                          uv.lock
```

The output of the command displayed below the command.

## Why Learn Bash?

Bash is a popular shell, that is readily available in the cloud.  It's a tool you can easily find in places where serious computing is done.

A lot of cloud computing is done on machines running some form of Linux, with the Bash shell often installed with the operating system.  Cloud CI/CD tools like GitHub Actions or Azure Devops usually use run Bash to run pipeline components by default.

Learning how to use a shell will allow you to:

- **Create CI/CD pipelines**: Most pipelines are sequences of shell commands, commonly written in `.yaml` files.

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          # these are all shell commands!
          python -m pip install --upgrade pip
          pip install pytest
          pip install -e .
      - name: Run tests
        run: |
          pytest
```

- **Use Docker**: Dockerfiles are sequences of shell commands.

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# shell command
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

- **Repeat and automate tasks**: Repeating and automating text commands is easier than pointing and clicking.

```shell-session
$ file=data.csv python process_data.py "$file" > "${file%.csv}_processed.csv"
```

- **Unlock powerful CLI tools**: Some development tasks are best (or even only) done with shell tools.

```shell-session
$ sqlite3 db.sqlite "SELECT * FROM users"
```

**Bash is an enabling skill** - it enables workflows that have huge benefits for development:

- **Source control**: Version control and code history management
- **Automated testing**: Continuous integration (CI) processes
- **Automated deployments**: Continuous deployment (CD) pipelines

{{< img 
    src="/images/bash-enables-git-cicd.svg"
    width="500"
>}}

The shell is a key skill that allows you to use programming languages - it's the *everything else* or *other stuff* you need to know to be able to do what you really want to do (Python, SQL):

{{< img 
    src="/images/other-stuff-needed-to-program.svg"
    width="500"
>}}

## Terminal, Command-Line & Shell

The terminal, command line and shell are often used interchangeably. 

They are however different tools - all three are used when using a computer via text commands, but they do different things.

### Terminals

**The terminal (also called a console) is an interface that controls user input & output**.

**Historically a terminal was hardware**. The terminal originates in the mainframe era of computing.  Terminals could connect to other computers - you could run programs on a central computer from your terminal.

{{< img 
    src="/images/bash-shell/terminal.png"
    caption="The DEC VT100 terminal (Hardware)"
    width="500"
>}}

**Today terminals are often software** - using terminal emulator programs on a computer. 

{{< img 
    src="/images/bash-shell/terminal-software.png"
    caption="The Kitty terminal running tmux for terminal multiplexing (Software)"
    width="500"
>}}

Popular terminal emulators include:

- **Any OS**: VS Code
- **MacOS**: iTerm2 terminal application
- **Windows**: Windows Terminal
- **Ubuntu**: Gnome Terminal

Alongside an emulator, it's common to use a program like tmux or GNU Screen to multiplex multiple terminals in a single window.

### The Command-Line

The command-line is the space or interface in the terminal where you can type and execute text commands. 

When you launch your terminal, you are in a command-line interface.  The command-line below shows a Bash shell, with the `echo` command:

```shell-session
$ echo "this is the command line"
"this is the command line"
```

### Shells

Shells are mainly used in two ways:

1. **Interactive REPL**: A Read-Eval-Print Loop that runs commands interactively
2. **Scripting language**: A programming language that can be run in scripts

It's possible to use different shells for both of these - for example, you could use the Zsh shell in an interactive REPL to run Bash scripts.

#### Shell as a REPL

A REPL (Read-Eval-Print Loop) is an interactive programming process that:

1. Provides a command-line for user input
2. Evaluates user input in a subprocess shell
3. Displays output to user
4. Returns the results
5. Provides a new command-line for user input

We can use the shell as a REPL to list the current directory files & directories using the `ls` program:

```shell-session
$ ls
CLAUDE.md  Makefile  README.md  archetypes/  assets/  content/  data/  hugo.toml  i18n/  layouts/  pyproject.toml  static/  tests/
```

Other programs can be used as REPLs - we can use Python as a REPL as well via the `python` CLI:

```shell-session
$ python
Python 3.11.10 (main, Oct 16 2024, 08:56:36) [Clang 18.1.8 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello")
hello
>>> exit()
```

#### Shell Scripting

Shell scripts are text files that contain a sequence of shell commands. These scripts can be run in a shell, and the commands in the script will be executed in order.

We can use the shell as a programming language via shell scripting - an example shell script that lists the current directory using `ls`:

```bash { title = "script.sh" }
#!/usr/bin/env bash
echo "hello from the script"
ls
```

We can then execute this script in a shell REPL:

```shell-session
$ bash script.sh
hello from the script
CLAUDE.md  Makefile  README.md  archetypes/  assets/  content/  data/  hugo.toml  i18n/  layouts/  pyproject.toml  static/  tests/
```

Shell scripts can take input from command-line arguments or from environment variables.

#### Types of Shells

There are many different shells available -- commonly used shells are:

- **sh**: The Bourne Shell, the original Unix shell. It introduced features like redirection (`>`, `>>`, `<`) and piping (`|`)
- **Bash**: The Bourne Again Shell, an improved version of Bourne Shell, is the default shell for many Unix and Linux systems
- **zsh**: The Z shell, the default shell on MacOS, which improves on Bash
- **PowerShell**: A shell developed by Microsoft for Windows

You can combine different shells with a different terminal emulators. For example, you could use Bash, Zsh and Powershell with Windows Terminal.

### Common Bash Programs

**A shell has its own syntax and set of commands, along with a collection of programs available**.  

Some common Bash shell programs include:

- **ls**: List files & directories
- **pwd**: Print working directory
- **cd**: Change directory
- **cat**: Print file contents
- **clear**: Clear screen
- **echo**: Print text to terminal
- **mkdir**: Create directories
- **rm**: Remove files or directories
- **cp**: Copy files and directories
- **mv**: Move or rename files and directories
- **grep**: Search for patterns in files
- **find**: Search for files in a directory hierarchy
- **chmod**: Change file permissions
- **touch**: Create empty files or update timestamps
- **man**: Display manual pages for commands

The programs that are available in your shell are programs that are on the shell's `$PATH` environment variable - more on the `$PATH` and environment variables later.

You can use the `which` program to show where programs are located:

```shell-session
$ which can
/bin/cat
```

Other shell programs might be specific to your project:  

- **Cloud CLIs**: The AWS CLI or Azure CLI to interact with cloud services
- **Long Running Processes**: Run databases or servers
- **Custom CLIs**: Your own CLI programs with Python

## Tooling

**Different developers use different tools for using a Bash shell**.

Some developers run terminals inside an IDE like VS Code - one terminal can be used with different shells.  Others will use a separate program like Windows Terminal to run different shells.

| Operating System | Terminal Emulators        | Shells                           | Text Editor |
|------------------|---------------------------|----------------------------------|-------------|
| Windows          | Windows Terminal, VS Code | Bash on WSL, Git Bash on Windows | VS Code     |
| macOS            | iTerm2, VS Code           | Bash or Zsh                      | VS Code     |
| Linux            | VS Code, Gnome Terminal   | Bash or Zsh                      | VS Code     |

### Text Editors 

VS Code is a good choice for most!  You'll want a text editor to write things like shell scripts or configuration files (YAML, JSON etc).

VS Code also offers the ability to run a terminal alongside your editor, meaning you don't need to run a separate terminal application like Windows Terminal.

## Whitespace

Bash uses the space character to separate commands & arguments. This makes working at the shell natural, but requires some care.

**The shell will expand spaces by default into separate commands** - this means that spaces in the wrong places can cause shell scripts to break.

Space expansion is one reason why you should never put spaces in file names - use `-` or `_` as a separator in file names:

```bash
# don't do this
/folder name/file name.txt

# do this instead
/folder-name/file_name.txt
```

If you do use spaces, you may end up seeing (or having to write!) your paths by escaping the spaces with the escape character `\`:

```bash
# this is harder to work with
/folder\ name/file\ name.txt
```

## Shell Configuration

### Environment Variables

**A shell process is a stateful system** - it stores data in between execution of programs. One place to store state is in environment variables, which are similar to variables in other programming languages like Python.

**Environment variables can set and accessed in the shell, and then used as part of shell commands or in programs run from the shell**. Environment variables are commonly used to configure things like applications, databases or scheduled jobs.

Programming languages like Python can access environment variables - in Python we can use `os.ENVIRON` to access the environment variables of the shell process the Python program is running in.

#### Setting an Environment Variable

We can set an environment variable using `NAME=VALUE` - note the lack of space around the `=`:

```shell-session
$ stage=production
```

#### Accessing an Environment Variable

We can view the value of this environment variable with `echo`, using the `$NAME` syntax:

```shell-session
$ echo $stage
production
```

#### Exporting Environment Variables to Sub-Processes

Our shell is run in a process - there are hundreds of processes running on your computer now.

Many actions we take in a shell create a new process - this new process is called a sub-process.  For example, when we run a Python script in a shell, a new Python process is created.

Environment variables are not inherited by sub processes.

We can however make environment variables accessible to sub processes using `export`:

```shell-session
$ export stage=production
```
You will often see `export` used in the shell config scripts like `.bashrc`.  This is because these scripts are run during shell startup, and the environment variables defined in these scripts are supposed to be available to all sub processes.

#### Viewing All Environment Variables

You can see all the environment variables currently defined in your shell with the `env` command:

```shell-session
$ env
```

You can access an environment variable using the `$NAME` syntax.  

You can use `echo` to view the value of an environment variable:

```shell-session
$ echo $HOME
/Users/adamgreen
$ echo "user is $USER"
user is adamgreen
$ echo $SHELL
/bin/zsh
```

The value of the `HOME` variable will depend on the operating system and user name.

### `$PATH`

The `$PATH` environment variable is a special environment variable used by the shell.  It's used to tell the shell where to look for programs. It is a list of directories, separated by a `:`.

The `$PATH` environment variable is a list of directories that the shell will search when you type a command.  Appending a directory to `$PATH` makes that program accessible via a shell from any directory.

The `$PATH` variable will be quite long - a useful tip is to pipe the variable into `tr`, which can replace the `:` used to separate the paths with a new line `\n`:

```shell-session
$ echo $PATH | tr ":" "\n"
/usr/local/bin
/usr/bin
/bin
/usr/sbin
/sbin
/usr/local/go/bin
/opt/homebrew/bin
/Users/adamgreen/.local/bin
```

It's common to see the `PATH` variable modified in scripts by appending a new path onto the existing path:

```shell-session
$ export PATH=$PATH:$SPARK_HOME/bin
```

A common pattern you will see in install scripts is to copy this path update command into our shell configuration script:

```shell-session
$ echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc`
```

This will append `export PATH=$PATH:$SPARK_HOME/bin` to the user's `~/.bashrc`.  On next shell startup, the `$SPARK_HOME/bin` directory will be available in the user's `PATH`.

Any binary programs that exist in `$SPARK_HOME/bin` will now be available to run from the shell.

### Sourcing

**Sourcing a file executes the commands in the file in the current shell**.  

This is different from running a file, which will execute the commands in a new shell in a sub-process.

One common use of `source` is to load environment variables into the current shell:

```bash { title = "myfile" }
NAME=value
```

```shell-session
$ cat myfile
NAME=value
$ source myfile
$ echo $NAME
value
```

### RC Files

Your shell is configured using text files.  These text files are `source`'d during shell startup, before you see your first command line prompt.  Often these files are `.rc` files, which stands for "run command".

Which shell configuration file depends on both your shell and your operating system:

- `~/.bashrc` on Linux with Bash,
- `~/.zshrc` on Linux with Zsh,
- `~/.bashrc` & `~/.bash_profile` on MacOS with Bash,
- `~/.bashrc` & `~/.zshenv` on MacOS with Zsh.

Here's what a `.bashrc` might contain:

```bash { title = "~/.bashrc" }
# set environment variables
export PATH="$HOME/.local/bin:$PATH"
export EDITOR="vim"

# aliases
alias ll='ls -alF'
alias la='ls -A'
alias cls='clear && ls'
alias gs='git status'

# initialize tools
eval "$(pyenv init -)"
```

### Login vs. Non-Login Shells

A final complexity here is the difference between a login versus non-login shell.  

When you log into a system and start a shell, that's called a login shell. Login shells read certain configuration files, and the settings in those files persist for the session.

When you start a new terminal window or a new shell in an existing session, those are non-login shells. They read a different set of configuration files, and settings last only for the life of the shell.

This distinction depends on your operating system - for the shell and OS you are using, make sure you understand the intricacies of which configuration files are `source`'d.

### Aliases

A shell alias is a shortcut for a command or set of commands.  Aliases are commonly defined in your shell configuration files.

Here are some example aliases you can use for inspiration:

```bash
alias ls='ls -aGl'
alias c='clear'
alias cls='clear && ls'
```

You can use `"command"` to run a command without alias expansion:

```shell-session
$ "ls"
```

## Processes and Subprocesses

In Unix-like operating systems, a process is an instance of a running program. Every command you execute in a shell runs as a process with its own memory space and resources.

When a shell executes a command, it generally creates a new process (a child process or subprocess) to run that command:

```shell-session
$ echo "This runs in a subprocess"
```

A subprocess is any child process that's created by another process (the parent). When you run a command like `ls` or `python script.py`, the shell creates a subprocess to execute that command.

Subprocesses inherit environment variables from the parent process at the time the subprocess is created.  Understanding processes and subprocesses are crucial for using environment variables correctly.

Knowing how `export VAR=value` and `source file.sh` interact with subprocesses in different contexts can avoid some annoying debugging sessions.

### Subshells

A subshell is a child shell process created by the current shell. You can create a subshell explicitly with parentheses.

The command below will only change the current directory within the subshell, not in the parent shell:

```shell-session
$ (cd /tmp && ls)
```

Subshells are commonly used in command substitution with `$()` syntax, which executes commands in a subshell and captures their output:

```shell-session
$ echo "Today is $(date +%A)"
```

A subshell is specifically a child shell process - a new instance of the shell program itself. 

Child inherit environment variables from the parent shell but have their own working directory and local variables.

## `sudo`

**`sudo` (superuser do) is a command that allows users to run programs with the security privileges of another user**, by default the root user or system administrator. It's essential for operations that require elevated permissions, such as installing system packages or modifying system files.

{{< img 
    src="/images/bash-shell/please.jpg"
    width="500"
>}}

```shell-session
$ sudo apt update
[sudo] password for user: 
```

**Use `sudo` when you need to perform operations that require elevated privileges**. Common cases include:

- **Limited usage**: Only use sudo when absolutely necessary
- **Caution required**: Commands run with sudo can damage your system if used incorrectly
- **Command understanding**: Always know what a command does before giving it elevated privileges
- **Graphical applications**: Use specific tools like `gksudo` or `pkexec` instead
- **Avoid `sudo su`**: This gives you a root shell, which can be dangerous - prefer targeted sudo commands

```shell-session
$ sudo apt install python3-pip
$ sudo nano /etc/hosts
$ sudo systemctl restart nginx
$ sudo reboot
```

**While `sudo` allows temporary elevation of privileges for specific commands, logging in as root maintains elevated privileges for all commands**, which is generally considered less secure. Modern best practice is to use `sudo` for specific commands requiring elevated privileges rather than maintaining a root session.


## Keyboard Shortcuts

### Arrow Keys

The up and down arrow keys allow you to navigate through your command history:

- **Up arrow** (`↑`): Shows the previous command you typed. Press multiple times to go further back in history
- **Down arrow** (`↓`): Shows the next command in your history (after you've used the up arrow)
- **Left arrow** (`←`) and **right arrow** (`→`): Navigate within the current command line to edit characters

This feature is invaluable for reusing or modifying previously executed commands without retyping them.

### TAB Completion

The `TAB` key provides command and file path completion, saving you time and reducing typing errors:

- Press `TAB` once to complete a partial command or filename if there's only one possible match.
- Press `TAB` twice to show all possible completions if there are multiple matches.

Examples:
```shell-session
$ cd Doc[TAB]             # Autocompletes to "cd Documents/"
$ ls -[TAB][TAB]          # Shows all available options that start with "-"
$ cat Re[TAB]             # Autocompletes to "cat README.md" if that's the only match
```

TAB completion works with:

- **Commands**: Executable programs in PATH
- **File and directory names**: Local filesystem paths
- **Environment variables**: System configuration values
- **Username completion**: With tilde (~) prefix
- **Package names**: In package managers like apt

A common use of TAB completion is with the wildcard `*`. The asterisk wildcard matches any number of characters in file and directory names, making it powerful for filtering and batch operations.

If you have files and folders as follows:

```
$ tree
project/
├── data/
│   ├── sales-2024.csv
│   ├── sales-2023.csv
│   ├── customers.csv
│   └── products.json
├── docs/
│   ├── README.md
│   ├── SETUP.md
│   └── API.md
└── requirements.txt
```

When you use TAB completion with wildcards in this directory structure:

```shell-session
$ cat project/docs/*.md[TAB]      
$ cat project/docs/API.md project/docs/README.md project/docs/SETUP.md
```

```shell-session
$ ls project/data/sales-*[TAB]    
$ ls project/data/sales-2023.csv project/data/sales-2024.csv
```

This combination is particularly useful for:

- **Batch operations**: Quickly selecting multiple files with similar patterns (like all sales CSV files)
- **Verification**: Seeing exactly which files will be affected before executing a command
- **Exploration**: Discovering files matching certain patterns without listing everything
- **Command building**: Constructing complex commands with the right files

TAB completion with wildcards provides a safety mechanism - by expanding the wildcard before executing the command, you can verify exactly which files will be affected, preventing accidental operations on unintended files.

### CTRL-R

`CTRL-R` initiates a reverse search through your command history:

1. **Start search**: Press `CTRL-R` to begin searching
2. **Type query**: Enter a portion of the command you're looking for
3. **View matches**: The most recent matching command will appear
4. **Cycle matches**: Press `CTRL-R` again to see older matching commands
5. **Execute or edit**: Press `Enter` to run the displayed command or `Esc` to edit it

```shell-session
$ [Press CTRL-R]
(reverse-i-search)`git': git commit -m "Update documentation"
```

This is extremely useful for finding and reusing complex commands you've run previously without scrolling through your entire history.

Under the hood, your shell history is kept in a text file like `~/.bash_history`.

## Moving Around the File System

### Where Am I?

`pwd` shows us where we are in the file system - this is our current directory:

```shell-session
$ pwd
/Users/adamgreen/data-science-south-neu
```

We can remove output from the terminal with `clear`:

```shell-session
$ clear
```

### What is Here?

`ls` lists our current directory - showing us the files and folders:

```shell-session
$ ls
archetypes                      data-science-south.excalidraw   log.py                          public                          temp
assets                          data.txt                        main.py                         pyproject.toml                  temp.py
CLAUDE.md                       hugo.toml                       Makefile                        README.md                       temp.sh
content                         i18n                            mistake.py                      resources                       tests
data                            layouts                         out.xml                         static                          uv.lock
```

We can configure how `ls` works using **flags** - these are options that the `ls` program exposes.

Two common flags for `ls` are showing hidden files with `-a` in a long format with `-l`:

```shell-session
$ ls -al
total 48
drwxr-xr-x  12 adamgreen  staff   384 Mar  5 10:23 .
drwxr-xr-x   6 adamgreen  staff   192 Feb 15 09:42 ..
-rw-r--r--   1 adamgreen  staff  1176 Mar  5 10:23 CLAUDE.md
-rw-r--r--   1 adamgreen  staff   434 Jan 15 14:22 Makefile
-rw-r--r--   1 adamgreen  staff  1825 Jan 15 14:22 README.md
drwxr-xr-x   3 adamgreen  staff    96 Jan 15 14:22 archetypes
drwxr-xr-x   3 adamgreen  staff    96 Jan 15 14:22 assets
drwxr-xr-x   4 adamgreen  staff   128 Jan 15 14:22 content
drwxr-xr-x   3 adamgreen  staff    96 Jan 15 14:22 data
-rw-r--r--   1 adamgreen  staff  5125 Jan 15 14:22 hugo.toml
drwxr-xr-x   2 adamgreen  staff    64 Jan 15 14:22 i18n
drwxr-xr-x   6 adamgreen  staff   192 Jan 15 14:22 layouts
-rw-r--r--   1 adamgreen  staff   283 Jan 15 14:22 pyproject.toml
drwxr-xr-x   4 adamgreen  staff   128 Jan 15 14:22 static
drwxr-xr-x   3 adamgreen  staff    96 Jan 15 14:22 tests
```

### Changing Directories

We can change our current directory using `cd`, which will move down into a directory:

```shell-session
$ mkdir practice-dir
$ cd practice-dir
$ pwd
/Users/adamgreen/data-science-south-neu/practice-dir
```

We can move back up a directory with `cd ..` which moves into the parent directory:

```shell-session
$ cd ..
$ pwd
/Users/adamgreen/data-science-south-neu
```

Another useful `cd` command is `cd -` which moves to the directory we were previously in:

```shell-session
$ cd -
/Users/adamgreen/data-science-south-neu/practice-dir
$ pwd
/Users/adamgreen/data-science-south-neu/practice-dir
```

A special directory on Unix system is the home folder, which is the highest level folder for a user.  

We can get to the home folder in a few different ways:

```shell-session
$ cd ~
$ pwd
/Users/adamgreen
$ cd $HOME
$ pwd
/Users/adamgreen
$ cd
$ pwd
/Users/adamgreen
```

`~` is a special syntax that refers to the home folder. `$HOME` is an environment variable that is the path to your home folder.

The highest level of a file system on is in `/`. On MacOS contains folders like `/etc` and `/Users` - we can move to these directories using `cd`:

```shell-session
$ cd /bin
$ pwd
/etc
$ ls | head -n 5
.
..
[
bash
cat
```

Important top level directories include:

- **/etc**: Configuration files
- **/bin**: Programs
- **/Users**: User home directories (MacOS)
- **/home**: User home directories (Linux)

### Special Path Notation: Wildcards and Directory References

Unix-like systems use several special characters and symbols for referencing files and directories, making navigation more efficient:

**`.`** refers to the current directory

```shell-session
$ ls .
```

**`..`** refers to the parent directory:

```shell-session
$ cd ..
# Moves up one directory level
```

**`*`** is a wildcard that matches any number of characters in filenames:

```shell-session
$ ls *.txt
# Lists all .txt files in the current directory
```

**`?`** is a wildcard that matches exactly one character:

```shell-session
$ ls file?.txt
# Matches file1.txt, fileA.txt, but not file10.txt
```

**`[]`** a character class that matches any single character within the brackets:

```shell-session
$ ls file[123].txt
# Matches file1.txt, file2.txt, or file3.txt
```

These path notation symbols are especially powerful when combined:

```shell-session
$ ls ../*.md
# Lists all markdown files in the parent directory

$ cd ../..
# Moves up two directory levels

$ cp ./config.json ../backup/
# Copies a file from current directory to a backup directory one level up

$ rm ./*.log
# Removes all log files in the current directory
```

Mastering these path notations allows for efficient navigation and file operations without having to repeatedly type absolute paths.

## Files & Directories

### Making & Editing Files

We can make an empty file using `touch`:

```shell-session
$ touch myfile.txt
```

We can edit the contents of this file using a text editor.  

It's important to know how to use at least one of the text editors that are included with an operating system, for example `nano`:

```shell-session
$ nano myfile.txt
```

Or Vim:

```shell-session
$ vim myfile.txt
```

{{< img 
    src="/images/bash-shell/exiting-vi.png"
    caption="The DEC VT100 terminal (Hardware)"
    width="500"
>}}

### Making Directories

You can make a directory with `mkdir`:

```shell-session
$ mkdir practice
```

We can recursively create directories by passing the `-p` flag to `mkdir`:

```shell-session
$ mkdir -p practice/subfolder
```

### Moving Stuff

We can move a file or folder from one place to another with `mv`:

```shell-session
$ mv myfile.txt practice-dir/myfile.txt
```

Be careful with `mv` - it will overwrite the file!

We can copy a file or directory using `cp`:

```shell-session
$ cp myfile.txt practice-dir/myfile-copy.txt
```

### Removing Stuff

We can delete files with `rm`:

```shell-session
$ rm file
```

Be careful with `rm` - there is no trash can for `rm`!

We can also delete a folder using `rm`.  Two useful flags are `-r` which will recursively delete a folder and `-f` which will force deletion:

```shell-session
$ rm -rf directory
```

`-f` is needed as by default, `rm` will not delete a directory that has things in it.

### Viewing Files

`cat` is a program that prints the contents of a file to the terminal:

```shell-session
$ cat README.md
```

One common use of `cat` is at the start of a shell pipeline.  

For example, we can pipe the contents of a file into another program `grep`:

```shell-session
$ cat README.md | grep "data"
This is the source code for the Data Science South website, a resource for learning data science.
```

`head` will print the first `n` lines of a file:

```shell-session
$ head -n 3 README.md
# Data Science South

This is the source code for the Data Science South website, a resource for learning data science.
```

`tail` will print the last `n` lines of a file.

A file pager is a program that will keep a file open and allows you to move through that file.  

A most common pager is `less`:

```shell-session
$ less readme.md
```

## Searching 

We don't always know exactly where files or directories are, or what the contents of files are.

### Finding Directories

We can find directories using the `find` program:

```shell-session
$ find /path/to/search -type d -name "directory-name"
```

### Finding Files

To find a file by its name, we can use the `find` program.

If we have a directory structure as follows:

```
project/
├── data/
│   ├── data.csv
│   └── config.json
├── src/
│   ├── main.py
│   └── utils.py
└── docs/
    ├── readme.md
    └── setup.py
```

We can find all Python files in the project directory:

```shell-session
$ find project -type f -name "*.py"
project/src/main.py
project/src/utils.py
project/docs/setup.py
```

We can find a specific file by name:

```shell-session
$ find project -type f -name "config.json"
project/data/config.json
```

We can use the `-path` option to match part of the path:

```shell-session
$ find project -type f -path "*/data/*"
project/data/data.csv
project/data/config.json
```

### Finding Text in Files

To find a specific string in files, we can use `grep`.

If we have a file `data.txt`:

```text { title = "data.txt" }
haystack
a needle
haystack
another needle
haystack
haystack
```

We can show each line that has the string `hay`:

```shell-session
$ cat data.txt
haystack
a needle
haystack
another needle
haystack
haystack
$ grep "hay" data.txt
haystack
haystack
haystack
haystack
```

We can only show the filename:

```shell-session
$ grep -l "hay" data.txt
data.txt
```

Another useful flag is `-r`, which will search recursively through all files in a directory.

I use the following command many times per day:

```shell-session
$ grep -rl "pattern" .
```

### Finding Programs

To find where a program lives, we can use `which`:

```shell-session
$ which ls
/bin/ls
$ which python
/usr/bin/python
$ which bash
/bin/bash
```

This will show the location of the `ls` program, which is a binary that lives in the `/bin` folder.

## Redirection 

**Shells can redirect input and output between commands**.  

Redirection allows a program to accept text input and output text to another program.

**This enables the composition of shell programs, with programs generating text for each other**.

### Standard Input, Output & Error

The shell establishes three text streams:

1. **standard input** (STDIN) - the input stream (commonly a keyboard),
2. **standard output** (STDOUT) - the output stream (commonly a terminal console),
3. **standard error** (STDERR) - the error output stream (also usually goes to terminal console).

It's possible to direct these text streams to different places - for example to redirect STDOUT to a file, rather than the terminal console.

{{< img 
    src="/images/shell-redirection-1.svg"
    width="500"
>}}

### Pipes

**The pipe operator `|` allows you to chain commands together by passing the output of one command as input to another**. This enables composition of commands without using temporary files.

A pipe connects the standard output of the first command to the standard input of the second command.

Let's say we have a directory with these files:

```
project/
├── data.csv
├── report.txt
├── notes.txt
├── script.py
└── config.json
```

We can count the number of files in the directory:

```shell-session
$ ls project
data.csv  report.txt  notes.txt  script.py  config.json

$ ls project | wc -l
5
```

{{< img 
    src="/images/pipes.svg"
    width="400"
>}}

This first lists the files with `ls project`, then passes that output to `wc -l` which counts the lines.

We can filter for specific file types:

```shell-session
$ ls project | grep ".txt"
report.txt
notes.txt
```

Multiple pipes can be chained together to create more complex operations:

```shell-session
$ cat project/data.csv
name,age,city
alice,28,new york
charlie,35,chicago
bob,42,seattle
david,31,boston
eve,25,los angeles

$ cat project/data.csv | grep -v "name" | sort | head -n 3
alice,28,new york
bob,42,seattle
charlie,35,chicago
```

This pipeline:
1. Reads the CSV file
2. Removes the header line with `grep -v "name"`
3. Sorts the lines alphabetically
4. Shows only the first 3 results


### Redirecting Input

**The `<` operator is used to redirect input**. It reads input from a file instead of the keyboard.

If we have a file `numbers.txt`:

```text { title = "numbers.txt" }
5
3
8
1
4
2
```

We can use the `sort` command with input redirection to sort these numbers:

```shell-session
$ cat numbers.txt
5
3
8
1
4
2
$ sort < numbers.txt
1
2
3
4
5
8
```

This takes the contents of `numbers.txt` and passes it as input to the `sort` command.

{{< img 
    src="/images/shell-redirection-2.svg"
    width="500"
>}}

You can also achieve the same with (more on pipes `|` later):

```shell-session
$ cat numbers.txt | sort
```

### Redirecting Output

**The `>` operator is used to redirect output from a command to a file**. It will overwrite the file if it exists.

If we run a command that lists all files in the current directory:

```shell-session
$ ls -l > files.txt
$ cat files.txt
total 16
-rw-r--r--  1 user  staff  14 Aug  4 14:30 numbers.txt
-rw-r--r--  1 user  staff  98 Aug  4 14:31 files.txt
drwxr-xr-x  5 user  staff 160 Aug  4 14:29 project
```

The output that would normally be displayed in the terminal is instead written to `files.txt`.

{{< img 
    src="/images/shell-redirection-3.svg"
    width="300"
>}}

### Appending Output

**The `>>` operator appends output to the end of a file instead of overwriting it**.

If we already have a file and want to add more content:

```shell-session
$ echo "First line" > log.txt
$ cat log.txt
First line
$ echo "Second line" >> log.txt
$ cat log.txt
First line
Second line
```

The first command creates (or overwrites) `log.txt` with "First line", while the second command appends "Second line" to the file.

### Chaining Commands

You can chain commands together using various operators:

- **AND operator (`&&`)**: Run the second command only if the first command succeeds
- **OR operator (`||`)**: Run the second command only if the first command fails
- **Sequence operator (`;`)**: Run commands in sequence regardless of outcome

Example:

```shell-session
$ mkdir new_dir && cd new_dir || echo "Failed to create directory"
```

This attempts to create a directory and change into it. If either step fails, it prints an error message.

## Shell Scripting

### Why Use Shell Scripts?  

**Shell scripts allow code reuse and automation.** Bash is frequently used for scripting as it's the default shell on common Linux distributions like Ubuntu.

Even you are using Zsh as an interactive REPL via a terminal, you can still run scripts using the Bash program - below would work in both Zsh and Bash:

```shell-session
$ bash script.sh
```

### What is a Script?

A script is a text file containing lines of commands. Any command that can be executed in the terminal REPL with the Bash shell can also be put into a Bash script.

Below prints when we are using Bash as a REPL:

```shell-session
$ echo "this is printing in the Bash repl"
this is printing in the Bash repl
$ echo "Hello $USER, today is $(date +%A)"
Hello adamgreen, today is Tuesday
```

### Command Substitution

Command substitution allows you to capture the output of a command and use it as part of another command. This is one of Bash's most powerful features for creating dynamic, responsive scripts.

```shell-session
$ echo "Today is $(date +%A)"
Today is Tuesday
```

Command substitution creates a subshell for each command, which can impact performance in scripts with many substitutions.

#### Capturing Command Output in Variables

Command substitution is commonly used to store command output in variables:

```shell-session
$ current_date=$(date +%Y-%m-%d)
$ echo "Current date: $current_date"
Current date: 2025-03-05

$ file_count=$(find . -type f | wc -l)
$ echo "This project contains $file_count files"
This project contains 127 files
```


### The Shebang

The first line of a bash script usually begins with a 'shebang' (`#!`) followed by the path to the Bash program:

```bash
#!/usr/bin/env bash
```

This line tells the system that the file is a bash script and to use the Bash shell to interpret the script. 

A shebang is not necessary - even without a shebang, we can execute a script by specifying the `bash` program directly:

```shell-session
$ bash script.sh
```

A shebang allows us to execute a script like a standalone executable - without using Bash as part of our command:

```shell-session
$ ./script.sh
```

Common shebangs include:

- **Python**: `#!/usr/bin/env python` for Python scripts
- **Bash**: `#!/usr/bin/env bash` for Bash shell scripts
- **sh**: `#!/usr/bin/env sh` for POSIX-compliant shell scripts

We use `/bin/env` as this will find the program wherever it occurs in the `$PATH` shell environment variable.

### File Permissions and Execution

Before you can run your script using the `./` syntax, it must have execute permissions.

You can add execute permissions with the `chmod` command:

```shell-session
$ chmod +x script.sh
```

After setting this permission, we can execute our script like a standalone executable:

```shell-session
$ ./script.sh
```

You can also specify the program to run the script as part of the command - this works with and without a shebang in `script.sh`:

```shell-session
$ bash script.sh
```

### Writing a Hello World Bash Script

Let's start with the traditional Hello World program as a Bash script:

```bash { title = "hello.sh" }
#!/usr/bin/env bash

# comments in Bash use a #
echo "Hello, World!"
```

`echo` is a shell program that prints its arguments to standard out - commonly to a terminal.

We can add a variable for a name:

```bash { title = "hello.sh" }
#!/usr/bin/env bash

name="adam"
echo "Hello, $name!"
```

We use the `$name` syntax to refer to the value of the `name` variable within the script.

### Accepting Command Line Arguments in Shell Scripts

**Command line arguments provide a way to customize the behavior of a script each time it's run**. They are provided after the script name, separated by spaces.

Inside the script, you can access the arguments using special variables - `$1` refers to the first argument:

```bash { title = "myscript.sh" }
#!/usr/bin/env bash

name=$1
echo "Hello, $name!"
```

Running a Bash script with command line arguments:

```shell-session
$ chmod +x myscript.sh
$ ./myscript.sh adam
Hello, adam!
```

### Using Environment Variables in Shell Scripts

**Environment variables can also customize script behavior**. They can be set before running the script and accessed within the script.

To access environment variables in a script, use the `$VARIABLE_NAME` syntax:

```bash { title = "env-script.sh" }
#!/usr/bin/env bash

echo "Running in $STAGE environment"
# use a default value if the environment variable is not set
: "${LOG_LEVEL:=info}"
echo "Log Level: $LOG_LEVEL"
```

Running a script with environment variables:

```shell-session
$ STAGE=production ./env-script.sh
Running in production environment
Log Level: info

$ STAGE=dev LOG_LEVEL=debug ./env-script.sh
Running in dev environment
Log Level: debug
```

You can also set environment variables within your script, which will be available to any processes started by the script:

```bash { title = "set-env.sh" }
#!/usr/bin/env bash

# set environment variable for this process (script or REPL) and its child processes
export API_URL="https://api.example.com"

# script execution will have access to the API_URL environment variable
./call-api.sh
```

Environment variables are commonly used for:

- **Configuration settings**: Database connections, API endpoints, service URLs
- **Behavior control**: Debug mode, verbose output, logging levels
- **Sensitive information**: API keys, credentials, tokens
- **Inter-process communication**: Passing information between scripts or processes

It's important to understand that environment variables set in a script will not be automatically available in the parent shell that called the script. This is because each script runs in a separate subprocess:

```bash { title = "set-env.sh" }
#!/usr/bin/env bash

# not available in the parent shell
export MY_VAR="hello"
```

```shell-session
$ ./set-env.sh
$ echo $MY_VAR
# Nothing is printed because MY_VAR is not set in the parent shell
```

If you need to set environment variables in the parent shell, you can source the script instead of executing it:

```shell-session
$ source ./set-env.sh
$ echo $MY_VAR
hello
```

This pattern is commonly used in setup scripts like `activate` in Python virtual environments.

## Functions 

We can write a function in a Bash script using the `function` keyword:

```bash
function greet {
    echo "Hello, $1"
}

greet "adam"
```

## Summary

In this lesson we've covered:

- **What is Bash**: A shell program that runs other programs, enabling command execution, pipelines, scripting, and history features
- **Terminal vs shell vs command line**: Understanding the differences between these related but distinct components
- **Shell configuration**: Customizing your shell environment with `.bashrc`, `.zshrc`, and other configuration files
- **Environment variables**: Using and configuring your shell environment with variables like `$PATH`
- **Keyboard shortcuts**: Using arrow keys, tab completion, and CTRL-R for efficient command-line navigation
- **Sudo usage**: Running commands with elevated privileges safely and effectively
- **Navigation**: Moving around the filesystem with commands like `cd`, `pwd`, and special path references
- **Special path notation**: Using wildcards (`*`, `?`, `[]`) and directory references (`.`, `..`) for efficient file operations
- **File operations**: Creating, viewing, moving, and deleting files and directories with `touch`, `cat`, `mv`, `rm` and more
- **Redirection and pipes**: Connecting programs together using `|`, `>`, `>>`, and `<` to build powerful command pipelines
- **Shell scripting**: Writing reusable scripts with commands, variables, command-line arguments, and functions

These skills form the foundation for many data science workflows, enabling everything from automated data processing to CI/CD pipelines and Docker deployments.

### Next Steps

Recommended resources:

- **Survival guide for Unix newbies**: A short guide on Unix, available at [matt.might.net](https://matt.might.net/articles/basic-unix/)
- **Effective Shell**: A book of essentials on how to use the shell, available at [effective-shell.com](https://effective-shell.com/)
- **BashGuide**: A guide on Bash and Bash scripting, available at [mywiki.wooledge.org](https://mywiki.wooledge.org/BashGuide)
- **Missing semester**: Proficiency with tools, including shell, shell scripting and the command line, available at [missing.csail.mit.edu](https://missing.csail.mit.edu/)

Recommended next lessons:

- **Git**: Learn version control fundamentals at [datasciencesouth.com/lessons/git/](https://datasciencesouth.com/lessons/git/)
- **CI/CD**: Explore continuous integration and deployment at [datasciencesouth.com/lessons/ci-cd/](https://datasciencesouth.com/lessons/ci-cd/)
