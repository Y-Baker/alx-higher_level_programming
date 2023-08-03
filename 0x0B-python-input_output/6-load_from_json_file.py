#!/usr/bin/python3

"""New Module for creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """convert from str JSON to PY object"""

    with open(filename) as f:
        return json.load(f)
