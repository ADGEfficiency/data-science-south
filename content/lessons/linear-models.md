---
title: Linear Models
summary: TODO
draft: false
competencies:
- Algorithms
---

## Why Learn Linear Models?

The advantage of linear models are:

- **Closed form solutions** - linear models have a closed form solution, which means that convergence is guaranteed.
- **Interpretability** - The coefficients of a linear model are directly proportional to how each feature affects a prediction.

The disadvantages include: 

- **Limited Capacity** - model linear relationships between features,
- **No Feature Interactions** - 
- **Collinarity** - need to consider mutual infomation between features to ensure stable coefficients.

Other things to know:

- **Regularization** - Different regularization penalties can affect feature values (see the section of Regularization)

Linear models are a good choice when:

- there is a linear relationship between the features and the target variable,
- the feature effects are best described with linear combinations of the feature value,
- interpretability is important.

### Linear Models are Used For

The simplest form of the regression equation with one feature is the classic straight line:

$$y = m \cdot x + c$$

In the equation above, $y$ is the target variable, $x$ is the feature, $m$ is the coefficient of our feature (also the slope of the line), and $c$ is the y-intercept.

If we wanted to sound clever, we could describe $y$ as a linear combination of parameters, where our parameters are the slope $m$ and intercept $c$.

Entire or as a part of

Linear regression

Logistic regression

Fully connected neural network layer.  Bias = intercept.  Parameters are learnt.

## Languages of Linear Models (what is another work / phrase to use instead of language - taxonomy etc)

The equation for a linear model is written with two different forms of notation:

$$y = m \cdot x + c$$

$$y = \beta \cdot x + \alpha$$

There are also a few different languages used in linear regression.

The dependent variable $y$ is our target; it is the variable we want to predict.

The independent or explanatory variables $x$ are the variables we use to make predictions. 

It is important to inspect the learned parameters manually and also check the distribution of errors (i.e., through a histogram). In theory, the errors should be normally distributed, which indicates no collinearity between the features.

## Linearity

Linearity concerns how things change.

In a linear system, the system changes at the same rate at all points, while in a nonlinear system, the system changes at different rates at different points. 

This means that in a linear system, if we make a measurement of direction or change, we can be confident that this will hold for other data, but in a nonlinear system, this may not be the case.

Linear functions are additive, meaning that inputs are proportional to outputs. 

Nonlinear functions, on the other hand, are multiplicative and can be caused by accumulation or feedbacks, such as friction or diminishing returns. Networks are highly nonlinear.

## Co-Linearity

Collinearity refers to the correlation between features.

Collinearity can cause instability of parameters, which means we can't interpret the parameters.

If two or more features are highly correlated, it means that they provide redundant information, which can lead to multicollinearity. 

This can make it hard to determine the true relationship between each feature and the target variable, and can also make it difficult to interpret the coefficients of the model. 

It is important to check for collinearity among the features before fitting a linear model, and if collinearity is detected, the features should be removed or combined to reduce redundancy.

### Removing Collinearity

One way to address collinearity is to use Principal Component Analysis (PCA):

```python
from sklearn.decomposition import PCA

samples = 100
data = np.random.uniform(0, 1, size=samples)

dataset = np.vstack([
    data, 
    data + np.random.uniform(0, 0.5, size=samples),
    data - np.random.uniform(0, 0.5, size=samples)
]).T

assert dataset.shape[0] == samples
```

The covariance matrix shows collinearity:

```python
print(np.corrcoef(dataset, rowvar=False))
```

We can use PCA to remove it:

```python
tr = PCA(whiten=True)
clean = tr.fit_transform(dataset)
print(np.corrcoef(clean, rowvar=False))
```

The resulting correlation matrix shows that the features are now uncorrelated.

## Linear Models from Scratch

### Predicting a Constant

The simplest linear model has a single parameter $\alpha$ - for this model, our prediction is always a single value $\alpha$:

$$ y = \alpha $$

