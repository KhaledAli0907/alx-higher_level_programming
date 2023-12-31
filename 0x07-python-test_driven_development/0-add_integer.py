#!/usr/bin/python3
def add_integer(a, b=98) -> int:
    """
    Add to integers
    Args:
        a = int
        b = int
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")
