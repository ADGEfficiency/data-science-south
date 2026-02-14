---
title: Setting and Resetting LSTM Hidden States in TensorFlow 2
description: Getting control using a stateful and stateless LSTM.
date_created: 2019-05-01
date_updated: 2025-10-30
competencies:
  - Machine Learning
  - Software Engineering
aliases:
- 2019-05-01-tf2-lstm-hidden
- tf2-lstm-hidden

---

**TensorFlow 2 changed how we work with LSTM hidden states**. This post explains how to get fine-grained control of the hidden state of an LSTM layer in TensorFlow 2.

{{< img
    src="/images/lstm-hidden/fig1.svg"
    caption="LSTM hidden state flow"
    width="500"
>}}

## Using a Stateful LSTM

**A stateful LSTM means that the final states of batch `i` will be used as the initial states of batch `i+1`**. Often this isn't the behaviour that we want (when training each batch is independent of other batches) but it is required to be able to call `tf.keras.layers.RNN().reset_states(state)`.

Having a stateful LSTM means that you will need to reset the hidden state in between batches yourself if you do want independent batches. The default initial hidden state in TensorFlow is all zeros.

### Building the Model

First let's setup a simple, single layer LSTM with a fully connected output layer. **I use `tf.keras.Model` rather than `tf.keras.Sequential` so that I can have multiple outputs** (i.e. so I can access the hidden state after a forward pass):

```python
import numpy as np
import tensorflow as tf

np.random.seed(42)
tf.random.set_seed(42)

input_dim = 3
output_dim = 3
num_timesteps = 2
batch_size = 10
nodes = 10

input_layer = tf.keras.Input(shape=(num_timesteps, input_dim), batch_size=batch_size)

cell = tf.keras.layers.LSTMCell(
    nodes,
    kernel_initializer="glorot_uniform",
    recurrent_initializer="glorot_uniform",
    bias_initializer="zeros",
)

lstm = tf.keras.layers.RNN(
    cell,
    return_state=True,
    return_sequences=True,
    stateful=True,
)

lstm_out, hidden_state, cell_state = lstm(input_layer)

output = tf.keras.layers.Dense(output_dim)(lstm_out)

mdl = tf.keras.Model(inputs=input_layer, outputs=[hidden_state, cell_state, output])
```

### Testing the Stateful Behavior

We can now test what's going on by passing a batch through the network:

```python
x = np.random.rand(batch_size, num_timesteps, input_dim).astype(np.float32)
h_state, c_state, out = mdl(x)
print(np.mean(out))
# -0.011644869
```

**If we pass this same batch again, we get different result as the hidden state has been changed**:

```python
h_state, c_state, out = mdl(x)
print(np.mean(out))
# -0.015350263
```

### Resetting the Hidden State

**If we reset the hidden state, we can recover our initial output**:

```python
lstm.reset_states(states=[np.zeros((batch_size, nodes)), np.zeros((batch_size, nodes))])
h_state, c_state, out = mdl(x)
print(np.mean(out))
# -0.011644869
```

**This method also allows us to use other values than all zeros for the hidden state**:

```python
lstm.reset_states(states=[np.ones((batch_size, nodes)), np.ones((batch_size, nodes))])
h_state, c_state, out = mdl(x)
print(np.mean(out))
# -0.21755001
```

## Using a Non-Stateful LSTM

**One major downside of using a stateful LSTM is that you are forced to use the same batch sizes when doing forward and backward passes**. I wanted the ability to pass single sample through the LSTM as well as being able to train in batches.

This method actually overrides one of the functions used internally in TensorFlow (`tf.keras.layers.LSTMCell().get_initial_state`). I felt a bit dirty doing this but whenever I tried to pass the states through in the `call` I got a `TypeError: call() got an unexpected keyword argument 'states'`.

```python
import numpy as np
import tensorflow as tf

np.random.seed(42)
tf.random.set_seed(42)


class Model:
    def __init__(self):
        cell = tf.keras.layers.LSTMCell(
            nodes,
            kernel_initializer="glorot_uniform",
            recurrent_initializer="glorot_uniform",
            bias_initializer="zeros",
        )

        self.lstm = tf.keras.layers.RNN(
            cell,
            return_state=True,
            return_sequences=True,
            stateful=False,
        )
        lstm_out, hidden_state, cell_state = self.lstm(input_layer)
        output = tf.keras.layers.Dense(output_dim)(lstm_out)
        self.net = tf.keras.Model(
            inputs=input_layer, outputs=[output, hidden_state, cell_state]
        )

    def get_zero_initial_state(self, inputs):
        return [tf.zeros((batch_size, nodes)), tf.zeros((batch_size, nodes))]

    def get_initial_state(self, inputs):
        return self.initial_state

    def __call__(self, inputs, states=None):
        if states is None:
            self.lstm.get_initial_state = self.get_zero_initial_state

        else:
            self.initial_state = states
            self.lstm.get_initial_state = self.get_initial_state

        return self.net(inputs, states)
```

### Testing the Non-Stateful Behavior

So does this work? Let's generate another batch, this time a single sample:

```python
mdl = Model()
x = np.random.rand(1, num_timesteps, input_dim).astype(np.float32)
out, hidden_state, cell_state = mdl(x)
print(np.mean(out))
# 0.00057914766
```

**Unlike a stateful LSTM, if we try this again we get the same result**:

```python
out, hidden_state, cell_state = mdl(x)
np.mean(out)
# 0.00057914766
```

**And most importantly, we gain the ability to control the initial state for the sequence**:

```python
out, hidden_state, cell_state = mdl(
    x, states=[tf.ones((1, nodes)), tf.ones((1, nodes))]
)
np.mean(out)
# 0.25189233
```

## Summary

TensorFlow 2 changed how we work with LSTM hidden states.

Two approaches for controlling LSTM hidden states:

- **Stateful LSTM**: Use `reset_states()` to control hidden states, but requires fixed batch sizes
- **Non-stateful LSTM with override**: Override `get_initial_state()` for flexible batch sizes and full control

Key differences:

- **Stateful**: Final states of batch `i` become initial states of batch `i+1`
- **Non-stateful**: Each batch starts with fresh initial states
- **Batch size flexibility**: Non-stateful approach allows variable batch sizes during inference

Thanks for reading!
