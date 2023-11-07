#!/usr/bin/python3


def read_file(filename=""):
    """Read file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
