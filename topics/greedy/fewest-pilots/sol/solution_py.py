#!/usr/bin/env python3
# @check-accepted: *

k, n = [int(x) for x in input().split()]

pilots = [(k, k + 1, 0)]
for i in range(n):
    s, e = [int(x) for x in input().split()]
    pilots.append((s, e, i + 1))

pilots.sort()
res = []
reached = 0
curend = 0
last = -1
i = 0
while i < n + 1:
    start, end, index = pilots[i]
    if start <= reached:
        i += 1
        if curend < end:
            last = index
            curend = end
    else:
        res.append(last)
        reached = curend
        if start > curend:
            print(0)
            exit()

print(len(res))
print(*res)
