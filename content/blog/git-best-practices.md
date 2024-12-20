---
title: Git Best Practices
summary: Five patterns to guide your Git workflows.
---

## Commit Messages

**A commit message should describe the changes made in the commit and provide context for those changes**. 

This makes it easier to understand what was changed, when it was changed, and why it was changed when reviewing the commit history. 

```shell-session
$ git commit -m "docs: a clear and descriptive commit message"
```

Good commit messages are consistent, clear and concise.

### Conventional Commits

The [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#summary) provides a set of rules for commit messages:

```text
<type>[optional scope]: <description>
```

```shell-session
$ git commit -m "feat(auth): add login functionality"
$ git commit -m "fix(button): resolve alignment issue"
```

The types we use the most are `feat`, `docs`, `test` and `chore`.

### Including Ticket Numbers

If your development process includes tracking work through Jira tickets or GitHub issues, you can include ticket numbers in your commits to link them to specific tasks:

```shell-session
$ git commit -m "TECH-123: optimize database queries"
$ git commit -m "BUG-456: fix user registration error"
```

## Small, Frequent Commits

**Making small, frequent commits is a best practice in Git**. 

This helps keep your changes organized and reduces the risk of losing work if something goes wrong. It's also easier to review and understand a series of small, focused changes than one large, sprawling change. 

With smaller commits, you'll have more opportunities to review and refine your work, and you'll be able to roll back to a previous state if needed.

One big commit:

```shell-session
$ git add .
$ git commit -m "Add login feature, fix alignment, update documentation"
```

Smaller commits:

```shell-session
$ git add login_feature/*
$ git commit -m "feat(login): add login functionality"

$ git add styles/*
$ git commit -m "fix(styles): resolve button alignment issue"

$ git add docs/*
$ git commit -m "docs: update user guide"
```

## Don't Commit Trash

**It's important to be mindful of what you commit in Git**. 

Git remembers everything, so if you commit large files, binary files, or sensitive data, it will be stored in the repository forever.  

### Ignoring with a `.gitignore`

To avoid this, it's recommended to use a `lang:shell-session:.gitignore` file to exclude files and directories that you don't want to track in the repository.  

A `lang:shell-session:.gitignore` will mean that commands like `lang:shell-session:git add .` will avoid adding some files.

Ironically the `lang:shell-session:.gitignore` file should be checked into the repository.

An example `lang:shell-session:.gitignore` is below:

```text
fn:.gitignore
# Ignore specific files
secrets.json

# Ignore directories
node_modules/
build/

# Ignore all .log and .temp files
*.log
*.temp

# Except for this specific log
!important.log

# Ignore .cache files in all directories
**/*.cache
```

## Know What Commands Can Destructive

**When you're working with Git, it's important to be mindful of the commands you use**. 

Some commands like `lang:shell-session: git checkout` and `lang:shell-session:git reset` can overwrite your work.

### Checkout

`lang:shell-session:git checkout` allows you to switch between branches and restore files to a previous state:

```shell-session
$ git checkout -- <filename>
```

### Reset

`lang:shell-session:git reset` allows you to undo changes and return to a previous commit:

```shell-session
$ git reset <commit-hash>
```

## Use the Stash

The `lang:shell-session:$ git stash` command allows you to save changes that you haven't committed yet, switch to a different branch, and then restore the changes later. 

This is useful when you need to switch to a different branch to work on a bug fix or feature, but don't want to commit your changes yet. 

The stash allows you to save your changes and switch to the other branch without losing any work:

### Stash Changes

You can stash local, uncommitted changes with:

```shell-session
# To stash changes
$ git stash
```

### Unstash Changes

You can bring these changes back with:

```shell-session
$ git stash apply
```
