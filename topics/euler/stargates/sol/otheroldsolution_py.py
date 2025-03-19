#!/usr/bin/env python3
# @check-accepted: *
from collections import defaultdict


def dfs(v, adj, visited):
    stack = [v]
    while stack:
        node = stack.pop()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)


def euler(n, edges):
    adj = defaultdict(list)
    degree = defaultdict(int)
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)
        degree[v1] += 1
        degree[v2] += 1

    for v in degree:
        if degree[v] % 2 == 1:
            return False

    visited = [False] * n
    start, _ = degree.popitem()

    visited[start] = True
    dfs(start, adj, visited)

    for i in range(n):
        if not visited[i] and degree[i] != 0:
            return False
    return True


n, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(r)]

if euler(n + 1, edges):
    print("YES")
else:
    print("NO")
