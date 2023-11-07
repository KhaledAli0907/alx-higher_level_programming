#!/usr/bin/python3
"""
========================
MyInt module file
========================
"""


class MyInt(int):
    """class inhereting from int class"""

    def __eq__(self, __value: object) -> bool:
        """Alternating equality"""
        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        """Alternating non-equality"""
        return not super().__ne__(__value)
