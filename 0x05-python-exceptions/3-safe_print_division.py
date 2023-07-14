#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        re = a / b
    except (ZeroDivisionError, TypeError):
        re = None
    finally:
        print("Inside result: {}".format(re))
        return (re)
