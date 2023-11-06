#!/usr/bin/python3
Rectangle = __import__("9-rectangle.py").Rectangle

"""Sqaure module"""


class Sqaure(Rectangle):
    """Sqaure"""

    def __init__(self, size) -> None:
        self.integer_validator(size)
        self.__size = size

    def area(self) -> int:
        """Return area of the sqaure"""
        return self.__size**2
