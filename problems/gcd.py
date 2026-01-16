"""Greatest common divisor (GCD) problem: recursive vs iterative.

- Recursive implementation is provided.
- Iterative implementation is left as an exercise.
"""

from __future__ import annotations


def gcd_recursive(a: int, b: int) -> int:
    """Compute the greatest common divisor (GCD) of ``a`` and ``b`` using
    recursion and the Euclidean algorithm.

        gcd(a, b) = gcd(b, a % b)    until b == 0
        gcd(a, 0) = |a|

    You may assume ``a`` and ``b`` are not both zero.
    """
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """Compute the greatest common divisor (GCD) of ``a`` and ``b``
    iteratively using the same Euclidean algorithm.
    """
    # working with absolute values
    a, b = abs(a), abs(b)

    # we continue until b becomes zero
    while b != 0:
        # euclidean step: replace a with b and b with the remainder of a divided by b [a/b]
        a, b = b, a % b

    # when b become 0, the GCD is stored in a
    return abs(a)
