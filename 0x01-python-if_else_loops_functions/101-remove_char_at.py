#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    position = 0
    for c in str:
        if position != n:
            new += str[position]
        position += 1
    return new
