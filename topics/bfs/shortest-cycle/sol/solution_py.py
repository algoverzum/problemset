#!/usr/bin/env python3
# @check-accepted: *

from collections import deque

n, m, p = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
for b, a in edges:
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
parent = [-1] * (n + 1)
dist[p] = 0
q = deque([p])

min_dist = n + 1
e, a = -1, -1

while q:
    cs = q.popleft()
    for x in graph[cs]:
        if dist[x] == -1:
            q.append(x)
            dist[x] = dist[cs] + 1
            parent[x] = cs
        else:
            if dist[x] >= dist[cs] and min_dist > dist[x] + dist[cs] + 1:
                min_dist = dist[x] + dist[cs] + 1
                e, a = x, cs

    if min_dist == n + 1:
        print(-1)
    else:
        x, y = e, a
        path = [e]
        while x != p:
            path.append(parent[x])
            x = parent[x]

        print(min_dist)
        print(*reversed(path), a, end=" ")

        while parent[y] != p:
            print(parent[y], end=" ")
            y = parent[y]
        print()
