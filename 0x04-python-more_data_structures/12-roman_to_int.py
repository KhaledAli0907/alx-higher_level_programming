#!/usr/bin/python3
def roman_to_int(roman_string: str) -> int:
    if type(roman_string) != str or roman_string is None:
        return 0

    romanInts = {"I": 1, "V": 5, "X": 10,\
        "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(roman_string)):
        if romanInts[roman_string[i]] >\
            romanInts[roman_string[i - 1]] and i > 0:
            result += romanInts[roman_string[i]] -\
                2 * romanInts[roman_string[i - 1]]

        else:
            result += romanInts[roman_string[i]]

    return result
