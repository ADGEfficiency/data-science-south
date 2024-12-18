---
title: Attention from Scratch
summary: Attention and Multi-Head Attention in NumPy.
---

## Embedding Words 

The first step in using attention for natural language is to embed words into vectors.

Let's start with a four-word sentence, with word vectors of length three:

<!--phmdoctest-share-names-->
```python
import numpy as np

sentence = ["I", "love", "you", "today"]

vocabularly = {
    "I": [0, 1, 0],
    "love": [0, 1, 1],
    "you": [1, 1, 1],
    "today": [0, 0, 0],
}

words = np.array([vocabularly[word] for word in sentence])
print(f"words:\n{words}")
```

```
words:
[[0 1 0]
 [0 1 1]
 [1 1 1]
 [0 0 0]]
```

Our embedded sentence has a dimensionality of `(4, 3)`:

<!--phmdoctest-share-names-->
```python
d_sentence = len(sentence)
d_embedding = len(vocabularly["I"])

assert d_sentence == 4 == words.shape[0]
assert d_embedding == 3 == words.shape[1]
assert words.shape == (d_sentence, d_embedding)

print(f"{words.shape=}")
```

```
words.shape=(4, 3)
```

## Position Encoding

In the previous section we embedded a sentence into word vectors.

Currently our word vector embedding has no concept of the position or order of the words in the input sequence. 

Attention is permutation invariant - it doesn't consider the order or position of the elements in the input sequence. It treats each word independently. However, word order is critical for understanding language. 

**We need a way to inject information about the relative or absolute position of the words in the sequence - one way to do this is to add a position encoding to each input embedding**. 

The position encodings have the same dimension `d_embedding` as the word embeddings, so we can add them element-wise.

A simple position encoding scheme is to use powers of sine and cosine functions of different frequencies:

<!--phmdoctest-share-names-->
```python
def get_position_encoding(
    d_embedding: int, max_seq_len: int = 100, n: int = 10000
) -> np.ndarray:
    position_encoding = np.zeros((max_seq_len, d_embedding))
    for k in range(max_seq_len):
        for i in np.arange(int(d_embedding / 2)):
            denominator = np.power(n, 2 * i / d_embedding)
            position_encoding[k, 2 * i] = np.sin(k / denominator)
            position_encoding[k, 2 * i + 1] = np.cos(k / denominator)
    return position_encoding

position_encoding = get_position_encoding(d_embedding)
print(position_encoding[:10])
print(f"{position_encoding.shape=}")
```

```
[[ 0.          1.          0.        ]
 [ 0.84147098  0.54030231  0.        ]
 [ 0.90929743 -0.41614684  0.        ]
 [ 0.14112001 -0.9899925   0.        ]
 [-0.7568025  -0.65364362  0.        ]
 [-0.95892427  0.28366219  0.        ]
 [-0.2794155   0.96017029  0.        ]
 [ 0.6569866   0.75390225  0.        ]
 [ 0.98935825 -0.14550003  0.        ]
 [ 0.41211849 -0.91113026  0.        ]]
position_encoding.shape=(100, 3)
```

Each position has a unique encoding. The encodings form a sort of "positional space" where positions close to each other have more similar encodings compared to positions far apart.

Now we can add the position encodings to our word embeddings:

<!--phmdoctest-share-names-->
```python
position_encoded_words = words + position_encoding[range(words.shape[0])]
print(f"{position_encoded_words.shape=}")
```

```
position_encoded_words.shape=(4, 3)
```

## Query, Key and Value Weights

In previous sections we:

- embedded a sentence into word vectors,
- added positional encoding.

**Central to the attention mechanism are the query, key and value vectors**. These are the vectors we use to compute attention.

To calculate the query, key and value vectors we need three sets of weights.

The dimensionality of the embeddings and weights determine the dimensionality of the query, key and value vectors:

1. The query dimensionality is set by the embedding dimension and an arbitrary dimension `d_query`,
2. The key dimensionality is set by the query dimensionality `d_query`,
3. The values dimensionality is set by the values dimension `d_values`.

The values dimension `d_values` is arbitrary, and will set the size of the output context vector.

<!--phmdoctest-share-names-->
```python
d_query = 6
d_values = 8

w_query = np.random.rand(d_embedding, d_query)
w_key = np.random.rand(d_embedding, d_query)
w_value = np.random.rand(d_embedding, d_values)

print(f"{w_query.shape=}")
print(f"{w_key.shape=}")
print(f"{w_value.shape=}")
```

```
w_query.shape=(3, 6)
w_key.shape=(3, 6)
w_value.shape=(3, 8)
```

The shapes of these weights do not depend on the length of the input sequence. This is important, as it's how the attention mechanism can deal with sequences of arbitrary length.

### Query, Key and Value for One Word

Let's select one word to do attention over.

We select the second word, and use a dot product to calculate the query, key and value for a single word:

<!--phmdoctest-share-names-->
```python
word = words[1]

query = word.dot(w_query)
key = word.dot(w_key)
value = word.dot(w_value)

print("single word:")
print(f"{query.shape=}")
print(f"{key.shape=}")
print(f"{value.shape=}")
```

