#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict):
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
