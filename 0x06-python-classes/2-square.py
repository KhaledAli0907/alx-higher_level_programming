#!/usr/bin/python3
"""Define square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """
        Create new instrance of sqaure class
        Args:
            size: size of sqaure
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
