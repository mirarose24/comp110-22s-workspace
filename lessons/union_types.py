"""An example of Union types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """log is a function that can be called w _either_ an int or a str arguement."""
    if isinstance(info, str):
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")


log("hello world")
log(110)