```
single word:
query.shape=(6,)
key.shape=(6,)
value.shape=(8,)
```

### Query, Key and Value for All Words

Let's now do attention over all the words, which we can do with the same dot product:

<!--phmdoctest-share-names-->
```python
queries = words.dot(w_query)
keys = words.dot(w_key)
values = words.dot(w_value)

print("all the words:")
print(f"{queries.shape=}")
print(f"{keys.shape=}")
print(f"{values.shape=}")
```

```
all the words:
queries.shape=(4, 6)
keys.shape=(4, 6)
values.shape=(4, 8)
```

Now our queries, keys and values have an additional dimension - the number of words in the sentence.

## Attention Scores

In previous sections we:

- embedded a sentence into word vectors, 
- added positional encoding,
- transformed our input sentence into queries, keys and values.

**The attention score is a measure of how similar a query is to a key. It's computed using a dot-product**.

## Attention Scores for One Word with One Other Word

We can start by calculating the attention scores for a single word:

<!--phmdoctest-share-names-->
```python
query = words[1].dot(w_query)
key = words[1].dot(w_key)

scores = query.dot(key)
print(f"{scores.shape=}")
```

```
scores.shape=()
```

We can also calculate the attention scores between one word and another word:

<!--phmdoctest-share-names-->
```python
query = words[0].dot(w_query)
key = words[1].dot(w_key)

scores = query.dot(key)
print(f"{scores.shape=}")
```

```
scores.shape=()
```

## Attention Scores for One Word with All Other Words

We can extend this to calculate attention scores for one word with all other words:

<!--phmdoctest-share-names-->
```python
query = words[1].dot(w_query)
keys = words.dot(w_key)

scores = query.dot(keys.T)
print(f"{scores.shape=}")
```

```
scores.shape=(4,)
```

## Attention Scores for All Words with All Other Words

Finally, we can calculate the attention scores for all words with all other words:

<!--phmdoctest-share-names-->
```python
queries = words.dot(w_query)
keys = words.dot(w_key)
scores = queries.dot(keys.T)

assert scores.shape == (d_sentence, d_sentence)
print(f"{scores.shape=}")
```

```
scores.shape=(4, 4)
```

## Scaling

**Scaling a common technique used in attention - it has several benefits**:

- It reduces the variance of the dot products, making the softmax function more stable and less prone to yielding extreme values.
- It helps maintain reasonable gradients even for large input sequences, facilitating the training process.
- It becomes particularly important when using multi-headed attention, as it allows each head to specialize and attend to different aspects of the input.

## Scaled Attention Scores

<!--phmdoctest-share-names-->
```python
scores = queries.dot(keys.T) / np.sqrt(d_query)

assert scores.shape == (d_sentence, d_sentence)
print(f"{scores.shape=}")
```

```
scores.shape=(4, 4)
```

## Normalization

**Normalization is the process of converting the raw scores into a probability distribution using a softmax**. 

Normalization is important for several reasons:

- It converts the raw scores into a valid probability distribution, allowing the model to weigh the importance of each input in a principled way.
- It ensures that the attention weights are non-negative and sum up to 1, which is a desirable property for a weighting scheme.
- It introduces a degree of competition among the inputs - increasing the weight of one input necessarily decreases the weights of others.
- It makes the attention weights more interpretable and amenable to visualization and analysis.

## Attention Weights for One Word

We can use the softmax to normalize the scores for a single word:

<!--phmdoctest-share-names-->
```python
def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

scores = queries.dot(keys.T) / np.sqrt(d_query)
weights = softmax(scores[1])

assert len(weights) == d_sentence
np.testing.assert_almost_equal(weights.sum(), 1)
print(f"{weights.shape=}")
```

```
weights.shape=(4,)
```

## Attention Weights for All The Words

We can use the softmax to normalize the scores for all the words:

<!--phmdoctest-share-names-->
```python
def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)

scores = queries.dot(keys.T) / np.sqrt(d_query)
weights = softmax(scores)

assert weights.shape == (d_sentence, d_sentence)
np.testing.assert_almost_equal(weights.sum(axis=1), 1)
print(f"{weights.shape=}")
```

```
weights.shape=(4, 4)
```

## Calculating the Context Vector

In previous sections we:

- embedded a sentence into word vectors, 
- added positional encoding,
- transformed our input sentence into queries, keys and values,
- used scaling, a softmax & normalization to produce attention scores.


**The context vector aggregates the information from the entire sequence, weighted by relevance to each input word**. It is the output of the attention mechanism.

The context vector is a weighted sum of value vectors, where the weights are given by the attention scores. 

The context vector captures the relevant information from other parts of the input sequence needed to focus on specific elements during processing. 

## Context Vector for All The Words

We can calculate the context vector with matrix multiplication:

<!--phmdoctest-share-names-->
```python
context_vectors = np.matmul(scores, values)
assert context_vectors.shape == (d_sentence, d_values)
print(f"{context_vectors.shape=}")
```

