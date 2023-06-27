#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for idx, element in enumerate(list):
            print("{:d}".format(element), end="")
            if (idx != len(list) - 1):
                print(" ", end="")
        print()
