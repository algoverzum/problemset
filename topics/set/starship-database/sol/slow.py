#!/usr/bin/env python3
# @check-accepted: examples
# @check-time-limit-exceeded: all
# slow!!!

n = int(input())
database = []
for i in range(n):
    y, x = [int(z) for z in input().split()]
    if y == 1:
        if x not in database:
            database.append(x)
    elif y == 2:
        if x in database:
            database.remove(x)
    else:  # y == 3
        if x in database:
            print(1)
        else:
            print(0)
