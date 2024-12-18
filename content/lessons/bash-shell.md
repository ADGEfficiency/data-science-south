---
title: Bash Shell
summary: Learn how to use a shell, write shell scripts, and configure your shell environment.
competencies:
- "Software Engineering"
---

## Why Learn the Shell?

- **Efficiently use a computer** - precision
- **Repeat and automate tasks** - automating text based commands is easier than automating pointing and clicking. 
- **Unlock powerful tools** - some development tasks can only be done through the shell - many are best done through a shell.

## Terminal

The terminal, command line and shell are often used interchangeably. 

Each however is a distinct tool - all three are used when using a computer via text input.

**The terminal (also called a console) is an interface that controls user input & output**. It allows you to interact with computers through text commands.

![](/static/lesson/why-shell/f1.png '<a class="hover:text-cyan-400 hover:underline" href="https://en.wikipedia.org/wiki/File:DEC_VT100_terminal_transparent.png">The DEC VT100 Terminal</a>')

The terminal originates in the mainframe era of computing.  Historically a terminal was hardware, with a keyboard and a screen.  Terminals could connect to other computers - you could run programs on a central computer from your terminal.

The terminals most developers use today are software - using terminal emulator programs on a computer.  These software terminals can also be used to connect to other computers.

Popular terminal emulators include:
- iTerm2 (Mac), 
- Windows Terminal (Windows),
- Gnome Terminal (Linux).

## Command-Line

The command-line is the space or interface in the terminal where you type commands. 

When you launch your terminal, you are in a command-line interface.

```shell-session
$ echo "this is the command line"
this is the command line
```

## The Shell

A shell is a computer program that executes text commands. You can combine many different shells with a given terminal emulator.

Shells are used in two ways:

1. as a REPL (Read-Eval-Print Loop) that runs interactively,
2. as programming language that runs via scripts.

A shell is automatically started in a new terminal. When you write text in the command-line of a terminal, it is executed in a shell, the output displayed, and then a new command line prompt is shown, ready for the next user input.

**The shell we shall use in this lesson is the Bash shell**.

### Shells

There are many different shells available -- commonly used shells are:

- `sh` -- the Bourne Shell, the original Unix shell. It introduced features like redirection (`>`, `>>`, `<`) and piping (`|`).
- `bash` -- the Bourne Again Shell, an improved version of Bourne Shell, is the default shell for many Unix and Linux systems. 
- `zsh` -- the default shell on MacOS, which improves on Bash,
- `PowerShell` -- a shell developed by Microsoft for Windows.

The best shells to know are the ones that are most easily available in the cloud. Bash is the most common shell on Linux systems, which is the most common compute environment available in the cloud.

### Shell Notation

`$` indicates a command is run interactively in a Bash shell -- you don't need to write this leading `$` when you are typing in the shell.

For example, if you see:

```shell-session
$ ls
```

To reproduce this in your terminal, you only need to type `ls`.

### Using the Bash Shell as a REPL

We can use the shell as a REPL to list the current directory files & directories using the `ls` program:

```shell-session
$ ls
```

### Using the Shell as a Programming Language

We can use the shell as a programming language via shell scripting - an example shell script that lists the current directory using `ls`:

```bash { title = "script.sh" }
#!/usr/bin/env bash
ls
```

We can then execute this script in a shell REPL:

```shell-session
$ bash script.sh
```

### Common Shell Programs

A shell has its own syntax and set of commands, along with a collection of programs available.  

Common shell programs include:

- `ls` -- list files & directories,
- `pwd` -- print working directory,
- `cd` -- change directory,
- `cat` -- print file contents.

A shell program is a common way for developers to share their work.  AWS and Azure both offer a command-line interface (CLI) that allows interacting with resources on the AWS cloud.

The programs that are available in your shell are programs that are in the shell's `$PATH` environment variable - more on the `$PATH` and environment variables later.

## Whitespace

Bash use the space character to separate commands & arguments.  

This makes working at the shell natural, but requires some care when using with spaces.  

**The shell will expand spaces by default into separate commands** -- this means that spaces in the wrong places can cause shell scripts to break.

We can use the `echo` program to print text to the terminal.

The `echo` program takes an argument of the text to print -- enclosing our message `"this is fine"` in quotes will prevent the shell from expanding the spaces in our message:

```shell-session
$ echo "this is fine"
```

This space based expansion is one reason why you should never put spaces in file names -- use `-` or `_` as a separator in file names:

```bash
#  this is bad
/folder name/file name.txt

#  do this instead
/folder-name/file_name.txt
```

