#!/usr/bin/python3
def simple_delete(a_dictionary: dict, key=""):
    new = a_dictionary.copy()
    if key in new.keys():
        del new[key]

    return new
