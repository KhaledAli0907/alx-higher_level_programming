#!/usr/bin/python3
"""Save_to_json function"""

from json import dumb


def save_to_json_file(my_obj, filename):
    """Writes to a text file using JSON representaion"""
    with open(filename, "w", encoding="utf-8") as f:
        dumb(my_obj, f)
