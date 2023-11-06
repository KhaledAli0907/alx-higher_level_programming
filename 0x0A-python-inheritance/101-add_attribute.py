#!/usr/bin/python3
"""defines a function that add attribute to objects"""


def add_attribute(obj, att, value) -> None:
    """Add atrribute to the object if it possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, att, value)
