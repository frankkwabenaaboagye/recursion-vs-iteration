"""Factorial problem: recursive vs iterative.

- Recursive implementation is provided.
- Iterative implementation is left as an exercise.
"""

from __future__ import annotations


def factorial_recursive(n: int) -> int:
    """Return n! using a recursive algorithm.

    Constraints:
    - n is a non-negative integer.
    - 0! == 1
    - Raise ValueError if n < 0.

    Hint (recursive structure):
        n! = n * (n-1)!  with base case 0! = 1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Return n! using an *iterative* algorithm (no recursion).

    You should use a loop (for or while). Do NOT call ``factorial_recursive``
    here.
    """
    raise NotImplementedError
