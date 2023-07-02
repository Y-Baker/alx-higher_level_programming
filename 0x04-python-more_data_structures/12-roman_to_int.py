#!/usr/bin/python3

def roman_to_int(roman_string):
    sorce = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for letter in roman_string:
        if (letter == 'I'):
            if (roman_string[-1] != 'I'):
                value -= 1
            else:
                value += 1
        else:
            value += sorce[letter]
    return value
