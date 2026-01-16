"""Binary search problem: recursive vs iterative.

- Iterative implementation is provided.
- Recursive implementation is left as an exercise.
"""

from __future__ import annotations

from typing import Sequence


def binary_search_recursive(sorted_seq: Sequence[int], target: int) -> int:
    """Perform binary search recursively.

    Return the index of ``target`` in ``sorted_seq``, or -1 if not found.

    Assumptions:
    - ``sorted_seq`` is sorted in non-decreasing order.
    """
    def helper(lo, hi):

        # base case: target not found,  lo and hi have crossed
        if lo > hi:
            return -1

        # get the middle index and value
        mid = (lo + hi) // 2
        mid_val = sorted_seq[mid]

        if mid_val == target: # if the right value is found, return the index
            return mid
        
        elif mid_val < target: # search in the right half since the mid value is less than the target :: [mid + 1, hi]
            return helper(mid + 1, hi)
        else:
            return helper(lo, mid - 1) # search in the left half since the mid value is greater than the target :: [lo, mid - 1]

    # initial call to the helper function with the full range
    return helper(0, len(sorted_seq) - 1)


def binary_search_iterative(sorted_seq: Sequence[int], target: int) -> int:
    """Perform binary search iteratively using a while loop.

    Return the index of ``target`` in ``sorted_seq``, or -1 if not found.
    """
    lo, hi = 0, len(sorted_seq) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = sorted_seq[mid]
        if mid_val == target:
            return mid
        if mid_val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
