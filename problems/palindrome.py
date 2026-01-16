"""Palindrome problem: recursive vs iterative.

- Neither implementation is provided.
- You implement both recursive and iterative versions.
"""

from __future__ import annotations


def is_palindrome_recursive(s: str) -> bool:
    """Return True if ``s`` is a palindrome, False otherwise (using recursion).

    For this exercise:
    - Ignore case.
    - Ignore non-alphanumeric characters.
      (i.e., only consider letters and digits when checking.)

    Example:
        "Racecar"          -> True
        "A man, a plan..." -> True
        "hello"            -> False
    """
    # using lower case and we only consider alphanumeric characters
    normalized = '' 
    for char in s:
        if char.isalnum():
            normalized += char.lower()

    # empty string or single character is a palindrome
    if len(normalized) <= 1:
        return True
    
    # if the first and last characters are different, it's not a palindrome
    if normalized[0] != normalized[-1]:
        return False
    
    # recursive case: check the substring without the first and last characters
    return is_palindrome_recursive(normalized[1:-1])


def is_palindrome_iterative(s: str) -> bool:
    """Return True if ``s`` is a palindrome, False otherwise (using iteration).

    Implement the same "normalized" definition as
    :func:`is_palindrome_recursive`.
    """
    
    # normalizing the string, this time using another approach
    normalized = "".join( char.lower() for char in s if char.isalnum() )

    # using two-pointer technique to check for palindrome
    left, right = 0, len(normalized) - 1
    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1
    return True
