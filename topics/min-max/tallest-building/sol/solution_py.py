#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
heigths = [int(x) for x in input().split()]
maxi = heigths[0]
for heigth in heigths:
    if heigth > maxi:
        maxi = heigth
print(maxi)
