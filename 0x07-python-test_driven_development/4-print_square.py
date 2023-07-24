#!/usr/bin/python3

"""New Module that have print sqare shape with '#' in size parameter"""


def print_square(size):
    """Print sqare shape with '#' by size var
    size: int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()
