"""Integer power problem: recursive vs iterative.

- Recursive implementation is provided.
- Iterative implementation is left as an exercise.
"""

from __future__ import annotations


def power_recursive(base: int | float, exponent: int) -> int | float:
    """Compute ``base ** exponent`` using recursion for integer exponent >= 0.

    Requirements:
    - ``exponent`` must be >= 0, else raise ValueError.
    - ``power_recursive(x, 0) == 1`` for any non-zero x.
    """
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)


def power_iterative(base: int | float, exponent: int) -> int | float:
    """Compute ``base ** exponent`` using iteration (no recursion).

    You must not call ``power_recursive`` here.
    """
    raise NotImplementedError
