#!/usr/bin/python3

"""New Module for insert in specific place in file"""


def append_after(filename="", search_string="", new_string=""):
    """append string to next line that have the searching string"""

    with open(filename, "r+") as f:
        list_of_lines = f.readlines()
        to_write = list_of_lines.copy()
        for n, line in enumerate(list_of_lines):
            if search_string in line:
                to_write.insert(n + 1, new_string)
        lines = "".join(to_write)
        f.seek(0)
        f.write(lines)
