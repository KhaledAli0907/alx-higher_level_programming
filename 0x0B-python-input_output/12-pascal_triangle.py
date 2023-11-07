#!/usr/bin/python3
"""implementing pascal's triangle"""


def pascal_triangle(n: int) -> list:
    """Return pascal's triangle"""
    if n <= 0:
        return []

    lists = [[1]]
    while len(lists) != n:
        triangle = lists[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append[1]
        lists.append(temp)

    return lists
