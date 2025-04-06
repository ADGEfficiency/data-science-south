---
title: Hypermodern Terminal Toolbox
description: Terminal, shell and command-line tools setting the standard in 2023.
date: 2023-03-25
competencies:
- Software Engineering

---

**All developers use terminals; for some, their entire workflow is in the terminal**.

![Prompt: 'computer terminal console screen and keyboard on a rainbow desk, style of guy billout, colorful'. Seed: 77.<br />Created with Stable Diffusion 1.](/images/hypermodern-terminal/hero.png)

This post introduces the **Hypermodern Terminal Toolbox** - terminal, shell and command-line tools setting the standard in 2023.

## Kitty as a Terminal Emulator

**[Kitty](https://sw.kovidgoyal.net/kitty/) is a terminal emulator** - it's an alternative to the GNOME Terminal, Alacritty or the Windows Terminal.

![](/images/hypermodern-terminal/kitty-theme.png)

A terminal emulator is the program that runs your terminal. Different operating systems (OS) offer different terminal emulators, either as part of the OS or as installable third-party programs. 

Kitty is a GPU-accelerated, third-party terminal emulator.  Kitty is fast, highly customizable, and open source.

Configuration is done using a `kitty.conf` text file:

```text { title = "kitty.conf" }
font_family      Operator Mono Book
font_size 14.0
scrollback_lines 2000
```

Kitty offers extensive configuration of fonts, cursors, color scheme and keyboard shortcuts.

*Tip - when changing Kitty settings in `kitty.conf`, you will need to fully restart the Kitty program.*

## Zsh & Prezto as a Shell

**[Zsh](https://zsh.sourceforge.io/) is a shell written in C** - it's an alternative to Bash or Fish. 

A shell is an operating system text interface that runs inside a terminal. Shell commands perform tasks like creating files and running programs.

Zsh is an open source shell, offering more functionality and customizability than Bash.

Zsh is configured using a `.zshrc` file:

```bash { title = "~/.zshrc" }
HISTSIZE=9999
alias brew='arch -x86_64 brew'
export PATH="$HOME/dotfiles/scripts:$PATH"
```

**[Prezto](https://github.com/sorin-ionescu/prezto) is a configuration framework for Zsh** - it's an alternative to Oh My Zsh.

Features of Prezto include syntax highlighting and command tab completion.  Tab completion is useful for interactively exploring new command-line tools.

Prezto is configured using a `.zpreztorc` file:

```bash { title = "~/.zpreztorc" }
zstyle ':prezto:load' pmodule \
  'environment' \
  'terminal' \
  'editor' \
  'history' \
  'directory' \
  'spectrum' \
  'utility' \
  'completion' \
  'git' \
  'syntax-highlighting' \
  'history-substring-search' \
  'autosuggestions' \
  'prompt'
```

*Tip - Find a full list of [Prezto modules here](https://github.com/sorin-ionescu/prezto/tree/master/modules).*

## Neovim as a Text Editor

**[Neovim](https://neovim.io/) is a text editor written in C** - it's an alternative to Vim, Nano or Emacs.

![](/images/hypermodern-terminal/nvim.png)

Neovim is a popular successor to Vim. The entire ecosystem of Vim plugins written in Vimscript works in Neovim, on top of a bustling ecosystem of Neovim plugins written in Lua.

A well-configured Neovim has language servers for autocompletion (the same language servers available in VS Code), syntax highlighting with Treesitter, and Telescope for searching through different types of lists.

Configuration of Neovim is done in Lua - starting with an `init.lua` file:

```lua { title = "$XDG_CONFIG_HOME/nvim/init.lua" }
--  set size of a tab to be 4
--  vim command line `:set tabstop=2`
--  vimscript `set tabstop=2`
vim.opt.set.tabstop = 2

--  run vimscript in lua
vim.cmd([[set tabstop=2]])

--  set variable
--  vimscript `let g:zoom#statustext = 'Z'`
vim.g['zoom#statustext'] = 'Z'
```

To match the full functionality of an IDE like VS Code, Neovim requires extension with plugins.  You can set these up yourself; if you want to get set up quicker, you can use a distribution like [AstroNvim](https://github.com/AstroNvim/AstroNvim), which comes with plugins installed.

*Tip - subscribe to [This Week in Neovim](https://this-week-in-neovim.org/) for a weekly newsletter covering the bustling Neovim ecosystem.*

## Tmux for Multiple Terminals

**[Tmux](https://github.com/tmux/tmux) is a terminal multiplexer written in C** - it's an alternative to Screen, or running terminals in multiple windows.

![](/images/hypermodern-terminal/tmux.png)

Terminal multiplexers allow you to manage multiple terminal sessions within a single window.  

Tmux gives you persistent sessions, window and pane management with customizable key bindings. 

Tmux uses a hierarchy of concepts to manage multiple terminals:

- A pane is a rectangular area within a window. Each pane displays a separate terminal session.
- A window is a full-screen container that holds one or more panes.
- A session is a collection of one or more windows.

Tmux sessions can be created, attached, detached and reattached. 

You can start a new Tmux session with `tmux new`:

```shell-session
#  create a session named `work`
$ tmux new -s work
```

Tmux can be used to restore your working environment on a remote machine. If your SSH connection drops, you can restore the exact combination and layout of terminal sessions you had before by reattaching to the Tmux session on the remote machine.

You can reattach to a running Tmux session with `tmux attach`:

```shell-session
#  reattach to last session
$ tmux attach

#  reattach to the session named `work`
$ tmux attach -t work
```

Tmux operates using a prefix key, which defaults to `Ctrl-b`.  Tmux is used by first pressing the prefix, followed by a command key:

- `Ctrl-b c`: Create a new window.
- `Ctrl-b n`: Switch to the next window.
- `Ctrl-b p`: Switch to the previous window.

Tmux is configured using a `.tmux.conf` file:

```shell-session { title = "~/.tmux.conf" }
set -g default-terminal "screen-256color"
setw -g mode-keys vi
set -g status-left "#[fg=green,bold]Session: #S #[fg=white,bold]| #[fg=yellow,bold]Window: #W"
set-option -g prefix C-a
```

*Tip - [extend Tmux with this list of plugins](https://github.com/tmux-plugins/list)*.

## Starship for a Pretty Prompt

**[Starship](https://starship.rs/) is a shell prompt written in Rust** - it's an alternative to Powerlevel10k or Pure. 

![](/images/hypermodern-terminal/starship.png)

A prompt is a customizable part of the command line that provides context such as the current directory or Git branch.

Starship gives you a fast, customizable prompt.  

Configuration is done using a `starship.toml` file:

```toml { title = "$XDG_CONFIG_HOME/starship.toml" }
[username]
disabled = true

[hostname]
disabled = true

[git_status]
ahead = "↑"
behind = "↓"

[directory]
truncation_length = 2
```

*Tip - Take a look at the [Starship Presets](https://starship.rs/presets) for inspiration about what you can do with Starship.*

## Ripgrep for Searching Text 

**[Ripgrep](https://github.com/BurntSushi/ripgrep) is a text file searcher written in Rust** - it's an alternative to grep or find.

![](/images/hypermodern-terminal/rg.png)

Ripgrep's primary feature is speed - it's faster than alternative tools.

The basic use of Ripgrep is to search for a pattern in a directory:

```shell-session
$ rg 'pattern' ~/project
```

My alias for Ripgrep is using `g`, which searches for text through all files, returning the name of files that contain a pattern:

```bash
alias g='rg -l --hidden --smart-case --line-buffered'
```

You can use this alias as follows:

```shell-session
$ g 'some-pattern' some/directory
```

*Tip - configure the `--ignore`, `--hidden` and `--smart-case` options to control what files you include in your search.*

## fzf for Fuzzy Searching 

**[fzf](https://github.com/junegunn/fzf) is a fuzzy finder written in Go** - it's an alternative to deterministic search.

![](/images/hypermodern-terminal/fzf.png)

fzf allows you to search using a fuzzy search algorithm that matches regex patterns on incomplete information.  This allows search results to appear as you type, even with misspellings.

fzf can be run as a command-line program:

```shell-session
$ fzf
```

It can also used with a `**` syntax combined with a `TAB` button press - this allows you to run fzf inside specific directories:

```shell-session
#  fuzzy search all files in the `work` directory
$ cat ~/work/** <TAB>
```

fzf is often used in other programs - Neovim, Zsh and Sad all offer integration with fzf through plugins.  

fzf can be used with different search backends, such as find, grep or Ripgrep.

*Tip - use Ripgrep as the fzf backend by setting the `FZF_DEFAULT_COMMAND` environment variable `export FZF_DEFAULT_COMMAND='rg --files --hidden'`.*

## Exa for Listing Files

**[Exa](https://the.exa.website/) is a file-listing program written in Rust** - it's an alternative to ls and tree.  

![](/images/hypermodern-terminal/exa.png)

A file listing program shows you lists of files and directories. Exa offers features such as icons, Git integration, and versatile sorting options.  

Exa has a few different basic views:

```shell-session
#  list as a grid
$ exa -G
bp-historical-data  cities  data-science-south-data  predict-newspapers  README.md  titanic

#  list each item on one line
$ exa -1
bp-historical-data
cities
data-science-south-data
predict-newspapers
README.md
titanic

#  list as a table - same as `ls -l`
$ exa -l
drwxr-xr-x   - adam 26 Apr 20:20 bp-historical-data
drwxr-xr-x   - adam 14 Feb 16:42 cities
drwxr-xr-x   - adam 26 Apr 20:25 data-science-south-data
drwxr-xr-x   - adam 28 Apr 14:52 predict-newspapers
.rw-r--r-- 124 adam 29 Apr 15:20 README.md
drwxr-xr-x   - adam 26 Apr 17:31 titanic
```

Exa can also replace the tree program, showing a recursive view of all files:

```shell-session
$ exa --tree --level=2
├── bp-historical-data
│  ├── __pycache__
│  ├── dashboard.py
│  ├── data
│  ├── notebooks
│  ├── README.md
│  └── requirements.txt
├── README.md
└── titanic
   ├── data
   ├── requirements.txt
   ├── titanic.ipynb
   ├── titanic.md
   └── titanic.py
```

Exa's configuration options for the long, tabular view (the equivalent of `ls -l`) are extensive - allowing a complete configuration of columns and sorting order of items.

My aliases for Exa are:

```bash
alias ls='exa --long --icons --no-permissions --no-user --git --time-style long-iso --time=modified --group-directories-first -a'
alias tree='exa --tree'
```

*Tip - Try `exa --sort=size --reverse` to identify large files as a list sorted by size in descending order.*

## Bat for Viewing Files

**[Bat](https://github.com/sharkdp/bat) is a file viewer written in Rust** - it's an alternative to cat.

![](/images/hypermodern-terminal/bat.png)

A file viewer is a program that displays the contents of a file.

Bat offers functionality such as syntax highlighting, Git integration and automatic file paging.

Bat is used by pointing the program at a text file:

```shell-session
$ bat path/to/file
```

*Tip - Customize the appearance with themes by using the --theme flag like `bat --theme="TwoDark"`.*

## Sad for Replacing Text

**[Sad](https://github.com/ms-jpq/sad) is a stream editor written in Rust** - it's an alternative to sed or awk.

Stream editors perform search and replace operations on text streams or text files.

Sad (Space Age seD) will show proposed replacements before applying them, allowing you to check and select which replacements to make before committing them.

Sad is used as a command-line program:

```shell-session
$ sad '<pattern>' '<replacement>'
```

You can use Sad to replace text in a file or an input stream - below we replace the word `course` with `module` in a file `README.md`:

```shell-session
$ cat README.md
# Data Science South Projects

Example projects for the courses at [Data Science South](https://www.datasciencesouth.com/).

$ exa -1 | sad "courses" "modules"      

$ cat README.md
# Data Science South Projects

Example projects for the modules at [Data Science South](https://www.datasciencesouth.com/).
```

*Tip - Use `--commit` to write replacements without an interactive preview.*

## jq for Working with JSON

**[jq](https://stedolan.github.io/jq/manual/) is a JSON processor written in C** - it's an alternative to fx, jp, or processing JSON in a language like Python.

jq allows you to filter, transform, and manipulate JSON data, which is useful for working with API responses, configuration files, and data stores.

A central idea in jq is the filter, which applied to the input JSON:

```shell-session
$ jq 'filter_expression' input.json
```

Some useful jq filters are (using the Python key/value language for dictionaries):

- `.key` - extract the value of a key,
- `.[]` - extract all values from an array,
- `.[2]` - extract the third value from an array.

A few examples:

```shell-session
#  extract the `name` key
$ echo '{"name": "Alice", "data": [6, 12]}' | jq '.name'
"Alice"

#  extract the second element from the `data` list
$ echo '{"name": "Alice", "data": [6, 12]}' | jq '.data[1]'
12
```

*Tip - You can pretty-print JSON data with `cat input.json | jq`.*

## zoxide for Navigation

**[zoxide](https://github.com/ajeetdsouza/zoxide) is a terminal navigation utility written in Rust** - it's an alternative to cd, pushd, and popd. 

zoxide jumps to directories from your visit history. It assigns a score to each directory based on how frequently and recently they have been visited.

zoxide is used as a command line program:

```shell-session
#  move to a folder that best matches `code`
$ z code
```

*Tip - use `zoxide query -s -l` to see the directories in your zoxide database.*

## Tig for Viewing Git History

**[Tig](https://jonas.github.io/tig/) is a Git history viewer written in C** - it's an alternative to using the Git CLI or Lazygit.

![](/images/hypermodern-terminal/tig.png)

Tig provides a navigable, color-coded interface for browsing your Git commit history. It allows searching for commits, viewing the commit graph and showing files at a different point in time.

Tig is run as a command-line program:

```shell-session
$ tig
```

*Tip - Press `h` while running Tig to access help & display available commands.*

## direnv for Environment Variable Management

**[direnv](https://direnv.net/) loads and unloads shell environment variables** - written in Go, it's an alternative to using `$ source .env`.

direnv automatically loads & unloads environment variables as you navigate between different project directories. 

Using direnv avoids manual loading of environment variables, and protects against environment variables from one project being set in another project.

direnv uses a `.envrc` file to hold variables specific to your project, which is run as a shell script:

```bash { title = ".envrc" }
export PROJECT_NAME="alpha"
```

Running `direnv allow` will whitelist the `.envrc`, authorizing the automatic use of this specific `.envrc` file:

```shell-session
$ direnv allow .
```

Now the `PROJECT_NAME` variable will be loaded and unloaded automatically when moving in and out of the project directory.

A common practice is to optionally load a secret or private `.envrc`:

```bash
source_env_if_exists .envrc.secret
```

If `.envrc.secret` exists, it will be loaded, otherwise it will be ignored.

*Tip - Use `direnv exec <path> <command>` to run a command with the environment loaded for a specific directory without navigating to it.*

## Lazydocker for Docker

**[Lazydocker](https://github.com/jesseduffield/lazydocker) manages Docker containers and images** - written in Go, it's an alternative to Docker Desktop or the Docker CLI. 

![](/images/hypermodern-terminal/lazydocker.png)

Lazydocker makes it easy to view, start, stop, and remove containers and images through a terminal UI.  It can also provide a real-time overview of container status, logs, and resource usage.

Lazydocker is used as a command-line program:

```shell-session
$ lazydocker
```

*Tip - Press `?` in Lazydocker to view a list of available keybindings and their corresponding actions.*

## Markserv for Previewing Markdown

**[Markserv](https://github.com/markserv/markserv) renders Markdown files in a browser** - written in Node.js, it's an alternative to Grip or Markdown Preview.

![](/images/hypermodern-terminal/markserv.png)

Markserv renders Markdown to HTML in real time, automatically reflecting changes as you make them.

Markserv supports GitHub flavored Markdown, which means it formats code blocks & tables the same as Github. Markserv is great for previewing `README.md` files without pushing to Github.

To start a Markserv server on port 8010:

```shell-session
$ markserv -p 8010
```

*Tip - Use the `--browser` flag when starting Markserv to automatically open the served content in your default web browser.*

## Ngrok for Sharing Local Servers

[ngrok](https://ngrok.com/) creates tunnels to your local servers - written in Go, it's an alternative to Serveo, LocalTunnel, or PageKite. 

![](/images/hypermodern-terminal/ngrok.png)

ngrok exposes a local server behind a NAT or firewall to the internet. This is useful for sharing a development server with your team.

You can start a tunnel to port 8000 by running:

```shell-session
$ ngrok http 8000
```

*Tip - To expose non-HTTP services, use the `ngrok tcp` or `ngrok tls`.*

## Summary

The **Hypermodern Terminal Toolbox** is:

- [Kitty](https://sw.kovidgoyal.net/kitty/) for a GPU accelerated, highly customizable terminal,
- [Zsh](https://www.zsh.org/) for a shell & [Prezto](https://github.com/sorin-ionescu/prezto) for Zsh configuration,
- [Neovim](https://neovim.io/) as a text editor,
- [Tmux](https://github.com/tmux/tmux) for managing multiple terminals,
- [Starship](https://starship.rs/) for a pretty prompt,
- [Ripgrep](https://github.com/BurntSushi/ripgrep) for searching text files,
- [fzf](https://github.com/junegunn/fzf) for fuzzy searching,
- [Exa](https://the.exa.website/) for listing files,
- [Bat](https://github.com/sharkdp/bat) for viewing files,
- [Sad](https://github.com/ms-jpq/sad) for find and replace in text files,
- [jq](https://stedolan.github.io/jq/) for working with JSON,
- [zoxide](https://github.com/ajeetdsouza/zoxide) for navigation,
- [Tig](https://jonas.github.io/tig/) for viewing Git history,
- [direnv](https://direnv.net/) for environment variable management,
- [Lazydocker](https://github.com/jesseduffield/lazydocker) for Docker,
- [Markserv](https://github.com/markserv/markserv) for previewing Markdown,
- [ngrok](https://ngrok.com/) for exposing local servers to the internet.

Don't feel pressured to learn all these tools at once. Steadily learn one tool at a time to become a terminal master 🧙
