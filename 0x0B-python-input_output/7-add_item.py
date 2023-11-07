#!/usr/bin/python3

"""function add_item"""

from sys import argv

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

args = list(argv[:1])
try:
    old = load_from_json_file("add_item.json")
except Exception:
    old = []

old.extend(args)
save_to_json_file(old, "add_item.json")
