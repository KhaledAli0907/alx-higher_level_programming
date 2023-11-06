#!/usr/bin/bash
"""
is_same class function
"""


def is_same_class(obj: object, a_class) -> bool:
    """Return true if object is an inctance of a class"""
    return type(obj) is a_class
