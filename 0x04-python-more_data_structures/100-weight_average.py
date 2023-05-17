#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    addOfMult, devidend = 0, 0
    for i in my_list:
        addOfMult += (i[0] * i[1])
        devidend += i[1]
    return addOfMult / devidend
