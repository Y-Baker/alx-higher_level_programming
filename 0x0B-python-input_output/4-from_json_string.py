#!/usr/bin/python3

"""New Module for returns an object-Python represented by a JSON string"""
import json


def from_json_string(my_str):
    """convert from JSON to python data structure"""

    return json.loads(my_str)
