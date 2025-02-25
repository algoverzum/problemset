#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
database = set()
for i in range(n):
    y, x = [int(z) for z in input().split()]
    if y == 1:
        database.add(x)
    elif y == 2:
        database.discard(x)
    else:  # y == 3
        if x in database:
            print(1)
        else:
            print(0)
