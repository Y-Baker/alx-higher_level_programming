#!/usr/bin/python3

"""New Module"""


class BaseGeometry:
    """For all Geometry shapes"""

    def area(self):
        """Calc area of the Geometry shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check Validation of the value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
