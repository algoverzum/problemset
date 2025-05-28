#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
l = []

for i in range(1, n + 1):
    item = list(map(int, input().split()))
    item.append(i)
    l.append(tuple(item))

l.sort(key=lambda x: (-x[0], x[1]))

print(*[x[2] for x in l])
