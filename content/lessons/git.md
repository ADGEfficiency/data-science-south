---
title: Git
summary: TODO
---

## Why Learn Git?

Why should you learn Git?

- **Widely used** - standard tool for version control for software engineers and data professionals.
- **Version control** - Git allows developers to maintain a history of changes in a code base.
- **Collaboration** - Git allows multiple developers to work on the same code base.

## Tooling

**Different developers use different tools for using Git**.

This lesson focuses on using Git through a terminal via a CLI.

Git commits & branches can be naturally visualized, making visual tools popular and useful.

If you prefer a more visual way to use Git, feel free to use a tool like GitKraken or Github Desktop and repeat the actions we do in the terminal in your Git GUI program.

### Git CLI

[Install Git here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - you can then use the Git CLI `lang:shell-session:$ git`:

```shell-session
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```

### Git Kraken

Git Kraken is a GUI developed by Axosoft -- [you can install it here](https://www.gitkraken.com).

![](/static/lesson/git-patterns/kraken.png)

### TODO - VS Code Plugins

### TODO - inside Databricks

## Version Control

**Git's main function is version control of files**.  Developers write code that is stored in text files.

Version control gives developers a history of their work, by providing the changes made to a given file.

Version control also allows switching between different versions of a codebase.

### How does Git track changes in a codebase?

**Git works by keeping track of every change made to a project**.

Every time a change is made and saved in Git, it is recorded in the project's history. This means that you can go back and see exactly what changes were made when.

This keep everything approach means that anything you commit to a repository will be there forever.  This is important to remember when working with secrets (like AWS keys) or with large datasets.

## Repos

### Local Repositories

A local repository is created on a developer's computer using the `lang:shell-session:$ git init`, and is contained in a folder called `lang:shell-session:.git`. 

It contains a copy of the entire project commit history, including all the commits and branches. A local repository can be used for version control and collaboration even when working offline.

### Remote Repositories

A remote repository is a copy of the local repository that is stored on a remote server, such as GitHub. 

The remote allows developers to share their work.

A remote repository can be created using `lang:shell-session:$ git remote add`, and it can be connected to a local repository using `lang:shell-session:$ git push` and `lang:shell-session:$ git pull`.



### Initializing a Repo

The `lang:shell-session:$ git init` command is used to initialize a new repository in the current directory:

```shell-session
$ git init
Initialized empty Git repository in .git/
```

It creates a directory `lang:shell-session:.git`, that contains data for the new Git repository:

```shell-session
$ ls .git
HEAD            config          description     hooks           info            objects         refs
```

You don't need to understand or look at these files - the most important thing to know is that the `lang:shell-session:.git` folder is where Git will store the entire history of your Git project:

```shell-session
$ tree .git
.git
├── config
├── description
├── HEAD
├── hooks
│  ├── applypatch-msg.sample
│  ├── commit-msg.sample
│  ├── fsmonitor-watchman.sample
│  ├── post-update.sample
│  ├── pre-applypatch.sample
│  ├── pre-commit.sample
│  ├── pre-merge-commit.sample
│  ├── pre-push.sample
│  ├── pre-rebase.sample
│  ├── pre-receive.sample
│  ├── prepare-commit-msg.sample
│  ├── push-to-checkout.sample
│  ├── sendemail-validate.sample
│  └── update.sample
├── info
│  └── exclude
├── objects
│  ├── info
│  └── pack
└── refs
   ├── heads
   └── tags
```

### Status

The `lang:shell-session:$ git status` command allows you to check the status of your repository:

```shell-session
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

### Deleting a Repo

You can delete a Git repo by:

```shell-session
$ rm -rf .git
```

This can be useful when you get a Git repo into a bad state (it happens - for example if you checked in secrets) and just want to start again.

Be careful though - if you remove this folder (and you don't have a remote copy on a service like GitHub) then you entire project history will be lost.

**A repository (or repo) holds all the files and metadata associated with a codebase, including the codebase's commit history and branches**.  

A repository is created using `lang:shell-session:$ git init`. A repository can be either local or remote.

Status will show you what files are staged or unstaged and tracked versus untracked.

## Commits

**The commit is the atomic unit of Git**.

Git joins changes from multiple files into a single unit - a commit.  These commits are snapshots of your project at different points in time.

**A Git commit is a snapshot of an entire codebase at one point in time**.  

### Commit Hashes

A commit has unique hash identifier - a string like `lang:shell-session:d6a583a419797104d985ab8aaa471a153cd24d2f`.  

The hash uniquely identifies a commit.

### Diffs

**The difference between one commit to another is known as a diff**.  

When developers are reviewing the commits of others, they often only look at the diff between one commit and another.

### Adding Untracked Files to a Commit

Commits are created using `lang:shell-session:$ git commit` and include a message - a short bit of text that describes what changes are made with each commit.

Let's create a new Git repository with `lang:shell-session:$ git init`, and create a file `lang:shell-session:README.md`:

```shell-session
$ git init
$ touch README.md
```

If we now check what is going on, Git tells us that there is an untracked file:

```shell-session
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md

nothing added to commit but untracked files present (use "git add" to track)
```

We can add this file to the repository, which makes the file tracked and staged:

```shell-session
$ git add README.md
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

We can then commit this file, which turns the staged changes into committed changes:

```shell
$ git commit -m 'initial commit'
[master (root-commit) db9a248] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
[master (root-commit) 19d0f58] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

We now have this commit in our history, which we can see through `lang:shell-session:$ git log`:

```shell-session
$ git log --stat
commit 19d0f58e53bfcf2ee449477e60680285cd7a2d4e (HEAD -> master)
Author: Adam Green <adam.green@adgefficiency.com>
Date:   Sat Aug 5 15:14:38 2023 +1200

    initial commit

 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
```


These changes to our Git repository live only on our local machine.

### Adding Multiple Files to a Commit 

Let's simulate some more work by changing our `lang:shell-session:README.md` file.

Git now tells us that we have changes to tracked files that are unstaged:

```shell-session
$ echo "readme changes" >> README.md
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

Let's add a new file - this file `lang:shell-session:main.py` is untracked by Git:

```shell-session
$ touch main.py
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py

no changes added to commit (use "git add" and/or "git commit -a")
```

We can add both of these changes into a single commit with `lang:shell-session:$ git add .`, which adds all changes in the current directory and subdirectories:

```shell-session
$ git add .
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   README.md
	new file:   main.py
```

We now have two changes staged for commit - one change to a tracked file `lang:shell-session:README.md` and a new untracked file `lang:shell-session:main.py`.

We can create the Git commit using `lang:shell-session:$ git commit -m 'message`:

```shell-session
$ git commit -m 'second commit'
[master e8f9742] second commit
 2 files changed, 1 insertion(+)
 create mode 100644 main.py
```

`lang:shell-session:git log` now shows our two commits:

```shell-session
$ git log --stat
commit e8f9742ab4f0c61333ce350c78cd3653bda77a9a (HEAD -> master)
Author: Adam Green <adam.green@adgefficiency.com>
Date:   Sat Aug 5 15:27:56 2023 +1200

    second commit

 README.md | 1 +
 main.py   | 0
 2 files changed, 1 insertion(+)

commit 19d0f58e53bfcf2ee449477e60680285cd7a2d4e
Author: Adam Green <adam.green@adgefficiency.com>
Date:   Sat Aug 5 15:14:38 2023 +1200

    initial commit

 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
```

### Ways to Add Files to a Git Commit

There are a few ways to add files to a Git commit:

- `lang:shell-session:$ git add README.md` - tracks & changes in a file `README.md`,
- `lang:shell-session:$ git add .` - tracks & changes all files in all directories,
- `lang:shell-session:$ git add -u` - adds changes in all tracked files (untracked files are ignored),
- `lang:shell-session:$ git add *` - tracks & changes all files in the current directory only.

### Commit History

Commits are organized in a linear sequence which allows developers to see the entire history of changes made to the project. This linear sequence is the commit history.

The entire commit history is stored in the project's repository and can be viewed using `lang:shell-session: $ git log`.

### Log

The `lang:shell-session:$ git log` command displays a list of all the commits made to the repository.

Each entry shown by `lang:shell-session:$ git log` includes the commit's SHA-1 checksum, the author's name and email, the date and time of the commit, and the commit message.

```shell-session
$ git log
commit 8a121f9375c5e33277d34810a674410c94588b8d (HEAD -> master)
Author: Your Name <your-email@example.com>
Date:   Mon May 30 23:12:39 2023 +0000

    Initial commit
```

Two useful `lang:shell-session:$ git log` commands are:

- show all files changed in the last 5 commits - `lang:shell-session:git log --pretty=fuller --abbrev-commit --stat -n 5`,
- show all files changed with diffs in the last 5 commits - `lang:shell-session:git log --pretty=fuller --abbrev-commit --stat -n 5`,

## GitHub

### What is Github?

GitHub is a web-based platform that hosts Git repositories and adds collaboration features on top of Git.

Git is the version control system that tracks changes in your code. GitHub is a service that hosts Git repositories and makes it easier to collaborate with others.

GitHub is as a central hub where developers can share their code, contribute to others' projects, and collaborate on software development.

### Creating a Repository on Github

So far we have only created a Git repository locally - it only exists on our local machine.

To put a Git repo onto Github, we need to do a few things:

1. [sign up for a GitHub account](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwj09Nify8SAAxVMaPUHHRv2DhYQFnoECBEQAQ&url=https%3A%2F%2Fgithub.com%2Fjoin&usg=AOvVaw0H9TK-nu7JfXaoNeNMgJEk&opi=89978449) & authorize locally,
2. create the remote repository on GitHub through the web UI,
3. push your local Git repository to the Github repository.

### Create the Remote Repository on GitHub

After logging in to Github, you'll find a `'+'` button on the upper right side where you can add a new repository:

![](/static/lesson/git-patterns/github.png)

You'll be directed to a new page where you'll be asked to fill out some information:

```text
Repository Name: Choose a name for your GitHub repository. It should ideally match your local repository to avoid confusion.

Description (optional): You can provide a short description of your project.

Visibility: Choose whether the repository should be public (visible to everyone) or private (only visible to you and collaborators you choose).

Initialize this repository with: This section should typically be left blank as you're pushing an existing repository.
```

Almost always it's best to initialize empty repositories on GitHub.

![](/static/lesson/git-patterns/github1.png)

### Push the Local Git Repository to the GitHub Repository

Next, you need to link your local repository to the remote repository on GitHub and push your commits to it. To do this, use the following commands:

Now you have a repository on GitHub, you can push your local repo up into GitHub by adding it as a remote repository called `lang:shell-session:origin`:

```shell-session
$ git remote add origin https://github.com/USER/the-repo-name
$ git push -u origin master
```

`lang:shell-session:git push -u origin master` pushes your commits to the 'master' branch of the 'origin' repository. The `lang:shell-session:-u` flag tells Git to remember the parameters.

Now your local Git repository is connected & backed up to your GitHub repository, enabling version control.  

Other developers can now clone and work on it separately, enabling collaboration.

## Branching

**A branch is a copy of the codebase that can be worked on independently**. 

**Branches allow you to work on multiple features or bug fixes in parallel without affecting the main development branch**. 

A branch is given a human readable name like `lang:shell-session:amazing-new-feature` or `lang:shell-session:fix-the-bug`.

### Creating a New Branch

A branch is created using the `lang:shell-session:$ git branch` command and can be switched between using the `lang:shell-session:git checkout` command. 

When a branch is created, it is based on the current state of the codebase, and it includes all the commits up to that point. 

Any new commits made while on that branch will be added to that branch, creating a separate branch history.

### Merging Branches

Once the work on a branch is finished, it can be merged back into the main codebase using `lang:shell-session:$ git push`, `lang:shell-session:$ git pull` or `lang:shell-session:$ git merge`. This allows developers to incorporate their work into any other branch.

The ability to work on multiple branches allows developers to work on features or bug fixes in separate versions of the same codebase, without affecting other branches of the codebase.

### Branch Naming

Similar to commit messages, consistency around branch naming can be useful.

For example, prefixing with `feature/` or `bug/` or a GitHub issue number can help other understand what a branch is used for.

### Master Branch is the Default

By default Git starts on the master branch:

For Git the `lang:shell-session:master` branch is the default branch - it's the one that is automatically created when you create a Git repository:

```shell-session
$ git status
On branch master
nothing to commit, working tree clean
```

It's also common for the default branch to be called `lang:shell-session:main`.

### Creating a New Branch

We can create a new branch using `lang:shell-session:git branch`:

```shell-session
$ git branch tech/requirements
```

We can then switch to this branch with `lang:shell-session:git checkout`:

```shell-session
$ git checkout tech/requirements
Switched to branch 'tech/requirements'
```

This new branch is at the same state as `lang:shell-session:master`.

### Adding Commits to a Branch

We can add commits to a branch using our `lang:shell-session:git add` and `lang:shell-session:git commit` workflow:

```shell-session
$ echo "pandas" >> requirements.txt
$ git add .
$ git commit -m 'added Python pip requirements'
[tech/requirements 9a963bf] added Python pip requirements
 1 file changed, 1 insertion(+)
 create mode 100644 requirements.txt
```

### Showing the Diff Between Two Branches

We now have two branches `lang:shell-session:master` and `lang:shell-session:tech/requirements`.

We can look at the difference between these branches using `lang:shell-session:git diff`:

```shell-session
$ git diff master tech/requirements
diff --git a/requirements.txt b/requirements.txt
new file mode 100644
index 0000000..fb6c7ed
--- /dev/null
+++ b/requirements.txt
@@ -0,0 +1 @@
+pandas
```

Diffs can be quite large -- many developers will view the diff between branches on a tool like GitHub or using [git difftool](https://git-scm.com/docs/git-difftool).

### Merging Branches

We can bring our changes from `lang:shell-session:tech/requirements` into our `lang:shell-session:master` branch using `lang:shell-session:git pull`:

```shell-session
$ git checkout master
Switched to branch 'master'
$ git pull . tech/requirements
From .
 * branch            tech/requirements -> FETCH_HEAD
Updating e8f9742..9a963bf
Fast-forward
 requirements.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 requirements.txt
```

`lang:shell-session:git pull` allows specifying the repository (in the command above `lang:shell-session:.`).

It's also possible to use `lang:shell-session:git merge`:

```shell-session
$ git checkout master
Switched to branch 'master'
$ git merge tech/requirements
Updating e8f9742..9a963bf
Fast-forward
 requirements.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 requirements.txt
```

### Pushing a Branch to the GitHub Remote

Currently we have our two branches locally -- we can push these branches up to our remote repository `lang:shell-session:origin` on GitHub:

```shell-session
$ git push origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (9/9), 727 bytes | 727.00 KiB/s, done.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), done.
To github.com:ADGEfficiency/the-repo-name.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```

```shell-session
$ git push origin tech/requirements
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'tech/requirements' on GitHub by visiting:
remote:      https://github.com/ADGEfficiency/the-repo-name/pull/new/tech/requirements
remote: 
To github.com:ADGEfficiency/the-repo-name.git
 * [new branch]      tech/requirements -> tech/requirements
```
