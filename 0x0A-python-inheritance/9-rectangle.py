#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height) -> None:
        """Initiate class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """string represintaion to the class"""
        return "[Reactangle] {}/{}".format(self.__width, self.__height)
