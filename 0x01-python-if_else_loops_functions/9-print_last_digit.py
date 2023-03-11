#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        abs = number * -1
        digit = (abs % 10)
    else:
        digit = number % 10

    print("{:d}".format(digit), end="")
    return digit
