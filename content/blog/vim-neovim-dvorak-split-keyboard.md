---
title: From Vim & QWERTY to Neovim & DVORAK
description: And never back again.
date_created: 2023-11-21
date_updated: 2025-09-22
competencies:
  - Software Engineering
aliases:
  - 2023-11-21-vim-neovim-dvorak-split-keyboard
  - vim-neovim-dvorak-split-keyboard
---

{{< img
    src="/images/vim-neovim-dvorak/dylan.png"
    width="500"
>}}

{{< quote text="There are no veils, curtains, doors, walls or anything between what pours out of Bob's hand onto the page and what is somehow available to the core of people who are believers in him. There's some people who'd say 'You know, not interested'. But if you're interested, he goes way, way deep." author="Joan Baez on Bob Dylan - No Direction Home" >}}

**I'm a Neovim, DVORAK & split keyboard user**.  I wasn't born that way.

This post details the transitions I've made to arrive at my current toolset:

- Atom to Vim to **Neovim**
- QWERTY to **Dvorak keyboard layout**
- Traditional to **split keyboard**

## The Journey

I started my programming journey in early 2017 - on Windows laptop using the now deceased Atom editor. I didn't know any better!

Programming is both my profession and a hobby. **I enjoy working on improving my tools and workflows**, which have additional benefits of making me a more effective programmer and improving the health of my aging, tired body.

**Not all developers are like this** - some of the best programmers I've worked with have no interest in changing keyboard shortcuts, let alone learning Lua to configure their text editor.

To each their own - **but if you are interested, this goes way, way deep**.

## Vim

I started to learn Vim in the Christmas holidays of 2017 - I cannot remember exactly why.

{{< img
    src="/images/vim-neovim-dvorak/vim.png"
    caption="Vim editor"
    width="500"
>}}

**The first few days were tough** - it took around a week to feel comfortable with the basics of Vim such as `hjkl`, the different modes (Normal, Insert etc), moving between splits and moving to different places a file.

**After two weeks I felt as productive as I was in Atom** - beyond that my productivity has become more powerful than you could possibly imagine.

