---
title: 'DDQN Solving Open AI Cartpole'
description: Finally - stable learning.
date_created: 2018-10-31
date_updated: 2025-11-06
github: https://github.com/ADGEfficiency/energy-py/tree/46fd1bf36f744918c962539eb8a84df96102d930
competencies:
  - Machine Learning
  - Reinforcement Learning
aliases:
- 2018-10-31-dqn-solving

---

This is the final post in a three part series of debugging and tuning the energypy implementation of DQN. **In the previous posts I debugged and tuned the agent using a *problem - hypothesis - solution* structure**. In this post I share some final hyperparameters that solved the Cartpole environment - but more importantly ended up with stable policies.

1. [DQN debugging using Open AI gym Cartpole](https://adgefficiency.com/dqn-debugging/)
2. [DDQN hyperparameter tuning using Open AI gym Cartpole](https://adgefficiency.com/dqn-tuning/)
3. [Solving Open AI gym Cartpole using DQN](https://adgefficiency.com/dqn-solving/)

## Key Changes for Stable Learning

The main changes that (I think!) contributed towards the high quality and stable policy were:

- **Small neural network**: Two hidden layers of (8, 4) nodes
- **Increased target network update frequency**: 10,000 steps between updates
- **Larger replay memory**: Holds the entire history of the agent's experience
- **Lower learning rate**: 0.0001

I ran four runs - two with an epsilon-greedy policy and two with a softmax policy. The experiments were run on [the master branch of energypy at this commit](https://github.com/ADGEfficiency/energy-py/tree/868129cb1a9912bbc69239eb9d2882137dbbff68).

**The performance of the four agents is shown below in Figure 1. This environment (`Cartpole-v0`) is considered solved when the agent achieves a score of 195 over 100 consecutive episodes** - which occurred after around 150,000 steps for the epsilon-greedy agents.

{{< img
    src="/images/dqn-solving/fig1.png"
    caption="Learning curves on Cartpole-v0"
    width="800"
>}}

## Policy Comparison: Epsilon-Greedy vs. Softmax

**The epsilon-greedy policy outperformed the softmax policy** - although I wasn't quite sure how to decay the softmax temperature (in the runs above I decayed it from 0.5 to 0.1 over the experiment). The softmax policy implementation is shown below - it lives in the energypy library at [energypy/common/policies/softmax.py](https://github.com/ADGEfficiency/energy-py/blob/master/energypy/common/policies/softmax.py).

```python
softmax = tf.nn.softmax(tf.divide(q_values, temp), axis=1)
log_probs = tf.log(softmax)

entropy = -tf.reduce_sum(softmax * log_probs, 1, name="softmax_entropy")

samples = tf.multinomial(log_probs, num_samples=1)
policy = tf.gather(discrete_actions, samples)
```

## Network Architecture Insights

Previously I had been using much larger neural networks - typically three layers with 50 to 250 nodes per layer. **For the Cartpole problem this is far too much! A smaller and shallower network has enough capacity to represent the action-value function for a high quality policy**.

There is an argument for larger networks:

- **Learning capacity**: The agent can learn to only use the capacity required
- **Stability through reduced weight sharing**: A larger network will mean less weight sharing which should give more stability

But on the other hand:

- **More weights to update**: A larger network means more weights to change
- **Higher risk**: More of a chance that a bad gradient will destroy the policy

## Stability vs. Speed Trade-offs

**Increasing the number of steps between target network updates and lowering the learning rate both reduce the speed of learning but should give more stability**. In reinforcement learning stability is the killer - although sample efficiency is a big problem in modern reinforcement learning you would rather have a slow, stable policy than a fast unstable one!

The idea behind increasing the size of the replay memory was to smooth out the distribution of the batches. What I was quite often seeing was good performance up to the first 100,000 steps followed by collapse - so I thought that maybe the agent was suffering with changes in distribution over batches as it learnt. **Cartpole doesn't have a particularly complex state space, so it's likely that all states are useful for learning throughout an agent's lifetime**.

## Hyperparameters

The hyperparameters used in the four Cartpole runs are shown below:

```ini
[DEFAULT]
total_steps=400000
agent_id=dqn
policy=e-greedy
discount=0.9
update_target_net=10000
tau=1.0
batch_size=512
layers=8, 4
learning_rate=0.0001
learning_rate_decay=1.0
epsilon_decay_fraction=0.4
initial_epsilon=1.0
final_epsilon=0.01
memory_fraction=1.0
memory_type=array
double_q=True

[softmax1]
policy=softmax
epsilon_decay_fraction=1.0
initial_epsilon=0.5
final_epsilon=0.1
seed=5

[softmax2]
policy=softmax
epsilon_decay_fraction=1.0
initial_epsilon=0.5
final_epsilon=0.1
seed=42

[egreedy1]
policy=e_greedy
seed=5

[egreedy2]
policy=e_greedy
seed=42
```

## Generalization Test: Pendulum Environment

**Because I've spent so much time tuning this DQN agent to Cartpole, I wanted to see if I was overfitting by looking at how the agent performed on another benchmark problem from gym, the Pendulum environment**. This environment doesn't have solved criteria - however the maximum possible reward per episode is 0. Figure 2 shows the performance of the same set of agents on Pendulum.

{{< img
    src="/images/dqn-solving/fig3.png"
    caption="Learning curves on Pendulum-v0"
    width="800"
>}}

**Pendulum has a continuous action space - I chose to discretize the space with five actions**. It's possible that this is too coarse of a discretization for the agent to find the optimal policy. It's also possible that Pendulum might need a larger network to model the action-value function.

## Summary

**Stability, not speed, is the goal in reinforcement learning**:

- **Network size**: You probably don't need that three layer, hundreds of nodes per layer network
- **Target network updates**: Increase the steps between updates for stability
- **Learning rate**: Lower learning rates provide more stable learning
- **Replay memory**: Larger memory can smooth out distribution changes

Thanks for reading!
