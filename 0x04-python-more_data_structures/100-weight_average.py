#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    points = 0
    for tup in my_list:
        total += tup[0] * tup[1]
        points += tup[1]
    return (float(total / points))
