#!/usr/bin/python3
"""New module has the say my name function"""


def say_my_name(first_name, last_name=""):
    """
        print full name
        first_name: str
        last_name: str
        Errors: if the name not a str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
