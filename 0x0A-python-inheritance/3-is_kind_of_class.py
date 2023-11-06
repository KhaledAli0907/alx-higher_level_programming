#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj: object, a_class) -> bool:
    """return true if object is intance of a class"""
    return isinstance(obj, a_class)
