"""Exercise 06 -- pracitce with dictionaries and their abilities."""

__author__ = "730440093"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Function to invert entries of dictionary."""
    inverted: dict[str, str] = {}
    for key in input:
        if input[key] in inverted:
            raise KeyError("Duplicate!!")
        inverted[input[key]] = key            
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    """Returns most frequently answered favorite color."""
    color_list: dict[str, int] = {}
    for name in input:
        if input[name] in color_list:
            color_list[input[name]] += 1 
        else:
            color_list[input[name]] = 1
    favorite: str = ""
    for color in color_list:
        if favorite == "":
            favorite = color 
        if color_list[color] > color_list[favorite]:
            favorite = color
    output: str = favorite
    return output


def count(input: list[str]) -> dict[str, int]:
    """Asdfghjk."""
    result: dict[str, int] = {}
    for word in input:
        if word in result:
            result[word] += 1
        else: 
            result[word] = 1
    return result

    