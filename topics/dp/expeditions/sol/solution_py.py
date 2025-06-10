#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
start = [0] * n
end = [0] * n
credit = [0] * n
ends_at = [[] for _ in range(m + 1)]

for i in range(n):
    start[i], end[i], credit[i] = map(int, input().split())
    ends_at[end[i]].append(i)

dp = [0] * (m + 1)
last = [-1] * (m + 1)

for i in range(1, m + 1):
    dp[i] = dp[i - 1]
    last[i] = last[i - 1]
    for j in ends_at[i]:
        if dp[i] < dp[start[j] - 1] + credit[j]:
            dp[i] = dp[start[j] - 1] + credit[j]
            last[i] = j

print(dp[-1])

ans = []
cur = last[-1]
while cur >= 0:
    ans.append(cur)
    cur = last[start[cur] - 1]

ans.sort()
print(*[idx + 1 for idx in ans])
