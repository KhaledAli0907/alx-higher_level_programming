#!/usr/bin/python3
"""
=====================
write function module
=====================
"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
