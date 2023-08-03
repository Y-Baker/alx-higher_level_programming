#!/usr/bin/python3

"""New Module for returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Convert py obj to str JSON"""

    str_json = json.dumps(my_obj)
    return str_json
