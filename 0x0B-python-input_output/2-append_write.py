#!/usr/bin/python3

"""New Module For appends a string at the end of a text file
(UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Function to append to the file"""

    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
