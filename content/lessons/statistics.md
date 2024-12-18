---
title: Statistics
summary: Don't be fooled by randomness!
competencies:
- Algorithms
draft: true
---

## Why Learn Statistics?

- **Decision making** - Make good decisions by separating signal from noise.
 
## Uncertainty

Uncertainty is inherent in real-world decision-making. Managing uncertainty is required to make good decisions.

For example, when driving traffic and unscheduled road maintenance leads to uncertainty about which route is best to take.

### Sources of Uncertainty

Any decision involves uncertainty. Being specific about where uncertainty comes from is the first step to managing it.

### 1. Stochastic Environments

A stochastic environment is one where the outcome of events are random - stochastic is a fancy way of saying random.

An event is random if we cannot predict it - examples include flipping a coin and weather forecasting.

### 2. Incomplete Observability

Incomplete observability occurs when we lack data (samples or variables) about the world.  Incomplete observability of variables arises from incomplete sampling of data (think rows), and from noise or errors in data collection (think columns).

For example, in climate modeling, incomplete observability arises from a lack of samples (our network of weather sensors doesn't cover the entire planet) and from noise in data collection (from weather sensors that are uncalibrated).

### 3. Incomplete Models

Incomplete models fail to fully extract signal from data. Think about a map that doesn't show all the roads - it's incomplete and can't be used for navigation.

## What is Statistics?

My favourite definition of statistics to *don't be fooled by randomness*. A statisticians primary concern is making sure nature hasn't tricked us.

Determining whether an observation is due to chance, is needed for us to *separate out the signal from the noise* (my second favourite definition of statistics).

### What is a Statistic?

A statistic is a summary of data. It is a numeric measure that captures, extracts and summarizes information about data. A statistic is a lower dimensional summary of a larger dataset.

The value of these summaries is that we can reason about data that is to large to fit in our brain.  Many datasets are too large for us to understand.  

Like data itself, a statistic can contain both signal and noise.

We can simulate this by generating a dataset with both signal and noise:

```python
import numpy as np

np.random.seed(42)

n_samples = 1000
truth = 5
signal = np.full(n_samples, truth)
noise = np.random.normal(0, 1, n_samples)

data = signal + noise
print(np.mean(data))
```

```
5.019332055822326
```

Our statistic (in this case the `mean`) allows us to take a high dimensional dataset of `1000` samples and measure its central tendency.  What we get back is close to the `signal` value of `5`, but not exactly.

The mean is not the only statistic we can measure - we could also estimate the standard deviation:

```python
print(np.std(data))
```

```
0.9787262077473542
```

As with our estimate of the mean, our estimate of the standard deviation is close to the truth, but not exactly.  It contains both noise and signal.

### All Statistics Are Wrong

All statistics are a fiction that don't exist in reality.  Any statistic removes information about the data is it summarizing.

Take for example the `mean` we measure above - with the `mean` alone, we have no idea about the spread of the distribution. Likewise if we only have our estimate of the standard deviation, we don't know what the central tendency of the data is.

All statistics involve some form of aggregation - this aggregation in one dimension leads to a loss of information.  This is an example of uncertainty coming from incomplete modelling.

All statistics are estimates - they all aggregate across samples.  These samples are noisy and contain error - an example of uncertainty coming from a stochastic environment.

## What is Probability?

Probability is a set of tools developed to deal with uncertainty.  Like statistics, probability allows us to make better decisions by reasoning about uncertainty.

A single probability measures the likelihood of an event - how often an event will occur.

Probability is essential in machine learning, with applications such as:

- Maximum likelihood, finding model parameters that maximize the probability of observing training data,
- Kullback-Leibler (KL) divergence minimization, forcing two distributions to be similar, used in training generative models for realistic images or text,
- Reinforcement learning, modeling a policy as a probability distribution over actions based on the current state.

## Frequentist vs. Bayesian Probability

There are two main perspectives on probability - the Frequentist perspective and the Bayesian perspective.

### Frequentist Perspective 

The Frequentist probability measures the frequency at which an event occurs. It is calculated by the number of times it occurs in a large number of trials.

Below is an example of calculating the probability of rolling a four on a six-sided die. We roll the die 1000 times and calculate the frequency at which a four is rolled. The probability of rolling a four is the frequency of rolling a four divided by the total number of trials:

```python
from collections import Counter
import random

num_trials = 1000
dice_sides = 6

results = Counter()
for i in range(num_trials):
    result = random.randint(1, dice_sides)
    results[result] += 1

prob = results[4] / num_trials
print(f"probability of rolling a four: {100 * prob.2f} %")
```

```
probability of rolling a four: 16.80 %
```

### Bayesian Perspective

Bayesian probability expresses belief about event occurrence. It incorporates prior knowledge and uncertainty in probability estimates, which is useful when data is limited, noisy, or ambiguous.

One example of belief in the Bayesian world is the prior, which is a probability distribution that reflects our initial beliefs about how likely an event is. This prior distribution can be based on past experience, expert knowledge, or other sources of information.

In the example of flipping a coin, a natural prior is a fair coin with 50% heads and 50% tails.

Bayesian methods allow us to update this prior using data.  As we receive data from the world, we can use it to update our prior into a posterior.

This represents our revised belief about the event's likelihood, and can become our next prior when we have more data.

```python
import random

def update_belief(prior_heads, prior_total, new_heads, new_flips):
    """Update belief about probability of heads after seeing new flips"""
    return prior_heads + new_heads, prior_total + new_flips

def probability_of_heads(heads, total):
    """Calculate probability of heads"""
    return heads / total

# Starting belief: we've seen 1 heads out of 2 flips
heads = 1
total_flips = 2

print(f"Starting belief: {probability_of_heads(heads, total_flips):.3f}")

# Simulate 10 flips of a biased coin (70% chance of heads)
for flip_number in range(10):
    # Flip coin (True = heads, False = tails)
    new_flip = 1 if random.random() < 0.7 else 0
    
    # Update our belief
    heads, total_flips = update_belief(heads, total_flips, new_flip, 1)
    
    # Calculate and print new probability
    prob = probability_of_heads(heads, total_flips)
    print(f"After flip {flip_number + 1}: {prob:.3f}")
```

```
Starting belief: 0.500
After flip 1: 0.667
After flip 2: 0.750
After flip 3: 0.600
After flip 4: 0.500
After flip 5: 0.429
After flip 6: 0.375
After flip 7: 0.444
After flip 8: 0.500
After flip 9: 0.455
After flip 10: 0.500
```

### Bayes' Theorem

Bayes' Theorem is a mathematical formula that describes how to update our probability estimates based on new data. It states that:

$$\text{Posterior Probability} = \frac{\text{Prior Probability} \times \text{Likelihood}}{\text{Evidence}}$$

Here, the posterior probability is the updated probability estimate, the prior probability is our initial belief about the event's likelihood, the likelihood is the probability of observing the data given the event, and the evidence is the probability of observing the data.

## Classical vs. Modern Statistics

Statistics originated in a world without computers - reaching back to the 17th century.

Statistics emerged at a time when computation was expensive and data was a sparse resource, leading mathematicians to spend a lot of effort to avoid calculations.

Today the inverse is true - we live in a world with access to cheap compute and lots of data.  This means that the best approach to statistics today can differ a lot from statistical techniques taught in the second half of the 20th century - perhaps even what you were taught at school.

An example of this is the rise of bootstrap based methods to calculate confidence intervals and determine statistical significance.

Another example of modern statistics is the double descent curve - a phenomenon where the performance of a model can improve with more data, even after it has started to overfit. This counteracts traditional statistical thinking where the more training you do, the more likely you are to overfit.

## Distributions

A distribution is a set of values and their corresponding probabilities. It describes how likely each value is to occur.

## Central Tendency

The central tendency of is the middle of a distribution.

Three statistics used to measure the central tendency of a distribution are the mean, the median and the mode.  

The mean will be influenced by outliers (extreme values), where the median is not influenced by outliers.

Measures of central tendency are not appropriate for multi modal data, as the data has multiple middles.

Central tendency is meaningful for homogeneous groups, but for diverse groups is can be meaningless.

### Mean

The mean, also known as the average, is a measure of central tendency that represents the typical or representative value of a distribution.

It is calculated by summing up all the values in the distribution and dividing by the total number of values. In mathematical notation, the mean is denoted by the symbol $\mu$ (pronounced "mu"), and it is calculated as:

$$
\mu = \frac{\sum_{i=1}^{n} x_i}{n}
$$


where $p(x_i)$ is the probability of the value $x_i$.

Alternatively, we can express the mean as a weighted sum of the values, where the weights are given by the probabilities of the values. In mathematical notation, this is:

$$
\mu = \sum_{i=1}^{n} x_i \cdot p(x_i)
$$

where $p(x_i)$ is the probability of the value $x_i$. This formula is particularly useful when dealing with discrete distributions.

The mean demonstrates well the limitations of using a single statistic to represent data.

Take the classic example of the person with their feet in a fridge and head in the fireplace - on average they are comfortable but at both extremes they are not comfortable:

```python
import numpy as np

temperatures = {"head": 40, "body": 37, "feet": 32}

print(sum(temperatures.values()) / len(temperatures))
print(np.mean(temperatures.values()))
```

Another example is taking the average of all the people in a room that includes a single billionaire:

```python
net_worths = [10_000, 50_000, 80_000, 50_000]
print(sum(net_worths) / len(net_worths))

#  now let's add a single millionaire
net_worths = [10_000, 50_000, 80_000, 50_000, 1_000_000]
print(sum(net_worths) / len(net_worths))
```

This sensitivity to extreme values is a weakness of the mean.

The problem with expected value thinking is that sometimes, the expected outcome is impossible!

Also there is no person with this net worth in our dataset.

### Expected Value

The expectation is the same as the mean - a weighted average across all possible outcomes.  The weight is the probability of that event happening.

When a statistician says 'on expectation' or 'the expected value of this function', they mean on average.

```python
win = {'amount': 100, 'probability': 0.1}
lose = {'amount': -10, 'probability': 0.9}

expectation = (win['amount'] * win['probability']) + (lose['amount'] * lose['probability'])
# (100 * 0.9) + (-10 * 0.9)
# 1.0
```

Sometimes preferable to take a lower expected value, but higher probability choice

Expected value is distorted with extreme value.

### Median

The median is another measure of central tendency that represents the middle value of a distribution. It is the value that separates the distribution into two equal halves: half of the values are greater than the median, and half of the values are less than the median.

In many ways, the median is the true centre of the data - it's by definition in the middle.  It's also not sensitive to outliers, so it will be a more stable statistic over time.

```python
import numpy as np

def stats(data):
    print(np.mean(net_worths))
    print(np.median(net_worths))

net_worths = [10_000, 50_000, 80_000, 50_000]
stats(net_worths)

#  now let's add a single millionaire
net_worths = [10_000, 50_000, 80_000, 50_000, 1_000_000]
stats(net_worths)
```

### Mode

The mode is the value in a dataset that occurs most frequently. In other words, it is the value that has the highest frequency or probability of occurrence. The mode is denoted by the symbol $M$.

In some cases, there may be more than one mode in a dataset, in which case the dataset is said to be bimodal, trimodal, or multimodal. If there is no value that occurs more frequently than others, the dataset is said to have no mode.

Like the mean and median, the mode is a measure of central tendency that can provide useful information about the dataset. However, it is important to note that the mode is not always a useful or appropriate measure of central tendency, especially when dealing with continuous data.

Advantages:

    Useful for categorical data: The mode is a useful measure of central tendency for categorical data, such as colors, names, or types of products. In such cases, the mode provides information about the most common category in the dataset.

    Easy to calculate: The mode is relatively easy to calculate, especially for small datasets. It simply requires counting the frequency of each value in the dataset and identifying the value(s) with the highest frequency.

Disadvantages:

    Limited use for continuous data: The mode is not a useful measure of central tendency for continuous data, such as height or weight, because the probability of any specific value occurring is very small. In such cases, the mode may not provide any meaningful information about the dataset.

    May not exist or be unique: The mode may not exist or be unique in some datasets, especially those with a uniform or random distribution. In such cases, the mode is not a useful measure of central tendency.

Overall, the mode is a useful measure of central tendency in certain situations, especially for categorical data. However, it should be used with caution and in conjunction with other measures of central tendency, such as the mean and median, to provide a more complete picture of the dataset.

## Quantiles

A quantile cuts and divides a probability distribution.

Quantiles are a way of dividing a distribution into intervals, where each interval contains an equal proportion of the data. The median is a special case of a quantile, where the data is divided into two equal parts. The median is a quantile set at the middle of a distribution.

The mean is good for homogeneous distributions but is sensitive to outliers.

Quantiles are able to deal with heterogeneous distributions - this means that quantiles are useful for summarizing and analyzing distributions that are not uniform or evenly distributed. In other words, they can handle distributions that have significant differences or disparities in the values or frequencies of their data points.

Quantiles are generally less sensitive to outliers than the mean.

### Finding a Quantile

To find the $p$-th quantile of a distribution, we need to find the value $q_p$ such that $p$ percent of the data is below $q_p$, and $(1-p)$ percent of the data is above $q_p$. The $p$-th quantile is denoted by $Q_p$.

For example, the 25th quantile (also known as the first quartile) is the value $Q_{0.25}$ such that 25% of the data is below $Q_{0.25}$ and 75% of the data is above $Q_{0.25}$.

We can find the $p$-th quantile of a distribution using the numpy.quantile function. For example, to find the first quartile of the net_worths list, we can use:

```python
import numpy as np

net_worths = [10_000, 50_000, 80_000, 50_000, 1_000_000]
q1 = np.quantile(net_worths, 0.25)
print(q1)
```

In this example, the first quartile is $50,000$.

We can also find multiple quantiles at once using the numpy.quantile function. For example, to find the first and third quartiles of the net_worths list, we can use:

```python
import numpy as np

net_worths = [10_000, 50_000, 80_000, 50_000, 1_000_000]
q1, q3 = np.quantile(net_worths, [0.25, 0.75])
print(q1, q3)
```

In this example, the first quartile is $50,000$ and the third quartile is $80,000$. We can use the first and third quartiles to calculate the interquartile range (IQR), which is a measure of the spread of the middle 50% of the data:

```python
import numpy as np

net_worths = [10_000, 50_000, 80_000, 50_000, 1_000_000]
q1, q3 = np.quantile(net_worths, [0.25, 0.75])
iqr = q3 - q1
print(iqr)
```

## Deviation 

Deviation measures are used to characterize how spread out or random a distribution is.  You should be thinking about deviation measures as measuring the space or width of a distribution.

### Mean Absolute Deviation

Mean absolute deviation is the average of the absolute differences between each value in the dataset and the mean:

$$
\text{MAD} = \frac{1}{n} \sum_{i=1}^{n} |x_i - \bar{x}|
$$

```python
import numpy as np

wide = np.random.uniform(low=0, high=10, size=5)
narrow = np.random.uniform(low=4, high=6, size=5)

def mean_absolute_deviation(data):
    mu = np.mean(data)
    return np.mean(np.abs(data - mu))

print(mean_absolute_deviation(wide), mean_absolute_deviation(narrow))
```

### Maximal Deviation

Maximal deviation is the largest absolute difference between any value in the dataset and the mean:
$$
d_{\max} = \max_i |x_i - \bar{x}|
$$

```python
import numpy as np

# create two numpy arrays of size 5 with random uniform values
wide = np.random.uniform(low=0, high=10, size=5)
narrow = np.random.uniform(low=4, high=6, size=5)

def max_deviation(data):
    mu = np.mean(data)
    return np.max(np.abs(data - mu))

print(max_deviation(wide), max_deviation(narrow))
```

### Standard Deviation

The most commonly used deviation measure is the standard deviation, which measures the spread of the dataset from the mean. It is calculated by taking the square root of the variance:

$$
\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})^2}
$$

