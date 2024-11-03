#!/usr/bin/env python3
# @check-accepted: *

a = int(input())
b = int(input())

for i in range(a + 1, b):
    if i % 7 == 0:
        print(i, end=" ")
print("")
