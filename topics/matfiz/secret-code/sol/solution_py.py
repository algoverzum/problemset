#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
a = int(input())
b = int(input())
c = int(input())

db = 0
volt = False

for i in range(1, 10**n):
    if i % 5 == a and i % 7 == b and i % 11 == c:
        if not volt:
            print(i)
            volt = True
        db += 1

if db > 0:
    print(db)
else:
    print(-1)
