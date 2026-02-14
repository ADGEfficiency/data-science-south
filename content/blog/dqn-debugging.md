---
title: 'DQN debugging using Open AI gym Cartpole'
description: Debugging the new energy-py DQN reinforcement learning agent.
date_created: 2018-07-07
date_updated: 2025-11-04
github: https://github.com/ADGEfficiency/energy-py/tree/46fd1bf36f744918c962539eb8a84df96102d930
competencies:
  - Machine Learning
  - Reinforcement Learning
aliases:
- 2018-07-07-dqn-debugging

---

*This is the first post in a three part series on getting DQN to work*

1. [DQN debugging using Open AI gym Cartpole](https://adgefficiency.com/dqn-debugging/)
2. [DDQN hyperparameter tuning using Open AI gym Cartpole](https://adgefficiency.com/dqn-tuning/)
3. [Solving Open AI gym Cartpole using DQN](https://adgefficiency.com/dqn-solving/)

---

**This is the story of debugging and hyperparameter tuning of the new energy-py implementation of DQN**.

[energy-py is a reinforcement learning library for energy systems that I've been building for the past two years](https://github.com/ADGEfficiency/energy-py).  The experiments ran on the dev branch of energypy at [this commit](https://github.com/ADGEfficiency/energy-py/tree/46fd1bf36f744918c962539eb8a84df96102d930).  The [environment is the energy-py wrapper around the Open AI gym CartPole-v0 environment](https://github.com/ADGEfficiency/energy-py/blob/master/energy-py/envs/register.py).

**Cartpole is a simple, classic reinforcement learning problem - it's a good environment to use for debugging**. A good debug environment is one where you are familiar with how fast an agent should be able to learn.

**Once learning has been proven on a simple environment, the generalizability of reinforcement learning should mean it can learn on more difficult environments as well**.

The idea of documenting the debug and tuning process comes from [Lessons Learned Reproducing a Deep Reinforcement Learning Paper](http://amid.fish/reproducing-deep-rl). This post recommends keeping a detailed log of your debugging and also taking the time to form hypotheses about what might be wrong. **This is because of the long lead time between cause and effect for reinforcement learning experiments**.

This is a contrast to the ability to quickly see cause and effect when debugging software.  **If experiments are cheap it makes more sense to not waste time thinking about the problem, and to just get on and solve it**.

**This post shows the thought process I used when debugging, the kinds of silly errors that can easily be made and to show how Cartpole often performs using DQN**. It then starts the hyperparameter tuning process, [which is finished in the second post](https://adgefficiency.com/dqn-tuning/).

This is the third iteration of DQN that I've built - this one was significantly influenced by the [Open AI baselines implementation of DQN](https://github.com/openai/baselines/tree/master/baselines/deepq).

## The DQN Rebuild

{{< img
    src="/images/dqn-debugging/graph.png"
    caption="DQN architecture diagram"
    width="500"
>}}

This is energy-py's third DQN agent.  **Each iteration is a complete rewrite**.  I find it a luxury to write something from scratch, and believe that iteration is the only way progress .  I'm proud of how far I've come, and of how poor my first implementation looks to me today!

> If you are not embarrassed by the first version of your product, you've launched too late - Reid Hoffman

> I know you don't hit it on the first generation, don't think you hit it on the second, on the third generation maybe, on the fourth & fifth, that is when we start talking -  Linus Torvalds

Two more rebuilds to go...

## A Brief History

### Version 1

[version 1](https://github.com/ADGEfficiency/energy-py/tree/d21c3832e9116cba00891361e6777b8b896f9b78)

- **Built in Keras**: No target network
- **Single output structure**: Structuring the neural network with a single output. This means n passes are required to predict Q(s,a) for n actions, rather than a single pass in a network with n output nodes (one per action). It does allow the network to connect to the action as an array, so the network can sense the shape of the action

### Version 2

[version 2](https://github.com/ADGEfficiency/energy-py/commit/774ff3c9cd63b1b1e50359ab606edc7737121c86)

- **Built in Tensorflow**: Target network implemented
- **Multiple session calls**: Running act or learn requires running multiple session calls, because the algorithm switches between numpy and Tensorflow for operations
- **E-greedy policy only**: No other exploration policies

### Version 3

[version 3](https://github.com/ADGEfficiency/energy-py)

- **Single session call**: Built in Tensorflow, with a single session call per `agent.action()` and `agent.learn()`
- **Advanced features**: Gradient clipping, learning rate decay
- **Flexible policy**: Policy is split out to allow either epsilon greedy or a softmax policy to be used

## The Setup

**While I think obsession over what tools (i.e. which editor to use) is unhelpful, I do think that anyone who takes their work seriously should take pride in the toolset they use**.  For this experiment I used a combination of tmux, vim, an info & debug log and Tensorboard to try get an understanding of what's going on.

I used two tmux windows, one that kept track of the experiment and another with the `energy-py/agents/dqn.py` script open for editing in vim.  The experiment window shows both the `info.log` and `debug.log`.  The debug log moves too fast to be viewed but is useful for seeing if the agent is working.

**Switching between tmux windows is as easy at `Ctrl b p`**.

{{< img
    src="/images/dqn-debugging/tmux_setup.png"
    caption="Tmux setup - left pane running the script and showing the info log, the top right pane showing the debug log using tail -f debug.log, a Tensorboard server running in the bottom right pane"
    width="500"
>}}

{{< img
    src="/images/dqn-debugging/vim_setup.png"
    caption="Vim with agent/dqn.py open"
    width="500"
>}}

## Debugging Code

**For the debug process I wrote a barebones implementation of an experiment under the `if __name__ == '__main__':` block in `energy-py/agents.dqn.py`**.  It exposes the functionality that is all taken care of automatically when using the `experiment()` function in energy-py (`from energy-py import experiment`).

**Doing this in the same script as the DQN agent means I can easily make changes, and removes dependencies on the rest of the project**.

```python
import random

from energy-py.scripts.experiment import Runner
from energy-py.scripts.utils import make_logger

make_logger(
	{'info_log': 'info.log',
	'debug_log': 'debug.log'}
	)

discount = 0.99
total_steps = 400000

seed = 15
random.seed(seed)
np.random.seed(seed)
tf.set_random_seed(seed)

env = energy-py.make_env('Battery')

with tf.Session() as sess:
agent = DQN(
    sess=sess,
    env=env,
    total_steps=total_steps,
    discount=discount,
    memory_type='deque',
    act_path='./act_tb',
    learn_path='./learn_tb',
    learning_rate=0.001,
    decay_learning_rate=1.0,
)

runner = Runner(
	sess,
	{'tb_rl': './tb_rl',
	 'ep_rewards': './rewards.csv'},
	total_steps=total_steps
	)

step = 0
while step < total_steps:

    done = False
    obs = env.reset()
    while not done:

	act = agent.act(obs)
	next_obs, reward, done, info = env.step(act)

	runner.record_step(reward)
	agent.remember(obs, act, reward, next_obs, done)

	agent.learn()

	obs = next_obs
	step += 1

    runner.record_episode()
```

**This setup is enough to get logging setup with two log files and Tensorboard running**.  Three Tensorboard writers are used - one for `agent.act()`, one for `agent.learn()` and one for `runner.record_episode()`.  I setup these log files in the local directory.  To view the Tensorboard log files I start a server in the same directory that the `dqn.py` script lives in.

```bash
$ cd energy-py/energy-py/agents

$ Tensorboard --logdir='.'
```

## Problem: Reward Collapsing After Exploration

{{< img
    src="/images/dqn-debugging/fig1.png"
    caption="Figure 1 - Collapsing reward after exploration is over"
    width="500"
>}}

**When using an epsilon greedy exploration policy, early stages of the experiment are mostly randomly selected actions**.  For Cartpole this ends up being an average reward per episode of between 20 - 30.  For a working implementation the episode returns will stay in this range and start to increase as the agent learns.

**What I was seeing was a drop in average reward to around 10 per episode after exploration was over**.  This suggests that the argmax over `Q(s,a)` was selecting the same action each time, resulting in a poor policy that quickly failed the Cartpole task.  This policy is worse than a random policy!

##  Hypothesis: Are My Weights Changing

**The idea was that if the online network weights were never changed, then the argmax across the online network might select the same action in every state - leading to the behaviour we saw**.

To do this I added the weights as histograms in Tensorboard by indexing a list of parameters for the online and target networks.  This is hacky - Tensorflow didn't like iterating over this list so I just indexed out the last layer weights and biases for both networks.

```python
self.act_summaries.extend(
    [
        tf.summary.histogram(self.online_params[-1].name, self.online_params[-1]),
        tf.summary.histogram(self.online_params[-2].name, self.online_params[-2]),
        tf.summary.histogram(self.target_params[-1].name, self.target_params[-1]),
        tf.summary.histogram(self.target_params[-2].name, self.target_params[-2]),
    ]
)
```

This allows visibility of the weights at each step. Figure 2 below shows that both the weights and biases are being changed.

{{< img
    src="/images/dqn-debugging/fig2.png"
    caption="Figure 2 - Online network weights changing"
    width="500"
>}}

##  Hypothesis: How Am I Changing the Weights - aka What is the Target

**In DQN learning is done by minimizing the difference between predicted Q values and Bellman targets**.  Creation of the Bellman target is core to the algorithm and a common place for errors.

**Reinforcement learning can be though of as a data generation process** - interacting with the environment generates sequences of experience tuples of `(s, a, r, s')`.  **In order to learn from this data we need to label it** - in DQN this labelling process is doing by creating a Bellman target for each sample in a batch.  This then allows supervised learning to be used to fit our predicted `Q(s,a)` to the target.

From experience with DQN and Cartpole I expected to see a inflation in the Q values.  **This optimism comes from the max operation over `Q(s',a)` in the Bellman target**.  When I took a look at the Bellman target I saw something quite different - an increase until a small value of around 2.0.  Since rewards for Cartpole are +1 for each step, this meant that the max across `Q(s',a)` was approximately 1.0 as well.

{{< img
    src="/images/dqn-debugging/fig3.png"
    caption="Figure 3 - The Bellman target showing a plateau at around 2"
    width="500"
>}}

We now can see that the target doesn't seem right - **we can check the loss to see if this improperly formed target is being learnt**.  Even though DQN uses a target network for the approximation of `max Q(s',a)`, this approximation is still influenced by the online network via the target net copy operations.

Taking a look at the loss function (Figure 4) we can see that the agent is learning to fit this improperly formed Bellman target.

{{< img
    src="/images/dqn-debugging/fig4.png"
    caption="Figure 4 - A nice looking but wrong loss function"
    width="500"
>}}

##  Hypothesis: The Target Isn't Being Created Correctly

**The Bellman target has two parts - the reward and the discounted max value of the next state `max Q(s',a)`**. Getting the reward is as simple as unpacking the batch, meaning the error is most likely in the estimated maximum value of the next state.

**One key part of Q-Learning is setting this value to zero for terminal states**.  In terminal states the discounted return is simply the reward.  This means that for terminal states, we need to mask out the return from the next state.

I added this part of the Bellman equation to Tensorboard - both the unmasked and masked `Q(s',a)` values.

{{< img
    src="/images/dqn-debugging/fig5.png"
    caption="Figure 5 - The unmasked and masked approximations of max Q(s',a)"
    width="500"
>}}

As expected none of the unmasked values are zero, because they are maximums across all possible actions. **But looking at the masked values, it seemed that far too many were zero!**  If our batch is sampled well from memory, we would expect the distribution of terminals (and associated zero `Q(s',a)` values) to match the distribution we see in training.  For Cartpole with an episode length of around 20, we would expect to see 20 times as many non-zero values as zeros.  From Figure 5 we see the opposite.

**Looking at how I was doing the masking the error became clear - I had the masking around the wrong way!**  Terminal is a boolean that is `True` when the episode is over, and `False` otherwise.

```python
#  the corrected masking of terminal states Q(s',a) values
next_state_max_q = tf.where(
    self.terminal,
    tf.zeros_like(unmasked_next_state_max_q),
    unmasked_next_state_max_q,
    name="terminal_mask",
)
```

After making this change, the distribution of masked `Q(s',a)` values looks better.

{{< img
    src="/images/dqn-debugging/fig6.png"
    caption="Figure 6 - Proper masking out of Q(s',a)"
    width="500"
>}}

As part of the DQN rebuild I added a [suite of tests](https://github.com/ADGEfficiency/energy-py/blob/master/energy-py/tests/test_dqn.py) to test the new agent.  Tests include the variable sharing and copy operations, along with checking the Bellman target creation for both DQN and DDQN.

**Unfortunately I had repeated the same error with `tf.where` in my test for the Bellman target creation!**  I actually wrote a note pointing out the test mirrored the tensorflow code exactly... maybe my subconscious saw something I didn't.

Now after running the experiment we see the increase in Q values that I saw with previous implementations of DQN.  **This optimism is a function of the aggressive and positively biased maximum value done in creating the Bellman target**.  We know this because a pessimistic target (which we had previously with our incorrect `tf.where`) doesn't see this optimism.

{{< img
    src="/images/dqn-debugging/fig7.png"
    caption="Figure 7 - Increasingly optimistic Bellman targets and a loss function that now reflects the non-stationary target creation"
    width="500"
>}}

The loss function in Figure 7 is maybe scary for supervised learners - a increasing loss function means that your errors in predicting the target are getting worse.  **In the context of reinforcement learning this loss function is a commentary on the non-stationary target being used to train**.  Increases in loss function can actually be seen as a good thing, as this means the agent is surprised about how much return it should expect for a particular sample of experience.

**This surprise can be used to improve the agents understanding of actions that are good or bad**.

## Hypothesis: Improperly Scaled Bellman Target

Figure 7 shows that the Bellman target is rather large.  **For gradient based methods the optimizer usually expects to see inputs and outputs in the range of -1 to 1** - hence the use of standardization and normalization using training set statistics in supervised learning.

**In reinforcement learning we have the problem of not know what are good approximations for the statistics of `Q(s,a)`**.  To combat this I used a tensorflow batch normalization layer to process the Bellman target before it is used in the loss function.

I manually wrote Processor objects to do normalization and standardization in energy-py previously.  **Using tensorflow to to the processing will allow me to keep the processing within the tensorflow graph, and mean less code for me to maintain**.

There are three different implementations of batch norm in tensorflow - tf.nn.batch_normalization, tf.layers.batch_normalization or tf.contrib.layers.batch_norm.  I chose the implementation from the layers module.

```python
bellman = self.reward + self.discount * next_state_max_q

#  batch norm requires some reshaping with a known rank
#  reshape the input into batch norm, then flatten in loss
#  training=True because we want to normalize each batch

bellman_norm = tf.layers.batch_normalization(
    tf.reshape(bellman, (-1, 1)),
    training=True,
    trainable=False,
)

error = tf.losses.huber_loss(
    tf.reshape(bellman_norm, (-1,)), q_selected_actions, scope="huber_loss"
)
```

**One of the hyperparameters in using batch norm is whether to use accumulated statistics across multiple batches (`training=False`) or to process based on statistics from only the current batch (`training=True`)**.  My intuition is that processing only across the batch removes the difficulty of figuring out how best to remember and forget statistics, and just focus on favouring some actions within the batch more than others.

{{< img
    src="/images/dqn-debugging/fig8.png"
    caption="Figure 8 - The Bellman target before and after batch normalization"
    width="500"
>}}

After making these changes the first signs of life appeared.

{{< img
    src="/images/dqn-debugging/fig9.png"
    caption="Figure 9 - It's alive!"
    width="500"
>}}

## Tuning

After seeing some initial signs of life, I am pretty happy that there are no errors in the algorithm.  **I know from experience that a random agent (i.e. `epsilon=1.0` achieves a mean episode return of 20 - 30**.  Seeing these jumps is evidence that learning is possible - but it is not stable.  **Learning stability is a key challenge** - the early DeepMind work on DQN was focused on learning stability and generalization, not absolute performance.

**Getting good performance from a reinforcement learning requires a good set of hyperparameters and comparisons of runs over multiple different random seeds**.

The hyperparameter tuning process followed a similar hypothesis - problem structure.

## Problem: Unstable Learning

{{< img
    src="/images/dqn-debugging/fig10.png"
    caption="Figure 10 - Examples of learning and forgetting. Note the different y-axis on the second plot. The second plot shows the collapse to a policy that is worse than random. The third agent actually solves the environment (Open AI consider the env solved for an average reward of 195 over 100 consecutive trails) but then forgets"
    width="500"
>}}

## Hypothesis: Learning Rate is Too High OR State Space Not Being Explored Well

At this point I had two main thoughts about what might cause an unstable policy:

- **Large learning rate**: A large learning rate means that the optimizer is forced to change policy weights, even when the policy is performing well
- **Insufficient exploration**: The exploration period being too short means that only late in life does the agent see certain parts of the state space, making the policy unstable in these regions of the state space

I previous had the `epsilon_decay_fraction` hyperparameter set to `0.3` - this meant that the entire epsilon decay is done in the first 30% of the total steps for this experiment.  **I changed this to `0.5` - giving the agent more of a chance to see the state space early in life**.  This could be investigated further by looking at how the distribution of the observations (either during acting or training) were changing. I decided not to do this.

The second set of changes were with the learning rate.  Historically with DQN I had used a fixed learning rate of `0.0001`.  This was a chance to play with the decay.

When I saw Vlad Mnih speak at the 2017 Deep RL bootcamp, he mentioned that **larger neural networks can be more stable because they alias less**.  By alias I mean less weights are shared.  One option here would be to introduce a larger neural network, but this comes with the risk of overfitting.

Another change I made at this point was to set `centre=False` to the target batch normalization.  John Schulman notes in the talk **The Nuts and Bolts of Deep RL Research** ([video](https://www.youtube.com/watch?v=8EcdaCk9KaQ) and [slides](https://github.com/ADGEfficiency/dsr_rl/blob/master/literature/reinforcement_learning/2016_schulman_nuts-and-bolts.pdf) that **removing the mean from the target might affect the agent's will to live**.

```python
bellman_norm = tf.layers.batch_normalization(
    tf.reshape(self.bellman, (-1, 1)),
    center=False,
    training=True,
    trainable=False,
)
```
{{< img
    src="/images/dqn-debugging/fig11.png"
    caption="Figure 11 - Learning rate decay"
    width="500"
>}}

{{< img
    src="/images/dqn-debugging/fig12.png"
    caption="Figure 12 - Learning curves across three random seeds"
    width="500"
>}}

And here is the setup these final three agents:

```python
agent = DQN(
    sess=sess,
    env=energy - py.make_env("cartpole-v0"),
    total_steps=400000,
    discount=0.9,
    memory_type="deque",
    act_path="./act_tb",
    learn_path="./learn_tb",
    learning_rate=0.0001,
    decay_learning_rate=0.05,
    epsilon_decay_fraction=0.5,
)
```

## Concluding Thoughts

### Best Practices Followed

- **Simple environment**: Using simple env that I'm familiar with
- **Multiple seeds**: Running comparisons across multiple random seeds
- **Detailed logging**: Keeping a detailed log of your thoughts

### Error Fixes

- **Incorrect masking**: Incorrect masking of Q(s',a)
- **Test code error**: Test code repeating error of incorrect masking

### Hyperparameters

- **Batch normalization**: Batch normalization setup to only scale and not remove the mean
- **Exploration decay**: Exploration decay fraction from `0.3` to `0.5`
- **Learning rate**: Learning rate reduced and decayed

[The next post in this series continues the story with hyperparameter tuning of the DQN agent](https://adgefficiency.com/dqn-tuning/) - [or skip right ahead to the final post where the agent solves the Cartpole environment](https://adgefficiency.com/dqn-solving/).

Thanks for reading!