where $\mu$ is the mean of the dataset, and $n$ is the number of values in the dataset.

```python
import numpy as np

# create two numpy arrays of size 5 with random uniform values
wide = np.random.uniform(low=0, high=10, size=5)
narrow = np.random.uniform(low=4, high=6, size=5)

def standard_deviation(data):
    mu = np.mean(data)
    return np.sqrt(np.mean((data - mu)**2))

print(standard_deviation(wide))
print(standard_deviation(narrow))
```

If the data is not normally distributed, then the standard deviation may not accurately capture the spread of the dataset.

If a dataset is highly skewed, with most of the values concentrated on one side of the mean, the standard deviation may be larger than expected, because it is influenced by the few extreme values on the other side of the mean. 

If a dataset has multiple peaks or modes, the standard deviation may not accurately capture the spread of each individual mode.


### Variance

The variance is a measurement of how far a variable is away from the mean - technically it is the squared deviation from the mean.

Variance is a measure of how much of the dataset's variance is due to randomness. It is calculated as the average of the squared deviations from the mean:

$$
\sigma^2 = \frac{\sum_{i=1}^{n}(x_i - \mu)^2}{n}
$$

where $x_i$ is the $i^{th}$ value in the distribution, $\mu$ is the mean of the distribution, and $n$ is the number of values in the distribution.

