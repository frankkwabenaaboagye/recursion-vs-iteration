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
    # using a list to build the reversed characters
    result = [] 

    # iterate over the string indices in reverse order
    # this is sort of mirroring the recursive idea of moving forward through the string
    # while building the result backwards
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    
    # joining the collected characters into a single string - final reversed String
    return ''.join(result)