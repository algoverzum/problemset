#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = int(input())
if n % 2 == 0:
    print("YES")
elif k % 2 == 0 and n % 2 == 1:
    print("NO")
else:
    print("YES")
