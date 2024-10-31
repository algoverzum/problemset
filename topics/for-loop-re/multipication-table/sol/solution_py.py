#!/usr/bin/env python3
# @check-accepted: *
n = int(input())
if n == 1:
    print(1)
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()
