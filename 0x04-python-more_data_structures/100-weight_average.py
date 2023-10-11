#!/usr/bin/python3
def weight_average(my_list=[]) -> float:
    if len(my_list) == 0:
        return 0

    return sum(a * b for a, b in my_list) / sum(b for a, b in my_list)
