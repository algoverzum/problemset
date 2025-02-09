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
    degree = [0] * n
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)
        degree[v1] += 1
        degree[v2] += 1

    if any(deg % 2 != 0 for deg in degree):
        return False

    visited = [False] * n
    start = next((i for i in range(n) if degree[i] > 0), -1)

    if start == -1:
        return True

    visited[start] = True
    dfs(start, adj, visited)

    return all(visited[i] or degree[i] == 0 for i in range(n))


n, r = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(r)]
print("YES" if euler(n + 1, edges) else "NO")
