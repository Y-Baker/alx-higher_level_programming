#!/usr/bin/python3

"""New Module for returns dict description with simple data structure"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""

    return obj.__dict__
