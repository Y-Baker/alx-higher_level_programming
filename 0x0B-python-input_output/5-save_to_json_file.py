#!/usr/bin/python3

"""New Module for writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """Convert to JSON and save it in a file"""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
