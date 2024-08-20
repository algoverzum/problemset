#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
b = int(input())
if a % 2 == 0 and b % 2 == 0:
    print(2)
elif a % 2 == 0 or b % 2 == 0:
    print(1)
else:
    print(0)
