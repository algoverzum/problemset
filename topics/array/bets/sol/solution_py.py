#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
A = [int(x) for x in input().split()]
day_diff = []
for i in range(N - 1):
    day_diff.append(A[i + 1] - A[i])
diff_diff = []
for i in range(N - 2):
    diff_diff.append(day_diff[i + 1] - day_diff[i])
print(*day_diff)
print(*diff_diff)
