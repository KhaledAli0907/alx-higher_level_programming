#!/usr/bin/python3
"""Save_to_json function"""

from json import dumps


def save_to_json_file(my_obj, filename):
    """Writes to a text file using JSON representaion"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(dumps(my_obj))
