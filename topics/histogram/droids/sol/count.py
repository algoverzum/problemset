#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
szamok = [int(x) for x in input().split()]
db = []
for i in range(1, 11):
    db.append(szamok.count(i))
print(max(db))
