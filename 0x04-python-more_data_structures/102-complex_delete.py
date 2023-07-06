#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    deleted_keys = []
    for key in a_dictionary:
        if a_dictionary.get(key) == value:
            deleted_keys.append(key)
    list(map(lambda x: a_dictionary.pop(x), deleted_keys))
    return a_dictionary
