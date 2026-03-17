#!/usr/bin/env python3
# @check-accepted: *

a, b = map(int, input().split())

if a % 2 == 0 or b % 2 == 0:
    print(1)
else:
    print(0)
