#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if i != 113 and i != 101:
        print('{:c}'.format(i), end="")
