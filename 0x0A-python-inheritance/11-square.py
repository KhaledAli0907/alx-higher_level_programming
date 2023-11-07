#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""
=================================
module with class Square
=================================
"""


class Square(Rectangle):
    """
    Square class
    ...
    
    Atrributes
    ----------
    size: int
        integer hold the size data
        
    Methods
    -------
    area()
        calculate sqaurs's area
    """

    def __init__(self, size) -> None:
        """initiate class method"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        """Return area of the sqaure"""
        return self.__size**2

    def __str__(self) -> str:
        """string represintation to the class"""
        return f"[Square] {self.__size}/{self.__size}"
