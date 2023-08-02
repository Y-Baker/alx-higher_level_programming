#!/usr/bin/python3

"""New Module"""


class BaseGeometry:
    """For all Geometry shapes"""

    def area(self):
        """Calc area of the Geometry shape"""
        raise Exception("area() is not implemented")
