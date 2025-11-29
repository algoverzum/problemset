#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
a = [int(x) for x in input().split()]
if sum(a) % 2 == 0:
    print("YES")
else:
    print("NO")