```python
import numpy as np

# generate random data
y = np.random.rand(100, 1)

# linear model with a single parameter
beta_0 = 0.5

# predict the target
y_pred = beta_0 * np.ones_like(y)
print(y_pred)
```

This model is the simplest linear model possible - we always predict a constant value.  We don't need or use any features to make this prediction.

### Adding Dependent Variables

We can make our linear model more complex by adding our independent variables $x$:

$$y = \beta \cdot x + \alpha$$

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# generate random data
X = np.random.rand(100, 1)
y = np.random.rand(100, 1)

# linear regression model
model = LinearRegression()

# fit model with features and target
model.fit(X, y)

# predict the target
y_pred = model.predict(X)
print(y_pred)

# the learned coefficients
print("Learned coefficients:", model.coef_)
print("Learned intercept:", model.intercept_)
```

## Least Squares Linear Regression

In the examples above, our parameters $\beta$ and $\alpha$ were given to us.

In reality, we are not given parameters - we must learn them ourselves from data.

The least squares regression problem can be formulated as:

$$\beta = (X^TX)^{-1}X^Ty$$

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# generate random data
X = np.random.rand(100, 1)
y = np.random.rand(100, 1)

# linear regression model
model = LinearRegression()

# fit model with features and target
model.fit(X, y)

# predict the target
y_pred = model.predict(X)
print(y_pred)

# the learned coefficients
print("Learned coefficients:", model.coef_)
print("Learned intercept:", model.intercept_)
```

We can also do this from scratch in raw numpy:

```python
import numpy as np

# generate some random data
X = np.random.rand(100, 3)
y = np.dot(X, np.array([1, 2, 3])) + np.random.normal(size=100)

# compute the least squares solution
beta = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)

# the learned coefficients
print("Learned coefficients:", beta)
```

In this example, we first generate some random data with three independent variables and a dependent variable. We then compute the matrix products $X^TX$ and $X^Ty$ using the numpy.dot() function. Finally, we compute the coefficients $\beta$ using the formula above and the numpy.linalg.inv() function to compute the inverse of $X^TX$.

Note that computing the inverse of a matrix is generally not the most efficient way to solve a linear system of equations, especially for large matrices. In practice, it is often better to use specialized algorithms like QR decomposition or singular value decomposition (SVD) to solve the least squares problem. However, for small matrices, computing the inverse directly can be a reasonable approach.

### Deriving Least Squares

Let's consider the simple case of a linear regression problem with one independent variable. We have a set of $n$ observations $(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)$, where $x_i$ is the value of the independent variable for the $i$th observation, and $y_i$ is the corresponding value of the dependent variable. We want to find the line that best fits the data in a least squares sense, i.e., the line that minimizes the sum of the squared errors between the observed data and the predicted values of the line. The line can be represented as:

$$y = \beta_0 + \beta_1 x$$

where $\beta_0$ is the intercept of the line, and $\beta_1$ is the slope of the line. Our goal is to find the values of $\beta_0$ and $\beta_1$ that minimize the sum of the squared errors:

$$\text{minimize} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2$$

To find the minimum, we take the derivative of the sum of squared errors with respect to each coefficient, set the derivative equal to zero, and solve for the coefficient. Let's start with the intercept $\beta_0$. The derivative with respect to $\beta_0$ is:

$$\frac{\partial}{\partial \beta_0} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2 = -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)$$

Setting this derivative equal to zero and solving for $\beta_0$, we get:

$$\beta_0 = \frac{1}{n} \sum_{i=1}^{n} (y_i - \beta_1 x_i)$$

Next, let's find the derivative with respect to $\beta_1$. The derivative is:

$$\frac{\partial}{\partial \beta_1} \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2 = -2 \sum_{i=1}^{n} x_i (y_i - \beta_0 - \beta_1 x_i)$$

Setting this derivative equal to zero and solving for $\beta_1$, we get:

$$\beta_1 = \frac{\sum_{i=1}^{n} x_i y_i - n \bar{x} \bar{y}}{\sum_{i=1}^{n} x_i^2 - n \bar{x}^2}$$

