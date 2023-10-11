#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if type(roman_string) != str or roman_string == None:
        return 0

    romanInts = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for c in reversed(roman_string):
        result += romanInts[c] if result < romanInts[c] * 4 else -romanInts[c]

    return result
