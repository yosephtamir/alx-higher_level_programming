#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or len(my_list) < idx:
        return None
    for i in my_list:
        if my_list.index(i) == idx:
            return i
