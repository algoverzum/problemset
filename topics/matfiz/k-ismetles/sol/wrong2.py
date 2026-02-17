#!/usr/bin/env python3
# @check-accepted: *

k = int(input())
string = input()

res = "YES"

for betu in "abcdefghijklmnopqrstuvwxyz":
    c = string.count(betu)
    if c % k == 1:
        res = "NO"
        break

print(res)
