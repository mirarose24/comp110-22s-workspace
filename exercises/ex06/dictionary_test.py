"""Exercise 06 -- testing dictionaries."""

__author__ = "730440093"

from dictionary import invert, favorite_color, count
import pytest

# INVERT TESTING:


def test_invert_occurs() -> None:
    """Testing to ensure function correctly inverts dict inputs."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_no_mistaken_duplicate() -> None:
    """Testing to make sure that idential key and value are not mistaken as indentical keys."""
    assert invert({'haha': 'haha'}) == {'haha': 'haha'}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


# FAVORITE_COLOR TESTING:


def test_favorite_color() -> None:
    """Testing to ensure that str value that occurs the most is determined as the return."""
    assert favorite_color({"Miranda": "olive green", "Vincent": "olive green", "Krissy": "carolina blue", "Kendall": "purple"}) == "olive green"


def test_tied_favorites() -> None:
    """Testing to make sure the color that appears first in the dictionary is result when there are multiple colors of the same frequency."""
    assert favorite_color({"Mark": "yellow", "Diego": "blue", "Violet": "yellow", "Karen": "purple", "Daisy": "blue"}) == "yellow"


def test_empty_dict() -> None:
    """Testing to make sure result of an empty dictionary is no result."""
    assert favorite_color({}) == ""

# COUNT TESTING:


def test_count_goes_up() -> None:
    """Testing to ensure counting occurs."""
    assert count(['yellow', 'purple', 'olive green', 'magenta', 'olive green']) == {'yellow': 1, 'purple': 1, 'olive green': 2, 'magenta': 1}


def test_same_item() -> None:
    """Testing to make sure there is no limit to the count of an input."""
    assert count(['duke sucks', 'duke sucks', 'duke sucks', 'duke sucks', 'duke sucks', 'duke sucks']) == {'duke sucks': 6}


def test_empty_list() -> None:
    """Testing to make sure empty list returns empty dict."""
    assert count([]) == {}