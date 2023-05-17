#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    dhum = 0
    chang = (('I', 1), ('V', 5), ('X', 10),
                ('L', 50), ('C', 100), ('D', 500),
                ('M', 1000))

    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0

    for c in reversed(roman_string):
        for elem in chang:
            if c == elem[0]:
                if elem[1] < dhum:
                    sum -= elem[1]
                else:
                    sum += elem[1]
                dhum = elem[1]
    return sum
