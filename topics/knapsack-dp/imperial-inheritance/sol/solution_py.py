#!/usr/bin/env python3
# @check-accepted: *

INF = 10**9

N = int(input())
V = list(map(int, input().split()))
total = sum(V)
M = total
OFFSET = M

dp = [-INF] * (2 * M + 1)
ndp = [-INF] * (2 * M + 1)
par = [-1] * (N * (2 * M + 1))

dp[OFFSET] = 0

for i in range(N):
    v = V[i]
    for d in range(2 * M + 1):
        if dp[d] < 0:
            continue
        # 1) leave unassigned
        if dp[d] > ndp[d]:
            ndp[d] = dp[d]
            par[i * (2 * M + 1) + d] = 0
        # 2) assign to A (difference +v)
        if d + v <= 2 * M and dp[d] + v > ndp[d + v]:
            ndp[d + v] = dp[d] + v
            par[i * (2 * M + 1) + d + v] = 1
        # 3) assign to B (difference -v)
        if d - v >= 0 and dp[d] + v > ndp[d - v]:
            ndp[d - v] = dp[d] + v
            par[i * (2 * M + 1) + d - v] = 2
    dp, ndp = ndp, [-INF] * (2 * M + 1)

best = dp[OFFSET]
leftover = total - best
print(leftover)

# backtrack
A, B = [], []
d = OFFSET
for i in reversed(range(N)):
    choice = par[i * (2 * M + 1) + d]
    if choice == 1:
        A.append(i + 1)
        d -= V[i]
    elif choice == 2:
        B.append(i + 1)
        d += V[i]
    # else: unassigned

print(*A)
print(*B)
