#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0) -> None:
        """initialize the class with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """Returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self) -> int:
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        """String representation to the class"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self) -> str:
        """String represintation for the class for reproduction"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints message on deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
