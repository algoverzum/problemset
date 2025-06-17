#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
s = [[0] * (m + 2)]

for i in range(n):
    row = [int(x) for x in input().split()]
    s.append([0] + row + [0])
s.append([0] * (m + 2))


cnt = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s[i][j] == s[i - 1][j] or s[i][j] == s[i + 1][j] or s[i][j] == s[i][j - 1] or s[i][j] == s[i][j + 1]:
            cnt += 1

print(cnt)
