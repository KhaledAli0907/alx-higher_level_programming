#!/usr/bin/python3
def best_score(a_dictionary: dict):
    if not a_dictionary:
        return None

    best = 0
    string = ""
    for key in a_dictionary.keys():
        if a_dictionary[key] > best:
            best = a_dictionary[key]
            string = key
    return string
