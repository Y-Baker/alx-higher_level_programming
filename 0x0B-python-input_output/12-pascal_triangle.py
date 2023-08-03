#!/usr/bin/python3

"""New Module for representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """Return list of list for pascal triangle"""

    if n <= 0:
        return []

    re_list = [[] for _ in range(n)]
    for row in range(n):
        for col in range(row + 1):
            if col == 0 or col == row:
                re_list[row].append(1)
            else:
                if col > row / 2:
                    num = re_list[row][row - col]
                    re_list[row].append(num)
                else:
                    num = re_list[row - 1][col - 1] + re_list[row - 1][col]
                    re_list[row].append(num)
    return re_list
