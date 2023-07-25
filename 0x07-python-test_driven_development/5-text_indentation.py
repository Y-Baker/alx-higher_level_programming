#!/usr/bin/python3

"""New module that have function of txt"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of chars: ., ? and :
    text: str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.rstrip()
    if not text:
        return
    new_str = ""

    for idx, c in enumerate(text):
        if not new_str:
            if c == ' ':
                continue
        if new_str:
            if new_str[-1] == '\n' and c == ' ':
                continue
        new_str += c
        if c in ['.', '?', ':']:
            if idx == len(text) - 1:
                new_str += '\n'
            else:
                new_str += "\n\n"
    print(new_str)
