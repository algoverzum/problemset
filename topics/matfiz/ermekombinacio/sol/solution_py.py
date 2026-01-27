#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = int(input())
if n % 2 == 0:
    print("YES")
elif k % 2 == 1 and n >= k:
    print("YES")
else:
    print("NO")
