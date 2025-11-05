#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
dupla = 0
borton = False
for i in range(N):
    A, B = [int(x) for x in input().split()]
    if A == B:
        dupla += 1
        if dupla > 2:
            borton = True
            break
    else:
        dupla = 0
if borton:
    print("Yes")
else:
    print("No")
