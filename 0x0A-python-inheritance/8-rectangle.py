#!/usr/bin/python3

"""New Module Created for RECTANGLE"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """New Object Rectangle form BaseGeometry"""

    def __init__(self, width, height):
        """
        Intialize New Rectangel
        Args:
        width: int
        height: int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
