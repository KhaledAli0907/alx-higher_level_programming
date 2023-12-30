#!/usr/bin/python3
"""load_from_json function"""

from json import loads


def load_from_json_file(filename):
    """function that creates an Object from JSON file"""

    with open(filename) as f:
        return loads(f.read())
