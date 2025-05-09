#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
permits = []
for _ in range(n):
    a, b, k = map(int, input().split())
    permits.append((a, b, k))

dp = [0] * (m + 2)
choice = [-1] * (m + 2)
previous = [-1] * (m + 2)
permit_index = 0
for sector in range(1, m + 1):
    dp[sector] = dp[sector - 1]
    previous[sector] = sector - 1
    while permit_index < n and permits[permit_index][1] == sector:
        start_sector = permits[permit_index][0]
        credits = permits[permit_index][2]
        gain = dp[start_sector - 1] + credits
        if gain > dp[sector]:
            dp[sector] = gain
            choice[sector] = permit_index
            previous[sector] = start_sector - 1
        permit_index += 1

print(dp[m])
selected = []
current = m
while current > 0:
    if choice[current] != -1:
        selected.append(choice[current] + 1)
        current = previous[current]
    else:
        current -= 1

selected.sort()
print(*selected)
