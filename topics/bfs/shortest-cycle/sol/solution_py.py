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
branch = [-1] * (n + 1)

dist[p] = 0
branch[p] = p
q = deque([p])

min_dist = n + 1
cycle_end, cycle_start = -1, -1

while q:
    cs = q.popleft()
    for x in graph[cs]:
        if dist[x] == -1:
            parent[x] = cs
            dist[x] = dist[cs] + 1
            branch[x] = x if cs == p else branch[cs]
            q.append(x)
        else:
            if x == parent[cs]:
                continue

            if branch[cs] != branch[x]:

                if dist[x] >= dist[cs] and min_dist > dist[x] + dist[cs] + 1:
                    min_dist = dist[x] + dist[cs] + 1
                    cycle_end, cycle_start = x, cs


if min_dist == n + 1:
    print(-1)
else:

    x = cycle_end
    path = [x]
    while x != p:
        path.append(parent[x])
        x = parent[x]
    path = list(reversed(path))
    tail = [cycle_start]
    y = cycle_start
    while y != p:
        tail.append(parent[y])
        y = parent[y]
    print(min_dist)
    print(*path, end=" ")
    for v in tail:
        if v == p:
            break
        print(v, end=" ")
