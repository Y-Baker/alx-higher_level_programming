#!/usr/bin/python3

"""New module"""


class Square:
    """Square opject"""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): the size of the new sqare
        """
        self.__size = size

    @property
    def size(self):
        """Getter to size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the Square"""
        return (self.__size ** 2)
