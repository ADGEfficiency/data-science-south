---
title: Reinforcement Learning for Energy Assets with energy-py
description: A Python framework for training reinforcement learning agents on energy systems using Gymnasium and Stable Baselines 3.
date_created: 2017-04-03
date_updated: 2025-11-01
github: https://github.com/ADGEfficiency/energy-py
competencies:
  - Energy
  - Machine Learning
  - Reinforcement Learning
aliases:
- 2017-04-03-energy-py-reinforcement-learning-for-energy-systems

---

**Energy systems need intelligent control** - but most rely on simple heuristics that can't adapt to changing conditions like price volatility or renewable generation uncertainty.

**Reinforcement learning offers a solution** - agents can learn optimal control policies through trial and error, adapting to complex, dynamic energy systems.

**This post introduces energy-py** - a Python framework for training reinforcement learning agents on energy environments, starting with electric battery storage.

You can find the source code at [ADGEfficiency/energy-py](https://github.com/ADGEfficiency/energy-py).

## What is energy-py?

energy-py is a reinforcement learning framework for energy systems:

- **Gymnasium integration**: Custom energy environments following the Gymnasium API
- **Stable Baselines 3**: Pre-built RL agents (PPO, DQN, A2C) ready to use
- **Battery environment**: Electric battery storage for price arbitrage
- **Experiment framework**: Train and evaluate on separate datasets
- **Historical data**: Real electricity price data for realistic training

## Why Reinforcement Learning for Energy?

Reinforcement learning enables agents to learn control policies without explicit programming:

- **Adaptation**: Learns from experience, improves over time unlike static heuristics
- **Non-linear patterns**: Deep neural networks can capture complex relationships
- **Strong reward signals**: Energy offers clear objectives - cost and carbon intensity
- **Simulation**: Energy systems can be simulated, enabling sample-efficient learning

Traditional heuristics fail when conditions change - a rule to prefer biomass over gas breaks down when gas prices drop. Reinforcement learning adapts.

## energy-py vs energypylinear

These are two different approaches to the same problem:

**energy-py** uses reinforcement learning:

- **Learning-based**: Agent learns optimal policy through trial and error
- **Non-linear**: Can model complex, non-linear system dynamics
- **Sample inefficient**: Requires many training episodes
- **Stochastic**: Different training runs produce different policies

**energypylinear** uses mixed-integer linear programming:

- **Optimization-based**: Solver finds optimal dispatch mathematically
- **Linear only**: Limited to linear system models
- **Deterministic**: Same inputs always produce same outputs
- **Fast**: Solves efficiently, no training required

Use energypylinear when your system is linear and you need deterministic, fast solutions. Use energy-py when you need to model non-linear dynamics or want agents that adapt over time.

## Installation

Requires Python 3.11 or later:

```shell
$ git clone https://github.com/ADGEfficiency/energy-py
$ cd energy-py
$ make setup
```

## Example: Battery Arbitrage with Random Agent

Train a PPO agent on a battery with random electricity prices:

```python
import numpy as np
from stable_baselines3 import PPO
import energypy

env = energypy.make_env(electricity_prices=np.random.uniform(-1000, 1000, 1024 * 5))

agent = PPO(
    policy="MlpPolicy",
    env=env,
    learning_rate=0.0003,
    n_steps=1024,
    batch_size=64,
    policy_kwargs=dict(net_arch=[64, 64]),
)

config = energypy.ExperimentConfig(
    env_tr=env,
    agent=agent,
    name="battery_random",
    n_eval_episodes=5,
)

result = energypy.run_experiment(cfg=config)
```

The agent learns to charge when prices are low and discharge when prices are high.

## Example: Training on Historical Data

Use real electricity price data for more realistic experiments:

```shell
$ uv run examples/battery_arbitrage_experiments.py
```

This runs a full experiment:

- **Training**: Agent learns on historical price data
- **Evaluation**: Performance tested on separate validation data
- **Logging**: Tensorboard tracks training progress
- **Comparison**: Results compared against random and naive baselines

## Features

energy-py provides a complete framework for energy RL experiments:

- **Gymnasium environment**: `Battery` environment with configurable power, capacity, efficiency
- **Observation space**: State of charge plus custom features (prices, forecasts)
- **Action space**: Continuous charge/discharge power in MW
- **Reward signal**: Profit from price arbitrage
- **Episode structure**: Configurable episode length and frequency

## When to Use energy-py

energy-py is ideal for:

- **Research**: Exploring RL algorithms for energy control
- **Non-linear systems**: Systems that can't be modeled with linear programming
- **Adaptive control**: Agents that improve over time with experience
- **Stochastic environments**: Systems with high uncertainty

energy-py is not suitable for:

- **Linear systems**: Use energypylinear instead for deterministic, fast optimization
- **Production control**: RL agents require extensive validation before deployment
- **Real-time dispatch**: Training is slow, inference is fast but less reliable than optimization

## Summary

energy-py provides a framework for training reinforcement learning agents on energy systems.

Key features:

- **Gymnasium integration**: Standard RL environment API
- **Stable Baselines 3**: Pre-built RL algorithms ready to use
- **Battery environment**: Electric storage with price arbitrage
- **Experiment framework**: Training, evaluation and logging
- **Historical data**: Real electricity prices for realistic training

Comparison with energypylinear:

- **energy-py**: Learning-based, handles non-linear systems, sample inefficient
- **energypylinear**: Optimization-based, linear only, deterministic and fast

Learn more:

- **Source code**: [github.com/ADGEfficiency/energy-py](https://github.com/ADGEfficiency/energy-py)
- **Related post**: [Optimize Energy Assets with energypylinear](/blog/energypylinear/)

Thanks for reading!
