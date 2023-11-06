#!/usr/bin/python3
class BaseGeometry:
    """Class to hold geometry data"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
