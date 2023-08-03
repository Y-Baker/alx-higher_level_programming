#!/usr/bin/python3

"""New Module for Write a function that writes a string to a text file(UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Function for write in file"""

    with open(filename, "w", encoding="utf-8") as f:
        re = f.write(text)
        return re
