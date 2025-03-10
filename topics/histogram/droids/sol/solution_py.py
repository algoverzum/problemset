#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
szamok = [int(x) for x in input().split()]
db = [0] * 11
for szam in szamok:
    db[szam] += 1
print(max(db))
