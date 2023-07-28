#!/usr/bin/python3
"""New Module"""


class Rectangle:
    """Represent Opject Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def print_number_of_instances():
        print(f"The Number of Rectangle \
              Instances is {Rectangle.number_of_instances}")

    @classmethod
    def square(cls, size=0):
        new = cls(size, size)
        return new

    def __init__(self, width=0, height=0):
        """
        Create New Rectangle
        width: int
        height: int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                shape.append(str(self.print_symbol))
            shape.append('\n')
        shape.pop()
        return (''.join(shape))

    def __repr__(self):
        """The Official represent of the object"""
        str = f"{type(self).__name__}({self.__width}, {self.__height})"
        return str

    def __del__(self):
        """Called when the object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare Two Rectangle Opjects by their Area
        Args:
        rect_1: must be rectangle
        rect_2: must be rectangle
        Return: whose area are bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
