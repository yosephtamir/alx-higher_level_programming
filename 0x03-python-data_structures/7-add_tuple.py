#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        atupl = (tuple_a[0], 0)
    elif len(tuple_a) == 0:
        atupl = (0, 0)
    elif len(tuple_a) == 2:
        atupl = (tuple_a[0], tuple_a[1])
    else:
        atupl = (tuple_a[0], tuple_a[1])
    if len(tuple_b) == 1:
        btupl = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        btupl = (0, 0)
    elif len(tuple_a) == 2:
        btupl = (tuple_b[0], tuple_b[1])
    else:
        btupl = (tuple_b[0], tuple_b[1])
    addtuple = (atupl[0] + btupl[0], atupl[1] + btupl[1])
    return addtuple
