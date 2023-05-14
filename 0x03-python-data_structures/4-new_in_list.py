#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) <= idx:
        temp = my_list.copy()
        return temp
    else:
        temp = my_list[:]
        temp[idx] = element
        return temp