If you do use spaces, you may end up seeing (or having to write!) your paths by escaping the spaces with a `bash\`:

```bash
#  this is harder to work with
/folder\ name/file\ name.txt
```

## Navigation

### Where Am I?

`pwd` shows us where we are in the file system - this is our current directory:

```shell-session
$ pwd
```

We can remove output from the terminal with `clear`:

```shell-session
$ clear
```

### What is in the Current Directory?

`ls` lists our current directory - showing us the files and folders:

```shell-session
$ ls
```

We can configure how `ls` works using **flags** - these are options that the `ls` program exposes.

Two common flags for `ls` are showing hidden files with `-a` in a long format with `-l`:

```shell-session
$ ls -al
```

### Changing Directories

We can change our current directory using `cd`, which will move down into a directory:

```shell-session
$ cd practice-dir
```

We can move back up a directory with `cd ..`, which moves into the parent directory:

```shell-session
$ cd ..
```

Another useful `cd` command is `cd -`, which moves to the directory we were previously in:

```shell-session
$ cd -
```

A special directory on Unix system is the home folder, which is the highest level folder for a user.  

We can get to the home folder in a few different ways:

```shell-session
$ cd ~
$ cd $HOME
$ cd
```

`~` is a special syntax that refers to the home folder. `$HOME` is a special variable that contains the path to the home folder.

The highest level of a file system on MacOS contains folders like `/etc` and `/Users` - we can move to these directories using `cd`:

```shell-session
$ cd /etc
```

Important top level directories include:

- `/etc` - configuration files,
- `/bin` - programs,
- `/Users` - user home directories on MacOS,
- `/home` - user home directories on Linux.
- 
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
```

`head` will print the first `n` lines of a file:

```shell-session
$ head -n 3 readme.md
```

`tail` will print the last `n` lines of a file:

```shell-session
$ tail -n 3 readme.md
```

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

To find a file by it's name, we can use the `find` program:

```shell-session
$ find /path/to/search -type f -name "file-name"
```

We can use the wildcard character `*` to match any characters.

For example, to find all Python scripts:

```shell-session
$ find /path/to/search -type f -name "*.py"
```

### Finding Text in Files

To find a specific string in files, we can use `grep`:

```shell-session
$ grep "search-string" filename.txt
```

### Finding Programs

To find where a program lives, we can use `which`:

```shell-session
$ which ls
```

This will show the location of the `ls` program, which is a binary file.

## Redirection 

**Shells can redirect input and output between commands**.  

Redirection allows a program to accept text input and output text to another program.

This enables the composition of programs, with programs generating text for each other.

### Standard Input, Output & Error

The shell establishes three text streams:

- standard input (stdin) -- the input stream, in a REPL this is the keyboard,
- standard output (stdout) -- the output stream, in a REPL this is the terminal console,
- standard error (stderr) -- the error output stream, in a REPL this is also the terminal console.

![](/static/mermaid/redirection1.svg)

### Redirecting Input

The `<` operator is used to redirect input. It reads input from a file instead of the keyboard. For example:

```shell-session
$ sort < unsorted.txt
```

![](/static/mermaid/redirection2.svg)

### Redirecting Output

The `>` operator is used to redirect output from a command to a file, overwriting the file if it exists.

The following redirects the output of `ls -l` to a file named `files.txt`.

```shell-session
$ ls -l > files.txt
```

![](/static/mermaid/redirection3.svg)

### Appending Output

The `>` command will overwrite -- if you want to append the output to an existing file rather than overwriting it, you can use the >> operator.

```shell-session
$ ls -l >> files.txt
```

This will sort the lines in the `unsorted.txt` file.

### Pipes

The pipe operator `|` allows you to chain commands together by passing the output of one command as input to another. This enables powerful command combinations without needing temporary files.

A pipe connects the standard output of the first command to the standard input of the second command.

```shell-session
$ ls | wc -l
```

Multiple pipes can be chained together to create more complex operations:

```shell-session
$ ls -l | grep ".txt" | sort | head -n 5
```

## Shell Configuration

### Environment Variables

The shell is a stateful system -- a shell stores data in between execution of programs.  This data is stored in environment variables.

Environment variables can set and accessed in the shell, and then used as part of shell commands.

Programming languages like Python can access environment variables -- in Python we can use `os.ENVIRON` to access the environment variables of the shell process the Python program is running in.

#### Setting an Environment Variable

We can set an environment variable using `NAME=VALUE` -- note the lack of space around the `=`:

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

Our shell is run in a process -- there are hundreds of processes running on your computer now.

