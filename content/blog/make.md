---
title: Make for Data Science
description: Make your data science workflows better with this classic UNIX tool.
date_created: 2022-01-20
date_updated: '2023-12-05'
competencies:
- Software Engineering
---

## What is `make`?

`make` is a command-line program of the same pedigree & importance as classic UNIX programs like `grep` and `ssh`. 

A powerful tool that has stood the test of time, `make` is readily available in Linux and MacOS as a shell program.  Originally used as a build automation tool for making files, `make` can be used with any workflow that involves running shell programs.

This post shows how to use classic tool in a modern data science project:

1. why use a `Makefile` in a data science project,
2. the important elements of a `Makefile`,
3. develop a data pipeline `Makefile` to ingest and clean data.

## Why `make` for Data Science?

`make` is a great tool for data science projects - it provides:

1. **workflow documentation**,
2. **a central point of execution**,
3. **intelligent re-execution**.

### Documentation

Documenting your project is a [basic quality of a good data project](https://www.datasciencesouth.com/blog/data-science-project-checklist).

A `Makefile` serves as executable documentation of what your project does. Like any text file it's easy to track changes in source control.

Creating your pipeline as a sequence of `make` targets also naturally drives your pipelines to be modular - encouraging good functional decomposition of shell or Python scripts.

### Central Execution

A `Makefile` tightly integrates with the shell. We can easily configure variables at runtime via either shell environment variables or via command line arguments.

The `Makefile` below has two variables - `NAME` and `COUNTRY`:

```makefile { title = "Makefile" }
.PHONY: all

all:
	echo "$(NAME) is from $(COUNTRY)"
```

We can set variables using two different methods:

1. `EXPORT name=adam` - setting our variable `NAME` by to a shell environment variable,
2. `COUNTRY=NZ` - our `COUNTRY` variable by an argument passed to the `make` command.

```shell-session
$ export NAME=adam; make COUNTRY=NZ 
echo "$(NAME) is from $(COUNTRY)"
adam is from nz
```

We can also assign the output values of shell commands using:

```makefile
VAR = $(shell echo value)
```

### Intelligent Re-Execution

We have already seen the functionality of intelligent pipeline re-execution - it's a powerful way to not re-run code that doesn't need to run.

`make` uses timestamps on files to track what to re-run (or not re-run) - it won't re-run code that has already been run and will re-run if dependencies of the target change.

This can save you lots of time - not rerunning that expensive data ingestion and cleaning step when you are working on model selection.


## What is a `Makefile`?

A `Makefile` has three components:

1. **targets** - files you are trying to make or a `PHONY` target,
2. **dependencies** - targets that need to be run before a target,
3. **a workflow** - a sequence of `TAB` separated steps.

```makefile
target: dependencies
    echo "any shell command"
```

### Targets and Dependencies

Much of the power of a `Makefile` comes from being able to introduce dependencies between targets.

The simple `Makefile` below shows a two step pipeline with one dependency - our `run` target depends on the `setup` target:

```makefile { title = "Makefile" }
# define our targets as PHONY as they do not create files
.PHONY: setup run

setup:
    pip install -r requirements.txt

run: setup
    python main.py
```

This ability to add dependencies between targets allows a `Makefile` to represent complex workflows, including data science pipelines.

### Using a `Makefile`

The `Makefile` below creates an empty `data.html` file:

```makefile { title = "Makefile" }
data.html:
	echo "making data.html"
	touch data.html
```

Running `$ make` without a target will run the first target - in our case the only target, `data.html`. 

`make` prints out the commands as it runs:

```shell-session
$ make
making data.html
touch data.html
```

If we run this again, we see that `make` runs differently - it doesn't make `data.html` again:

```shell-session
$ make
make: `data.html' is up to date.
```

If we do reset our pipeline (by deleting `data.html`), running `make` will run our pipeline again:

```shell
$ rm data.html; make
making data.html
touch data.html
```

**This is `make` intelligently re-executing of pipeline**.

Under the hood, `make` makes use of the timestamps on files to understand what to run (or not run).

## A `make` Data Pipeline Example

### Pipeline

We will build a data pipeline - using Python scripts as mock for real data tasks - with data flowing from left to right.

Our ingestion step creates raw data, and our cleaning step creates clean data:

![](/static/blog/make/data.png "Data flows from left to right, in a two stage ingestion & cleaning process.")

We can look at the same pipeline in terms of the dependency between the data artifacts & source code of our pipeline - with dependency flowing from right to left:

![](/static/blog/make/dep.png "Dependency flows from right to left, with the data depending on the code that makes it")

Our clean data depends on both the code used to generate it and the raw data.  Our raw data depends only on the ingestion Python script.

### Data Ingestion and Cleaning

Lets look at the two components in our pipeline - an ingestion step and a cleaning step, both of which are Python scripts.

`ingest.py` writes some data to a JSON file:

```python { title = "ingest.py" }
#!/usr/bin/env python3
from datetime import datetime
import json
from pathlib import Path

fi = Path.cwd() / "data" / "raw.json"
fi.parent.mkdir(exist_ok=True)
fi.write_text(json.dumps({"data": "raw", "ingest-time": datetime.utcnow().isoformat()}))
```

We can run this Python script and use `cat` to take a look at it's JSON output:

```shell
$ ./ingest.py; cat data/raw.json
{"data": "raw", "ingest-time": "2021-12-19T13:57:53.407280"}
```

`clean.py` takes the raw data generated and updates the `data` field to `clean`:

```python { title = "clean.py" }
#!/usr/bin/env python3
from datetime import datetime
import json
from pathlib import Path

data = json.loads((Path.cwd() / "data" / "raw.json").read_text())
data["data"] = "clean"
data["clean-time"] = datetime.utcnow().isoformat()
fi = Path.cwd() / "data" / "clean.json"
fi.write_text(json.dumps(data))
```

We can use `cat` again to look at the result of our cleaning step:

```shell-session
$ ./clean.py; cat data/clean.json
{"data": "clean", "ingest-time": "2021-12-19T13:57:53.407280", "clean-time": "2021-12-19T13:59:47.640153"
```

### Pipeline Dependencies

Let's start out with a `Makefile` that runs our two stage data pipeline.

We are already taking advantage of the ability to create dependencies between our pipeline stages, making our `clean` target depend on our `raw` target.

We have also included a top level meta target `all` which depends on our `clean` step:

```makefile { title = "Makefile" }
.PHONY: all raw clean

all: clean

raw:
	mkdir -p data
	./ingest.py

clean: raw
	./clean.py
```

We can use this `Makefile` from a terminal using by running `make`, which will run our meta target `all`:

```shell-session
$ make
mkdir -p data
./ingest.py
ingesting {'data': 'raw', 'ingest-time': '2021-12-19T14:14:54.765570'}
./clean.py
cleaning {'data': 'clean', 'ingest-time': '2021-12-19T14:14:54.765570', 'clean-time': '2021-12-19T14:14:54.922659'}
```

If we go and run only the `clean` step of our pipeline, we run both the ingest and cleaning step again.  This is because our cleaning step depends on the output of data ingestion:

```shell-session
$ make clean
mkdir -p data
./ingest.py
ingesting {'data': 'raw', 'ingest-time': '2021-12-19T14:15:21.510687'}
./clean.py
cleaning {'data': 'clean', 'ingest-time': '2021-12-19T14:15:21.510687', 'clean-time': '2021-12-19T14:15:21.667561'}
```

What if we only want to re-run our cleaning step?  Our next `Makefile` iteration will avoid this unnecessary re-execution.

### Pipeline Outputs

Now let's improve our `Makefile`, by making changing our targets to be actual files - the files generated by that target. 

```makefile { title = "Makefile" }
.PHONY: all
all: clean

./data/raw.json:
	mkdir -p data
	./ingest.py

./data/clean.json: ./data/raw.json
	./clean.py
```

Removing any output from previous runs with `rm -rf ./data`, we can run full our pipeline with `make`:

```shell-session
$ rm -rf ./data; make
mkdir -p data
./ingest.py
ingesting {'data': 'raw', 'ingest-time': '2021-12-27T13:56:30.045009'}
./clean.py
cleaning {'data': 'clean', 'ingest-time': '2021-12-27T13:56:30.045009', 'clean-time': '2021-12-27T13:56:30.193770'}
```

Now if we run `make` a second time, nothing happens:

```shell-session
$ make
make: Nothing to be done for `all'.
```

If we do want to only re-run our cleaning step, we can remove the previous output and run our pipeline again - with `make` knowing that it only needs to run the cleaning step again with existing raw data:

```shell-session
$ rm ./data/clean.json; make 
./clean.py
cleaning {'data': 'clean', 'ingest-time': '2021-12-27T13:56:30.045009', 'clean-time': '2021-12-27T14:02:30.685974'}
```

### Source Code Dependencies 

The final improvement we will make to our pipeline is to track dependencies on source code.

Let's update our `clean.py` script to also track `clean-date`:

```python { title = "clean.py" }
#!/usr/bin/env python3
from datetime import datetime
import json
from pathlib import Path

data = json.loads((Path.cwd() / "data" / "raw.json").read_text())
data["data"] = "clean"
data["clean-time"] = datetime.utcnow().isoformat()
data["clean-date"] = datetime.utcnow().strftime("%Y-%m-%d")
fi = Path.cwd() / "data" / "clean.json"
fi.write_text(json.dumps(data))
```

And now our final pipeline:

```makefile { title = "Makefile" }
all: ./data/clean.json

./data/raw.json: ./data/raw.json ./ingest.py
	mkdir -p data
	./ingest.py

./data/clean.json: ./data/raw.json ./clean.py
	./clean.py
```

Our final step, after updating only our `clean.py` script, `make` will run our cleaning step again:

```shell-session
$ make
./clean.py
ingesting {'data': 'clean', 'ingest-time': '2021-12-27T13:56:30.045009', 'clean-time': '2021-12-27T14:10:06.799127', 'clean-date': '2021-12-27'}
```

## Summary

That's it!  We hope you have enjoyed learning a bit about `make` & `Makefile`, and are enthusiastic to experiment with it in your data work.

There is more depth and complexity to `make` and the `Makefile` - what you have seen so far is hopefully enough to encourage you to experiment and learn more while using a `Makefile` in your own project.

Key takeaways are:

- `make` is a powerful, commonly available tool that can run arbitrary shell workflows,
- a `Makefile` forms a natural central point of execution for a project, with a simple CLI that integrates well with the shell,
- `make` can intelligently re-execute your data pipeline - keeping track of the dependencies between code and data.
