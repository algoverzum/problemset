#!/usr/bin/env python3
# @check-accepted: *

from sys import stdin

input = stdin.readline
from collections import deque

n, m, p = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * (n + 1)
parent = [-1] * (n + 1)
branch = [-1] * (n + 1)

dist[p] = 0
branch[p] = p
queue = deque([p])

min_dist = n + 1
cycle_end, cycle_start = -1, -1

while queue:
    u = queue.popleft()
    for v in graph[u]:
        if dist[v] == -1:
            parent[v] = u
            dist[v] = dist[u] + 1
            if u == p:
                branch[v] = v
            else:
                branch[v] = branch[u]
            queue.append(v)
        else:
            if v == parent[u]:
                continue
            if branch[u] != branch[v]:
                if dist[v] >= dist[u] and min_dist > dist[v] + dist[u] + 1:
                    min_dist = dist[v] + dist[u] + 1
                    cycle_end, cycle_start = v, u

if min_dist == n + 1:
    print(-1)
else:
    u = cycle_end
    path = [u]
    while u != p:
        path.append(parent[u])
        u = parent[u]
    path = path[::-1]
    tail = [cycle_start]
    v = cycle_start
    while v != p:
        tail.append(parent[v])
        v = parent[v]
    print(min_dist)
    print(*path, *tail[:-1])
