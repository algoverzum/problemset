#!/usr/bin/env python3
# @check-accepted: *

k, n = [int(x) for x in input().split()]

pilots = [(k, k + 1, 0)]
for i in range(n):
    s, e = [int(x) for x in input().split()]
    pilots.append((s, e, i + 1))

pilots.sort()

ans = []
reached = 0
best = 0
best_end = 0

for start, end, index in pilots:
    if start <= reached:
        if end > best_end:
            best_end = end
            best = index
    else:
        if start > best_end:
            print(0)
            exit()
        reached = best_end
        ans.append(best)
        best_end = end
        best = index

print(len(ans))
print(*ans)
