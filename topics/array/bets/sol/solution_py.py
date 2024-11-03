#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
win = []
for i in range(N - 1):
    win.append(A[i + 1] - A[i])
diff = []
for i in range(N - 2):
    diff.append(win[i + 1] - win[i])
print(*win)
print(*diff)
