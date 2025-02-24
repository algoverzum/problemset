#!/usr/bin/env python3
# @check-accepted: *

N, M = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]
A = {int(x) for x in input().split()}
B = {int(x) for x in input().split()}
happiness = 0
for cargo in S:
    if cargo in A:
        happiness += 1
    if cargo in B:
        happiness -= 1

print(happiness)
