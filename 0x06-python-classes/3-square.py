#!/usr/bin/python3

"""New module"""


class Square:
    """Square opject"""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): the size of the new sqare
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the Square"""
        return (self.__size ** 2)
