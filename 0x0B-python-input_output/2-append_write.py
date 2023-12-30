#!/usr/bin/python3

"""
=====================
write function module
=====================
"""


def append_write(filename="", text=""):
    """write function"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
