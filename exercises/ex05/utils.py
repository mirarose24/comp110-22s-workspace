"""Exercise 5: function skeletons and implementations."""

__author__ = "730440093"


def only_evens(input: list[int]) -> list[int]:
    """When given list of numbers, only_evens returns only even characters."""
    output: list[int] = list()
    for item in input:
        if item % 2 == 0:
            output.append(item)
    return output


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """When given list and start + end indices, returns subset between indices."""
    output: list[int] = list()
    i: int = start
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return output
    if start < 0:
        i: int = 0 
    while i >= start and i <= end - 1:
        output.append(a_list[i])
        i += 1
    return output


def concat(l_one: list[int], l_two: list[int]) -> list[int]:
    """When given two lists, concat generate l_one followed by l_two."""
    output: list[int] = list()
    for item in l_one:
        output.append(item)
    for items in l_two:
        output.append(items)
    return output
