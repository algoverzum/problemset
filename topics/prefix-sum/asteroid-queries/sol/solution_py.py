#!/usr/bin/env python3
# @check-accepted: *

n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

for _ in range(q):
    line = input().split()
    if line[0] == "1":
        k = int(line[1])
        print(prefix_sum[k])
    else:
        l, r = int(line[1]), int(line[2])
        print(prefix_sum[r] - prefix_sum[l - 1])
