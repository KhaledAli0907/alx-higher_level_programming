#!/usr/bin/python3
"""define to_json_string function"""
from json import dumps


def to_json_string(my_obj):
    """Return json file as a string"""
    return dumps(my_obj)
