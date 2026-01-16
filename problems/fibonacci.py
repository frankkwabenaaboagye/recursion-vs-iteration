"""Fibonacci problem: recursive vs iterative.

- Iterative implementation is provided.
- Recursive implementation is left as an exercise.
"""

from __future__ import annotations


def fib_recursive(n: int) -> int:
    """Return the n-th Fibonacci number using recursion.

    We use 0-based indexing:
        fib(0) = 0
        fib(1) = 1
        fib(2) = 1
        fib(3) = 2
        fib(4) = 3
        ...

    - Raise ValueError if n < 0.

    Your task: implement this recursively (naive recursion is fine).
    """

    # guarding against invalid input
    if n < 0:
        raise ValueError("n must be non-negative")
    
    # the base case
    # recursion stops when n = 0 or when n = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # recursive case
    # each fibonacci number is the sum of the two preceding ones
    # the maths definition is:
    # fib(n) = fib(n-1) + fib(n-2) for n >= 2
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """Return the n-th Fibonacci number using iteration (no recursion)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
