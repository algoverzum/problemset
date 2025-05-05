#!/usr/bin/env python3
# @check-accepted: *
# Bellman-Ford O(NM)

import sys

input = sys.stdin.readline

INF = float("inf")


def solv():
    N, M = map(int, input().split())
    edges = []

    for _ in range(M):
        U, V, W = map(int, input().split())
        edges.append((U, V, W))

    dist = [INF] * (N + 1)
    dist[1] = 0

    for _ in range(N - 1):
        for U, V, W in edges:
            if dist[U] != INF and dist[U] + W < dist[V]:
                dist[V] = dist[U] + W

    for i in range(1, N + 1):
        if dist[i] == INF:
            dist[i] = "X"

    print(*dist[1:])


solv()
