#!/usr/bin/env python3
# @check-accepted: *

import sys

input = sys.stdin.readline

INF = 10**9


def solv():
    N, M = map(int, input().split())

    edges = [[] for _ in range(N)]
    for _ in range(M):
        U, V, W = map(int, input().split())
        edges[U].append((V, W))

    prev = [0] + [INF] * (N - 1)

    for step in range(1, N):
        curr = prev.copy()
        for u in range(N):
            if prev[u] < INF:
                for v, w in edges[u]:
                    if prev[u] + w < curr[v]:
                        curr[v] = prev[u] + w

        for j in range(1, N):
            if curr[j] < INF:
                print(curr[j], end=" ")
            else:
                print(-1, end=" ")
        print()

        prev = curr


solv()