where $\bar{x}$ and $\bar{y}$ are the sample means of $x$ and $y$, respectively.

In the case of multiple independent variables, the derivation is similar, but the matrix notation is used. We have a matrix $X$ of $n$ observations and $p$ independent variables, where each row of $X$ represents one observation, and a vector $y$ of $n$ dependent variable values. The linear regression model can be written as:

$$y = X\beta$$

where $\beta$ is a vector of $p+1$ coefficients, with the first element representing the intercept. The goal is still to minimize the sum of the squared errors between the observed data and the predicted values of the model. This can be written as:

$$\text{minimize} , ||y - X\beta||^2$$

To find the minimum, we take the derivative of the sum of squared errors with respect to each coefficient, set the derivative equal to zero, and solve for the coefficient. The derivative with respect to $\beta$ is:

$$\frac{\partial}{\partial \beta} ||y - X\beta||^2 = -2X^T(y-X\beta)$$

Setting this derivative equal to zero and solving for $\beta$, we get:

$$\beta = (X^TX)^{-1}X^Ty$$

This expression is known as the normal equations, and it gives the values of the coefficients that minimize the sum of the squared errors. Note that the matrix inversion $(X^TX)^{-1}$ is only possible if $X^TX$ is invertible. This is the case if the columns of $X$ are linearly independent, which means that no column can be expressed as a linear combination of the other columns.

In summary, the least squares method is a widely used technique for finding the coefficients of a linear regression model that best fits the observed data. The derivation involves taking the derivative of the sum of squared errors with respect to each coefficient, setting the derivative equal to zero, and solving for the coefficient. The normal equations provide a convenient way to express the coefficients as a matrix expression, but the matrix inversion is only possible if the columns of the matrix of independent variables are linearly independent.

## Ridge & Lasso Linear Regression

Ridge regression is particularly useful to mitigate the problem of multicollinearity in linear regression, which commonly occurs in models with large numbers of parameters.  The method provides improved efficiency in parameter estimation problems in exchange for a tolerable amount of bias.

Ridge regression is a variant of linear regression that adds a penalty term to the sum of squared errors, to prevent overfitting. The penalty term is a function of the magnitude of the coefficients, and it encourages the coefficients to be smaller in magnitude. This helps to reduce the complexity of the model, and it can improve the generalization performance on new data.

The ridge regression objective function can be written as:

$$\text{minimize} , ||y - X\beta||^2 + \alpha ||\beta||^2$$

Here, $\alpha$ is a hyperparameter that controls the strength of the penalty term. When $\alpha=0$, the ridge regression reduces to ordinary least squares. As $\alpha$ increases, the coefficients are penalized more heavily, and they are pushed towards zero.

```python
import numpy as np
from sklearn.linear_model import Ridge

# generate random data
np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.rand(100, 1)

# create a ridge regression model
model = Ridge(alpha=1.0)

# fit the model to the data
model.fit(X, y)

# make predictions
y_pred = model.predict(X)

# show the learned coefficients
print("Learned coefficients:", model.coef_)
print("Learned intercept:", model.intercept_)
```

Ridge regression is an example of regularization, which is a technique for preventing overfitting by adding a penalty term to the objective function. Regularization can be applied to other types of models as well, including logistic regression, support vector machines, and neural networks. The penalty term can take different forms, depending on the model and the type of regularization.

In addition to ridge regression, another common type of regularization is Lasso regression, which adds a penalty term that is proportional to the absolute value of the coefficients. Lasso regression can be more effective than ridge regression in situations where the number of features is very large and only a small subset of them are important for predicting the outcome.

Regularization is an important technique for building models that generalize well to new data, and it is widely used in machine learning and statistical modeling. The choice of the regularization hyperparameter, such as $\alpha$ in ridge regression, can have a significant impact on the performance of the model, and it is often chosen using cross-validation or other model selection techniques.
