#!/usr/bin/bash
"""
===================================
module with method is_same_of_class
===================================
"""

def is_same_class(obj: object, a_class) -> bool:
    """Return true if object is an inctance of a class"""
    return type(obj) is a_class
