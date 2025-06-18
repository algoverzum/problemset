#!/usr/bin/env python3
# @check-accepted: *

INF = 10**9

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dist[i][j] == -1:
            dist[i][j] = INF

for i in range(n):
    for j in range(n):
        if i != j:
            dist[i][j] = min(dist[i][0] + dist[0][j], dist[i][j])

for row in dist:
    print(*[x if x < INF else -1 for x in row])
