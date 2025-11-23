---
title: Looping with Minimum Effort collections.defaultdict
description: Using the defaultdict store results from temporal simulations in Python.
date_created: 2018-10-07
date_updated: 2025-11-01
competencies:
  - Software Engineering
  - Python
aliases:
  - 2018-10-07-defaultdict
mathjax: true
---

This post introduces a simple Python implementation for simulating processes through time using `defaultdict` from Python's `collections` module.

## The Workflow

A common workflow in data science work is simulating a process through time:

- **Simulate a process**: Run the simulation step by step
- **Collect the results**: Store data at each timestep
- **Output a plot**: Visualize variables over time

## Why defaultdict?

**The `defaultdict` provides flexibility** - instead of needing to initialize a key/value pair, you can add keys on the fly and append to an already initialized list.

```python
from collections import defaultdict

# Normal dictionary requires initialization
stats = {}
stats["variable"] = []
stats["variable"].append(var)

# defaultdict handles initialization automatically
stats = defaultdict(list)
stats["variable"].append(var)
```

## Converting to DataFrame

**Once our `defaultdict` is full of data, we can easily turn it into a pandas `DataFrame`**:

```python
stats = pd.DataFrame().from_dict(stats)
```

All values in our `stats` dictionary must be lists of the same length - this will be the case if we added one value for each variable at each step.

## Plotting Results

**We can use this dataframe with `matplotlib` to plot our data**:

```python
fig, axes = plt.subplots()
stats.plot(y="variable", ax=axes)
stats.plot(y="other_variable", ax=axes)
```

## Example: Updating the Value Function for a Bandit

This example solves a problem from Section 2.6 of *Sutton & Barto - An Introduction to Reinforcement Learning*. **The problem involves incrementally updating the value function for a bandit problem**.

The incremental update equation:

$$Q_{n+1} = Q_{n} + \alpha [R_{n} - Q_{n}]$$

**Sutton suggests that an improvement to using a constant step size** (say $\alpha=0.5$) is to use a step size $\beta$:

$$\beta_{n} = \frac{\alpha}{\overline{o}_{n}}$$

Where we update $\overline{o}_{n}$ by:

$$\overline{o}_{n} = \overline{o}_{n-1} + \alpha (1-\overline{o}_{n-1})$$

### Implementation

To get the figure to show, save the code snippet to `bandit.py`, then run in interactive mode (`$ python -i bandit.py`):

```python
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

alpha = 0.0001
q = 10
omega = 0

stats = defaultdict(list)

for step in range(50):
    stats["q"].append(q)
    stats["omega"].append(omega)

    omega = omega + alpha * (1 - omega)
    beta = alpha / omega
    stats["beta"].append(beta)

    reward = np.random.normal(loc=5, scale=1)
    stats["reward"].append(reward)

    q += beta * (reward - q)

result = pd.DataFrame().from_dict(stats)

f, a = plt.subplots(nrows=4)

result.plot(y="reward", ax=a[0])
result.plot(y="q", ax=a[1])
result.plot(y="omega", ax=a[2])
result.plot(y="beta", ax=a[3])

print("final estimate {}".format(stats["q"][-1]))

f.show()
```

### Results

**The results of the run are stored in the `result` DataFrame**:

```bash
>>> result.head()
q   omega      beta    reward
0  10.000000  0.0000  1.000000  4.762884
1   4.762884  0.0001  0.500025  4.623668
2   4.693273  0.0002  0.333367  4.734825
3   4.707125  0.0003  0.250038  4.573823
4   4.673794  0.0004  0.200040  3.663734
```

**What pops out is a simple time series plot of how our variables changed over time**.

## Summary

The `defaultdict` workflow provides a simple and flexible approach to time series simulations:

- **Automatic initialization**: No need to pre-define dictionary keys
- **Easy conversion**: Transform to pandas DataFrame in one line
- **Simple visualization**: Plot results directly from the DataFrame
- **Clean code**: Reduces boilerplate for collecting simulation results

This pattern works well for reinforcement learning problems, process simulations, and any temporal analysis where you need to track multiple variables over time.

Thanks for reading!
