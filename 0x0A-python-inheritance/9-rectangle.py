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

    def area(self):
        """Calc the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """own str function"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
