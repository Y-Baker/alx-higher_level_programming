#!/usr/bin/python3

"""Module have add Function"""


def add_integer(a, b=98):
    """Return the interger addition of a and b
        a: int
        b: int
        Errors: if a or b is not int or float
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
