#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
===================================
module with class BaseGeometry
===================================
"""


class Square(Rectangle):
    """Sqaure Class"""

    def __init__(self, size) -> None:
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Return area of the sqaure"""
        return self.__size**2
    
    def __str__(self) -> str:
        return f"[Square] {self.__size}/{self.__size}"