```
context_vectors.shape=(4, 8)
```

## Multi-Head Attention

**Multi-head attention involves multiple attention mechanisms - a single attention mechanism is a single head**.

Each head has its own set of query, key and attention weights. Each head can be used to learn different representations of the input at the same time.

One head may focus on learning syntax, with the other semantics. One head may focus on short term dependencies (between one token and the next) or long term dependencies (between one token and the end of the sentence).

## Embedding Words to Vectors

Let's start as we did previously, by embedding words to vectors.

This step is the same as with a single attention head:

<!--phmdoctest-share-names-->
```python
import numpy as np

def get_words() -> np.ndarray:
    sentence = ["I", "love", "you", "today"]
    vocabularly = {
        "I": [0, 1, 0],
        "love": [0, 1, 1],
        "you": [1, 1, 1],
        "today": [0, 0, 0],
    }
    return np.array([vocabularly[word] for word in sentence])
words = get_words()
d_sentence = words.shape[0]
d_embedding = words.shape[1]

print(f"{words.shape=}")
```

```
words.shape=(4, 3)
```

## Position Encoding

Next we encode position - this step is the same as with a single attention head:

<!--phmdoctest-share-names-->
```python
def get_position_encoding(
    d_embedding: int, max_seq_len: int = 100, n: int = 10000
) -> np.ndarray:
    position_encoding = np.zeros((max_seq_len, d_embedding))
    for k in range(max_seq_len):
        for i in np.arange(int(d_embedding / 2)):
            denominator = np.power(n, 2 * i / d_embedding)
            position_encoding[k, 2 * i] = np.sin(k / denominator)
            position_encoding[k, 2 * i + 1] = np.cos(k / denominator)
    return position_encoding

position_encoding = get_position_encoding(d_embedding)
position_encoded_words = words + position_encoding[range(words.shape[0])]
print(f"{position_encoded_words.shape=}")
```

```
position_encoded_words.shape=(4, 3)
```

## Multi-Head Attention Weights

Next we create our query, key and value weights.

This step is different from a single attention head, as we create a set of weights for each head:

<!--phmdoctest-share-names-->
```python
n_heads = 5
d_query = 6
d_values = 8

w_query = np.random.rand(n_heads, d_embedding, d_query)
w_key = np.random.rand(n_heads, d_embedding, d_query)
w_value = np.random.rand(n_heads, d_embedding, d_values)

print(f"{w_query.shape=}")
print(f"{w_key.shape=}")
print(f"{w_value.shape=}")
```

```
w_query.shape=(5, 3, 6)
w_key.shape=(5, 3, 6)
w_value.shape=(5, 3, 8)
```

## Query, Key and Value for One Word

Let's select one word to do attention over:

<!--phmdoctest-share-names-->
```python
word = words[1]

query = word.dot(w_query)
key = word.dot(w_key)
value = word.dot(w_value)

print("single word:")
print(f"{query.shape=}")
print(f"{key.shape=}")
print(f"{value.shape=}")
```

```
single word:
query.shape=(5, 6)
key.shape=(5, 6)
value.shape=(5, 8)
```

## Query, Key and Value for All Words

First we need to stack input embeddings - one for each head.  After this we can calculate the queries, keys and values:

<!--phmdoctest-share-names-->
```python
words = get_words()
if len(words.shape) == 2:
    words = np.repeat(words[np.newaxis, :, :], n_heads, axis=0)
print(f"{words.shape=}")

queries = np.matmul(words, w_query)
keys = np.matmul(words, w_key)
values = np.matmul(words, w_value)

assert queries.shape == (n_heads, d_sentence, d_query)
assert keys.shape == (n_heads, d_sentence, d_query)
assert values.shape == (n_heads, d_sentence, d_values)

print("all the words:")
print(f"{queries.shape=}")
print(f"{keys.shape=}")
print(f"{values.shape=}")
```

```
words.shape=(5, 4, 3)
all the words:
queries.shape=(5, 4, 6)
keys.shape=(5, 4, 6)
values.shape=(5, 4, 8)
```

## Scaled Attention Scores

After calculating queries and keys, we can calculate the attention scores:

<!--phmdoctest-share-names-->
```python
scores = np.matmul(queries, keys.transpose(0, 2, 1)) / np.sqrt(d_query)
print(f"{scores.shape=}")
```

```
scores.shape=(5, 4, 4)
```

## Normalized Attention Weights

As with a single head, we use a softmax function to normalize the attention scores:

<!--phmdoctest-share-names-->
```python
def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)

weights = softmax(scores)
print(f"{weights.shape=}")

assert np.allclose(weights.sum(axis=2), 1)
assert weights.shape == (n_heads, d_sentence, d_sentence)
```

```
weights.shape=(5, 4, 4)
```

## Context Vector

Finally we can calculate the context vector with matrix multiplication:

<!--phmdoctest-share-names-->
```python
context = np.matmul(weights, values)
assert context.shape == (n_heads, d_sentence, d_values)
print(f"{context.shape=}")
```

```
context.shape=(5, 4, 8)
```
