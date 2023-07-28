#!/usr/bin/python3
"""New Module"""


class Rectangle:
    """Represent Opject Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Create New Rectangle
        width: int
        height: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width Property [Getter]"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width [Setter]"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Property [Getter]"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height [Setter]"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The Area Method"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """The Perimeter Method"""
        if self.__width * self.__height == 0:
            return 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        """the special method that called when you call print fun"""
        if self.__width * self.__height == 0:
            return ""
        shape = []
        for row in range(self.__height):
            for col in range(self.__width):
                shape.append('#')
            shape.append('\n')
        shape.pop()
        return (''.join(shape))

    def __repr__(self):
        """The Official represent of the object"""
        str = f"{type(self).__name__}({self.__width}, {self.__height})"
        return str
