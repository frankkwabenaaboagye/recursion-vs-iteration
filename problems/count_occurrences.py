"""Count occurrences in nested list problem: recursive vs iterative.

- Iterative implementation is provided.
- Recursive implementation is left as an exercise.
"""

from __future__ import annotations

from typing import Any, List


def count_occurrences_recursive(nested: List[Any], value: Any) -> int:
    """Count how many times ``value`` appears in a possibly nested list
    using recursion.

    Example:
        data = [1, [2, 1, [1, 3]], 4]
        count_occurrences_recursive(data, 1) == 3
    """
    count = 0
    for item in nested:
        if isinstance(item, list):
            # here we recurse into the sublist
            count = count + count_occurrences_recursive(item, value)
        else:
            # atomic element: increment count if it matches value
            if item == value:
                count += 1
    return count



def count_occurrences_iterative(nested: List[Any], value: Any) -> int:
    """Count how many times ``value`` appears in a possibly nested list
    using iteration and an explicit stack or queue.
    """
    count = 0
    stack: List[Any] = [nested]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)
        else:
            if current == value:
                count += 1
    return count
