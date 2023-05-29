#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    try:
        for j in range(x):
            if isinstance(my_list[j], int):
                z += 1
                print("{:d}".format(my_list[j]), end="")
        print("")
        return z
    except IndexError as e:
        raise
