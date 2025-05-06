---
title: Linear Algebra
summary: TODO
draft: true
competencies:
- Analytics
---

## Why Learn Linear Algebra?

Linear algebra is the computational engine that powers modern data science and machine learning. Its importance goes beyond theoretical mathematics—it's the key to unlocking computational efficiency on today's hardware and implementing powerful mathematical algorithms.

- **Dimensionality Reduction**
- **Machine Learning**
- **Neural Networks**
- **Parallelization**: Linear algebra operations are naturally parallelizable, making them ideal for modern multi-core CPUs and GPUs. Matrix multiplication, for example, can be split across hundreds or thousands of processing cores simultaneously.
- **GPU Acceleration**: GPUs were originally designed for graphics rendering—a deeply linear algebraic process. Their architecture is perfectly suited for matrix operations, offering 10-100x speedups for tasks like neural network training.
- **Memory Efficiency**: Well-implemented linear algebra allows for cache-friendly memory access patterns, reducing bottlenecks in data movement between memory and compute units.

### Mathematical Capabilities

- **Transformations**: Linear algebra gives us powerful tools to transform data through operations like rotation, scaling, projection, and reflection—all expressible as matrix operations.
- **Systems of Equations**: Solve complex systems of linear equations efficiently using techniques like Gaussian elimination, LU decomposition, and matrix inversion. An example of linear regression, where the closed-form solution to fitting a linear model involves matrix multiplication and inversion.
- **Dimensionality Reduction**: Algorithms like Principal Component Analysis (PCA) and Singular Value Decomposition (SVD) help identify patterns in high-dimensional data and reduce dimensions while preserving key information.

- **Eigendecomposition**: Find eigenvalues and eigenvectors to understand the fundamental properties of linear systems, identify principal directions of variation, and solve differential equations.

### Algorithms Enabled by Linear Algebra

- **Optimization Algorithms**: Gradient descent, conjugate gradient methods, and Newton's method rely on linear algebra for efficient parameter updates in machine learning models.
- **Matrix Factorizations**: Techniques like QR, Cholesky, and LU decompositions enable stable and efficient solutions to many computational problems.
- **Spectral Methods**: Analyze graphs, networks, and signals by examining the spectrum (eigenvalues) of associated matrices.
- **Linear Regression**: The workhorse of predictive modeling uses the normal equation (a linear algebraic formulation) for exact solutions.
- **Recommendation Systems**: Matrix factorization methods like SVD and Alternating Least Squares power many collaborative filtering systems.

## Tooling

To run the Python code in this lesson, you need a Python interpreter and to install the following Python packages:

```shell-session
# TODO - pip versions???
$ pip install -q numpy pandas matplotlib
```

Give examples of JAX and PyTorch as well?

## Resources

