"""Flatten nested list problem: recursive vs iterative.

- Recursive implementation is provided.
- Iterative implementation is left as an exercise.
"""

from __future__ import annotations

from typing import Any, List


def flatten_recursive(nested: List[Any]) -> List[Any]:
    """Flatten a list that may contain nested lists into a single list
    (recursively).

    Example:
        flatten_recursive([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]

    Rule:
        - Only lists are considered "containers" to be flattened.
        - Other types (int, str, etc.) are treated as atomic elements.
    """
    flat: List[Any] = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_recursive(item))
        else:
            flat.append(item)
    return flat


def flatten_iterative(nested: List[Any]) -> List[Any]:
    """Flatten a nested list using an explicit stack and iteration
    (no recursion).

    Hint:
        Use your own list as a stack:
            stack = [nested]
        Then repeatedly pop from the stack and push its elements.
    """

    # to hold the final flattened result
    flat = []

    # using an explicit stack to avoid recursion
    stack = [nested]

    # process the stack until is empty
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            # Push elements of the list onto the stack in reverse order
            # we reverse to maintain the original order when popping
            stack.extend(reversed(current))
        else:
            # atomic element, add to the result
            flat.append(current)
    return flat