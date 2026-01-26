#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
k = int(input())
if k % 2 == 1:
    print("YES")
elif n % 2 == 0:
    print("YES")
else:
    print("NO")
