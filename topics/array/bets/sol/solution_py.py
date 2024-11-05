#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
money = [int(x) for x in input().split()]
win = []
for i in range(n - 1):
    win.append(money[i + 1] - money[i])
diff = []
for i in range(n - 2):
    diff.append(win[i + 1] - win[i])
print(*win)
print(*diff)
