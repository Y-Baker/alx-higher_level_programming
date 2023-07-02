#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return 'None'
    max = 0
    best = None
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            best = key
    return best
