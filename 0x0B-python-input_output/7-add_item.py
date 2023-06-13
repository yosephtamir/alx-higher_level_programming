#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
import json
from sys import argv


saveJson = __import__('5-save_to_json_file').save_to_json_file
loadJson = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    thisFile = loadJson(filename)
except (FileNotFoundError, ValueError):
    thisFile = []

for i in range(1, len(argv)):
    thisFile.append(argv[i])
saveJson(thisFile, filename)