Over the years I added colorschemes, plugins, keybinds, macros & abbreviations - [you can find my final `.vimrc` here](https://github.com/ADGEfficiency/dotfiles/blob/master/dotfiles/.vimrc).

I do still use Vim when I'm working on remote servers - sometimes I'll clone my [dotfiles](https://github.com/ADGEfficiency/dotfiles) if I'll be working there for a while and don't want to install Neovim.

### Essential Tools

Alongside Vim I use Tmux and fzf. **Tmux and fzf are as crucial for making Vim your main text editor as Vim itself**. Without any of the three, my terminal-based development style would not work. This is one of the places where people can get stuck with Vim - you need more than Vim to make a productive Vim setup.

**Tmux** is used for terminal multiplexing - allowing the ability to open terminal windows alongside each other or in different windows.

**fzf** I use for finding and opening files, both from the terminal with `**<TAB>` and within Vim using `<Space>` to run fzf in the current directory via a keybinding.

A healthy use of shell aliases and custom functions are also important to working with a terminal editor like Vim.

I use a script `s` to quickly use fzf to search for files to open in my `$EDITOR` from the current directory ([script is here](https://github.com/ADGEfficiency/dotfiles/blob/master/scripts/s)):

{{< img
    src="/images/vim-neovim-dvorak/s.png"
    caption="File search script with fzf"
    width="500"
>}}

```bash
#!/usr/bin/env zsh

TERM_HEIGHT=$(tput lines)
MIN_HEIGHT=20

# prompt for files using fzf
files=$(if [ "$TERM_HEIGHT" -ge "$MIN_HEIGHT" ]; then
    fzf --preview 'bat -p --color=always {}' --height 60% -m
  else
    fzf --no-preview --height 40% -m
fi)

# check if fzf was interrupted by Ctrl-C
if [ $? -eq 0 ]; then
  "$EDITOR" "${(f)files}"
fi
```

### Do I Recommend Vim?

**Vim is amazing, but outdated - use Neovim instead**.

Vim itself however still has a lot of awesomeness. The ecosystem of plugins and customization is still fantastic.

**The initial configuration for Vim can be challenging** - I would budget 1-2 days to get a basic setup working.

Even if you love VS Code, learning to use Vim is useful. **It's almost always available on remote servers**, and it's a better editor than other commonly available editors like nano.

**Vim keybindings are also everywhere** - you can enable them in the shell with `$ set -o vi` (instead of the default Emacs bindings), and many programs (IDEs or browsers) have Vim plugins.

## Neovim

I started my transition to Neovim in July 2022 - motivated by the Vimscript 9 schism that divided the Vim community.

{{< img
    src="/images/vim-neovim-dvorak/nvim.png"
    caption="Neovim editor"
    width="500"
>}}

**Transitioning to Neovim after 3 years of Vim was quick** - the in-editor experience is very similar.

It took around half a day to convert my `.vimrc` to a functional Lua based setup, followed by a week or two of tweaking my config and adding plugins.

**I was able to bring along all of my Vimscript plugins**, which is a huge selling point of Neovim. I do prefer Lua written plugins where possible, but still use many of the same plugins as with Vim - [you can find all my Neovim plugins here](https://github.com/ADGEfficiency/dotfiles/blob/master/nvim/lua/adam/plugins.lua).

### Do I Recommend Neovim?

**I would strongly recommend Neovim to anyone who is starting out with Vim or to experienced Vim users - it's great**.

Neovim is an improvement over Vim, and has a bubbling, exciting ecosystem of plugins and users. **I have found the language servers, linting, formatting and completion experience an improvement over Vim**.

**If you are a Vim user it's not a big transition** - all of your Vimscript plugins will work as expected.

**It's nice to use Lua for configuration** - it's more flexible and is a more useful, transferable skill that Vimscript.

If you want to get started with Neovim, look at [kickstart.nvim](https://github.com/nvim-lua/kickstart.nvim).

## DVORAK

I started my transition to DVORAK in May 2019 - motivated by a desire to improve the health of my hands.

{{< img
    src="/images/vim-neovim-dvorak/layout.png"
    caption="DVORAK keyboard layout"
    width="500"
>}}

After two and a half years of programming, I was suffering with muscular soreness & tiredness in my hands. **My hands felt fatigued - like they were doing too much work**.

I was aware that there were alternative keyboard layouts, designed to be kinder to our hands - a day or two of sporadic, random & repetitive searching on Google about the different options I decided to give Dvorak a shot.

It took me around 2 weeks to get back to a somewhat reasonable level of productivity, but I was not back to the my previous level of QWERTY.

**My typing remained inaccurate for a long time** - I only felt like I was back to where I was in August 2021 - making the transition over a year long.

Sometimes my typing is still less accurate than it was (particularly as I use a keyboard with blank keycaps) - but it's manageable. **I don't feel like DVORAK led to a significant productivity improvement**.

### Do I Recommend DVORAK?

**I would not recommend the DVORAK layout** - while I'm glad I have done it and wouldn't switch back, it takes a long, long time to get used to.

I can still type QWERTY if needed - it's keyboard & context dependent. **I can still type QWERTY on my phone without even realizing it's a different layout**.

## Split Keyboard

I started using a split keyboard in July 2021 - motivated by a desire to improve the health of my back.

{{< img
    src="/images/vim-neovim-dvorak/ergo.png"
    caption="Ergodox EZ split keyboard"
    width="500"
>}}

Previously I had used the Apple Keyboard, then moved to a [Vortex Race 3](https://vortexgear.store/products/race-3-micro-usb), which I still use today. The split keyboard I use today is the [Ergodox EZ](https://ergodox-ez.com).

**The main benefit of a split keyboard is that your hands rest further apart**. This allows your chest to expand, and reduces the strain on your upper and middle back - in particular reducing pain between the shoulder blades.

**It took around 1 week to get back to the same level of productivity as a QWERTY keyboard**. I have found a moderate level of productivity increase using a split keyboard.

The Ergodox EZ allows customization the keyboard layout using ORYX - [you can find my layout here](https://configure.zsa.io/ergodox-ez/layouts/vJLGQ/latest/0).

### Do I Recommend a Split Keyboard?

**I would recommend a split keyboard, especially if you have back pain in between your shoulder blades** - it's a small amount of time investment for a real health benefit.

**I have no problem going back to a normal keyboard** - unlike DVORAK, using a split keyboard will not impact your ability to use a normal keyboard.

## Thoughts on DVORAK and Vim

The combination of DVORAK and Vim is an interesting one - both are very opinionated about how you should use your keyboard.

I was already a proficient Vim user when I decided to switch to DVORAK.

**Foundational to any keyboard layout and Vim is remapping `<CAPSLOCK>` to `<ESCAPE>`**. In Vim you use the `<ESCAPE>` key to move from insert to normal mode - easy access to the escape key is essential.

### Why DVORAK?

Most computer keyboards are laid out in QWERTY - named for the keys in the first row.

**The big idea in Dvorak is the importance of the middle row** (also known as the home row).

**Vim users know the importance of the home row from `hjkl`** - the keys used for cursor movement in Vim. Dvorak puts all the vowels on the home row - the keys you access the most are closest to your fingers.

The other notable feature of Dvorak is the location of the punctuation characters `' , .` - these are located in a prime position.

**An interesting thing about learning DVORAK was that the time to learn keys is long tailed**. Some (such as `, .` and `aoeu`) come very easily, while others like `r y f g` took a while.

### Losing hjkl

In Vim `hjkl` are used for cursor movement - they are the keys you use to move your cursor around a file in normal mode.

**In DVORAK you lose the position and order of `hjkl`**. Initially I considered remapping `hjkl` to the same position as QWERTY, but decided against it. It's been fine.

### Combinations That Work Great

There are some common Vim key combinations that feel great in Dvorak:

- **`:` (Vim command mode)** is easy access
- **`:w` and `:wq`** feel great - you don't need to move either hand
- **`"`, `,` and `.`** are easy access
- **`.py`** are all next to each other
- **`ls`** is right next to each other
- **`gcc`** is easy access and `<C-r>` requires no hand movement

### Challenges

**One challenge is anything `g` or `f` related**. In Vim `gf` opens a file under the cursor - as these two keys are next to each other, it requires moving both hands from their natural position.

**Another challenge are the `{}` and `[]` keys** - on a DVORAK layout, these are hard to get at. A split keyboard helps this a lot, as you can put these on the thumb keys.

## Summary

My recommendations are:

- Don't use Vim, instead use **Neovim**. I highly recommend **Neovim** if you enjoy configuring your tooling
- I do not recommend switching to the **DVORAK keyboard layout**
- I do recommend a **split keyboard**, for the health benefits

Here is a summary of each of the tool and workflow transitions - years of human experience reduced to a Markdown table:

| Transition       | Time to Transition | Initial Setup Required | Productivity Increase | Health Improvement   | Recommended |
|------------------|--------------------|------------------------|-----------------------|----------------------|-------------|
| Atom to Vim      | 2 weeks            | 1 day                  | High                  | None                 | ✅          |
| Vim to Neovim    | 1/2 day            | 1/2 day                | Moderate              | None                 | ✅          |
| QWERTY to DVORAK | >1 year            | None                   | None                  | Less hand fatigue    | ❌          |
| Split Keyboard   | 3 weeks            | 1/2 day                | Moderate              | Back pain relief     | ✅          |

---

Thanks for reading!

Take a look at my [dotfiles](https://github.com/ADGEfficiency/dotfiles) if you're interested in my setup - [my Lua Neovim config is here](https://github.com/ADGEfficiency/dotfiles/tree/master/nvim).