```python
import numpy as np

# create two numpy arrays of size 5 with random uniform values
wide = np.random.uniform(low=0, high=10, size=5)
narrow = np.random.uniform(low=4, high=6, size=5)

def variance(data):
    mu = np.mean(data)
    return np.mean((data - mu)**2)

print(variance(wide))
print(variance(narrow))
```

Variance is closely related to standard deviation, as the standard deviation is the square root of the variance.

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(np.var(data))
```

One limitation of the variance is that it is in squared units, which can be difficult to interpret. To address this, the standard deviation is often used instead, which is simply the square root of the variance:

$$
\sigma = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \mu)^2}{n}}
$$

```python
import numpy as np

data = np.array([1, 2, 3, 4, 5])
print(np.std(data))
```

## Covariance

The covariance is a measure of how two variables change together, and it is defined as the expected value of the product of the deviations of the two variables from their respective means. A positive covariance indicates that the variables tend to move in the same direction, while a negative covariance indicates that the variables tend to move in opposite directions.

The covariance between two random variables X and Y is given by the formula:

$$ Cov(X, Y) = E[(X - \mu_X) \cdot (Y - \mu_Y)] $$

where $E$ denotes the expected value, $\mu_X$ is the mean of X, and $\mu_Y$ is the mean of Y.

Covariance can take on any value, positive or negative, depending on the relationship between the two variables. A positive covariance indicates that the two variables tend to increase or decrease together, while a negative covariance indicates that one variable tends to increase when the other decreases.

In Python, we can use the NumPy library to compute the covariance between two arrays of data. Here is an example:

The negative covariance indicates that the variables tend to move in opposite directions.

One limitation of covariance is that it is not standardized, which makes it difficult to compare covariances across different datasets. To overcome this limitation, we can use the correlation coefficient.

## Correlation

Correlation measures the strength of the relationship between two variables. It is a statistical technique used to determine how strongly two variables are related to each other. Correlation is typically measured using a correlation coefficient, which can range from -1 to +1.

A correlation coefficient of -1 indicates a perfect negative correlation, meaning that as one variable increases, the other variable decreases by an exact amount. A correlation coefficient of +1 indicates a perfect positive correlation, meaning that as one variable increases, the other variable also increases by an exact amount. A correlation coefficient of 0 indicates no correlation between the two variables.

### Pearson

Pearson correlation is a measure of the linear correlation between two variables. It is the most commonly used correlation coefficient, and is denoted by the symbol $r$. 

The Pearson correlation coefficient ranges from -1 to +1, where -1 indicates a perfect negative correlation, 0 indicates no correlation, and +1 indicates a perfect positive correlation.

The formula for Pearson correlation coefficient is:

$$
r_{X,Y} = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_i - \bar{X})^2} \sqrt{\sum_{i=1}^{n}(Y_i - \bar{Y})^2}}
$$

where $x_i$ and $y_i$ are the values of the two variables for the $i^{th}$ observation, and $\bar{x}$ and $\bar{y}$ are their means.

```python
import numpy as np
from scipy import stats

