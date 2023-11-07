#!/usr/bin/python3
from json import loads

"""from_json_string function"""


def from_json_string(my_str):
    """Retruns an object represented by JSON string"""
    return loads(my_str)
