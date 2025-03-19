#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
database = set()
for i in range(n):
    t, x = [int(z) for z in input().split()]
    if t == 1:
        database.add(x)
    elif t == 2:
        database.discard(x)
    else:
        if x in database:
            print(1)
        else:
            print(0)
