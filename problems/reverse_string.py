"""Reverse string problem: recursive vs iterative.

- Recursive implementation is provided.
- Iterative implementation is left as an exercise.
"""

from __future__ import annotations


def reverse_string_recursive(s: str) -> str:
    """Return the reverse of string ``s`` using recursion.

    Example:
        reverse_string_recursive("abc") == "cba"
    """
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


def reverse_string_iterative(s: str) -> str:
    """Return the reverse of string ``s`` using iteration (no recursion).

    You may use a loop and string concatenation or build a list of chars.
    Do NOT just use slicing ``s[::-1]`` here.
    """
    raise NotImplementedError
