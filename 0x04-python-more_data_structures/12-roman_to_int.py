#!/usr/bin/python3

sorce = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def roman_to_int(roman_string):
    if roman_string == 'None' or not roman_string:
        return 0
    value = 0
    idx = 0
    for letter in roman_string:
        if (check_sub(roman_string[idx:], sorce[letter])):
            value -= sorce[letter]
        else:
            value += sorce[letter]
        idx += 1
    return value

def check_sub(string, value):
    for x in string:
        if sorce[x] > value:
            return True
    return False
