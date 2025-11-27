"""Example problem: sum elements of a list (recursive vs iterative).

This module is **fully implemented** and serves as a reference.
Participants can look at this file to see one clear example of how to
implement both a recursive and an iterative solution for the same
problem.
"""

from __future__ import annotations

from typing import List


def sum_list_recursive(nums: List[int]) -> int:
    """Return the sum of all integers in ``nums`` using recursion.

    Recursive structure:
    - Base case: empty list -> 0
    - Recursive case: first element + sum of the rest
    """
    if not nums:
        return 0
    return nums[0] + sum_list_recursive(nums[1:])


def sum_list_iterative(nums: List[int]) -> int:
    """Return the sum of all integers in ``nums`` using iteration.

    This version uses a simple loop and an accumulator variable.
    """
    total = 0
    for n in nums:
        total += n
    return total