# generate data
independent = np.random.uniform(size=100)
dependent = independent + np.random.normal(size=100)
noise = np.random.normal(size=100)

# calculate Pearson correlation coefficient
r, p_value = stats.pearsonr(independent, dependent)
print("Pearson correlation coefficient:", r)
```

### Spearman

Spearman correlation is a non-parametric measure of the correlation between two variables. It is used when the variables are not normally distributed or when the relationship between the variables is non-linear. The Spearman correlation coefficient, denoted by the symbol $r_s$, ranges from -1 to +1, where -1 indicates a perfect negative correlation, 0 indicates no correlation, and +1 indicates a perfect positive correlation.

The formula for Spearman correlation coefficient is:

$$
\rho = 1 - \frac{6 \sum_{i=1}^{n} d_i^2}{n(n^2-1)}

$d_i = rank(X_i) - rank(Y_i)
$$

where $d_i$ is the difference between the ranks of $X_i$ and $Y_i$.

The Spearman correlation is based on the ranks of the observations so is more robust to outliers.

```python
import numpy as np
from scipy import stats

# generate data
independent = np.random.uniform(size=100)
dependent = independent + np.random.normal(size=100)
noise = np.random.normal(size=100)

# calculate Spearman correlation coefficient
rho, p_value = stats.spearmanr(independent, dependent)
print("Spearman correlation coefficient:", rho)
```

## Law of Large Numbers

The Law of Large Numbers states that as the sample size increases, the sample mean will tend to approach the population mean. Mathematically, for a sequence of independent and identically distributed (IID) random variables $X_1, X_2, ..., X_n$, with expected value $\mu$ and variance $\sigma^2$, the sample mean $\bar{X}$ approaches $\mu$ as $n$ approaches infinity:

$$\lim_{n\to\infty} \bar{X} = \mu$$

This is why statistics works - with more data, we can obtain more accurate estimates of the population statistics like the mean.

On the other hand, a single sample is high variance and should not be trusted as it may not be representative of the population.
