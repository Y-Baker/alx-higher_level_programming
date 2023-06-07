#!/usr/bin/python3
i = 0
while i < 9:
    j = i + 1
    while j < 10:
        if(i == 8 and j == 9):
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
        j += 1
    i += 1
