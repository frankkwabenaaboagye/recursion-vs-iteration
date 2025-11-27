"""Tests for recursion-vs-iteration exercises.

Each pair of functions (<name>_recursive, <name>_iterative) must produce
the same result on the same inputs.

If either side of a pair still raises NotImplementedError, the tests for
that pair will be skipped. Once you implement BOTH functions, the tests
for that pair become active and must pass.

Each problem now lives in its own module under ``problems/``.
"""

import pytest

from problems.factorial import factorial_recursive, factorial_iterative
from problems.sum_digits import sum_digits_recursive, sum_digits_iterative
from problems.reverse_string import reverse_string_recursive, reverse_string_iterative
from problems.fibonacci import fib_recursive, fib_iterative
from problems.power import power_recursive, power_iterative
from problems.flatten import flatten_recursive, flatten_iterative
from problems.binary_search import binary_search_recursive, binary_search_iterative
from problems.gcd import gcd_recursive, gcd_iterative
from problems.count_occurrences import (
    count_occurrences_recursive,
    count_occurrences_iterative,
)
from problems.palindrome import is_palindrome_recursive, is_palindrome_iterative
from problems.example_sum_list import sum_list_recursive, sum_list_iterative


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------


def _assert_pair_equal(func_recursive, func_iterative, expected, *args, **kwargs):
    """Call both functions with the same arguments and assert both equal
    the expected value.

    If either function raises NotImplementedError, skip the test.
    """
    try:
        r = func_recursive(*args, **kwargs)
        i = func_iterative(*args, **kwargs)
    except NotImplementedError:
        pytest.skip("Function not implemented yet")
    assert r == expected
    assert i == expected


def _assert_both_raise(exc, func_recursive, func_iterative, *args, **kwargs):
    """Assert that both functions raise the same exception type.

    If either function raises NotImplementedError, skip the test.
    """
    try:
        with pytest.raises(exc):
            func_recursive(*args, **kwargs)
        with pytest.raises(exc):
            func_iterative(*args, **kwargs)
    except NotImplementedError:
        pytest.skip("Function not implemented yet")


# ---------------------------------------------------------------------------
# 1. Factorial
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (4, 24), (6, 720)])
def test_factorial_values(n, expected):
    _assert_pair_equal(factorial_recursive, factorial_iterative, expected, n)


@pytest.mark.parametrize("n", [-1, -5])
def test_factorial_negative_raises(n):
    _assert_both_raise(ValueError, factorial_recursive, factorial_iterative, n)


# ---------------------------------------------------------------------------
# 2. Sum of digits
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (5, 5),
        (10, 1),
        (123, 6),
        (9999, 36),
    ],
)
def test_sum_digits(n, expected):
    _assert_pair_equal(sum_digits_recursive, sum_digits_iterative, expected, n)


# ---------------------------------------------------------------------------
# 3. Reverse string
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("hello", "olleh"),
        ("racecar", "racecar"),
    ],
)
def test_reverse_string(s, expected):
    _assert_pair_equal(reverse_string_recursive, reverse_string_iterative, expected, s)


# ---------------------------------------------------------------------------
# 4. Fibonacci
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
    ],
)
def test_fib_small(n, expected):
    _assert_pair_equal(fib_recursive, fib_iterative, expected, n)


@pytest.mark.parametrize("n", [-1, -10])
def test_fib_negative_raises(n):
    _assert_both_raise(ValueError, fib_recursive, fib_iterative, n)


# ---------------------------------------------------------------------------
# 5. Power
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, 0, 1),
        (2, 3, 8),
        (5, 1, 5),
        (3, 4, 81),
        (10, 2, 100),
    ],
)
def test_power(base, exponent, expected):
    _assert_pair_equal(power_recursive, power_iterative, expected, base, exponent)


@pytest.mark.parametrize("exp", [-1, -5])
def test_power_negative_exponent_raises(exp):
    _assert_both_raise(ValueError, power_recursive, power_iterative, 2, exp)


# ---------------------------------------------------------------------------
# 6. Flatten nested list
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "nested, expected",
    [
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([1, [2, [3, 4], 5], 6], [1, 2, 3, 4, 5, 6]),
        (([["a", ["b"]]]), ["a", "b"]),
    ],
)
def test_flatten(nested, expected):
    _assert_pair_equal(flatten_recursive, flatten_iterative, expected, nested)


# ---------------------------------------------------------------------------
# 7. Binary search
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([], 1, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 9, 4),
        ([1, 3, 5, 7, 9], 2, -1),
    ],
)
def test_binary_search(arr, target, expected):
    _assert_pair_equal(binary_search_recursive, binary_search_iterative, expected, arr, target)


# ---------------------------------------------------------------------------
# 8. GCD
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 1),
        (8, 12, 4),
        (12, 8, 4),
        (21, 14, 7),
        (100, 25, 25),
        (-8, 12, 4),  # sign should not matter
        (8, -12, 4),
    ],
)
def test_gcd(a, b, expected):
    _assert_pair_equal(gcd_recursive, gcd_iterative, expected, a, b)


# ---------------------------------------------------------------------------
# 9. Count occurrences in nested list
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "nested, value, expected",
    [
        ([], 1, 0),
        ([1, 2, 3], 1, 1),
        ([1, [1, 2], 3], 1, 2),
        ([1, [2, 1, [1, 3]], 4], 1, 3),
        (([["a", ["b", "a"]], "a"]), "a", 3),
    ],
)
def test_count_occurrences(nested, value, expected):
    _assert_pair_equal(
        count_occurrences_recursive,
        count_occurrences_iterative,
        expected,
        nested,
        value,
    )


# ---------------------------------------------------------------------------
# 10. Palindrome
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("racecar", True),
        ("RaceCar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
    ],
)
def test_is_palindrome(s, expected):
    _assert_pair_equal(is_palindrome_recursive, is_palindrome_iterative, expected, s)


# ---------------------------------------------------------------------------
# 11. Example: sum list
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([], 0),
        ([1], 1),
        ([1, 2, 3], 6),
        ([-1, 1, 2], 2),
    ],
)
def test_example_sum_list(nums, expected):
    """This problem is fully implemented and acts as a reference example.

    Both sum_list_recursive and sum_list_iterative should always pass.
    """
    _assert_pair_equal(sum_list_recursive, sum_list_iterative, expected, nums)
