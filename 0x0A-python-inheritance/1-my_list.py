#!/usr/bin/python3

"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
