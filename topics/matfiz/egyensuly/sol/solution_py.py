#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
A = [int(s) for s in input().split()]
maxi = max(A)
print(maxi * n - sum(A))
