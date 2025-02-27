#!/usr/bin/env python3

n, r = map(int, input().split())
degree = {}
for i in range(r):
    u, v = map(int, input().split())
    degree[u] = degree.get(u, 0) + 1
    degree[v] = degree.get(v, 0) + 1
even = True
for v in degree:
    if degree[v] % 2 == 1:
        even = False

if even:
    print("YES")
else:
    print("NO")
