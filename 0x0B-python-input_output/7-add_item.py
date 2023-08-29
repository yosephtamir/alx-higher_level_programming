#!/usr/bin/python3
'''This is to add arguments to a list'''
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def argHandler():
    ''' THE HANDLER'''

    innerlist = []
    filename = 'add_item.json'

    try:
        other = load_from_json_file(filename)
        innerlist = other
    except Exception:
        innerlist = []

    for arg in range(1, len(argv)):
        innerlist.append(argv[arg])
    save_to_json_file(innerlist, filename)


if __name__ == "__main__":
    argHandler()
