#!/usr/bin/python3

"""New Module"""


def is_same_class(obj, a_class):
    """Check if the obj is directly instance of class or not"""
    class_name = type(obj)

    return (class_name == a_class)
