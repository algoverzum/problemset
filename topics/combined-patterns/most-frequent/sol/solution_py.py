#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
A = [int(x) for x in input().split()]

mostFrequent = A[0]
count = 1

for a in A:
    c = A.count(a)
    if c > count:
        mostFrequent = a
        count = c
    elif c == count:
        mostFrequent = min(mostFrequent, a)

print(mostFrequent)
