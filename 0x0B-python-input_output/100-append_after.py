#!/usr/bin/python3
'''
This is used to search and append to a file
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    This is where the trick goas on
    '''
    innerStr = []

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            innerStr.append(line)

            if search_string in line:
                innerStr.append(new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        for line in innerStr:
            file.write(line)
