#!/usr/bin/python3


"""
================================
module fro inherits_from fnction
================================
"""


def inherits_from(obj, a_class) -> bool:
    """find if an object is subclass of aclass"""
    return type(obj) is not a_class and isinstance(obj, a_class)
