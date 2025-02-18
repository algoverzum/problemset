#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
A.sort(reverse=True)

res = A[1::2][::-1] + A[::2]

print(*res)
