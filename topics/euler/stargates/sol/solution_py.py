#!/usr/bin/env python3
# @check-accepted: *
import sys

sys.setrecursionlimit(1000)


def dfs(u):
    vis[u] = True
    for v in g[u]:
        if not vis[v]:
            dfs(v)


N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
vis = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1
    g[u].append(v)
    g[v].append(u)

dfs(1)
ans = "YES"
for u in range(1, N + 1):
    if deg[u] % 2 != 0 or (not vis[u] and deg[u] > 0):
        ans = "NO"

print(ans)
