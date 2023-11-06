#!/usr/bin/python3


class MyInt(int):
    """class inhereting from int class"""

    def __eq__(self, __value: object):
        """Alternating equality"""
        return not super().__eq__(__value)

    def __ne__(self, __value: object):
        return not super().__ne__(__value)
