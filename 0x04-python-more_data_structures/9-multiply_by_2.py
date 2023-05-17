#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ab = dict(a_dictionary)
    for i in ab.items():
        ab[i[0]] = i[1] * 2
    return ab
