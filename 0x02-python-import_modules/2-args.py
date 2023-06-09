#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    str = "argument"
    if (len != 1):
        str += "s"
    if (len == 0):
        str += "."
    else:
        str += ":"
    print("{:d} {:s}".format(len, str))
    for i in range(1, len + 1):
        print(f"{i}: {sys.argv[i]}")
