#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value) -> bool:
    result = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: ", err, file=stderr)
        result = False
    return result
