"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.


# TODO: Implement for Task 0.1.

def mul(x, y):
    return x * y


def id(x):
    return x


def add(x, y):
    return x + y


def neg(x):
    return float(-x)


def lt(x, y):
    return 1.0 if x < y else 0.0


def eq(x, y):
    return 1.0 if x == y else 0.0


def max(x, y):
    return x if x > y else y


def is_close(x, y):
    return abs(x - y) < 1e-2


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def relu(x):
    return (x > 0) * x


EPS = 1e-6


def log(x):
    return math.log(x + EPS)


def exp(x):
    return math.exp(x)


def log_back(x, d):
    return d / x


def inv(x):
    return 1 / x


def inv_back(x, d):
    return -d / x ** 2


def relu_back(x, d):
    return d if x > 0 else 0.0


def sigmoid_back(x, d):
    return d * exp(-x) / ((1 + exp(-x)) ** 2)



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
