#!/usr/bin/env python3

from limits import *

import sys
import os


def usage():
    print("Usage: %s file_input.txt [subtask_number]" % sys.argv[0], file=sys.stderr)
    exit(1)


def run(f, st):
    for k, v in subtasks[st].items():
        globals()[k] = v

    N, M = map(int, next(f).split())
    assert MINN <= N <= MAXN
    assert MINM <= M <= MAXM
    edges = {}
    for i in range(M):
        U, V, W = map(int, next(f).split())
        assert 1 <= U <= N
        assert 1 <= V <= N
        assert U != V
        assert MINW <= W <= MAXW
        assert (U, V) not in edges
        edges[(U, V)] = W

    assert next(f, None) is None

    INF = float("inf")
    dist = [INF] * (N + 1)
    dist[1] = 0

    for _ in range(N - 1):
        for (U, V) in edges:
            W = edges[(U, V)]
            if dist[U] != INF and dist[U] + W < dist[V]:
                dist[V] = dist[U] + W

    # Optional: check for negative cycles
    for (U, V) in edges:
        W = edges[(U, V)]
        if dist[U] != INF and dist[U] + W < dist[V]:
            assert False and "Negative cycle detected"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

    # Di default, ignora i subtask
    st = 0

    if len(sys.argv) == 3:
        st = int(sys.argv[2])

    f = open(sys.argv[1])
    run(f, st)
