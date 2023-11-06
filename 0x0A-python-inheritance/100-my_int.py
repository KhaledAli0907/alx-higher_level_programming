#!/usr/bin/python3


class MyInt(int):
    """class inhereting from int class"""

    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value) -> bool:
        """Alternating equality"""
        return not super().__eq__(value)

    def __ne__(self, value) -> bool:
        """Alternating non Equality"""
        return not super().__ne__(value)
