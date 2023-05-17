#!/usr/bin/python3
def uniq_add(my_list=[]):
    ab = set(my_list)
    add = 0
    for i in ab:
        add += i
    return add
