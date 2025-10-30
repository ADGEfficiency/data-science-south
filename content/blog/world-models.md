---
title: 'World Models (The Long Version)'
description: Ha & Schmidhuber's World Models reimplemented in Tensorflow 2.0.
date_created: 2019-12-21
date_updated: 2025-10-06
competencies:
  - Machine Learning
aliases:
  - 2020-04-25-world-models
---

{{< img
    src="/images/world-models/f0.gif"
    caption="Performance of the final agent on a conveniently selected random seed. The cumulative episode reward is shown in the lower left. This agent & seed achieves 893. 900 is solved."
    width="600"
>}}

## Summary

**In 2019 I reimplemented the 2018 paper World Models by David Ha & Jürgen Schmidhuber**. This post takes a unapologetically deep and indulgent look at the theory and practice of the reimplementation.

The remiplementation source code is in [ADGEfficiency/world-models](https://github.com/ADGEfficiency/world-models). References & resources are in [ADGEfficiency/rl-resources/world-models](https://github.com/ADGEfficiency/rl-resources/tree/master/world-models). I gave a short talk about this project - [you can find the slides here](https://adgefficiency.com/world-models/).

**This project took around ten months**:

{{< img
    src="/images/world-models/commits-month.png"
    caption="Commits per month (excludes blog post commits)"
    width="600"
>}}

**The final agent achieved an acceptable performance**:

{{< img
    src="/images/world-models/final_hist.png"
    caption="Histogram of the best agent (Agent Five, generation 229) episode rewards across 48 random seeds. 900 is solved."
    width="600"
>}}

**I spent a total of $USD 3,648 on the project**:

| AWS Costs           |   Cost [$] |
|:--------------------|-----------:|
| compute-total       |       2,485 |
| storage-total       |       1,162 |
| total               |       3,648 |

An overview of the reimplementation source code file structure:

```bash
$ tree worldmodels

worldmodels
├── __init__.py
├── control
│   ├── controller.py
│   └── train_controller.py
├── data
│   ├── __init__.py
│   ├── car_racing.py
│   ├── sample_latent_stats.py
│   ├── sample_policy.py
│   └── tf_records.py
├── memory
│   ├── __init__.py
│   ├── memory.py
│   └── train_memory.py
├── params.py
├── tests
│   ├── test_gif_creation.py
│   ├── test_starmap.py
│   └── test_tf_records.py
├── utils.py
└── vision
├── __init__.py
├── images.py
├── train_vae.py
└── vae.py
```

## References

A full list of reference material for this project is kept in a repository I use to store my reinforcement learning resources - you can find the World Models references at [ADGEfficiency/rl-resources/world-models](https://github.com/ADGEfficiency/rl-resources/tree/master/world-models).

## Motivations and Context

In this post the agent refers to the World Models agent as introduced by Ha & Schmidhuber.  When I refer to this agent as **our** agent, this is not showing ownership over the idea, only the instance of our agent that lived on the CPU I paid for.

### Why Reimplement a Paper?

The genesis of the idea was from a Open AI job advertisement.  Seeing a tangible goal that could put me in the ballpark of a world class machine learning lab, I set out looking for a paper to reimplement.  **The advertisement specified a high quality implementation** - this echoed in my mind as I developed the project.

**I had never worked with any of the techniques used in the agent.** The influence of learning how the components work has been visible in the projects of my students at [Data Science Retreat](https://www.datascienceretreat.com/), where I was working while doing this reimplementation on the side.

To Mack (who used a mixed density network to predict hospital triage codes), Samson (who used a Variational Autoencoder to detect images of football games) and Stas (who combined the World Models vision & memory with a PPO controller!) - thank you to them for allowing me to improve my understanding in parallel with theirs.

### Why Reimplement World Models?

World Models is one of my three most significant reinforcement learning papers.  Here by significance, I mean has made the most impact on how I have spent my the time in my life.

### DQN

This paper blew me away without even reading it.  I have a memory of seeing a YouTube video DQN playing the Atari game Breakout, well before I made the transition into data science.  Even though I knew nothing of reinforcement learning, the significance of a machine could learn to play a video game from pixels was made clear.

<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/V1eYniJ0Rnk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<figcaption>DQN playing Atari Breakout</figcaption>
</center>

I had no way of knowing that the algorithm I was watching would be one I implement four times, or that I would teach the mechanics of DQN and it's evolution into Rainbow over twenty times.

### AlphaGo Zero

I had just completed the second iteration of teaching a reinforcement learning class when AlphaGo Zero was published in October 2017.

{{< img
    src="/images/world-models/Zero_act_learn.png"
    caption="Silver et. al (2017) Mastering the game of Go without human knowledge with additional annotations"
    width="600"
>}}

At this stage (9 months after my transition into data science), I didn't fully grasp all of the mechanics in AlphaGo.  But I knew enough to understand the significance of some the changes from AlphaGo to AlphaGo Zero - *tabula rasa* learning among the most important.

### World Models

The third paper is World Models, which introduced a novel machine learning algorithm that solved a previously unsolved continuous action space, pixel observation space control problem.  The paper trains an agent on two environments, `Car-Racing-v0` and `ViSDoom`.  The scope of this reimplementation is only of the `Car-Racing-v0` work.

{{< img
    src="/images/world-models/ha-blog.png"
    caption="https://worldmodels.github.io/"
    width="600"
>}}

**World Models is strong technical work presented well**. Ha & Schmidhuber's [2018 paper](https://github.com/ADGEfficiency/rl-resources/blob/master/world-models/2018_Ha_world_models.pdf) was accompanied by a [blog post](https://worldmodels.github.io/) that was both interactive and full of `.gif`, making the work engaging.

### The Promise of Learning a Model of the World

So what is a world model?

**A world model is an abstract representation of the spatial or temporal dimensions of our world**.  A world model can be useful in a number of ways.

**One use of a world model is to use their low dimensional, internal representations for control**.  We will see that the agent uses it's vision and memory in this way.  The value of having these low dimensional representations is that both prediction and control are easier in low dimensional spaces.

**Another is to generate data for training**.  A model that is able to approximate the environment transition dynamics can be used recurrently to generate rollouts of simulated experience.

**Being able to generate data is a superpower for a reinforcement learning agent.**  The primary problem in modern reinforcement learning is sample efficiency - the algorithms require vast amounts of data.  Being able to learn an environment model and sample transitions means this sample inefficiency can managed.

These two uses can be combined together, where world models are used to generate synthetic rollouts in the low dimensional, internal representation spaces.  **This is learning within a dream**, and is demonstrated by Ha & Schmidhuber on the `ViSDoom` environment.

**World models can also be used for planning**. An offline planning algorithm (such as Monte Carlo Tree Search, which powers AlphaGo) can be used to take the action that performs the best in the simulation of many rollouts.

Now that we understand the motivations and context of this project, we can look at one side of the Markov Decision Process (MDP) coin - the environment (*if you aren't familiar with what an MDP is, take a look at Appendix One*).

## The Environment

The agent interacts with the `car-racing-v0` environment from OpenAI's `gym` library.  I used the same version of `gym` as the paper codebase (`gym==0.9.4`).

**`car-racing-v0` has two attributes that make it a challenging control problem - a high dimensional observation space and a continuous action space.**

### Working with `car-racing-v0`

Lets describe the `car-racing-v0` environment as a Markov Decision Process.

In the `car-racing-v0` environment, the agents observation space is raw image pixels $(96, 96, 3)$.  The observation has both a spatial $(96, 96, 3)$ and temporal structure, given the sequential nature of sampling transitions from the environment.  An observation is always a single frame.

**The action space has three continuous dimensions - `[steering, gas, break]`.**  This is a continuous action space - the most challenging for control.

The reward function is $-0.1$ for each frame, $+1000 / N$ for each tile visited, where $N$ is the total tiles on track.  This reward function encourages quickly driving forward on the track.

The horizon (aka episode length) is set to $1000$ throughout the paper codebase.

### Getting the Resizing Right

The raw observation is an image of shape $(96, 96, 3)$ - this is cropped and resized to $(64, 64, 3)$.

**This was where I made my first mistake.**  After training my first agent, I inspected the performance of the agent:

{{< img
    src="/images/world-models/first.gif"
    caption="Performance of Agent One with the incorrect resizing."
    width="600"
>}}

**The rendering of the observation was blocky, compared to the images from the paper.**  After some investigation, I found the reason - a different resampling filter. You can see more detail in [world-models/notebooks/resizing-observation.ipynb](https://github.com/ADGEfficiency/world-models/blob/master/notebooks/resizing-observation.ipynb).

**The final function used is given below, and uses `PIL.Image.BILINEAR`:**

```python
def process_frame(
    frame, screen_size=(64, 64), vertical_cut=84, max_val=255, save_img=False
):
    """crops, scales & convert to float"""
    frame = frame[:vertical_cut, :, :]
    frame = Image.fromarray(frame, mode="RGB")
    obs = frame.resize(screen_size, Image.BILINEAR)
    return np.array(obs) / max_val
```

Using this, the agent's observation appears similar to the images from the paper:

{{< img
    src="/images/world-models/f1-final.png"
    caption="The raw observation (96, 96, 3) - the correctly resized observation (64, 64, 3) - the learnt latent variables (32,) (more on them later)"
    width="600"
>}}

### Avoiding Corrupt Observations

**One important required hack when working with `car-racing-v0` is to use `env.viewer.window.dispatch_events()` in the `reset()` and `step()` methods of the environment** ([see the issue here](https://github.com/openai/gym/issues/976)). If you don't do this you will get corrupt environment observations!

{{< img
    src="/images/world-models/corrupt.jpeg"
    caption="If you see this, your environment observation is corrupt!"
    width="600"
>}}

An example of using this correctly is the `step` function of the environment:

```python
def step(self, action, save_img=False):
    """one step through the environment"""
    frame, reward, done, info = super().step(action)

    #  needed to get image rendering
    #  https://github.com/openai/gym/issues/976
    self.viewer.window.dispatch_events()

    obs = process_frame(
        frame, self.screen_size, vertical_cut=84, max_val=255.0, save_img=save_img
    )
    return obs, reward, done, info
```

See the [`worldmodels/notebooks/car_race_consistency.ipynb`](https://github.com/ADGEfficiency/world-models/blob/master/notebooks/car_race_consistency.ipynb) for more about avoiding corrupt `car-racing-v0` observations.

### Implementing the Environment Code

The code responsible for generating data lives in [ADGEfficiency/worldmodels/data](https://github.com/ADGEfficiency/world-models/tree/master/worldmodels/data):

```bash
$ tree worldmodels

worldmodels
├── __init__.py
├── control
├── data
│   ├── __init__.py
│   ├── car_racing.py
│   ├── sample_latent_stats.py
│   ├── sample_policy.py
│   └── tf_records.py
├── memory
├── params.py
├── tests
├── utils.py
└── vision
```

The interface with the OpenAI `gym` `car-racing-v0` environment, including that all important image resize:

```python
## worldmodels/dataset/car_racing.py

from gym.spaces.box import Box
from gym.envs.box2d.car_racing import CarRacing
import numpy as np
from PIL import Image


def process_frame(
    frame, screen_size=(64, 64), vertical_cut=84, max_val=255, save_img=False
):
    """crops, scales & convert to float"""
    frame = frame[:vertical_cut, :, :]
    frame = Image.fromarray(frame, mode="RGB")
    obs = frame.resize(screen_size, Image.BILINEAR)
    return np.array(obs) / max_val


class CarRacingWrapper(CarRacing):
    screen_size = (64, 64)

    def __init__(self, seed=None):
        super().__init__()
        if seed:
            self.seed(int(seed))

        #  new observation space to deal with resize
        self.observation_space = Box(low=0, high=255, shape=self.screen_size + (3,))

    def step(self, action, save_img=False):
        """one step through the environment"""
        frame, reward, done, info = super().step(action)

        #  needed to get image rendering
        #  https://github.com/openai/gym/issues/976
        self.viewer.window.dispatch_events()

        obs = process_frame(
            frame, self.screen_size, vertical_cut=84, max_val=255.0, save_img=save_img
        )
        return obs, reward, done, info

    def reset(self):
        """resets and returns initial observation"""
        raw = super().reset()

        #  needed to get image rendering
        #  https://github.com/openai/gym/issues/976
        self.viewer.window.dispatch_events()

        return process_frame(
            raw, self.screen_size, vertical_cut=84, max_val=255.0, save_img=False
        )
```

Code to sample data with a random policy or with a learned World Models agent controller:

```python
## worldmodels/data/sample_policy.py

import argparse
from collections import defaultdict
from functools import partial
from multiprocessing import Pool
import os
from time import sleep

import numpy as np

from worldmodels.control.train_controller import episode
from worldmodels.data.car_racing import CarRacingWrapper
from worldmodels.data.tf_records import save_episode_tf_record
from worldmodels.params import home


def random_rollout(env, episode_length, results=None, seed=None):
    """runs an episode with a random policy"""
    if results is None:
        results = defaultdict(list)

    env = env(seed=seed)
    done = False
    observation = env.reset()
    step = 0
    while not done:
        action = env.action_space.sample()
        next_observation, reward, done, info = env.step(action)
        transition = {"observation": observation, "action": action}
        for key, data in transition.items():
            results[key].append(data)

        observation = next_observation
        step += 1
        if step >= episode_length:
            done = True

    env.close()
    return results


def get_max_gen():
    """gets the newest controller parameters"""
    path = os.path.join(home, "control", "generations")
    gens = os.listdir(path)
    gens = [int(s.split("_")[-1]) for s in gens]
    max_gen = max(gens)
    return max_gen


def get_controller_generation(generation):
    """loads controller params"""
    if generation == "max":
        max_gen = get_max_gen()
        return int(max_gen)

    elif generation == "best":
        max_gen = get_max_gen()
        path = os.path.join(home, "control", "generations")
        gens = list(range(max_gen - 5, max_gen))
        gen_best = []
        for gen in gens:
            rew = np.load(
                os.path.join(path, "generation_{}".format(gen), "epoch-results.npy")
            )
            gen_best.append(max(rew))

        best_gen = gens[np.argmax(gen_best)]
        print("max gen {} best gen {} {}".format(max_gen, best_gen, max(rew)))

        sleep(3)
        return int(best_gen)

    else:
        return int(generation)


def get_controller_params(generation):
    path = os.path.join(
        home,
        "control",
        "generations",
        "generation_{}".format(generation),
        "best-params.npy",
    )
    print("loading controller from {}".format(path))
    return np.load(path)


def controller_rollout(controller_gen, seed=42, episode_length=1000):
    """runs an episode with pre-trained controller parameters"""
    controller_gen = get_controller_generation(controller_gen)
    params = get_controller_params(controller_gen)
    results = episode(
        params, collect_data=True, episode_length=episode_length, seed=seed
    )
    return results[2]


def save_episode(results, process_id, episode, seed, dtype="tfrecord"):
    """saves data from a single episode to either record or np"""
    if dtype == "tfrecord":
        save_episode_tf_record(results_dir, results, process_id, episode)
    else:
        assert dtype == "numpy"
        save_episode_numpy(results, seed)


def save_episode_numpy(results, seed):
    """results dictionary to .npy"""
    path = os.path.join(home, "controller-samples", str(seed))
    os.makedirs(path, exist_ok=True)

    for name, data in results.items():
        results[name] = np.array([np.array(a) for a in data])
        print(name, results[name].shape)
        np.save(os.path.join(path, "{}.npy".format(name)), data)


def rollouts(
    process_id,
    rollout_start,
    rollout_end,
    num_rollouts,
    env,
    episode_length,
    results_dir,
    policy="random",
    generation=0,
    dtype="tfrecord",
):
    """runs many episodes"""
    #  seeds always the length of the total rollouts per process
    #  so that if we start midway we get a new seed
    np.random.seed(process_id)
    seeds = np.random.randint(0, high=2**32 - 1, size=num_rollouts)
    seeds = seeds[rollout_start:rollout_end]
    episodes = list(range(rollout_start, rollout_end))
    assert len(episodes) == len(seeds)

    for seed, episode in zip(seeds, episodes):
        if policy == "controller":
            results = controller_rollout(
                generation, seed=seed, episode_length=episode_length
            )

        else:
            assert policy == "random"
            results = random_rollout(env, seed=seed, episode_length=episode_length)

        print(
            "process {} episode {} length {}".format(
                process_id, episode, len(results["observation"])
            )
        )

        save_episode(results, process_id, episode, dtype=dtype, seed=seed)
        paths = os.listdir(results_dir)
        episodes = [path for path in paths if "episode" in path]
        print("{} episodes stored locally".format(len(episodes)))
```

Code to sample the learned latent space statistics of the VAE:

```bash
## worldmodels/data/sample_latent_stats.py

import argparse
from os.path import join

import tensorflow as tf

from worldmodels.data.tf_records import encode_floats, batch_episodes, parse_random_rollouts
from worldmodels.params import vae_params, results_dir
from worldmodels.utils import list_records, make_directories
from worldmodels.vision.vae import VAE


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--episode_start', default=0, nargs='?', type=int)
parser.add_argument('--episodes', default=10000, nargs='?', type=int)
parser.add_argument('--data', default='local', nargs='?')
parser.add_argument('--dataset', default='random', nargs='?')
args = parser.parse_args()
print(args)

records = list_records(args.dataset+'-rollouts', 'episode', args.data)
make_directories('latent-stats')
results_dir = join(results_dir, 'latent-stats')

episode_start = args.episode_start
episodes = args.episodes
records = records[episode_start: episode_start + episodes]
dataset = batch_episodes(parse_random_rollouts, records, episode_length=1000)

model = VAE(**vae_params)
for episode in range(episode_start, episode_start + episodes):
print('processing episode {}'.format(episode))
obs, act = next(dataset)
assert obs.shape[0] == 1000
mu, logvar = model.encode(obs)

path = join(results_dir, 'episode{}.tfrecord'.format(episode))
print('saving to {}'.format(path))
with tf.io.TFRecordWriter(path) as writer:
encoded = encode_floats({
    'action': act.numpy(),
    'mu': mu.numpy(),
    'logvar': logvar.numpy(),
})
writer.write(encoded)


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--num_process', default=2, nargs='?', type=int)
parser.add_argument('--episodes', default=10, nargs='?', type=int)
parser.add_argument('--episode_length', default=1000, nargs='?', type=int)
parser.add_argument('--start_episode', default=0, nargs='?', type=int)
parser.add_argument('--policy', default='random', nargs='?')
parser.add_argument('--generation', default=0, nargs='?')
parser.add_argument('--dtype', default='tfrecord', nargs='?')
args = parser.parse_args()
print(args)

num_process = int(args.num_process)
episodes = args.episodes
episodes_per_process = int(episodes / num_process)
episode_length = args.episode_length

rollout_start = args.start_episode
rollout_end = episodes_per_process
assert rollout_end <= episodes_per_process

results_dir = os.path.join(home, args.policy+'-rollouts')
os.makedirs(results_dir, exist_ok=True)

env = CarRacingWrapper
total_eps = num_process * episodes_per_process

with Pool(num_process) as p:
p.map(
  partial(
    rollouts,
    rollout_start=rollout_start,
    rollout_end=rollout_end,
    num_rollouts=episodes_per_process,
    env=env,
    episode_length=episode_length,
    results_dir=results_dir,
    policy=args.policy,
    generation=args.generation,
    dtype=args.dtype
  ),
  range(num_process)
)
```

And finally code to interface with `tf.data`.  Raw data was saved into `tfrecord` files.

```python
## worldmodels/data/tf_records.py
import os

import tensorflow as tf


def encode_float(value):
    """single array"""
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def encode_floats(features):
    """multiple arrays"""
    package = {}
    for key, value in features.items():
        package[key] = encode_float(value.flatten().tolist())

    example_proto = tf.train.Example(features=tf.train.Features(feature=package))
    return example_proto.SerializeToString()


def save_episode_tf_record(results_dir, results, process_id, episode):
    """results dictionary to .tfrecord"""

    path = os.path.join(
        results_dir, "process{}-episode{}.tfrecord".format(process_id, episode)
    )

    print("saving to {}".format(path))
    with tf.io.TFRecordWriter(path) as writer:
        for obs, act in zip(results["observation"], results["action"]):
            encoded = encode_floats({"observation": obs, "action": act})
            writer.write(encoded)


def parse_episode(example_proto):
    """used in training VAE"""
    features = {
        "observation": tf.io.FixedLenFeature((64, 64, 3), tf.float32),
        "action": tf.io.FixedLenFeature((3,), tf.float32),
    }
    parsed_features = tf.io.parse_single_example(example_proto, features)
    return parsed_features["observation"], parsed_features["action"]


def parse_latent_stats(example_proto):
    """used in training memory"""
    features = {
        "action": tf.io.FixedLenFeature(
            (
                1000,
                3,
            ),
            tf.float32,
        ),
        "mu": tf.io.FixedLenFeature(
            (
                1000,
                32,
            ),
            tf.float32,
        ),
        "logvar": tf.io.FixedLenFeature(
            (
                1000,
                32,
            ),
            tf.float32,
        ),
    }
    return tf.io.parse_single_example(example_proto, features)


def shuffle_samples(
    parse_func,
    records_list,
    batch_size,
    repeat=None,
    shuffle_buffer=5000,
    num_cpu=8,
):
    """used in vae training"""
    files = tf.data.Dataset.from_tensor_slices(records_list)

    #  get samples from different files
    dataset = files.interleave(
        lambda x: tf.data.TFRecordDataset(x),
        num_parallel_calls=num_cpu,
        cycle_length=num_cpu,
    )
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(parse_func, num_parallel_calls=num_cpu)
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.repeat(repeat).prefetch(1)
    return iter(dataset)


def batch_episodes(parse_func, records, episode_length, num_cpu=4):
    """used in sampling latent stats"""
    files = tf.data.Dataset.from_tensor_slices(records)

    dataset = files.interleave(
        lambda x: tf.data.TFRecordDataset(x),
        num_parallel_calls=num_cpu,
        cycle_length=num_cpu,
        block_length=episode_length,
    )
    dataset = dataset.map(parse_func, num_parallel_calls=num_cpu)
    dataset = dataset.batch(episode_length)
    dataset = dataset.repeat(None)
    return iter(dataset)
```

## The Agent

{{< img
    src="/images/world-models/agent.png"
    caption="The World Models agent"
    width="600"
>}}

The World Models agent is a [Popperian intelligence](https://adgefficiency.com/four-competences/) - able to improve via global selection, respond to reinforcement and to learn models of it's environment.

**The agent has three components - vision, memory and a controller.**

### The Three Components

**The first component is vision - a Variational Autoencoder (VAE) that compresses the environment observation $x$ into a latent space $z$ and then reconstruct it into $x'$.**

The controller doesn't ever use the reconstruction $x'$ - instead it uses the lower dimensional latent representation $z$. This low dimensional, latent representation $z$ is used as one of the controllers two inputs.

**The second component is memory, which uses a Long Short-Term Memory (LSTM) network with a Mixed Density Network (MDN) to predict environment transitions in latent space - to predict $z'$ given $z$ and an action $a$.**

The controller doesn't ever use the prediction $z'$,  but instead the hidden state $h$ of the LSTM. The prediction $z'$ represents only one step in the future - hidden state $h$ contains information many steps into the future, and is the controllers second input.

**The third component is the controller, a linear function that maps the vision latent state $z$ and memory hidden state $h$ to an action $a$.**  The controller parameters are found using an evolutionary algorithm called CMA-ES, with a fitness function of total episode reward.

### The Controller Never Sees the Real World

**The attentive reader will note that the controller never uses the final outputs of the vision or memory** - either for the VAE's reconstructed environment observation or the memory's predicted next latent state.

**The controller never sees the real world directly - instead it only has access to the internal state of the vision and memory**.  These low dimensional representations are all that is used for control.  Using smaller dimension inputs means less parameters in the controller, opening up using an evolutionary method to find the controller parameters.

### The Vision and Memory Never See Rewards

**Both the vision & memory components are trained without access to rewards - they learn only from observations and actions.** Rewards are only used when learning parameters of the controller.

**By training the vision and memory without access to rewards, these components are not required to concurrently learn both representations of the environment and assign credit.**

This allows all three components to focus on one task.  It can however mean that without the context of reward information, the vision & memory might learn features of the environment that are not useful for control.

### Independent Model Learning

**The decomposition of the agent different tasks to be trained separately (but still sequentially):**

- first train the vision on observations
- then train the memory using sequences of observations and actions.  The observations are encoded into latent space $z$ statistics, meaning we can sample a different $z$ each epoch
- finally train the controller, using the vision to provide $z$ and the memory to provide $h$, using total episode reward

**One benefit of independent learning is stability.**  Reinforcement learning is notoriously unstable - by training the vision and memory on a fixed dataset, the training will be more stable than the more common situation in reinforcement learning, where as the policy improves the data distribution changes.

Another factor changing the distribution of the data is exploration.  Whether you learn from a fixed dataset or a non-stationary one, the exploration-exploitation dilemma cannot be ignored.  The fixed dataset will have been generated with a suboptimal policy (if it wasn't, you already have the optimal policy!).

A final benefit of decomposing the training is being able to use the correct hardware for each component.  Both the vision and memory are trained on GPU, with the controller being trained on 64 CPUs.  Being able to spin up earh instance separately helps to keep the

Now that we have been introduced to the agent, we can take a look at each of it's three components in detail - starting with vision.

## Vision

> It's not what you look at that matters, it's what you see - Henry David Thoreau

{{< img
    src="/images/world-models/vae.png"
    caption="The World Models vision"
    width="600"
>}}

The vision of our agent is a generative model, that models the conditional distribution of the environment observation $x$ and a latent representation $z$:

$$z \sim E_{\theta}(z \mid x)$$

### Why Do We Need to See?

**We use vision to understand our environment - our agent does the same.** Here we will see vision as dimensionality reduction - the process of reducing high dimensional data into a lower dimensional space.

**The vision component provides a low dimensional representation of the environment to the controller.**  The value of this representation is that it is easier to make decisions in low dimensional spaces.

A canonical example in computer vision is image classification, where an image can be mapped throughout a convolutional neural network to a predicted class. A business can use that predicted class to make a decision. Another example is the flight or fight response, where visual information is mapped to a binary decision.

In our `car-racing-v0` environment, a low dimensional representation of the environment observation might be something like:

```python
observation = [
	on_road=1,
	corner_to_the_left=1,
	corner_to_the_right=0,
	on_straight=1
]
```

Using this representation, we could imagine deriving a simple control policy.  Try to do this with $27,648$ numbers, even if they are arranged in a shape $(96, 96, 3)$.

Note that we don't know which variables to have in our latent representation. **The latent representation is hidden - it is unobserved**. For a given image, we have no labels for these variables.  We don't know how many there are - or if they even exist at all!

### How Does Our Agent See?

We have a definition of vision as reducing the dimensionality of data, so that we can use it to take actions.  How then does our agent see?

**The vision of the agent reduces the environment observation $x$ $(96, 96, 3)$ into a low dimensional, latent representation $z$ $(32,)$.**

How do we learn this latent representation if we don't have examples? **Our agent uses a Variational Autoencoder**.

### The Variational Autoencoder

**A Variational Autoencoder (VAE) forms the vision of the World Models agent.**

**The VAE is a generative model that learns the data generating process $P(x,z)$ - the joint distribution over our data (the probability of $x$ and $z$ occurring together).**

*If the concept of generative or discriminative models is unfamiliar, take a look at Appendix Two.*

### Context in Generative Modelling

The VAE sits alongside the Generative Adversarial Network (GAN) as the state of the art in generative modelling.

**The progress in GANs has been outstanding.**  GANs typically outperform VAEs on reconstruction quality, with the VAE providing better support over the data (support meaning the number of different values a variable can take).

{{< img
    src="/images/world-models/gan.png"
    caption="Progress in GANS - Adverserial Machine Learning - Ian Goodfellow - ICLR 2019"
    width="600"
>}}

The VAE has less in common with classical (sparse or denoising) autoencoders, which both require the use of the computationally expensive Markov Chain Monte Carlo.

The contributions of the VAE include:
- using variational inference to approximate the latent space $P(z)$
- compression / regularization of the latent space using a Kullback-Leibler Divergence between our learnt latent space and a prior $P(z) = \mathbf{N} (0, 1)$
- stochastic encoding of a sample $x$ into the latent space $z$ and into a reconstruction $x'$

### Why Use a Variational Autoencoder?

A major benefit of generative modelling is the ability to generate new samples $x'$.  Yet our agent never uses $x'$ (the data it generates, whether a reconstruction or a new sample).

**The role of the VAE in our agent is to provide a compressed representation $z$ by learning to encode and decode a latent space**.  This lower dimensional latent space is easier for our memory and controller to work with.

What qualities do we want in our latent space?  **One is meaningful grouping**.  This requirement is a challenge in traditional autoencoders, which tend to learn spread out latent spaces.

Meaningful grouping means that similar observations exist in the same part of the latent space, with samples that are close together in the latent space producing similar images when decoded.  This grouping means that even observations that the agent hadn't seen before could be responded to the same way.

**Meaningful grouping allows interpolation**.  Encoding similar observations close together makes the space between observed data meaningful.

**So how do we get meaningful encoding?** The intuition behind autoencoders is to constrain the size of the latent space ($32$ variables for our agent's VAE).  **The VAE takes this one step further by imposing a Kullback-Leibler Divergence on the latent space** - we will expand on this more below.

### VAE Structure

The VAE is formed of three components - an encoder, a latent space and a decoder.

As the raw data is an image, the VAE makes use of convolution and deconvolution layers.  *If you need a quick refresher on convolution, see Appendix Three.*

### Encoder

**The primary function of the encoder is recognition**.  The encoder is responsible for recognizing and encoding the hidden latent variables.

The encoder is built from convolutional blocks that map from the input image $x$ $(64, 64, 3)$ to statistics (means & variances) of the latent variables ($(64,)$ - 2 statistics per latent space variable).

### Latent Space

**Constraining the size of the latent space to $(32, )$ is one way auto-encoders learn efficient compression of images.**  All of the information needed to reconstruct a sample $x$ must exist in only $32$ numbers!

**The statistics parameterized by the encoder are used to form a distribution over the latent space - a multivariate Gaussian with a diagonal covariance matrix.**  This covariance matrix has zero for all the covariances (meaning that the variables are all independent).

$$\sigma_{\theta} = \begin{bmatrix}\sigma_{\theta,1} & 0 & 0\\0 & \sigma_{\theta,2} & 0\\ 0 & 0 & \sigma_{\theta,3}\end{bmatrix}$$

**This parameterized Gaussian (by weights $\theta$) is an approximation** - using it will limit how expressive our latent space is. **We can sample from this latent space distribution, making the encoding of an image $x$ stochastic.**

$$z \sim P(z \mid x)$$

$$ z \mid x \approx \mathbf{N} \Big(\mu_{\theta}, \sigma_{\theta}\Big) $$

**Ha & Schmidhuber propose that this stochastic encoding promotes a robust controller.** Because the latent space fed to the decoder is spread (controlled by the parameterized variance of the latent space), it learns to decode a range of variations for a given $x$.

### Decoder

**The decoder uses deconvolutional blocks to reconstruct the sampled latent space $z$ into $x'$.**  In the agent, we don't use the reconstruction $x'$ - we are interested in the lower dimensional latent space representation $z$.

### The Three Forward Passes

**Now that we have the structure of the VAE mapped out, we can be specific about how we pass data through the model.**  We have three ways to do this:
- compression of a sample $x$ into a latent representation $z$
- reconstruction of a $x$ into a decoded $x'$
- generation of $x'$ from $z$

### Compression

$x$ -> $z$

- encode an image $x$ into a distribution over a low dimensional latent space
- sample a latent space $z \sim E_{\theta}(z \mid x)$

### Reconstruction

$x$ -> $z$ -> $x'$

- encode an image $x$ into a distribution over a low dimensional latent space
- sample a latent space $z \sim E_{\theta}(z \mid x)$
- decode the sampled latent space into a reconstructed image $x' \sim D_{\theta}(x' \mid z)$

### Generation

$z$ -> $x'$

- sample a latent space $z \sim P(z)$
- decode the sampled latent space into a reconstructed image $x' \sim D_{\theta}(x' \mid z)$

```python
## worldmodels/vision/vae.py


class VAE(tf.keras.Model):
    kl_tolerance = 0.5

    def __init__(self, latent_dim, results_dir, learning_rate=0.0001, load_model=True):
        super().__init__()
        self.latent_dim = latent_dim
        self.optimizer = tf.keras.optimizers.Adam(learning_rate)

        #  the encoder
        self.inference_net = tf.keras.Sequential(
            [
                tf.keras.layers.InputLayer(input_shape=(64, 64, 3)),
                tf.keras.layers.Conv2D(
                    filters=32, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=64, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=128, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=256, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(latent_dim + latent_dim),
            ]
        )

        #  the decoder
        self.generative_net = tf.keras.Sequential(
            [
                tf.keras.layers.InputLayer(input_shape=(latent_dim,)),
                tf.keras.layers.Dense(units=4 * 256, activation=tf.nn.relu),
                tf.keras.layers.Reshape([-1, 1, 4 * 256]),
                tf.keras.layers.Conv2DTranspose(
                    filters=128, kernel_size=5, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=64, kernel_size=5, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=32, kernel_size=6, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=3, kernel_size=6, strides=(2, 2), activation="sigmoid"
                ),
            ]
        )
```

Later in that same file (and in the same class, `VAE`), we have the code for our three forward passes:

```python
## worldmodels/vision/vae.py

    def forward(self, batch):
        """ images to reconstructed """
        means, logvars = self.encode(batch)
        latent = self.reparameterize(means, logvars)
        return self.decode(latent)

    def encode(self, batch):
        """ images to latent statistics """
        mean, logvar = tf.split(
            self.inference_net(batch), num_or_size_splits=2, axis=1
        )
        return mean, logvar

    def reparameterize(self, means, logvars):
        """ latent statistics to latent """
        epsilon = tf.random.normal(shape=means.shape)
        return means + epsilon * tf.exp(logvars * .5)

    def decode(self, latent):
        """ latent to reconstructed """
        return self.generative_net(latent)
```

### The Backward Pass

*This section owes much to the excellent tutorial [What is a variational autoencoder? by Jaan Altosaar](https://jaan.io/what-is-variational-autoencoder-vae-tutorial/).*

Above we mapped out the various forward passes we can do in our VAE.  But before are able to make meaningful forward passes, we need to train the VAE using backwards passes.

**We do backward passes to learn - maximizing the joint likelihood of an image $x$ and the latent space $z$**.

**The VAE uses likelihood maximization to learn this joint distribution $P(x,z)$.**  Likelihood maximization maximizes the similarity between two distributions.  In our case these distributions are over our training data (the data generating process, $P(x,z)$) and our parametrized approximation (a convolutional neural network $E_{\theta}(z \mid x))$.

Let's start with the encoder. We can write the encoder $E_{\theta}$ as model that given an image $x$, is able to sample the latent space $z$.  The encoder is parameterized by weights $\theta$:

$$ z \sim E_{\theta}(z \mid x) $$

The encoder is an approximation of the true posterior $P(z \mid x)$ (the distribution that generated our data).  Bayes Theorem shows us how to decompose the true posterior:

$$P(z \mid x) = \dfrac{P(x \mid z) \cdot P(z)}{P(x)}$$

The challenge here is calculating the posterior probability of the data $P(x)$ - this requires marginalizing out the latent variables. Evaluating this is exponential time:

$$P(x) = \int P(x \mid z) \cdot P(z) \, dz$$

**The VAE sidesteps this expensive computation by approximating the true posterior $P(z \mid x)$ using a diagonal Gaussian:**

$$ x \mid z \sim \mathbf{N} \Big(\mu_{\theta}, \sigma_{\theta}\Big) $$

$$P(x \mid z) \approx E(x \mid z ; \theta) = \mathbf{N} \Big(x \mid \mu_{theta}, \sigma_{\theta}\Big)$$

**This approximation is variational inference - using a family of distributions (in this case Gaussian) to approximate the latent variables**.  This use of variational inference to approximate is a key contribution of the VAE.

Now that we have made a decision about how to approximate the latent space distribution, we want to think about how to bring our parametrized latent space $E_{\theta}(z \mid x)$ closer to the true posterior $P(z \mid x)$.

In order to minimize the difference between our two distributions, we need way to measure the difference.  The VAE uses a Kullback-Leibler divergence ($\mathbf{KLD}$),  which has a number of interpretations - measuring:
- the information lost when using one distribution to approximate another
- the non-symmetric difference between two distributions
- how close distributions are

$$\mathbf{KLD} \Big (E_{\theta}(z \mid x) \mid \mid P(z \mid x) \Big) = \mathbf{E}_{z \sim E_{\theta}} \Big[\log E_{\theta}(z \mid x) \Big] - \mathbf{E}_{z \sim E_{\theta}} \Big[ \log P(x, z) \Big] + \log P(x)$$

This $\mathbf{KLD}$ is something that we can minimize - it is a loss function.  But our exponential time $P(x)$ (in the form of $\log P(x)$) has reappeared!

Now for another trick from the VAE.  We will make use of the Evidence Lower Bound ($\mathbf{ELBO}$) and Jensen's Inequality.  The $\mathbf{ELBO}$ is given as the expected difference in log probabilities when we are sampling our latent vectors from our encoder $E_{\theta}(z \mid x)$:

$$\mathbf{ELBO}(\theta) = \mathbf{E}_{z \sim E_{\theta}} \Big[\log P(x,z) - \log E_{\theta}(z \mid x) \Big]$$

Combining this with our $\mathbf{KLD}$ we can form the following:

$$\log P(x) = \mathbf{ELBO}(\theta) + \mathbf{KLD} \Big (E_{\theta}(z \mid x) \mid \mid P(z \mid x) \Big) $$

A third trick - we know from [Jensen's Inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality#Information_theory) that the $\mathbf{KLD}$ is always non-negative.  Because $\log P(x)$ is constant (and does not depend on our parameters $\theta$), a large $\mathbf{ELBO}$ requires a small $\mathbf{KLD}$ (and vice versa).

**Remember that we have a $\mathbf{KLD}$ we want to minimize!**  We have just shown that we can do this by ELBO maximization.  After a bit more mathematical massaging )) we can arrive at:

$$ \mathbf{ELBO}(\theta) = \mathbf{E}_{z \sim E_{\theta}} \Big[ \log D_{\theta}(x' \mid z) \Big] - \mathbf{KLD} \Big (E_{\theta}(z \mid x) \mid \mid P(z) \Big) $$

Note the appearance of our decoder $D_{\theta}(x \mid z)$.  The decoder is used to approximate the true posterior $P(x' \mid z)$ - the conditional probability distribution over the reconstruction of latent variables into a generated $x'$ (given $x$).

The last step is to convert this $\mathbf{ELBO}$ maximization into a more familiar loss function minimization.

**We now have the VAE loss function's final mathematical form - in all it's tractable glory**:

$$ \mathbf{LOSS}(\theta) = - \mathbf{E}_{z \sim E_{\theta}} \Big[ \log D_{\theta} (x' \mid z) \Big] + \mathbf{KLD} \Big( E_{\theta} (z \mid x) \mid \mid P(z) \Big)  $$

{{< img
    src="/images/world-models/grail.jpg"
    caption="Ich habe es gesehen!"
    width="600"
>}}

Our final loss function has two terms - the log probability of the reconstruction (aka the decoder) and a $\mathbf{KLD}$ between the latent space (sampled from our encoder) and the latent space prior $P(z)$.

The genesis of this loss function is our original maximization the log-likelihood of our data.  It is perfect in it's mathematical expression - yet to implement this in code will require more work.

### Implementing the Loss Function in a Python Program

Although our loss function is in it's final mathematical form, we will make three more modifications before we implement it in code:
- convert the log probability of the decoder into a pixel wise reconstruction loss
- use a closed form solution to the $\mathbf{KLD}$ between our encoded latent space distribution and the prior over our latent space $P(x)$
- refactor the randomness using the reparameterization trick

### First Term - Reconstruction Loss

$$ - \mathbf{E}_{z \sim E_{\theta}} \Big[ \log D_{\theta} (x' \mid z) \Big] $$

The first term in the VAE loss function is the log-likelihood of reconstruction - given latent variables $z$, the distribution over $x'$.  The latent variables are sampled from our encoder (hence the expectation $\mathbf{E}_{z \sim E_{\theta}}$).

**Minimizing the negative log-likelihood is equivalent to likelihood maximization.**  In our case, the likelihood maximization maximizes the similarity between  the distribution over our training data $P(x \mid z)$ and our parametrized approximation.

[Section 5.1 of Deep Learning (Goodfellow, Benjio & Courville)](http://www.deeplearningbook.org/) shows that for a Gaussian approximation, maximizing the log-likelihood is equivalent to minimizing mean square error ($\mathbf{MSE}$):

$$\mathbf{MSE} = \frac{1}{n} \sum \Big[ \mid \mid x' - x \mid \mid \Big]^{2} $$

**This gives us the form of loss function that is often implemented in code - a pixel wise reconstruction loss (also known as the L2 loss):**

$$ \mathbf{E}_{z \sim E_{\theta}} \Big[ \mid \mid x' - x \mid \mid \Big]^{2} $$

```python
## worldmodels/vision/vae.py

reconstruction_loss = tf.reduce_mean(
    tf.reduce_sum(tf.square(batch - generated), axis=[1, 2, 3])
)
```

This is intuitive - this reconstruction loss penalizes the network based on the average squared difference of pixel values.

### Second Term - Regularization

**The second term in the VAE loss function is the $\mathbf{KLD}$ between the and the latent space prior $P(z)$.** The intuition of the second term in the VAE loss function is compression or regularization.

$$ \mathbf{LOSS}(\theta) = - \mathbf{E}_{z \sim E_{\theta}} \Big[ \log D_{\theta} (x' \mid z) \Big] + \mathbf{KLD} \Big( E_{\theta} (z \mid x) \mid \mid P(z) \Big)  $$

We haven't yet specified what the prior over the latent space should be.  A convenient choice is a Gaussian with a mean of zero, variance of one (the Standard Normal).

**Minimizing the $\mathbf{KLD}$ means we are trying to make the latent space look like random noise.**  It encourages putting encodings near the center of the latent space.

**The KL loss term further compresses the latent space.**  This compression means that using a VAE to generate new images requires only sampling from noise!  This ability to sample without input is the definition of a generative model.

Because we are using Gaussians for the encoder $E_{theta}(z \mid x)$ and the latent space prior $ P(z) = \mathbf{N} (0, 1) $, the $\mathbf{KLD}$ has closed form solution ([see Odaibo - Tutorial on the VAE Loss Function](https://arxiv.org/pdf/1907.08956.pdf)).

$$\mathbf{KLD} \Big( E_{\theta} (z \mid x) \mid \mid P(z) \Big) = \frac{1}{2} \Big( 1 + \log(\sigma_{\theta}^{2}) - \sigma_{\theta}^{2} - \mu_{\theta} \Big)$$

This is how the $\mathbf{KLD}$ is implemented in the VAE loss.  Note that we use a clip on the KLD at half the latent space sizein order to balance the two losses:

A note on the use of $\log \sigma^{2}$ - we force our network to learn this by taking the exponential later on in the program:

```python
## worldmodels/vision/vae.py

unclipped_kl_loss = -0.5 * tf.reduce_sum(
    1 + logvars - tf.square(means) - tf.exp(logvars), axis=1
)

kl_loss = tf.reduce_mean(
    tf.maximum(unclipped_kl_loss, self.kl_tolerance * self.latent_dim)
)
```

### Reparameterization Trick

Because our encoder is stochastic, we need one last trick - a rearrangement of the model architecture, so that we can backprop through it.  **This is the reparameterization trick**. It results in a latent space architecture as follows:

$$ n \sim \mathcal{N}(0, 1) $$

$$ z = \sigma_{theta} (x) \cdot n + \mu_{theta} (x) $$

After the refactor of the randomness, we can now pass the gradients from our loss function through the latent space and into the encoder.

### Final VAE Loss Function

A quick summary - first in math:

$$ \mathbf{E}_{z \sim E_{\theta}} \Big[ \mid \mid x' - x \mid \mid \Big]^{2} $$

$$ \mathbf{LOSS}(\theta) = - \mathbf{E}_{z \sim E_{\theta}} \Big[ \log D_{\theta} (x' \mid z) \Big] + \mathbf{KLD} \Big( E_{\theta} (z \mid x) \mid \mid P(z) \Big)  $$

And in code:

```python
## worldmodels/vision/vae.py


def loss(self, batch):
    """batch to loss"""
    means, logvars = self.encode(batch)
    latent = self.reparameterize(means, logvars)
    generated = self.decode(latent)

    reconstruction_loss = tf.reduce_mean(
        tf.reduce_sum(tf.square(batch - generated), axis=[1, 2, 3])
    )

    unclipped_kl_loss = -0.5 * tf.reduce_sum(
        1 + logvars - tf.square(means) - tf.exp(logvars), axis=1
    )

    kl_loss = tf.reduce_mean(
        tf.maximum(unclipped_kl_loss, self.kl_tolerance * self.latent_dim)
    )
    return {
        "reconstruction-loss": reconstruction_loss,
        "unclipped-kl-loss": unclipped_kl_loss,
        "kl-loss": kl_loss,
    }
```

Below a few artifacts from the training the VAE, which was done on GPU:

{{< img
    src="/images/world-models/vae-training.png"
    caption="Training curve of the first iteration VAE over 8 epochs. You can clearly see the effect of the `kl_tolerance=16` in the second plot."
    width="600"
>}}

{{< img
    src="/images/world-models/vae-reconstructions.png"
    caption="Observations (`true`) and their reconstructions (`recon`) from the final VAE, along with the reconstruction loss and KLD loss"
    width="600"
>}}

{{< img
    src="/images/world-models/vae-noise.png"
    caption="Images reconstructed from sampling the latent space prior $z \sim \mathbf{N} (0, 1)$"
    width="600"
>}}

### Implementing the Vision in Code

Below the code for the vision component, see the source in ([world-models/vision](https://github.com/ADGEfficiency/world-models/blob/master/worldmodels/vision)).

```python
## worldmodels/vision/train_vae.py
import argparse
import os

import tensorflow as tf

from worldmodels import setup_logging
from worldmodels.data.tf_records import parse_episode, shuffle_samples
from worldmodels.params import vae_params, results_dir
from worldmodels.vision.vae import VAE
from worldmodels.vision.images import compare_images, generate_images, generate_gif
from worldmodels.utils import calc_batch_per_epoch, list_records, make_directories


def train(model, records, epochs, batch_size, log_every, save_every):
    logger = setup_logging(os.path.join(results_dir, "training.csv"))
    logger.info("epoch, batch, reconstruction-loss, kl-loss")

    dataset = shuffle_samples(parse_episode, records, batch_size)
    sample_observations = next(dataset)[0]

    sample_observations = sample_observations.numpy()[:4]
    sample_latent = tf.random.normal(shape=(4, model.latent_dim))

    epochs, batch_size, batch_per_epoch = calc_batch_per_epoch(
        epochs=epochs, batch_size=batch_size, records=records, samples_per_record=1000
    )

    image_dir = os.path.join(results_dir, "images")
    for epoch in range(epochs):
        generate_images(model, epoch, 0, sample_latent, image_dir)

        for batch_num in range(batch_per_epoch):
            batch, _ = next(dataset)
            losses = model.backward(batch)

            msg = "{}, {}, {}, {}".format(
                epoch,
                batch_num,
                losses["reconstruction-loss"].numpy(),
                losses["kl-loss"].numpy(),
            )
            logger.info(msg)

            if batch_num % log_every == 0:
                print(msg)

            if batch_num % save_every == 0:
                model.save(results_dir)
                generate_images(model, epoch, batch_num, sample_latent, image_dir)
                compare_images(model, sample_observations, results_dir)
                generate_gif(image_dir, results_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--load_model", default=1, nargs="?")
    parser.add_argument("--log_every", default=100, nargs="?")
    parser.add_argument("--save_every", default=1000, nargs="?")
    parser.add_argument("--epochs", default=10, nargs="?")
    parser.add_argument("--data", default="local", nargs="?")
    parser.add_argument("--dataset", default="random-rollouts", nargs="?")
    args = parser.parse_args()

    make_directories("vae-training/images")
    results_dir = os.path.join(results_dir, "vae-training")

    if args.dataset == "random":
        records = list_records(
            path="random-rollouts", contains="episode", data=args.data
        )

    else:
        records = list_records(
            path="controller-rollouts", contains="episode", data=args.data
        )

    vae_params["load_model"] = bool(int(args.load_model))
    model = VAE(**vae_params)

    training_params = {
        "model": model,
        "epochs": int(args.epochs),
        "batch_size": 256,
        "log_every": int(args.log_every),  # batches
        "save_every": int(args.save_every),  # batches
        "records": records,
    }

    print("cli")
    print("------")
    print(args)
    print("")

    print("training params")
    print("------")
    print(training_params)
    print("")

    print("vision params")
    print("------")
    print(vae_params)
    print("")

    train(**training_params)
```

The code for the VAE structure:

```python
## worldmodels/vision/vae.py
import os

import tensorflow as tf


class VAE(tf.keras.Model):
    kl_tolerance = 0.5

    def __init__(self, latent_dim, results_dir, learning_rate=0.0001, load_model=True):
        super().__init__()
        self.latent_dim = latent_dim
        self.optimizer = tf.keras.optimizers.Adam(learning_rate)

        #  the encoder
        self.inference_net = tf.keras.Sequential(
            [
                tf.keras.layers.InputLayer(input_shape=(64, 64, 3)),
                tf.keras.layers.Conv2D(
                    filters=32, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=64, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=128, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2D(
                    filters=256, kernel_size=4, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(latent_dim + latent_dim),
            ]
        )

        #  the decoder
        self.generative_net = tf.keras.Sequential(
            [
                tf.keras.layers.InputLayer(input_shape=(latent_dim,)),
                tf.keras.layers.Dense(units=4 * 256, activation=tf.nn.relu),
                tf.keras.layers.Reshape([-1, 1, 4 * 256]),
                tf.keras.layers.Conv2DTranspose(
                    filters=128, kernel_size=5, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=64, kernel_size=5, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=32, kernel_size=6, strides=(2, 2), activation="relu"
                ),
                tf.keras.layers.Conv2DTranspose(
                    filters=3, kernel_size=6, strides=(2, 2), activation="sigmoid"
                ),
            ]
        )

        self.models = {
            "inference": self.inference_net,
            "generative": self.generative_net,
        }

        if load_model:
            self.load(results_dir)

    def save(self, filepath):
        """only model weights"""
        filepath = os.path.join(filepath, "models")
        os.makedirs(filepath, exist_ok=True)
        print("saving model to {}".format(filepath))

        for name, model in self.models.items():
            model.save_weights("{}/{}.h5".format(filepath, name))

    def load(self, filepath):
        """only model weights"""
        filepath = os.path.join(filepath, "models")
        print("loading model from {}".format(filepath))

        for name, model in self.models.items():
            model.load_weights("{}/{}.h5".format(filepath, name))
            self.models[name] = model

    def forward(self, batch):
        """images to reconstructed"""
        means, logvars = self.encode(batch)
        latent = self.reparameterize(means, logvars)
        return self.decode(latent)

    def encode(self, batch):
        """images to latent statistics"""
        mean, logvar = tf.split(self.inference_net(batch), num_or_size_splits=2, axis=1)
        return mean, logvar

    def reparameterize(self, means, logvars):
        """latent statistics to latent"""
        epsilon = tf.random.normal(shape=means.shape)
        return means + epsilon * tf.exp(logvars * 0.5)

    def decode(self, latent):
        """latent to reconstructed"""
        return self.generative_net(latent)

    def loss(self, batch):
        """batch to loss"""
        means, logvars = self.encode(batch)
        latent = self.reparameterize(means, logvars)
        generated = self.decode(latent)

        reconstruction_loss = tf.reduce_mean(
            tf.reduce_sum(tf.square(batch - generated), axis=[1, 2, 3])
        )

        unclipped_kl_loss = -0.5 * tf.reduce_sum(
            1 + logvars - tf.square(means) - tf.exp(logvars), axis=1
        )

        kl_loss = tf.reduce_mean(
            tf.maximum(unclipped_kl_loss, self.kl_tolerance * self.latent_dim)
        )
        return {
            "reconstruction-loss": reconstruction_loss,
            "unclipped-kl-loss": unclipped_kl_loss,
            "kl-loss": kl_loss,
        }

    def backward(self, batch):
        """images to loss to new weights"""
        with tf.GradientTape() as tape:
            losses = self.loss(batch)
            gradients = tape.gradient(sum(losses.values()), self.trainable_variables)

        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))
        return losses
```

## Memory

> Prediction is very difficult, especially if it's about the future - Nils Bohr

{{< img
    src="/images/world-models/memory.png"
    caption="The World Models memory - the latent space `z` and last action `a` are used to predict the next latent state `z'`"
    width="600"
>}}

The memory is the second of our agent's three components. **The memory predicts how the environment will respond to its actions.**  This prediction is not done in the high dimensional space $x$, but instead in the lower dimensional latent space $z$ learnt by the vision component.

The memory is a discriminative model, that models the conditional probability of seeing an environment transition in latent space (from $z$ to $z'$) conditional on an action $a$:

$$ M_{\theta}(z'| z, a, h, c) $$

The memory is predicting how the environment will change based on the last action it took.  As with the vision component, the final output of the memory (the predicted next environment latent representation $z'$) is not used by the controller.

**Instead, the controller makes use of an internal representation learnt by the memory - the hidden state $h$ of an LSTM**.  This internal representation is a compressed representation of time - a compressed representation of what the memory has learnt is useful to predict the future.

### Why Do We Remember?

Some think that the entire purpose of a human life is to generate memories, to be looked back on after a life well lived.  Human memory is fantastic in it's ability to recall details (such as lyrics of a tune heard long ago), while also being able to completely misremember recent events.

There is a fascinating intersection between memory and identity, with misremembering twisting towards being consistent with an established self image.  Certainly perfect recall is not ideal (or efficient) - yet misremembering to align with a self image is somewhat troubling.  What of our well lived life that we love to look back on?

All that in mind, the value of memory to our agent is to learn from experience. **One way to learn from past experience is to use it to predict the future**.

### Mixed Density Networks

**The memory has two components - an LSTM and a Gaussian Mixture head - together these form a Mixed Density Network**.  Mixed Density Networks were introduced in 1994 by Christopher Bishop (author of the classic *Pattern Recognition and Machine Learning*).

A Mixed Density Network combines a neural network (that can represent arbitrary non-linear functions) with a mixture model (that can model arbitrary conditional distributions).

**A primary motivation of Mixed Density Networks is to learn multimodal distributions**. Many distributions we are interested in are multimodal, with multiple peaks in probability density.

We saw above in the derivation of the VAE loss function, that if we make the assumption of Gaussian distributed data, we can derive the mean square error loss function from likelihood maximization.  This loss function leads to learning of the conditional average of the target.

Learning the conditional average can be useful, but also has drawbacks.  **For multimodal data, taking the average is unlikely to be informative**.  An example is Nassim Taleb's 3 foot deep river, which demonstrates how misleading the average can be.

{{< img
    src="/images/world-models/4ft.png"
    caption="The Flaw of Averages - Sam L. Savage"
    width="600"
>}}

### Gaussian Mixtures

In the 1994 paper *Mixture Density Networks*, Bishop shows that by training a neural network using a least squares loss function, we are able to learn two statistics.

One is the conditional mean, which is our prediction.  The second statistic is the variance, which we can approximate from the residual.  **We can use these two statistics to form a Gaussian**.

Being able to learn both the mean and variance motivates the parametrization of a mixture model with Gaussian kernels.  A mixture model is a linear combination of kernel functions:

$$ P(z' \mid z) = \sum_{mixes} \alpha(z) \cdot \phi(z' \mid z) $$

Where $\alpha$ are mixing coefficients, and $\phi$ is a conditional probability density.  Our kernel of choice is the Gaussian, which has a probability density function:

$$ \phi (z' \mid z, a) = \frac{1}{\sqrt{(2 \pi) \sigma(z, a)}} \exp \Bigg[ - \frac{\lVert z' - \mu(z, a) \rVert^{2}}{2 \sigma(z, a)^{2}} \Bigg] $$

The cool thing about Gaussian mixtures is their ability to approximate complex probability densities using Gaussian's with a diagonal covariance matrix.

**Any probability distribution can be approximated with a mixture of Gaussians.**

The flexibility is similar to a feed forward neural network (see the [Universal approximation theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem)), and likely has the same distinction between being able to approximate in theory versus being able to learn with our data.

In practice, the mixture probabilities are parameterized as $\log \pi$, recovering the probabilities by taking the exponential.  These probabilities are priors of the target having been generated by a mixture component.  These are transformed via a softmax:

$$ \pi = \frac {\exp (\pi)}{\sum exp(\pi)} $$

Meaning our mixture probabilities satisfy the constraint:

$$ \sum_{mixes} \pi(z, a) = 1 $$

As with the Variational Autoencoder, the memory $\theta$ parameters are found using likelihood maximization.

$$ M(z' \mid z, a) = \sum_{mixes} \alpha(z, a) \cdot \phi (z'| z, a) $$

$$ \mathbf{LOSS} = - \log M(z' \mid z, a)$$

$$ \mathbf{LOSS} = - \log  \sum_{mixes} \alpha(z, a) \cdot \phi (z'| z, a) $$

**In a more general setting, the variances learnt by a Gaussian mixture can be used as a measure of uncertainty.**

A mixture model requires statistics (probabilities, means and variances) as input.  In the World Models memory, these statistics are supplied by a long short-term memory (LSTM) network.  (*If the LSTM is unfamiliar, take a look at Appendix Four*).

### Implementing the Memory in Python

The reimplementation memory is built in a way that the Gaussian mixture can be tested separately from the LSTM, using a simpler feedforward neural network feeding the mixture statistics.

From a software development perspective, development of the `Memory` class was done in two distinct approaches.

### Performance Based Testing

The first was testing the generalization of the MDN on a toy dataset.  The inspiration and dataset came directly from [Mixture Density Networks with TensorFlow by David Ha](http://blog.otoro.net/2015/11/24/mixture-density-networks-with-tensorflow/). It is in Tensorflow 1.0, which required updating to Tensorflow 2.0.  You can see the notebook I used to develop the MDN + LSTM at [world-models/notebooks/memory-quality-check.ipynb](https://github.com/ADGEfficiency/world-models/blob/master/notebooks/memory-quality-check.ipynb).

The next test was with an LSTM generating the statistics of the mixture:

{{< img
    src="/images/world-models/mdn-test2.png"
    caption="Training curve for the memory for Agent Four (40 epochs)"
    width="600"
>}}

### Unit Testing

The performance based testing was combined with lower level unit style testing (the tests are still within the notebooks).  You can see the notebook I used to develop the MDN + LSTM at [worldmodels/notebooks/Gaussian-mix-kernel-check.ipynb](https://github.com/ADGEfficiency/world-models/blob/master/notebooks/Gaussian-mix-kernel-check.ipynb) - a short snippet is below:

```python
## worldmodels/notebooks/Gaussian-mix-kernel-check.ipynb
import math
import numpy as np
import tensorflow as tf
from tensorflow_probability import distributions as tfd

sample = 0.0
mu = 0.0
sig = 0.1

nor = tfd.Normal(loc=mu, scale=sig)
nor.prob(sample)
## <tf.Tensor: id=124, shape=(), dtype=float32, numpy=3.989423>

constant = 1 / math.sqrt(2 * math.pi)
gaussian_kernel = np.subtract(sample, mu)
gaussian_kernel = tf.square(tf.divide(gaussian_kernel, sig))
gaussian_kernel = -1 / 2 * gaussian_kernel
tf.divide(tf.exp(gaussian_kernel), sig) * constant
## <tf.Tensor: id=133, shape=(), dtype=float64, numpy=3.989422804014327>
```

{{< img
    src="/images/world-models/memory-training.png"
    caption="Training curve for the memory for Agent Four (40 epochs)"
    width="600"
>}}

Below the code for the memory component, see the source in ([world-models/memory](https://github.com/ADGEfficiency/world-models/blob/master/worldmodels/memory)).

```python
# worldmodels/memory/train_memory.py
import argparse
import os

import numpy as np
import tensorflow as tf

from worldmodels.data.tf_records import shuffle_samples, parse_latent_stats
from worldmodels.memory.memory import Memory
from worldmodels.params import memory_params, home

from worldmodels.utils import calc_batch_per_epoch, list_records, make_directories
from worldmodels import setup_logging


def train(model, records, epochs, batch_size, batch_per_epoch, save_every):
    logger = setup_logging(os.path.join(results_dir, "training.csv"))
    logger.info("epoch, batch, loss")

    dataset = shuffle_samples(
        parse_latent_stats,
        records,
        batch_size=batch_size,
        shuffle_buffer=500,
        num_cpu=8,
    )

    for epoch in range(epochs):
        batch_loss = np.zeros(batch_per_epoch)
        for batch_num in range(batch_per_epoch):
            batch = next(dataset)
            mu = batch["mu"]
            logvars = batch["logvar"]
            action = batch["action"]

            epsilon = tf.random.normal(shape=mu.shape)
            z = mu + epsilon * tf.exp(logvars * 0.5)

            x = tf.concat((z[:, :-1, :], action[:, :-1, :]), axis=2)

            y = z[:, 1:, :]

            assert x.shape[0] == y.shape[0]
            assert y.shape[1] == 999
            assert x.shape[2] == 35
            assert y.shape[2] == 32
            state = model.lstm.get_zero_hidden_state(x)

            batch_loss[batch_num] = model.train_op(x, y, state)

            msg = "{}, {}, {}".format(epoch, batch_num, batch_loss[batch_num])
            logger.info(msg)

            if batch_num % save_every == 0:
                model.save(results_dir)

        model.save(results_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--load_model", default=0, nargs="?")
    parser.add_argument("--data", default="local", nargs="?")
    parser.add_argument("--cpu", default=8, nargs="?")
    parser.add_argument("--epochs", default=40, nargs="?")  # paper says 40
    args = parser.parse_args()

    make_directories("memory-training/models")
    records = list_records("latent-stats", "episode", args.data)

    results_dir = os.path.join(home, "memory-training")
    epochs, batch_size, batch_per_epoch = calc_batch_per_epoch(
        epochs=memory_params["epochs"],
        batch_size=memory_params["batch_size"],
        records=records,
    )

    memory_params["batch_per_epoch"] = batch_per_epoch
    memory_params["load_model"] = bool(int(args.load_model))
    model = Memory(**memory_params)

    training_params = {
        "records": records,
        "model": model,
        "epochs": args.epochs,
        "batch_size": batch_size,
        "batch_per_epoch": batch_per_epoch,
        "save_every": 20,  # batches
    }

    print("cli")
    print("------")
    print(args)
    print("")

    print("training params")
    print("------")
    print(training_params)
    print("")

    print("memory params")
    print("------")
    print(memory_params)
    print("")

    train(**training_params)
```


```python
# worldmodels/memory/memory.py

import math
import os

import numpy as np
import tensorflow as tf


def get_pi_idx(pis, threshold):
    """Samples the probabilities of each mixture"""
    if threshold is None:
        threshold = np.random.rand(1)

    pdf = 0.0
    #  one sample, one timestep
    for idx, prob in enumerate(pis):
        pdf += prob
        if pdf > threshold:
            return idx

    #  if we get to this point, something is wrong!
    print("pdf {} thresh {}".format(pdf, threshold))
    return idx


class MLP(tf.keras.Model):
    """used for testing only"""

    def __init__(self, num_mix, hidden_nodes):
        super().__init__()
        self.perceptron = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(
                    24,
                    dtype="float32",
                    activation="tanh",
                    kernel_initializer=tf.initializers.RandomNormal(stddev=0.5),
                ),
                tf.keras.layers.Dense(num_mix * 3, dtype="float32"),
            ]
        )

    def __call__(self, input_tensor):
        return self.perceptron(input_tensor)


class LSTM:
    """car racing defaults"""

    def __init__(self, input_dim, output_dim, num_timesteps, batch_size, nodes):
        self.input_dim = input_dim
        self.nodes = nodes
        self.batch_size = batch_size

        input_layer = tf.keras.Input(
            shape=(num_timesteps, input_dim), batch_size=batch_size
        )

        cell = tf.keras.layers.LSTMCell(
            nodes,
            kernel_initializer="glorot_uniform",
            recurrent_initializer="glorot_uniform",
            bias_initializer="zeros",
        )

        self.lstm = tf.keras.layers.RNN(
            cell, return_state=True, return_sequences=True, stateful=False
        )

        lstm_out, hidden_state, cell_state = self.lstm(input_layer)
        output = tf.keras.layers.Dense(output_dim)(lstm_out)

        self.net = tf.keras.Model(
            inputs=input_layer, outputs=[output, hidden_state, cell_state]
        )

    def get_zero_hidden_state(self, inputs):
        #  inputs dont matter here - but batch size does!
        return [
            tf.zeros((inputs.shape[0], self.nodes)),
            tf.zeros((inputs.shape[0], self.nodes)),
        ]

    def get_initial_state(self, inputs):
        return self.initial_state

    def __call__(self, inputs, state):
        self.initial_state = state
        self.lstm.get_initial_state = self.get_initial_state
        return self.net(inputs)


class GaussianMixture(tf.keras.Model):
    def __init__(self, num_features, num_mix, num_timesteps, batch_size):
        self.num_mix = num_mix

        #  (batch_size, num_timesteps, output_dim * num_mix * 3)
        #  3 = one pi, mu, sigma for each mixture
        mixture_dim = num_features * num_mix * 3

        input_layer = tf.keras.Input(
            shape=(num_timesteps, mixture_dim), batch_size=batch_size
        )

        #  (batch, time, num_features, num_mix * 3)
        expand = tf.reshape(input_layer, (-1, num_timesteps, num_features, num_mix * 3))

        #  (batch, time, num_features, num_mix)
        pi, mu, sigma = tf.split(expand, 3, axis=3)

        #  softmax the pi's (alpha in Bishop 1994)
        pi = tf.exp(tf.subtract(tf.reduce_max(pi, 3, keepdims=True), pi))
        pi = tf.divide(pi, tf.reduce_sum(pi, 3, keepdims=True))

        sigma = tf.maximum(sigma, 1e-8)
        sigma = tf.exp(sigma)

        super().__init__(inputs=[input_layer], outputs=[pi, mu, sigma])

    def kernel_probs(self, mu, sigma, next_latent):
        constant = 1 / math.sqrt(2 * math.pi)

        #  mu.shape
        #  (batch_size, num_timesteps, num_features, num_mix)

        #  next_latent.shape
        #  (batch_size, num_timesteps, num_features)
        #  -> (batch_size, num_timesteps, num_features, num_mix)
        next_latent = tf.expand_dims(next_latent, axis=-1)
        next_latent = tf.tile(next_latent, (1, 1, 1, self.num_mix))

        gaussian_kernel = tf.subtract(next_latent, mu)
        gaussian_kernel = tf.square(tf.divide(gaussian_kernel, sigma))
        gaussian_kernel = -1 / 2 * gaussian_kernel
        conditional_probabilities = tf.divide(tf.exp(gaussian_kernel), sigma) * constant

        #  (batch_size, num_timesteps, num_features, num_mix)
        return conditional_probabilities

    def get_loss(self, mixture, next_latent):
        pi, mu, sigma = self(mixture)
        probs = self.kernel_probs(mu, sigma, next_latent)
        loss = tf.multiply(probs, pi)

        #  reduce along the mixes
        loss = tf.reduce_sum(loss, 3, keepdims=True)
        loss = -tf.math.log(loss)
        loss = tf.reduce_mean(loss)
        return loss


class Memory:
    """initializes LSTM and Mixture models"""

    def __init__(
        self,
        input_dim=35,
        output_dim=32,
        num_timesteps=999,
        batch_size=100,
        lstm_nodes=256,
        num_mix=5,
        grad_clip=1.0,
        initial_learning_rate=0.001,
        end_learning_rate=0.00001,
        epochs=1,
        batch_per_epoch=1,
        load_model=False,
        results_dir=None,
    ):
        decay_steps = epochs * batch_per_epoch
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.batch_size = batch_size

        mixture_dim = output_dim * num_mix * 3

        self.lstm = LSTM(input_dim, mixture_dim, num_timesteps, batch_size, lstm_nodes)

        self.mixture = GaussianMixture(output_dim, num_mix, num_timesteps, batch_size)

        learning_rate = tf.keras.optimizers.schedules.PolynomialDecay(
            initial_learning_rate=initial_learning_rate,
            decay_steps=decay_steps,
            end_learning_rate=end_learning_rate,
        )

        self.optimizer = tf.keras.optimizers.Adam(learning_rate, clipvalue=grad_clip)

        self.models = {"lstm": self.lstm.net, "gaussian-mix": self.mixture}

        if load_model:
            self.load(results_dir)

    def save(self, filepath):
        """only model weights"""
        filepath = os.path.join(filepath, "models")
        os.makedirs(filepath, exist_ok=True)
        print("saving model to {}".format(filepath))
        for name, model in self.models.items():
            model.save_weights("{}/{}.h5".format(filepath, name))

    def load(self, filepath):
        """only model weights"""
        filepath = os.path.join(filepath, "models")
        print("loading model from {}".format(filepath))

        for name, model in self.models.items():
            model.load_weights("{}/{}.h5".format(filepath, name))
            self.models[name] = model

    def __call__(self, x, state, temperature, threshold=None):
        """
        forward pass

        hardcoded for a single step - because we want to pass state
        inbetween
        """
        x = tf.reshape(x, (1, 1, self.input_dim))
        assert x.shape[0] == 1

        temperature = np.array(temperature).reshape(1, 1)
        assert temperature.shape[0] == x.shape[0]

        mixture, h_state, c_state = self.lstm(x, state)

        pi, mu, sigma = self.mixture(mixture)  # , temperature

        #  single sample, single timtestep
        pi = np.array(pi).reshape(self.output_dim, pi.shape[3])
        mu = np.array(mu).reshape(self.output_dim, mu.shape[3])
        sigma = np.array(sigma).reshape(self.output_dim, sigma.shape[3])

        #  reset every forward pass
        idxs = np.zeros(self.output_dim)
        mus = np.zeros(self.output_dim)
        sigmas = np.zeros(self.output_dim)
        y = np.zeros(self.output_dim)

        for num in range(self.output_dim):
            idx = get_pi_idx(pi[num, :], threshold=threshold)

            idxs[num] = idx
            mus[num] = mu[num, idx]
            sigmas[num] = sigma[num, idx]

            y[num] = mus[num] + np.random.randn() * sigmas[num] * np.sqrt(temperature)

        #  check no zeros in pis
        assert sum(idxs) > 0

        return y, h_state, c_state

    def train_op(self, x, y, state):
        """backward pass"""
        with tf.GradientTape() as tape:
            out, _, _ = self.lstm(x, state)
            loss = self.mixture.get_loss(out, y)
            gradients = tape.gradient(loss, self.lstm.net.trainable_variables)

        self.optimizer.apply_gradients(
            zip(gradients, self.lstm.net.trainable_variables)
        )
        return loss
```


## Control

> Never let the future disturb you. You will meet it, if you have to, with the same weapons of reason which today arm you against the present - Marcus Aurelius

The final component of our agent is the controller.  **The controller is a learner and a decision maker**.  It has two roles - to make decisions, and to learn to make better decisions.  Balancing well between these two means our agent has made an effective trade off between exploitation of it's current knowledge with the need to explore the unknown.

The controller uses the compressed representations of the current $z$ and future environment $h$, provided by the vision and memory components, to select the next action $a$:

$$ C_{\theta}(a \mid z, h) $$

The controller uses a linear function to map from these compressed representations ($z$ and $h$) to an action $a$.  These representations were learnt without access to rewards.

The controller learns the parameters of this linear function that maximize the expected reward of our agent in the `Car-Racing-v0` environment.  This is an optimization problem.

The algorithm used by the agent for finding these parameters is Covariance Matrix Adaptation Evolution Strategy (CMA-ES).

### Why Do We Need Control?

Decision making requires a goal. In a Markov Decision Process, the goal is to take actions that maximize expected reward.

**To maximize expected reward an agent must perform credit assignment** - determining which actions lead to reward. An agent that understands how to assign credit can take good actions.

**In reinforcement learning, this credit assignment is often learnt by a function that also learns other tasks, such as learning a low dimensional representation of a high dimensional image.**  An example is DQN, the action-value function learns to both extract features from the observation and map them to an action.

**In the agent these tasks are kept separate, with vision responsible for learning a spatial representation and the memory learning a temporal representation.**  This separation allows the use of a simple linear controller, completely dedicated to learning how to assign credit.

Both of these compressed representations are learnt without access to rewards.  It is only the controller that has access to the reward signal, in the form of total episode reward.

**Having a simple, low parameter count controller opens up less sample efficient but more general methods for finding the model parameters.**  The downside of this is that our vision and memory might use capacity to learn features that are not useful for control, or not learn features that are useful.

### How the Agent Controls

The agent controls using all three of it's components.  The vision takes the environment observation $x$ and encodes it into a latent representation $z$.  The memory uses the latent representation of the environment and the last action $a$ to predict $z'$, updating it's hidden state $h$ in the process.

The controller takes the latent representation on the current environment observation $z$ and the memory LSTM hidden state $h$ and maps to an action $a$.

The question is how we find good parameters for our linear controller. For MDPs, reinforcement learning is a common choice.  However, our low parameter count ($784$ parameters) controller opens up more options - the one chosen by the agent chooses an evolutionary algorithm called CMA-ES.  Before we dive into the details of computational evolution and CMA-ES, we will consider evolution.

### Evolution

[Evolution is an example of Darwinian competence](https://adgefficiency.com/four-competences/), with agents that don't learn within their lifetime.  From a computational perspective, this means that the controller parameters are fixed within each generation.

**Evolution is the driving force in our universe.**  At the heart of evolution is a paradox - failure at a low level leading to improvement at a high level.  Examples include biology, business, training neural networks and personal development.

**Evolution is iterative improvement using a generate, test, select loop:**
- in the **generate** step a population is generated, using information from previous steps
- in the **test** step, the population interacts with the environment, and is assigned a single number as a score
- in the **select** step, members of the current generation are selected (based on their fitness) to be used to generate the next step

There is so much to learn from this evolutionary process:
- failure at a low level driving improvement at a higher level
- the effectiveness of iterative improvement
- the requirement of a dualistic (agent and environment) view


We now have an understanding of the general process of evolutionary learning.  Let's look at how we do this *in silico*.

### Computational Evolution

**Computational evolutionary algorithms are inspired by biological evolution.**  They perform non-linear, non-convex and gradient free optimization.  Evolutionary methods can deal with the challenges that discontinuities, noise, outliers and local optima pose in optimization.

Computational evolutionary algorithms are often the successive process of sampling parameters of a function (i.e. a neural network) from a distribution.  This process can be further extended by other biologically inspired mechanics, such as crossover or mutation - known as genetic algorithms.

**A common Python API for computation evolution is the ask, evaluate and tell loop**.  This can be directly mapped onto the generate, test & select loop introduced above:

```python
for population in range(populations):
    #  generate
    parameters = solver.ask()
    #  test
    fitness = environment.evaluate(parameters)
    #  select
    solver.tell(parameters, fitness)
```

From a practical standpoint, the most important features of computational evolutionary methods are:
- general purpose optimization that can handle noisy, ill-conditioned, non-linear problems
- poor sample efficiency, due to learning from a weak signal (total episode reward)
- parallelizable, due to the rollouts of each population member being independent of the other population members
- invariant to monotonic transformations of the fitness - only the ranks matter

### General Purpose Optimization

**Evolutionary algorithms learn from a single number per generation - the total episode reward.**  This single number serves as a measurement of a population's fitness.

This is why evolutionary algorithms are **black box** - unlike less general optimizers they don't learn from the temporal structure of the MDP.  They are also gradient free.

**This black box approach, combined with a reliance on random search, allows evolutionary methods to be robust in challenging search spaces.**  They can handle problems that other, more complex optimization methods struggle with, such as discontinuities, local optima and noise.

### Sample Inefficiency

**The cost of having a more general purpose learning method is sample efficiency.** By not exploiting information such as the temporal structure of an episode, or gradients, evolutionary methods must rely on lots of sampling to learn.

How sample efficient an algorithm is depends on how much experience (measured in transition between states in an MDP) an algorithm needs to achieve a given level of performance.  It is of key concern if compute is purchased on a variable cost basis.

The inherit sample inefficiency of evolutionary algorithms is counteracted by requiring less computation per episode (i.e. no gradient updates inbetween transitions) and being able to parallelize rollouts.

### Parallel Rollouts

**A key feature of Darwinian learning is fixed competence, with population members not learning within lifetime.**  This feature means that each population member can learn independently, and hence be parallelized.  This is a major benefit of evolutionary methods, which helps to counteract their sample inefficiency.

### $(1, \lambda)$-ES

[A Visual Guide to Evolution Strategies - David Ha](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/)

I hadn't worked with evolutionary algorithms before this project.  Due to possessing a simple mind that relies heavily on empirical understanding, I often find implementing algorithms a requirement for understanding.

The simplest evolution strategy (ES) is $(1, \lambda)$-ES.  This basic algorithm involves sampling a population of parameters from a multivariate Gaussian, using the best performing member of the previous generation as the mean and a fixed, identity covariance matrix.

I implemented $(1, \lambda)$-ES and a wrapper around `pycma` in a separate repo [ADGEfficiency/evolution](https://github.com/ADGEfficiency/evolution) - refer to the repo for more on the algorithms and optimization problems implemented.  Below is the performance of $(1, \lambda)$-ES on the simple `Sphere` optimization problem:

{{< img
    src="/images/world-models/sphere-simple-solver.gif"
    caption=""
    width="600"
>}}

Mutation of the population between generations is controlled by two mechanisms.  The first is the selection, which in the case of $(1, \lambda)$-ES is only the most elite set of parameters.  The second is the covariance matrix used when sampling the next generation.  Using an identity matrix means that even as our population improves, the next generation will still be spread with the same variance.

More advanced evolutionary algorithms take control of the covariance matrix. If we increase the number of elite parameters we select, we can estimate a covariance matrix from the previous generation's elite parameters.  A step further is for the algorithm to adapt and control how the covariance changes from generation to generation.

The evolutionary algorithm the agent uses performs this kind of covariance matrix adaptation.  **The algorithm is CMA-ES**.

### CMA-ES

*This section was heavily influenced by the excellent [Hansen (2016) The CMA Evolution Strategy: A Tutorial](https://arxiv.org/pdf/1604.00772.pdf)*.

The Covariance Matrix Adapation Evolutionary Strategy (CMA-ES) is the algorithm used by our agent to find parameters of it's linear controller.

{{< img
    src="/images/world-models/sphere-pycma.gif"
    caption=""
    width="600"
>}}


A key feature of CMA-ES is the successive estimation of a full covariance matrix.  **Unlike the algorithms we have discussed above, CMA-ES approximates a full covariance matrix of our parameter space**. This means that we model the pairwise dependencies between parameters - how one parameter changes with another.

This is different to the multivariate Gaussians we parameterized in the vision and memory components.  These have diagonal covariances, which mean each variable changes independently of the other variables.

If you are wondering whether CMA-ES could be useful for your control problem, David Ha suggests that CMA-ES is effective for up to 10k parameters, as the covariance matrix calculation is $O(n^{2})$.

We can describe CMA-ES in the context of the generate, test and select loop that defines evolutionary learning.

### Generate

The generation step involves sampling a population from a multivariate Gaussian, parameterized by a mean $\mu$ and covariance matrix $\mathbf{C}$.  The step size $\sigma$ is used to control the scale of the sampling distribution.

$$ x \sim \mu + \sigma \cdot \mathbf{N} \Big(0, \mathbf{C} \Big) $$

### Test

The test step involves parallel rollouts of the population parameters in the environment.  In the agent, each parameter is rolled out $16$ times, with the results being averaged to give the fitness for each set of parameters.  This leads to a total of $1,024$ rollouts per generation!

### Select

The selection step involves selecting the best $n_{best}$ members of the population.  These population members are used to update the statistics of our multivariate Gaussian.

We first update our estimate of the mean using a sample average over $n_{best}$ from the current generation $g$:

$$ \mu_{g+1} = \frac{1}{n_{best}} \sum_{n_{best}} x_{g} $$

Our next step is to update our covariance matrix $C$.  *You can find a refresher on estimating a covariance matrix from samples in Appendix Five.*

The CMA-ES covariance matrix estimation is more complex than this, and involves the combination of two updates known as rank-one and rank-$\mu$.  Combining these update strategies helps to prevent degeneration with small population sizes, and to improve performance on badly scaled or non-separable problems.

### Rank-One Update

In the context of our agent, we might estimate the covariance of our next population $g+1$ using our samples $x$ and taking a reference mean value from that population:

$$ \mathbf{C}_{g+1} = \frac{1}{N_{best} - 1} \sum_{pop} \Big( x_{g+1} - \mu_{x_{g+1}} \Big) \Big( x_{g+1} - \mu_{x_{g+1}} \Big) $$

Using the mean of the actual sample $\mu_{g+1}$ leads to an estimation of the covariance within the sample. The approach used in a rank-one update instead uses a reference mean value from the **previous generation** $g$:

$$ \mathbf{C}_{g+1} = \frac{1}{N_{best}} \sum_{pop} \Big( x_{g+1} - \mu_{x_{g}} \Big) \Big( x_{g+1} - \mu_{x_{g}} \Big) $$

Using the mean of the previous generation $\mu_{g}$ leads to a covariance matrix that estimates the covariance of the **sampled step**.  The rank-one update introduces information of the correlations between generations using the history of how previous populations have evolved - known as the **evolution path**:

$$ p_{g+1} = \Big(1-c_{c}\Big)p_{g} + \sqrt{c_{c} \Big(2-c_{c} \mu_{eff}\Big)} \frac{\mu_{g+1} - \mu_{g}}{\sigma_{g}} $$

Where $c_{c}$ and $\mu_{eff}$ are hyperparameters.

The evolution path is a sum over all successive steps, but can be evaluated using only a single step - similar to how we can update a value function over a single transition.  The final form of the rank-one update is below:

$$ \mathbf{C}_{g+1} = \Big(1-c_{1}\Big) \mathbf{C}_{g} + c_{1} p_{g+1} p_{g+1}^{T} $$

### Rank-$\mu$ Update

With the small population sizes required by CMA-ES, getting a good estimate of the covariance matrix using a rank-one update is challenging.  The rank-$\mu$ update uses a reference mean value that uses information from all previous generations.  This is done by taking an average over all previous estimated covariance matrices:

$$ \mathbf{C} = \frac{1}{g+1} \sum_{gens} \frac{1}{\sigma^{2}} \mathbf{C} $$

We can improve on this by using an exponential weights $w$ to give more influence to recent generations.  CMA-ES also includes a learning rate $c_{\mu}$, to control how fast we update:

$$ \mathbf{C}_{g+1} = \Big(1-c_{\mu}\Big) \mathbf{C} + c_{\mu} \sum_{gens} w \cdot \Big( \frac{x_{g+1} - \mu_{g}}{\sigma_{g}} \Big) \cdot \Big( \frac{x_{g+1} - \mu_{g}}{\sigma_{g}} \Big)^{T} $$

### CMA-ES Step-Size Control

The covariance matrix estimation we see above does not explicitly control for scale.  CMA-ES implements an different evolution path ($p_{sigma}$) that is independent of the covariance matrix update seen above, known as **cumulative step length adaptation** (CSA).  This helps to prevent premature convergence.

The intuition CSA is:
- for short evolution paths, steps are cancelling each other out -> decrease the step size
- for long evolution paths, steps are pointing in the same direction -> increase the step size

To determine whether an observed evolution path is short or long, the path length is compared with the expected length under random selection.  Comparing the observed evolution path with a random (i.e. independent) path allows CMA-ES to determine how to update the step size parameter $c_{\sigma}$.

Our evolution path $p_{\sigma}$ is similar to the evolution path $p$ except it is a conjugate evolution path.  After some massaging, we end up with a step size update:

$$ \sigma_{g+1} = \sigma_{g} \exp \Big[ \frac{c_{\sigma}}{d_{\sigma}} \Big(  \frac{\mid\mid p_{\sigma, g} \mid\mid}{ \mathbf{E} \mid\mid \mathbf{N} (0, I)} - 1 \Big) \Big] $$

Where $c_{\sigma}$ is a hyperparameter controlling the backward time horizon, and $d_{\sigma}$ is a damping parameter.

### The Final CMA-ES Update

The mean is updated using a simple average of the $N_{best}$ population members from the previous generation:

$$ \mu_{g+1} = \frac{1}{N_{best}} \sum_{N_{best}} x_{g} $$

The covariance matrix is updated using

$$ C_{g+1} = (1 - c_{1} - c_{\mu} \cdot \sum w) \cdot C_{g} + c_{1} \cdot p_{g+1} \cdot p_{g+1}^{T} + c_{\mu} \cdot \sum_{gens} w \cdot \Big( \frac{x_{g+1} - \mu_{g}}{\sigma_{g}} \Big) \cdot \Big( \frac{x_{g+1} - \mu_{g}}{\sigma_{g}} \Big)^{T} $$

These updates allow separate control of the mean, covariance and step-size:
- mean update controlled by $c_{m}$
- covariance matrix $\mathbf{C}$ update controlled by $c_{1}$ and $c_{\mu}$
- step size update controlled by damping parameter $d_{sigma}$

### Implementing the Controller & CMA-ES

Above we looked at some of the mechanics of CMA-ES.

I did not need to reimplement CMA-ES from scratch - I used [`pycma`](https://github.com/CMA-ES/pycma).

Using `pycma` required only a simple wrapper class around the ask, evaluate and tell API of `pycma`.

For each generation the rollout of the linear controller parameters are parallelized using Python's `multiprocessing`.  When using `multiprocessing` with both `pycma` and `tensorflow`, care is required to import these packages at the correct place - **within the child process**.  Do these imports in the wrong place, and you are going to have a bad time.

The original runs 16 rollouts per generation, with the fitness for a population member being the average across the 16 rollouts.  With a population size of 64, this leads to 1024 rollouts per generation.

I also experienced a rather painful bug where some episode rollouts would stall.  This would lead to one of the 64 processes not returning, holding up all the other processes.

My solution to this was a band-aid - putting an alarm on AWS to terminate the instance if the CPU% fell below 50% for 5 minutes, along with code to restart the experiment from the latest generation saved in `~/world-models-experiments/control/generations/`.

### Implementing the Controller in Code

```bash
$ tree worldmodels

worldmodels
├── control
│   ├── controller.py
│   └── train_controller.py
├── data
│   ├── car_racing.py
│   ├── sample_policy.py
│   └── tf_records.py
├── memory
│   ├── memory.py
├── params.py
├── tests
├── utils.py
└── vision
└── vae.py
```

Below is the code for the controller, see the source in ([world-models/control](https://github.com/ADGEfficiency/world-models/blob/master/worldmodels/control)).

```python
## worldmodels/control/train_controller.py

from collections import defaultdict
import logging
from multiprocessing import Pool
import os
import pickle

import numpy as np

from worldmodels.control.controller import get_action
from worldmodels.data.car_racing import CarRacingWrapper
from worldmodels.params import vae_params, memory_params, env_params, home


def make_logger(name):
    """sets up experiment logging to a file"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fldr = os.path.join(home, "control")
    os.makedirs(fldr, exist_ok=True)
    fh = logging.FileHandler(os.path.join(fldr, "{}.log".format(name)))
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def episode(params, seed, collect_data=False, episode_length=1000, render=False):
    """runs a single episode"""
    #  needs to be imported here for multiprocessing
    import tensorflow as tf
    from worldmodels.vision.vae import VAE
    from worldmodels.memory.memory import Memory

    vision = VAE(**vae_params)

    memory_params["num_timesteps"] = 1
    memory_params["batch_size"] = 1
    memory = Memory(**memory_params)

    state = memory.lstm.get_zero_hidden_state(np.zeros(35).reshape(1, 1, 35))

    env = CarRacingWrapper(seed=seed)
    total_reward = 0
    data = defaultdict(list)
    np.random.seed(seed)
    obs = env.reset()
    for step in range(episode_length):
        if render:
            env.render("human")
        obs = obs.reshape(1, 64, 64, 3).astype(np.float32)
        mu, logvar = vision.encode(obs)
        z = vision.reparameterize(mu, logvar)

        action = get_action(z, state[0], params)
        obs, reward, done, _ = env.step(action)

        x = tf.concat(
            [tf.reshape(z, (1, 1, 32)), tf.reshape(action, (1, 1, 3))], axis=2
        )

        y, h_state, c_state = memory(x, state, temperature=1.0)
        state = [h_state, c_state]
        total_reward += reward

        if done:
            print("done at {} - reward {}".format(step, reward))
            break

        if collect_data:
            reconstruct = vision.decode(z)
            vae_loss = vision.loss(reconstruct)
            data["observation"].append(obs)
            data["latent"].append(np.squeeze(z))
            data["reconstruct"].append(np.squeeze(reconstruct))
            (data["reconstruction-loss"].append(vae_loss["reconstruction-loss"]),)
            data["unclipped-kl-loss"].append(vae_loss["unclipped-kl-loss"])
            data["action"].append(action)
            data["mu"].append(mu)
            data["logvar"].append(logvar)
            data["pred-latent"].append(y)
            data["pred-reconstruct"].append(np.squeeze(vision.decode(y.reshape(1, 32))))
            data["total-reward"].append(total_reward)

    env.close()
    logger.debug(total_reward)
    return total_reward, params, data


class CMAES:
    def __init__(self, x0, s0=0.5, opts={}):
        """wrapper around cma.CMAEvolutionStrategy"""
        self.num_parameters = len(x0)
        print("{} params in controller".format(self.num_parameters))
        self.solver = CMAEvolutionStrategy(x0, s0, opts)

    def __repr__(self):
        return "<pycma wrapper>"

    def ask(self):
        """sample parameters"""
        samples = self.solver.ask()
        return np.array(samples).reshape(-1, self.num_parameters)

    def tell(self, samples, fitness):
        """update parameters with total episode reward"""
        return self.solver.tell(samples, -1 * fitness)

    @property
    def mean(self):
        return self.solver.mean


logger = make_logger("all-rewards")
global_logger = make_logger("rewards")


if __name__ == "__main__":
    generations = 500
    popsize = 64
    epochs = 16

    results_dir = os.path.join(home, "control", "generations")
    os.makedirs(results_dir, exist_ok=True)

    #  need to open the Pool before importing from cma
    with Pool(popsize, maxtasksperchild=32) as p:
        from cma import CMAEvolutionStrategy

        input_size = vae_params["latent_dim"] + memory_params["lstm_nodes"]
        output_size = env_params["num_actions"]

        weights = np.random.randn(input_size, output_size)
        biases = np.random.randn(output_size)
        x0 = np.concatenate([weights.flatten(), biases.flatten()])

        previous_gens = os.listdir(results_dir)
        sort_idx = [int(s.split("_")[1]) for s in previous_gens]
        previous_gens = [p for (i, p) in sorted(zip(sort_idx, previous_gens))]

        if len(previous_gens) > 0:
            previous_gen = previous_gens[-1]
            start_generation = int(previous_gen.split("_")[-1]) + 1

            with open(os.path.join(results_dir, previous_gen, "es.pkl"), "rb") as save:
                es = pickle.load(save)
                print("loaded from previous generation {}".format(previous_gen))

        else:
            es = CMAES(x0, opts={"popsize": popsize})
            start_generation = 0

        print("starting from generation {}".format(start_generation))
        for generation in range(start_generation, generations):
            population = es.ask()

            epoch_results = np.zeros((popsize, epochs))
            for epoch in range(epochs):
                seeds = np.random.randint(low=0, high=10000, size=population.shape[0])

                results = p.starmap(episode, zip(population, seeds))
                rew, para, data = zip(*results)
                epoch_results[:, epoch] = rew

            epoch_results = np.mean(epoch_results, axis=1)
            assert epoch_results.shape[0] == popsize
            global_logger.debug(np.mean(epoch_results))

            es.tell(para, epoch_results)

            best_params_idx = np.argmax(epoch_results)
            best_params = population[best_params_idx]
            gen_dir = os.path.join(results_dir, "generation_{}".format(generation))
            os.makedirs(gen_dir, exist_ok=True)

            np.save(os.path.join(gen_dir, "population-params.npy"), population)
            np.save(os.path.join(gen_dir, "best-params.npy"), best_params)
            np.save(os.path.join(gen_dir, "epoch-results.npy"), epoch_results)

            with open(os.path.join(gen_dir, "es.pkl"), "wb") as save:
                pickle.dump(es, save)
```

```python
## worldmodels/controller/controller.py

import numpy as np


def get_action(z, state, params):
    """takes an action based on z, h and controller params"""
    w, b = shape_controller_params(params)
    net_input = np.concatenate([z, state], axis=None)
    action = np.tanh(net_input.dot(w) + b)
    action[1] = (action[1] + 1.0) / 2.0
    action[2] = np.clip(action[2], 0.0, 1.0)
    return action.astype(np.float32)


def shape_controller_params(params, output_size=3):
    """split into weights & biases"""
    w = params[:-output_size].reshape(-1, output_size)
    b = params[-output_size:]
    return w, b
```

## Methods

> Kurtz: Are my methods unsound?
>
> Willard: I don't see any method at all, sir.
>
> Apocalypse Now (1979)

{{< img
    src="/images/world-models/methods.jpg"
    caption="Francis Ford Coppola and Marlin Brando - Apocalypse Now"
    width="600"
>}}

This section shines light on the implementation methodology. Instructions to download a pretrained agent or to train your own agent from scratch are in the [readme of the reimplementation source code](https://github.com/ADGEfficiency/world-models).

### Agents Trained

**A number of iterations were required to work through bugs (Agents One & Two) and then to explore (Agent Three & Four) and finally to exploit (Agent Five).**

| Agent | Policy | Episodes | VAE epochs | Memory epochs |
|---|---|---|
|one| random | 10,000 | 10 | 20 |
|two| random | 10,000 | 10 | 20 |
|three| controller two | 5,000 | 10 | 20 |
|four| controller three |5,000 | 15 | 40 |
|five| controller three |5,000 | 15 | 80 |

### Timeline

**Below is a rough outline of the work done on the 11 months of this project.**  Eight months were spent on the technical reimplementation, with three writing this blog post.

*April 2019*

- April 6th - `echo "hello world"`
- sampling from the environment using a random policy
- wrote VAE model & training
- memory development - LSTM hidden state, Mixed Density Network

*May 2019*

- development of memory model & training scripts
- working on understanding evolutionary methods
- `tf.data`

*June 2019*

I didn't work on this project in June - I was busy with lots of teaching for Batch 19 at Data Science Retreat.

*July 2019*

- development of memory
- first run of the full agent *Agent One* - achieved an average of 500

{{< img
    src="/images/world-models/first.png"
    caption="Agent One performance"
    width="600"
>}}

*August 2019*

- transfer from `ADGEfficiency/mono` to `ADGEfficiency/world-models-dev`.
- train second VAE with fixed resize

*September 2019*

- trained second memory

*October 2019*

Very little work done in October - I was busy with lots of teaching for Batch 20 at Data Science Retreat.

- working on controller training
- move out of TF 2.0 beta

*November 2019*

- controller training development - saving parameters, ability to restart, random seeds for environment
- sampling episodes from trained controller
- train **Agent Two** - problem with the VAE not being able to encode images (i.e. off track), memory trains well - gets confused when on the edge of track
- train **Agent Three** - using data sampled from the controller (5000 episodes),
- train **Agent Four** - using data sampled from the controller, 40 epochs on memory

> Know you don’t hit it on the first generation, don’t think you hit it on the second, on the third generation maybe, on the fourth & fifth, that's when we start talking - Linus Torvalds

*December 2019*

**This was the final month of technical work (finishing on December 19), where Agent Five was trained.**  Work achieved this month:
- training Agent Five
- code to visualize the rollouts of the Agent Five controller
- code cleanup & refactors

*January 2020*

- blog post writing
- refactors and code cleanup

*February 2020*

- draft one done (13 Feb)
- readme cleanup, code cleanup

*March 2020*

- code to download pretrained model
- draft two done (7 March)

*April 2020*

- editing of draft two
- notebook clean up
- transfer from `ADGEfficiency/world-models-dev` to `ADGEfficiency/world-models`

### Working Habits

{{< img
    src="/images/world-models/commits-month.png"
    caption="Commits per month"
    width="600"
>}}

{{< img
    src="/images/world-models/commits-week.png"
    caption="Commits grouped by weekday"
    width="600"
>}}

{{< img
    src="/images/world-models/commits-hour.png"
    caption="Commits grouped by hour of the day"
    width="600"
>}}


### Training From Scratch

The methodology for training the entire agent from scratch (including the second iteration) is given in the `readme.md` of the Github repo.  The basic methodology is:
- sample rollouts from a random policy
- train a VAE using the random policy rollouts
- sample the VAE statistics (mean & variances of the latent space) for the random policy data
- train the memory by sampling from the VAE statistics
- train the controller using the VAE & memory

### Using a Pretrained Vision, Memory and Controller

The methodology for using pretrained agent is given in the `readme.md` of the Github repo - it involves running a bash script `pretrained.sh` to download the pretrained vision, memory & controller from a Google Drive link.

## Final Results

This section summarizes the performance of the final agent, along with training curves for the agent components. Due to the expense of training the controller (see the section on AWS costs below), [I was very glad to find the following from David Ha](http://blog.otoro.net/2018/06/09/world-models-experiments/):

> After 150-200 generations (or around 3 days), it should be enough to get around a mean score of ~ 880, which is pretty close to the required score of 900.
> If you don’t have a lot of money or credits to burn, I recommend you stop if you are satistifed with a score of 850+ (which is around a day of training).
> Qualitatively, a score of ~ 850-870 is not that much worse compared to our final agent that achieves 900+, and I don’t want to burn your hard-earned money on cloud credits. To get 900+ it might take weeks (who said getting SOTA was easy? :)

**The training curve for the controller.**  We show a much worse performing minimum than Ha & Schmidhuber, perhaps due to the use of a much higher `sigma` in `pycma`.

{{< img
    src="/images/world-models/final.png"
    caption="Training of the controller for Agent Five"
    width="600"
>}}

Performance of the best controller (generation 299):

{{< img
    src="/images/world-models/final_hist.png"
    caption="Histogram of the best agent (generation 229) episode rewards across 48 random seeds"
    width="600"
>}}

A debug gif I used at various stages of the project:

{{< img
    src="/images/world-models/rollout.gif"
    caption="A tool used for debugging - notice how noisy the memory prediction can be!"
    width="600"
>}}

### AWS Costs

See the project AWS costs in [worldmodels/notebooks/aws-costs.ipynb](https://github.com/ADGEfficiency/world-models/blob/master/notebooks/aws-costs.ipynb).  Compute costs are the EC2 costs - storage is EBS, S3 and all other costs.

|                     |   Cost [$] |
|:--------------------|-----------:|
| controller          |       1506 |
| vae-and-memory      |        602 |
| data                |         95 |
| sample-latent-stats |        255 |
| misc                |         25 |
| compute-total       |       2485 |
| s3                  |         54 |
| ebs                 |       1108 |
| storage-total       |       1162 |
| total               |       3648 |

Breakdown of compute cost per component:

| component      |   Cost [$] |   Cost [%] |
|:---------------|-----------:|-----------:|
| controller     |    1309.72 |      80.38 |
| vae-and-memory |     263.04 |      16.14 |
| data           |      56.68 |       3.48 |
| total          |    1629.43 |     100    |

Cost per component, per month:

| month   |   controller |   vae-and-memory |   data |   sample-latent-stats |   misc |   compute-total |    s3 |    ebs |   storage-total |   total |
|:--------|-------------:|-----------------:|-------:|----------------------:|-------:|----------------:|------:|-------:|----------------:|--------:|
| 1/04/19 |         0    |             0    |   0    |                  0    |   0    |            0    |  0    |   0    |            0    |    0    |
| 1/05/19 |         0    |             0    |   0    |                  0    |   0    |            0    |  0    |   0    |            0    |    0    |
| 1/06/19 |         0    |            90.94 |  29.37 |                  0    |  16.99 |          137.93 |  0    |  76.61 |           76.61 |  214.55 |
| 1/07/19 |         0    |           208.51 |   0.83 |                254.51 |   8.05 |          471.9  |  0    | 152.36 |          152.36 |  624.26 |
| 1/08/19 |         0    |           144.97 |  16.35 |                  0    |   0    |          162.62 | 15.41 | 215.99 |          231.39 |  394.02 |
| 1/09/19 |         0    |            25.25 |   0    |                  0    |   0    |           25.25 | 11.12 | 421.73 |          432.84 |  458.09 |
| 1/10/19 |       104.51 |             0    |   0    |                  0    |   0    |          104.51 | 11.12 |  48.53 |           59.64 |  164.15 |
| 1/11/19 |       673.23 |             0    |  48.33 |                  0    |   0    |          721.56 | 11.42 |  52.72 |           64.14 |  785.7  |
| 1/12/19 |       728.43 |           132.27 |   0.51 |                  0    |   0    |          861.72 |  4.91 | 140.31 |          145.22 | 1006.94 |

**One painful mistake occurred in September 2019 - leaving a ~ 1TB SSD volume sitting unconnected for a month, leading to a very expensive month!**

{{< img
    src="/images/world-models/aws.png"
    caption=""
    width="600"
>}}

## Discussion

### Requirement of an Iterative Training Procedure

**The most significant difference between this reimplementation and the 2018 paper is the requirement of iterative training.**

**Section 5 of Ha & Schmidhuber (2018) notes that they were able to train a world model using a random policy, and that more difficult environments would require an iterative training procedure.**  This was not true with our reimplementation - we required two iterations - one using data from a random policy to train the full agent, then a second round using data sampled from the first agent.

The paper codebase implements a random policy by randomly initializing the VAE, memory and controller parameters.  The reimplementation [ctallec/world-models](https://github.com/ctallec/world-models) has two methods for random action sampling - white noise (using the `gym` `env.action_space.sample()` or as a Brownian motion ([see here](https://github.com/ctallec/world-models/blob/master/utils/misc.py)).  The Brownian motion action sampling is the default.

**This suggests that slightly more care is needed than relying on a random policy.**  An interesting next step would be to look at optimizing the frequency of the iterative training for a given budget of episode sampling.

### Important Debugging Steps

**Most of the time I stuck to using the same hyperparameters as in the paper code base.**  Hyperparameters I changed:
- batch size to 256 in the VAE training (originally 32)
- CMA-ES `s0` set to 0.5
- amount of training data & epochs for the later iterations of VAE & memory training
- image antialiasing
- VAE not performing well when it went off track (loss + inspect the reconstruction) - exporation problem

### Tensorflow 2.0

**This reimplementation was started during the beta of Tensorflow 2.0.**  It is a massive improvement over Tensorflow 1.0.  The Tensorflow 1.0 `tf.Session` abstraction no longer gets in the way.

The main learning points are adapting to the style of inheriting from `tf.keras.Model`, and then using the `__call__` method of your child class to implement the forward pass. [One issue I had was with passing around the hidden state of the LSTM](https://adgefficiency.com/tf2-lstm-hidden/).

### `tf.data`

**For datasets larger than memory, batches must loaded from disk as needed.**  Holding a buffer of batches also makes sense to keep GPU utilization high.

**One way to achieve this is using `tf.data`.**  The API for this library is challenging, and we were required to use the `tf.data` at three different levels of abstraction (a tensor of floats, multiple tensors and a full dataset).

```python
## worldmodels/data/tf_records.py


def encode_float(value):
    """single array"""
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def encode_floats(features):
    """multiple arrays"""
    package = {}
    for key, value in features.items():
        package[key] = encode_float(value.flatten().tolist())

    example_proto = tf.train.Example(features=tf.train.Features(feature=package))
    return example_proto.SerializeToString()


def save_episode_tf_record(results_dir, results, process_id, episode):
    """results dictionary to .tfrecord"""

    path = os.path.join(
        results_dir, "process{}-episode{}.tfrecord".format(process_id, episode)
    )

    print("saving to {}".format(path))
    with tf.io.TFRecordWriter(path) as writer:
        for obs, act in zip(results["observation"], results["action"]):
            encoded = encode_floats({"observation": obs, "action": act})
            writer.write(encoded)
```

Two types of `tfrecord` files were saved and loaded:
- observations and actions for an episode (random or controller policy) - used to train VAE
- VAE latent statistics for an episode - used to train memory

```python
def parse_episode(example_proto):
    """used in training VAE"""
    features = {
        "observation": tf.io.FixedLenFeature((64, 64, 3), tf.float32),
        "action": tf.io.FixedLenFeature((3,), tf.float32),
    }
    parsed_features = tf.io.parse_single_example(example_proto, features)
    return parsed_features["observation"], parsed_features["action"]


def parse_latent_stats(example_proto):
    """used in training memory"""
    features = {
        "action": tf.io.FixedLenFeature(
            (
                1000,
                3,
            ),
            tf.float32,
        ),
        "mu": tf.io.FixedLenFeature(
            (
                1000,
                32,
            ),
            tf.float32,
        ),
        "logvar": tf.io.FixedLenFeature(
            (
                1000,
                32,
            ),
            tf.float32,
        ),
    }
    return tf.io.parse_single_example(example_proto, features)
```

Two configurations of `tf.data.Dataset` were used
- VAE trained using a dataset of shuffled observations
- memory trained using a dataset shuffled on the episode level (need to keep the episode sequence structure)

```python
def shuffle_samples(
    parse_func,
    records_list,
    batch_size,
    repeat=None,
    shuffle_buffer=5000,
    num_cpu=8,
):
    """used in vae training"""
    files = tf.data.Dataset.from_tensor_slices(records_list)

    #  get samples from different files
    dataset = files.interleave(
        lambda x: tf.data.TFRecordDataset(x),
        num_parallel_calls=num_cpu,
        cycle_length=num_cpu,
    )
    dataset = dataset.shuffle(shuffle_buffer)
    dataset = dataset.map(parse_func, num_parallel_calls=num_cpu)
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.repeat(repeat).prefetch(1)
    return iter(dataset)


def batch_episodes(parse_func, records, episode_length, num_cpu=4):
    """used in sampling latent stats"""
    files = tf.data.Dataset.from_tensor_slices(records)

    dataset = files.interleave(
        lambda x: tf.data.TFRecordDataset(x),
        num_parallel_calls=num_cpu,
        cycle_length=num_cpu,
        block_length=episode_length,
    )
    dataset = dataset.map(parse_func, num_parallel_calls=num_cpu)
    dataset = dataset.batch(episode_length)
```

The coverage for our implementation of `tf.data` is tested - see [worldmodels/tests/test_tf_records.py'](https://github.com/ADGEfficiency/world-models/blob/master/worldmodels/tests/test_tf_records.py).

Occasionally I get corrupt records - a small helper utility is given in [worldmwodels/utils.py](https://github.com/ADGEfficiency/world-models/blob/master/worldmodels/utils.py):

It is possible to load the `.tfrecord` files directly from S3.  As neural network training requires multiple passes over the dataset, it makes more sense to pull these down onto the instance using the S3 CLI and access them locally.

### AWS Lessons

I had experience running compute on AVS before this project, but not on setting up an entire account from scratch.  The progress was fairly painless, with a reasonable around of time configuring the infrastructure I needed.

The main tasks to get setup were:
- using IAM to create a user (seen as a best practice, even though my account has only one user)
- creating an S3 bucket, with permissions for the IAM user
- security group with ports open for SSH
- requesting allowances for instances - slightly frustrating, but the AWS support always got back within 24 hours
- using a `setup.txt` to automate some of the instance setup

Most of these tasks involved creating a few wrappers around the AWS CLI:

```bash
run-instance() {
  INSTANCE=${1:-t2.micro}
  SIZE=${2:-8}
  IAM="access-s3"
  INSTANCEID=$(aws ec2 run-instances --image-id "$AMI" --count 1 --instance-type "$INSTANCE" --key-name "$KEYNAME" --user-data file://"$USERDATA" --output text --iam-instance-profile Name="$IAM" | awk '/INSTANCE/{print $7}')
  echo "$INSTANCEID" > /dev/stderr
  sleep 10
  VOLID=$(aws ec2 describe-volumes --filters Name=attachment.instance-id,Values="$INSTANCEID" --output text | awk '/VOLUMES/{print $9}') > /dev/stderr
  aws ec2 modify-volume --volume-id "$VOLID" --size "$SIZE" > /dev/stderr
  echo "$INSTANCEID"
}

running-instances () {
  aws ec2 describe-instances --query 'Reservations[*].Instances[*].[Placement.AvailabilityZone, State.Name, InstanceId, PublicDnsName, InstanceType]' --output text | grep running | awk '{print $0}'
}

sshi () {
  INSTANCEID=$1

  ssh-add -K ~/.ssh/id_rsa
  DNS=$(aws ec2 describe-instances --instance-ids "$INSTANCEID" --query 'Reservations[*].Instances[*].[Placement.AvailabilityZone, State.Name, InstanceId, PublicDnsName, InstanceType]' --output text | grep running | awk '{print $4}')
  echo "$DNS"
  ssh -i "$KEY" -tt ubuntu@"$DNS"
}

kill-instances() {
  aws ec2 terminate-instances --instance-ids "$(aws ec2 describe-instances --filters  "Name=instance-state-name,Values=pending,running,stopped,stopping" --query "Reservations[].Instances[].[InstanceId]" --output text | tr '\n' ' ')"
}
```

### Future Hyperparameter Tweaking

As I was working on this project, a number of other hyperparameters that could be optimized came to mind:
- VAE loss balancing - in the paper implementation this is done using a `kl_tolerance` parameter of 0.5

```python
kl_loss = tf.reduce_mean(
    tf.maximum(unclipped_kl_loss, self.kl_tolerance * self.latent_dim)
)
```

- improving the random policy sampling
- number of mixtures of in the mixed density network
- number of rollouts per generation

Agent horizon
Changing this can have interesting effects on agent performance.  It is unclear how convenient this choice is - LSTM's (which power the agent's memory) can often struggle with very long sequences.

## What Did I Learn / Takeaways

### Use of a `home` to Save Data

```python
# worldmodels/params.py
from os import environ, path

home = path.join(environ["HOME"], "world-models-experiments")

# worldmodels/utils.py
from worldmodels.params import home


def make_directories(*dirs):
    """make many directories at once"""
    [os.makedirs(os.path.join(home, d), exist_ok=True) for d in dirs]
```

### Reimplement Papers

**This was the first machine learning paper I have reimplemented.**  It is something I am going to do again, and would recommend.

**The work closely matches the work data scientists often do on the job (taking existing code and using it for your task).**

**If you are thinking about remiplementating a paper, key questions are if the official codebase for the paper available or are there many other reimplemenations.**

**You may think that there is no oppourtunity to do anything new when remiplementating a paper.**  There are actually many oppourtunities to improve when reimplementing - including upgrading to new libraries (such as the move to Tensorflow 2.0).

### More Tools in the Machine Learning Toolbelt

**I hadn't worked with a VAE or MDN before this project.**  Both are now important tools in my toolbox - I expect MDN's in particular to be very useful in business context's, due to the estimation of uncertainty that the parameterized variance provides.

**I now have a decent grasp of evolutionary methods.** I know there are many more algorithms out there than CMA-ES, and I look forward to learning about them in the future.

### Create Bodies of Work

**One of the more pleasant insights I had while working on this project was discovering the many blog posts by David Ha on the various components of the agent** (in particular MDNs & evolutionary algorithms), a few of my favourites are below:

- [Mixture Density Networks with TensorFlow](http://blog.otoro.net/2015/11/24/mixture-density-networks-with-tensorflow/)
- [A Visual Guide to Evolution Strategies](http://blog.otoro.net/2017/10/29/visual-evolution-strategies/)
- [Evolving Stable Strategies](http://blog.otoro.net/2017/11/12/evolving-stable-strategies/)

**It is inspiring to actually be able to see and follow some of the strands of the development.**  It is also a perfect example of why working in machine learning is amazing - world class reseachers publicly sharing content that helps others learn.

**Another example of this is David Silver.**  Being able to see the career of work that started with a PhD on using computers to play Go and ends with AlphaGo is inspiring.  His publicly available UCL lectures where a key resource for me when learning reinforcement learning.

**A final example is Andrej Karpathy, who works at Tesla.** His blog posts are legendary!

**We always knew that greatness was built in small steps.**  What is wonderful about the modern machine learning community is that you can see and learn from the small steps of others, which are made in public.

**This reimplementation of World Models is one of my small steps.**  Thanks for reading!

## Appendix

### Appendix One - Markov Decision Process

A Markov Decision Process (MDP) is a mathematical framework for decision making.  Commonly the goal of an agent in an MDP is to maximize the expectation of future rewards.  It can be defined as a tuple:

$$ (\mathcal{S}, \mathcal{A}, \mathcal{R}, P, R, d_0, \gamma, H) $$

- set of states $\mathcal{S}$
- set of actions $\mathcal{A}$
- set of rewards $\mathcal{R}$
- state transition function $ P(s' \mid s,a) $
- reward transition function $ R(r \mid s,a,s') $
- distribution over initial states $d_0$
- discount factor $\gamma$
- horizion $H$

It is common to make the distinction between the state $s$ and observation $x$.  The state represents the true state of the environment and has the Markov property. The observation is what the agent sees.  The observation is less informative, and often not Markovian.

Because the agent uses the total episode reward as a learning signal, there is no role for a discount rate $\gamma$.

The data collected by an agent interacting with an environment is a sequence of transitions, with a transition being a tuple of observation, action, reward and next state:

$$ (x, a, r, x') $$

- $x$ observation
- $a$ action
- $r$ reward
- $x'$ next observation

### Appendix Two - Generative versus discriminative models

To better understand the context of the VAE, let's take a quick detour into a useful categorization of predictive modelling - generative versus discriminative.

All approaches in predictive modelling can be categorized as either generative or discriminative.

### Generative Models

**Generative models learn a joint distribution** $P(x, z)$ (the probability of $x$ and $z$ occurring together).  Generative models generate new, unobserved data $x'$.

We can derive this process for generating new data, from the definition of conditional probability:

$$ P(x \mid z) = \frac{P(x, z)}{P(z)} $$

Rearranging this definition gives us a decomposition of the joint distribution. This is the product rule of probability:

$$P(x, z) = P(x \mid z) \cdot P(z)$$

This decomposition describes the entire generative process.  First sample a latent representation:

$$z \sim P(z)$$

Then sample a generated data point $x'$, using the conditional probability $P(x \mid z)$:

$$x' \sim P(x \mid z)$$

These sampling and decoding steps only describe the generation of new data $x'$ from an unspecified generative model.  It doesn't describe the structure of the model we use to approximate $$P(x \mid z)$$.

### Discriminative Models

Unlike generative models, **discriminative models learn a conditional probability** $P(x \mid z)$ (the probability of $x$ given $z$).  Discriminative models predict, using observed $z$ to predict $x$.  This is simpler than generative modelling.

A common discriminative computer vision problem is classification, where a high dimensional image is fed through convolutions and outputs a predicted class.

### Appendix Three - Convolution

{{< img
    src="/images/world-models/conv.png"
    caption="2D convolution with a single filter"
    width="600"
>}}

Naturally we associate an image as having two dimensions - height & width.  Computers look at images in three dimensions - height, width and colour channels.

The kind of convolution used in neural networks to process images are therefore volume to volume operations - they take a volume as input and produce a volume as output.

At the heart of convolution is the filter (sometimes called a kernel).  These are usually defined as two dimensional, with the third dimension being set to match the number of channels in the image (3 for RGB).

Different kernels are learnt at different layers - shallower layers learn basic features such as edges, with later layers having filters that detect complex compositions of simpler features.

We can think about these kernels operating on tensors of increasing size:
- matrix (3, 3) * kernel (3, 3) -> scalar (1, )
- image (6, 6, 1) * kernel (3, 3, 1) -> image (6, 6, 1)
- image (6, 6, 1) * n kernels (n, 3, 3, 1) -> tensor (6, 6, 1, n)

Important hyperparameters in convolutional neural networks:
- size of filters (typically 3x3)
- number of filters per layer
- padding
- strides

Due to reusing kernels, the convolution neural network is translation invariant, meaning the features can be detected in different parts of the images.  This is ideal in image classification.  Max-pooling (commonly used to downsample the size of the internal representation) also produces translation invariance (along with a loss of information).

### Appendix Four - LSTM

*For a deeper look at LSTM's, I cannot recommend the blog post [Understanding LSTM Networks - colah's blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) highly enough.*

The motivation for using an LSTM to approximate the transition dynamics of the environment is that an LSTM is a **recurrent neural network**.  In the `car-racing-v0` environment the data is a sequence of latent representations $z$ of the observation

Recurrent neural networks process data in a sequence:

$$ P(x' | x, h) $$

Where $h$ is the hidden state of the recurrent neural network.

The LSTM was introduced in 1997 by Hochreiter & Schmidhuber.  A key contribution of the LSTM was overcoming the challenge of long term memory with only a single representation of the future.

The LSTM is a recurrent neural network, that makes predictions based on the following:

$$ P(x' | x, h, c) $$

Where $h$ is the hidden state and $c$ is the cell state.  Using two variables for the LSTM's internal representation allows the LSTM to learn both a long and short term representation of the future.

The long term representation is the **cell state** $c$.  The cell state is an information superhighway.

The short term representation is the **hidden state** $h$.

Sigmoid often used as an activation for binary classification.  For LSTMs, we use the sigmoid to control information flow.

Tanh is used to generate data.  Neural networks like values in the range -1 to 1, which is exactly how a tanh generates data (with some non-linearity in between).

Information is added or removed from both the cell and hidden states using gates.

The gates are functions of the hidden state $h$ and the data $x$.

The gates can be thought of in terms of the methods of a REST API (GET, PUT and DELETE) or the read, update and delete functions in CRUD.

{{< img
    src="/images/world-models/lstm.png"
    caption="The LSTM - from Understanding LSTM Networks"
    width="600"
>}}

### Forget Gate

The first gate is the **forget gate**.  The forget gate works like the `DELETE` request in an REST API.

The forget gate multiplies the cell state by a sigmoid.  A gate value of 0 would mean forget the entire cell state.  A gate value of 0 would mean remember the entire cell state.

The sigmoid used to control the forget gate is a function of the hidden state $h$ and the data $x$.

### Input Gate

The second gate is the **input gate**.  The input gate works like a `PUT` or `POST` request.

This gate determines how we will update the cell state from $c$ to $c'$.  The information added to the cell state is formed from a sigmoid (that controls which values to update) and a tanh (that generates the new values).

### Output Gate

The final gate determines what the LSTM outputs.  This gate works like a `GET` request.

A sigmoid (based on the hidden state $h$) determines which parts of the cell state we will output.  This sigmoid is applied to the updated cell state $c'$, after the updated cell state $c'$ was passed through a tanh layer.

### Appendix Five - Estimating a covariance matrix

Before detailing how CMA-ES estimates it's covariance matrix, we can first review how we would estimate the covariance matrix of a distribution, if we were given only samples from that distribution (i.e. samples from a set of parameters that did well on a control task).

Let's imagine we have a parameter space with two variables, $x$ and $y$, along with samples from the distribution $P(x,y)$.  We can estimate the statistics needed for a covariance matrix as follows.  First the means:

$$ \mu_{x} = \frac{1}{N} \sum_{pop} x $$

$$ \mu_{y} = \frac{1}{N} \sum_{pop} y $$

Then the covariances on the diagonal:

$$ \sigma^{2}_{x} = \frac{1}{N-1} \sum_{pop} \Big( x - \mu_{x} \Big)^{2} $$

$$ \sigma^{2}_{y} = \frac{1}{N-1} \sum_{pop} \Big( y - \mu_{y} \Big)^{2} $$

And the covariance of how our two parameters vary together:

$$ \sigma_{xy} = \frac{1}{N-1} \sum_{pop} \Big( x - \mu_{x} \Big) \Big( y - \mu_{y} \Big) $$

This then gives us our estimated covariance matrix for our samples:

$$\mathbf{C} = \begin{bmatrix}  \sigma^{2}_{x} & \sigma_{xy} \\ \sigma_{yx} &  \sigma^{2}_{y}\end{bmatrix}$$

The method above will approximate the covariance matrix from data (in our case, a population of controller parameters).  We can imagine successively selecting only the best set of parameters, and approximating better covariance matrices.
