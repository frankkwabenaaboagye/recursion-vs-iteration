"""Sum of digits problem: recursive vs iterative.

- Iterative implementation is provided.
- Recursive implementation is left as an exercise.
"""

from __future__ import annotations


def sum_digits_recursive(n: int) -> int:
    """Return the sum of the digits of a non-negative integer ``n`` using
    recursion.

    Example:
        sum_digits_recursive(0)   == 0
        sum_digits_recursive(123) == 6

    Hint:
        Separate last digit and "rest":
            last_digit = n % 10
            rest      = n // 10
    """

    # since the iterative version explicitly says Assumes n >= 0
    # I will not be raising an error for negative numbers

    # This is the base case: when n reaches 0, there are no digits left to sum
    if n == 0:
        return 0
    else:
        # In the recursive case:
        # - we extract the last digit
        # - and then recurse on the remaining digits
        last_digit = n % 10
        rest = n // 10
        return last_digit + sum_digits_recursive(rest)


def sum_digits_iterative(n: int) -> int:
    """Return the sum of the digits of a non-negative integer ``n`` using
    iteration (no recursion).

    Assumes ``n`` is >= 0.
    """
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
