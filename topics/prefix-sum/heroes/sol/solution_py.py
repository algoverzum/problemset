#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
cnt = [0] * 1000002
for i in range(n):
    arr, leave = [int(x) for x in input().split()]
    cnt[arr] += 1
    cnt[leave + 1] -= 1
ans = 0
for i in range(1, 1000001):
    cnt[i] += cnt[i - 1]
    ans = max(ans, cnt[i])
print(ans)
