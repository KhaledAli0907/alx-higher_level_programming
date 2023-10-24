#!/usr/bin/python3
"""Define square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Create new instance of sqaure class
        Args:
            size: size of sqaure
        """
        self.__position = position
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

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """Sets the sqaure size to a value"""
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """Check and set the postion value"""
        if (
            not (isinstance(value, tuple))
            or not (isinstance(value[0], int))
            or not (isinstance(value[1], int))
            or (value[0] < 0)
            or (value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))