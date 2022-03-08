"""Exercise 5: funciton unit tests."""

__author__ = "730440093"

from utils import only_evens, sub, concat


# ONLY_EVENS:


def test_only_evens_empty_list() -> None:
    """Testing to make sure imput of an empty list gives output of an empty list."""
    assert only_evens([]) == []


def test_only_evens_odd_numbers() -> None:
    """Testing to make sure that no odds numbers are evaluated as even given only odds."""
    assert only_evens([1, 3, 5, 7]) == []


def test_only_evens_even_numbers() -> None:
    """Testing to make sure that all even numbers are evaluated given only evens."""
    assert only_evens([2, 4, 6, 8, 10, 12, 14]) == [2, 4, 6, 8, 10, 12, 14]


# SUB TESTING:


def test_sub_empty_list() -> None:
    """Testing to make sure imput empty list gives output of empty list."""
    assert sub([], 1, 2) == []


def test_sub_long_list() -> None:
    """Testing to make sure that lenth of list does not impact function."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 5) == [3, 4, 5]


def test_sub_star_equal_length() -> None:
    """Testing to make sure that when start index is equivalent to length of list it evaluates to an empty list."""  
    assert sub([3, 4, 5], 2, 2) == []

# If the start index is negative, start from the beginning of the list. If the end index is greater than the length of the list, end with the end of the list.
# If the length of the list is 0, start > len of the list or end <= 0, return the empty list.


# CONCAT TESTING:


def test_concat_empty_lists() -> None:
    """Testing to make sure empty list concatenates to empty list."""
    assert concat([], []) == []


def test_concat_diff_lengths() -> None:
    """Testing to make sure lists of different lengths evaulte correctly."""
    assert concat([1, 2, 3, 4, 5], [6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_negative_lists() -> None:
    """Testing to make sure that negtive numbers have no impact of concatenation."""
    assert concat([-1, 3, 8, -10], [-4, 7, 830]) == [-1, 3, 8, -10, -4, 7, 830]
