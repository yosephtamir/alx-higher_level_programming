#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            newStr = newStr + i
    return newStr
