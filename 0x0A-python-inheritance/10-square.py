#!/usr/bin/python3

"""New Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new object square from Rectangel"""

    def __init__(self, size):
        """
        Intialize New Square
        Args:
        size: int
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calc the area of the Square"""
        return (self.__size ** 2)
