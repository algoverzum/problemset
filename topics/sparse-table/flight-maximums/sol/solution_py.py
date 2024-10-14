#!/usr/bin/env python3
# @check-accepted: examples small

n, q = map(int, input().split())
h = [0] + list(map(int, input().split()))
for i in range(q):
    s, k = map(int, input().split())
    print(max(h[s : s + 2**k]))
