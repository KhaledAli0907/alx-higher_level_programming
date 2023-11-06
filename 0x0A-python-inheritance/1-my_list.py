#!/usr/bin/python3

"""
Class inherits from list class
"""


class MyList(list):
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(list(self)))
