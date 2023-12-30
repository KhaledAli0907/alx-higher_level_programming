#!/usr/bin/python3
"""Module for reading file"""


def read_file(filename=""):
    """Read file to the stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
