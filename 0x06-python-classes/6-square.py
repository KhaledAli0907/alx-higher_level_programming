#!/usr/bin/python3
"""Define square class"""


class Square:
    """Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """Create new instance of sqaure class
        Args:
            size: size of sqaure
            position: position of the sqaure
        """
        self.size = size
        self.position = position

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
        """Returns the position of the square"""
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
            len(value) != 2
            or not (isinstance(value, tuple))
            or not (isinstance(value[0], int))
            or not (isinstance(value[1], int))
            or (value[0] < 0)
            or (value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """Prints the sqaure to stdout"""
        if self.__size == 0:
            print()
            return
        # print newlines based in the y position
        [print() for _ in range(0, self.__position[1])]
        # print #'s and spaces
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                print(" ", end="")
            print("#" * self.__size)
