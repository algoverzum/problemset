#!/usr/bin/env python3
# @check-accepted: *

for i in range(10, 100):
    A = i // 10
    B = i % 10
    if A == B - 2:
        print(i - 8)
