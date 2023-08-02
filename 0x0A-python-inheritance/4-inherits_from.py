#!/usr/bin/python3

"""New Module"""


def inherits_from(obj, a_class):
    """True if obj is instance of a class inherited from specified class"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