Many actions we take in a shell create a new process -- this new process is called a sub-process.  For example, when we run a Python script in a shell, a new Python process is created.

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

You can access an environment variable using the `$NAME` syntax.  We can use `echo` to view the value of an environment variable:

```shell-session
$ echo $HOME
```

### The `PATH`

The `PATH` environment variable is a list of directories, separated by a `:`.

The `PATH` environment variable is a list of directories that the shell will search when you type a command.  Appending a directory to `PATH` makes that program accessible via a shell from any directory.

The `PATH` variable will be quite long -- a useful tip is to pipe the variable into `tr`, which can replace the `:` used to separate the paths with a new line `\n`:

```shell-session
$ echo $PATH | tr ":" "\n"
```

It's common to see the `PATH` variable modified in scripts by appending a new path onto the existing path:

```shell-session
$ export PATH=$PATH:$SPARK_HOME/bin
```

A common pattern you will see in install scripts is to copy this path update command into our shell configuration script:

`$ echo 'export PATH=$PATH:$SPARK_HOME/bin' >> ~/.bashrc`

This will append `export PATH=$PATH:$SPARK_HOME/bin` to the user's `~/.bashrc`.  On next shell startup, the `$SPARK_HOME/bin` directory will be available in the user's `PATH`.

Any binary programs that exist in `$SPARK_HOME/bin` will now be available to run from the shell.


### Sourcing

Sourcing a file executes the commands in the file in the current shell.  

This is different from running a file, which will execute the commands in a new shell in a sub-process.

One common use of `source` is to load environment variables into the current shell:

```bash { title = "myfile" }
NAME=value
```

```shell-session
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

### Login vs. Non-Login Shells

A final complexity here is the difference between a login versus non-login shell.  

When you log into a system and start a shell, that's called a login shell. Login shells read certain configuration files, and the settings in those files persist for the session.

When you start a new terminal window or a new shell in an existing session, those are non-login shells. They read a different set of configuration files, and settings last only for the life of the shell.

This distinction depends on your operating system -- for the shell and OS you are using, make sure you understand the intricacies of which configuration files are `source`'d.

## Aliases

A shell alias is a shortcut for a command or set of commands.  Aliases are commonly defined in your shell configuration files.

Here are some example aliases you can use for inspiration:

```bash
alias ls='ls -aGl'
alias c='clear'
alias cls='clear && ls'
alias bashrc='vim ~/git/dotfiles/.bashrc'
```

You can use `"command"` to run a command without alias expansion:

```shell-session
$ "ls"
```

## Shell Scripting

Why shell scripts?  Shell scripts allow:

- code reuse,
- automation of routine tasks, 
- running jobs in the background, 
- chaining together multiple commands or scripts. 

Bash is frequently used for scripting as it's the default shell on common Linux distributions like Ubuntu.

Even you are using Zsh as an interactive REPL via a terminal, you can still run scripts using the Bash program -- below would work in both Zsh and Bash:

```shell-session
$ bash script.sh
```

The shell is able to find the program `bash` in it's `$PATH`.

### What is a Script?

A script is a text file containing lines of commands.

Any command that can be executed in the terminal can also be put into a Bash script.

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

- Python `#!/usr/bin/env python`,
- Bash `#!/usr/bin/env bash`,
- Sh `#!/usr/bin/env sh`.

We use `/bin/env` as this will find the program wherever it occurs in the `$PATH` shell environment variable.

## File Permissions and Execution

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

## Writing a Bash Script

### Hello World

Let's start with the traditional Hello World program as a Bash script:

```bash { title = "script.sh" }
#!/usr/bin/env bash

#  comments in Bash use a #
echo "Hello, World!"
```

`echo` is a shell program that prints its arguments to standard out - commonly to a terminal.

### Adding Variables

We can add a variable for a name:

```bash { title = "script.sh" }
#!/usr/bin/env bash

name="adam"
echo "Hello, $name!"
```

We use the `$name` syntax to refer to the value of the `name` variable within the script.

### Functions in Bash

We can write a function in a Bash script using the `function` keyword:

```bash
function greet {
    echo "Hello, $1"
}

greet "adam"
```

### Accepting Command Line Arguments

Command line arguments provide a way to customize the behavior of a script each time it's run. They are provided after the script name, separated by spaces.

Here is an example of running a bash script with command line arguments:

```shell-session
$ ./myscript.sh adam
```

Inside the script, you can access the arguments using special variables -- `$1` refers to the first argument:

```bash { title = "script.sh" }
#!/usr/bin/env bash

name=$1
echo "Hello, $name!"
```
