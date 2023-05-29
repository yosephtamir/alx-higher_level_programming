#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    for j in my_list:
        k += 1
    if k < x:
        x = k
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return int(x)
    except Exception:
        pass
