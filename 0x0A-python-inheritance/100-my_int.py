#!/usr/bin/python3

"""New Module"""


class MyInt(int):
    """New Fack int"""

    def __eq__(self, value):
        """Fack equal"""
        return self.real != value

    def __ne__(self, value):
        """Fack Not Equal"""
        return self.real == value