Chapter 2 of [Deep Learning - Ian Goodfellow, Yoshua Bengio and Aaron Courville](https://www.deeplearningbook.org/)

[Array programming with NumPy - Nature](https://www.nature.com/articles/s41586-020-2649-2)

[Matrix Cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)

[A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/) 

[Understanding the internals of NumPy to avoid unnecessary array copying](https://ipython-books.github.io/45-understanding-the-internals-of-numpy-to-avoid-unnecessary-array-copying/)

Scipy lectures:
- [1.3. NumPy: creating and manipulating numerical data](http://scipy-lectures.org/intro/numpy/index.html)
- [2.2. Advanced NumPy](http://scipy-lectures.org/advanced/advanced_numpy/)

## Why Learn NumPy?

NumPy is a foundational part of the SciPy Python ecosystem. Central to NumPy is a n-dimensional array.  

Working with a NumPy array is fast - it stores and operates on data using C structures.

Pandas, a popular tabular data Python library, sits on top of `numpy`. Below we access the numpy array that holds data in a Pandas dataframe:

```python
import pandas as pd

pd.DataFrame([1, 2]).values
```

PyTorch, the leading Python deep learning library, uses NumPy arrays as input and output:

```python
TODO
```

Functionality
- vector, matrix & tensor operations

Uses less memory
- fixed data types

### Speed

- fixed data types (benefit from static typing)
- C implementation

Below we implement a sum operation using a Python loop:

```python
def loop(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    data = np.zeros(left.shape[0])
    for i in range(data.shape[0]):
        data[i] = left[i] + right[i]
    return data
    
left = np.arange(10000000)
right = np.arange(10000000)

# TODO - add timing
lp = loop(left, right)
```

Now lets try it using `numpy` addition:

```python
# TODO - add timing
check = left + right
assert check == lp
```

Note that not only is NumPy quicker, it is also **more readable**!

### Vectorization

The reason that `numpy` is faster is **vectorization**
- running multiple operations from a single instruction

Many CPU's have operation that run in parallel (modern x86 chips have the SSE instructions)

Vectorization is
- the process of rewriting a loop 
- instead of processing a single element of an array N times
- it processes 4 elements of the array simultaneously N/4 times

## The `np.array`

shape, dimensions (same as axes or rank), size

### `list` versus `np.array`

Python list
- general-purpose container - can hold different data types
- support (fairly) efficient insertion, deletion, appending, and concatenation
- list comprehensions make them easy to construct and manipulate
- only a few list operations can be carried out in C (because of the need for type checking)
- the list holds pointers to items scattered across memory

Numpy array
- **only one data type**
- less flexible
- vectorized operations
- fixed size
- data in one place in memory

Only holding one data type means that numpy can efficiently store data in memory

A list doesn't know what the next object will be - this makes storing it in memory challenging

```python
[0, 1.0, '2.0']
```

We can make an array from a list - `numpy` will make assumptions about what datatype the array should hold:
<!-- #endregion -->

```python
#  the integer 10 is converted to a float
a = np.array([10, 20.0, 0])
```

```python
a[0] = '3'
```

```python
a.dtype
```

We can see the data type by accessing the `.dtype` attribute:

```python
#  64 bits (0 or 1) per float
np.array([10, 20.0]).dtype
```

We can change the datatype of an array:

```python
np.array([10, 20.0]).astype('int')
```

Note that changing the datatype will by default create a newly allocated array (new location in memory) - you can control this using a an argument:

```python
np.array([10, 20.0], copy=False).astype('int')
```

We can see the number of elements in an array:

```python
np.array([10, 20.0, 30]).size
```

For a vector the size will be the same as the shape:

```python
np.array([10, 20.0, 30]).shape
```

We can also get the number of elements in a vector using the Python bulitin `len`:

```python
len(np.array([10, 20.0, 30]))
```


## Scalars

Let's start with the most basic building block of linear algebra: the scalar.

A scalar is a single number:

```python
x = np.array(3)
```

You can think about the scalar as a single point on a line:

```goat
                         x
                         ▼
    -3  -2  -1   0   1   2   3
     |   |   |   |   |   |   |
  ---+---+---+---+---+---+----->
```

Our scalar has no shape:

```python
print(x.shape)
```

Our scalar has no dimensions:

```python
print(x.ndim)
```

```python
print(x.size)
```

## Vectors

A vector has multiple dimensions.

$\textbf{x} = \begin{bmatrix}x_{1} \\ x_{2} \\ \vdots \\ x_{n} \end{bmatrix}$

- array of $n$ numbers
- lowercase, bold 
- $x_{1}$ = first element
- line

A two dimensional vector is a list of two numbers:

```python
y = np.array([2, 3])
```

```goat
y
   ^     v = [2,3]
 4 |                ↗
   |
 3 |            •
   |
 2 |        ↗
   |
 1 |   ↗
   |
 0 +---+---+---+---+---> x
   0   1   2   3   4
```

A vector has a shape:

```python
print(y.shape)
```

```
(2,)
```

### Vectors

$\begin{bmatrix}x_{1} & x_{2} & \cdots & x_{n} \end{bmatrix}$

- array of $n$ numbers
- lowercase, bold $\textbf{x}$
- $x_{1}$ = first element
- line


We can visualize a vector as a line:

```python
data = np.array([4, 6, 8, 8, 6, 4])

_ = plt.plot(data)
```

### Vector Arithmetic

In Python when we add iterables together they are joined:

```python
[0, 1, 2] + [1]
```

`numpy` works differently - addition works **element wise**:

<img src="assets/add.png" alt="" width="300"/>

```python
np.array([1, 2]) + np.array([1, 1])
```

All of the logic above holds for subtraction, multiplication etc:

```python
np.array([0, 1, 2]) - np.array([1]) 
```

```python
np.array([0, 1, 2]) * np.array([2]) 
```

All of these are examples of broadcasting.

### Broadcasting

The smaller array will be broadcast across the larger array

<img src="assets/broad.png" alt="" width="300"/>

```python
np.array([1, 2]) + np.array([1.6]) 
```

Note how different adding lists together is:

```python
[1, 2] + [1.6]
```

Broadcasting is important because the larger array **keep its shape**
- matrix multiplication (ie dot products) often result in differently shaped arrays

### Working in a single dimension

Vectors - flat lists

#### Indexing

<img src="assets/idx.png" alt="" width="500"/>

#### Aggregation

<img src="assets/agg.png" alt="" width="800"/>

### Vector norms

Size of a vector

Function that maps from a vector to a non-negative scalar

$||x||_{p} = \left( \sum |x|^{p} \right)^{\frac{1}{p}} $

A common operation in machine learning is **gradient clipping** - this can be done by clipping by value, norm or global norm
- global norm will keep their relative scale 

We can do a norm in `numpy` using:

```python
p = 2

# %timeit sum([abs(x)**p for x in data])**(1 / p)
```

```python
data = np.arange(100000)

# %timeit np.linalg.norm(data, ord=2)
```

There are various kinds of norms:
- $L^1$ = used when the difference between 0 and close to 0 elements is important = encourages sparsity when used for regularization
- $L^2$ = Euclidean norm

### Practical - Euclidean norm

Implement $L^{2}$ norm in pure Python

```python

```

### Making vectors

`np.arange` - similar to the Python builtin `range`

```python
np.arange(start=0, stop=10, step=2)
```

`np.linspace` - evenly spaced between two points

```python
np.linspace(0, 100, 15)
```

### Sampling random uniform

This can be done two ways
- `np.random.random`
- `np.random.rand`

Only difference is the shape argument is not a tuple
- saves writing the brackets

Sample uniformly across the interval [0, 1)

```python
#  shape defined as a tuple
np.random.random((2, 4))
```

```python
#  shape defined as *args
np.random.rand(2, 4)
```

### Sample from a standard normal

`np.random.randn`

$\mathcal{N}(0,1)$

```python
np.random.randn(2, 4)
```

### Sample from a Gaussian

`np.random.normal`

$\mathcal{N}(\mu,\sigma)$

We choose the statistics (mean & standard deviation)

```python
np.random.normal(1, 2, size=(2, 4))
```

#### Matrix

$\textbf{A}_{2, 2} = \begin{bmatrix}A_{1, 1} & A_{1, 2} \\ A_{2, 1} & A_{2, 2}\end{bmatrix}$

- two dimensional
- uppercase, bold $\textbf{A}_{m, n}$
- $A_{1, 1}$ = first element
- area

## Matricies

### Eigenvalues and Eigenvectors

How to compute them using NumPy (np.linalg.eig())
Visualization of eigenvectors as "directions that don't change under transformation"
Applications in stability analysis, differential equations, and PCA

---

Eigenvalues and eigenvectors are crucial in:

- Principal Component Analysis (PCA): Finding the directions of maximum variance in data
- Differential Equations: Solving systems of differential equations
- Google's PageRank Algorithm: Determining webpage importance
- Quantum Mechanics: Describing quantum states
- Stability Analysis: Determining whether a system is stable
- Machine Learning: Used in various algorithms including dimensionality reduction

#### Analogies for Eigenvalues and Eigenvectors

A workable analogy for eigenvalues and eigenvectors is with factors of an integer.

We can factor the integer 9 into factors of (3, 3) and (9, 1).

Just as we decompose 9 into its fundamental components (3 and 3), we can decompose a matrix using eigenvalues and eigenvectors into more fundamental components.

For a matrix A, finding its eigenvalues (λ) and eigenvectors (v) allows us to understand the matrix's essential behavior through the relationship:

$$\mathbf{A}\vec{v} = \lambda\vec{v}$$

Just as the factors of 9 tell us something about its divisibility and structure, the eigenvalues and eigenvectors of a matrix tell us about its fundamental properties:

- **Scale** - Eigenvalues tell us about scaling (stretching or shrinking) in key directions.
- **Direction** - Eigenvectors tell us what those key directions are.

So when we have a matrix $\mathbf{A}$ with eigenvector $\vec{v}$ and eigenvalue $\lambda$, the relationship $\mathbf{A}\vec{v} = \lambda\vec{v}$ shows us that applying the matrix to that special direction (the eigenvector) is equivalent to simple scaling by the eigenvalue.


#### Numpy

```python
import numpy as np

# Create a 2x2 matrix
A = np.array([[3, 1], 
              [1, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors (as columns):")
print(eigenvectors)

# Verify the eigenvector property: A·v = λ·v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lambda_v = eigenvalues[i] * v
    Av = A @ v
    
    print(f"\nFor eigenvalue {eigenvalues[i]:.2f}:")
    print(f"A·v = {Av}")
    print(f"λ·v = {lambda_v}")
    print(f"Difference: {np.linalg.norm(Av - lambda_v):.10f}")
```

```python
import jax
import jax.numpy as jnp

# Create a 2x2 matrix
A = jnp.array([[4, 2], 
               [1, 3]])

# JAX doesn't have a direct eigendecomposition function like NumPy
# We can use the SciPy-like API in JAX
from jax.scipy.linalg import eigh

# Note: eigh is for Hermitian (symmetric) matrices
# For general matrices, you can use the following function:
def eig(A):
    # This is a simplified version - JAX has more optimized methods for production
    # For a real demonstration, you would use jax.scipy.linalg.eig,
    # but we implement a basic version for clarity
    return jnp.linalg.eig(A)

eigenvalues, eigenvectors = eig(A)

print("Matrix A:")
print(A)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors (as columns):")
print(eigenvectors)

# Verify the eigenvector property using JAX: A·v = λ·v
def verify_eigenvector(A, v, eigenvalue):
    Av = A @ v
    lambda_v = eigenvalue * v
    difference = jnp.linalg.norm(Av - lambda_v)
    return Av, lambda_v, difference

# Use JAX's vmap to vectorize this operation across all eigenvectors
vectorized_verify = jax.vmap(
    lambda i: verify_eigenvector(A, eigenvectors[:, i], eigenvalues[i]), 
    out_axes=1
)(jnp.arange(len(eigenvalues)))

Avs, lambda_vs, differences = vectorized_verify

for i in range(len(eigenvalues)):
    print(f"\nFor eigenvalue {eigenvalues[i]}:")
    print(f"A·v = {Avs[:, i]}")
    print(f"λ·v = {lambda_vs[:, i]}")
    print(f"Difference: {differences[i]}")
```

### Eigendecomposition

If a matrix has a complete set of eigenvectors (which is always true for symmetric matrices), we can decompose it as:

$$A = PDP^{-1}$$

Where:
* P is the matrix of eigenvectors (as columns)
* D is the diagonal matrix of eigenvalues
* P⁻¹ is the inverse of P

\text{Where:}
\begin{itemize}
\item P \text{ is the matrix of eigenvectors (as columns)}
\item D \text{ is the diagonal matrix of eigenvalues}
\item P^{-1} \text{ is the inverse of } P
\end{itemize}

## Matrix Decompositions

These should follow the Eigenvalues and Eigenvectors section, as many decompositions build on these concepts. This section would cover:

SVD (Singular Value Decomposition)
QR Decomposition
LU Decomposition
Cholesky Decomposition
How to implement these using NumPy's linalg module
Applications of each decomposition type

#### Tensor

- n-dimensional
- 3 = volume
- uppercase, bold $\textbf{A}_{i,j,k}$

This notebook uses many images from the excellent [A Visual Intro to NumPy and Data Representation](https://jalammar.github.io/visual-numpy/) from [Jay Alammar](https://jalammar.github.io/).

In the first notebook ([vector.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/1.vector.ipynb)) we dealt with vectors (one dimensional). 

Now we deal with **Matricies** - arrays with two dimensions.

$\textbf{A}_{2, 2} = \begin{bmatrix}A_{1, 1} & A_{1, 2} \\ A_{2, 1} & A_{2, 2}\end{bmatrix}$

- two dimensional
- uppercase, bold $\textbf{A}_{m, n}$
- $A_{1, 1}$ = first element
- area
- tabular data

### Reshaping

Now that we have multiple dimensions, we need to start considering shape.

We can see the shape using `.shape`

```python
data = np.arange(16)

data.shape
```

And the number of elements using `.size`

```python
data.size
```

The **shape** of a matrix becomes more than just an indication of the length.  We can change the shape using reshape:

```python
data.reshape(4, 4)
```

A very useful tool when reshaping is using `-1` - this is a free dimension that will be set to match the size of the data
- this is often set to the batch / number of samples dimension

```python
data.reshape(2, -1)
```

```python
data.reshape(-1, 4)
```

We can use `.reshape` to flatten

```python
data.reshape(-1)
```

We can also use `.flatten`

```python
data.flatten()
```

And finally `.ravel`

```python
data.ravel()
```

`.flatten` always returns a copy - `.ravel` doesn't (if it can)

Closely related to a reshape is the **transpose**, which flips the array along the diagonal:

<img src="assets/trans.png" alt="" width="300"/>

```python
np.arange(0, 6).reshape(3, -1)
```

```python
np.arange(0, 6).reshape(3, -1).T
```

Reshape is (usually) computationally **cheap** - to understand why we need to know a little about how a `np.array` is laid out in memory

### The `np.array` in memory

- the data is stored in a single block
- the shape is stored as a tuple

Why is storing in a single block (known as a contiguous layout) a good thing?
- to access the next value an the array 
- we just move to the next memory address
- length = defined by the data type

> ... storing data in a contiguous block of memory ensures that the architecture of modern CPUs is used optimally, in terms of memory access patterns, CPU cache, and vectorized instructions - [iPython coobook](https://ipython-books.github.io/45-understanding-the-internals-of-numpy-to-avoid-unnecessary-array-copying/)

Changing the shape only means changing the tuple 
- the layout of the data in memory is not changed

The operations that will change the memory layout are ones that change the order of the data - for example a transpose:

```python
data = np.arange(10000000).reshape(5, -1)
res = %timeit -qo data.reshape((1, -1))
'{:.8f} seconds'.format(res.average)
```

```python
data = np.arange(10000000).reshape(5, -1)
res = %timeit -qo data.T.reshape((1, -1))
'{:.8f} seconds'.format(res.average)
```

### Two dimensional indexing

<img src="assets/idx2.png" alt="" width="500"/>

```python
data = np.random.rand(2, 3)
data
```

We specify both dimensions using a familiar `[]` syntax

`:` = entire dimension

```python
#  first row
data[0, :]
```

`-1` = last element

```python
#  last column
data[:, -1]
```

#### Two dimension aggregation

<img src="assets/agg-2d.png" alt="" width="900"/>

Now that we are working in two dimensions, we have more flexibility in how we aggregate
- we can specify the axis (i.e. the dimension) along which we aggregate

```python
data
```

```python
#  average over all the data
np.mean(data)
```

```python
#  average over the rows - so we end up with an array with one element per column (3)
np.mean(data, axis=0)
```

```python
#  average over the columns - so we end up with an array with one element per row (2)
np.mean(data, axis=1)
```

By default `numpy` will remove the dimension you are aggregating over:

```python
data
```

```python
np.mean(data, axis=1).shape
```

You can choose to keep this dimension using a `keepdims` argument:

```python
np.mean(data, axis=1, keepdims=True).shape
```

### Practical

Aggregate by variance `np.var` 
- over the rows
- over the columns
- over all data

```python

```

### Two dimensional broadcasting

The general rule with broadcasting - dimensions are compatible when
- they are equal
- or when one of them is 1

<img src="assets/broad-2d.png" alt="" width="500"/>

```python
data = np.arange(1, 7).reshape(3, 2)
data
```

```python
data + np.array([0, 1, 1]).reshape(3, 1)
```

```python
data + 1
```

### Matrix arithmetic

Can make arrays from nested lists:

```python
np.array([[1, 2], [3, 4]])
```

We can add matricies of the same shape as expected:


<img src="assets/add-matrix.png" alt="" width="300"/>

```python
#  more on ones_like below!
data + np.ones_like(data)
```

### Matrix multiplication

This kind of matrix multiplication will often **change the shape** of the array
- this is what happens in neural networks

<img src="assets/dot1.png" alt="" width="900"/>

This operation can be visualized:

<img src="assets/dot2.png" alt="" width="900"/>

```python
data = np.array([1, 2, 3])

powers_of_ten = np.array([10**n for n in range(6)]).reshape(3, 2)

powers_of_ten
```

This is done in numpy using either `np.dot()`:

```python
np.dot(data, powers_of_ten)
```

Or calling the `.dot()` method on the array itself:

```python
data.dot(powers_of_ten)
```

### Making arrays from nested lists

```python
data = np.array([[1, 2], [3, 4]])

data
```

### Making arrays from shape tuples

The argument to these functions is a tuple

#### `zeros`, `ones`, `full`

```python
#  array of all zeros
np.zeros((2, 4))
```

```python
#  array of all ones
np.ones((2, 4))
```

```python
#  array filled with a value we choose
np.full((2, 4), 3)
```

#### `zeros_like`, `ones_like`, `full_like`

Similar to counterparts above, except their shape is defined by another array:

```python
parent = np.arange(10).reshape(2, 5)
parent
```

```python
np.zeros_like(parent)
```

```python
np.ones_like(parent)
```

```python
np.full_like(parent, 3)
```

#### `empty`

Similar to `zeros`, except the array is filled with garbage from RAM 
- this is a bit quicker than `zeros`

```python
d = np.empty(4)
for e in range(4):
    d[e] = e
    
d
```

#### `eye`

Identity matrix :

```python
np.eye(2)
```

The linear algebra verision of a 1

```python
d = np.arange(4).reshape(2, 2)

d
```

```python
np.dot(np.eye(2), d)
```

```python
import numpy as np
```

## Tensors

In the first notebook ([vector.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/1.vector.ipynb)) we dealt with vectors (one dimensional).  In the second notebook ([matrix.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/2.matrix.ipynb)) we looked at arrays with two dimensions.

Now we deal with **Tensors** - arrays that can have many dimensions.

- n-dimensional arrays
- 3 = volume
- uppercase, bold $\textbf{A}_{i,j,k}$

### Working in three dimensions

Extension of two dimensions
- everything we saw in the previous notebook holds

Images
- height
- width
- channels (colors)

Sequential models
- (batch_size, num_timesteps, *features)

```python
#  three rows, three columns, three channels
image = np.random.rand(3, 3, 3)

image.shape
```

### Practical

Create an array filled from a normal distribution, with the shape
- 100 samples
- 64 timesteps
- 32 height
- 16 width
- 3 channels

```python

```

### Practical

Aggregate by standard deviation `np.std` 
- over the width
- over the height
- over the channels
- over all data

```python

```

### Practical - convolution

Implement the convolution operation - we will do this together as a class!

```python

```
# NumPy

<img src="assets/reddit.png" alt="" width="800"/>

A one day course introducing NumPy and linear algebra.  The course is split into three notebooks:
1. [vector.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/1.vector.ipynb) - single dimension arrays
2. [matrix.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/2.matrix.ipynb) - two dimensional arrays
3. [tensor.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/numpy/3.tensor.ipynb) - n dimensional arrays

## Dot-Products
