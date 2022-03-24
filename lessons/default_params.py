"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:  # Once you define a default paramter, all following parameters must be defaulted as well. Any data type can be defaulted (ex. s: str = "hello")
    """Example of a default parameter where y and z parameters are 0 by default."""
    return x + y + z


print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
