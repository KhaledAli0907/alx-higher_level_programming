#!/usr/bin/python3
"""from_json_string function"""

from json import loads


def from_json_string(my_str):
    """Retruns an object represented by JSON string"""
    return loads(my_str)
