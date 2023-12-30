#!/usr/bin/python3
"""module for task7"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    "Main function"
    args = list(argv[1:])
    old = []
    try:
        # try loading data
        old = load_from_json_file("add_item.json")
    except Exception:
        len(old) == 0

    old.extend(args)
    save_to_json_file(old, "add_item.json")


if __name__ == "__main__":
    "Call main function"
    main()
