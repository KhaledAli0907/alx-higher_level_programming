#!/usr/bin/python3
"""Define square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0):
        """Create new instance of sqaure class
        Args:
            size: size of sqaure
        """

        self.__size = size

    def area(self):
        """Calculate the current sqaure area
        Returns:
            the current square area
        """
        return self.__size**2

    @property
    def size(self):
        """Gets the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the sqaure size to a value"""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """Prints the sqaure to stdout"""
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)
