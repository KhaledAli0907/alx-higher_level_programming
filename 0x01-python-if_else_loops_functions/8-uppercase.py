#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            char = ord(c) - 32
        else:
            char = ord(c)
        print("{:c}".format(char), end="")
    print("\n")
