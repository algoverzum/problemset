#!/usr/bin/env python3
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True) + [0]

wood = 0
for i in range(N):
    diff = A[i] - A[i + 1]
    if diff == 0:
        continue

    width = i + 1
    possible = diff * width

    if wood + possible >= M:
        remaining = M - wood
        drop = remaining // width
        if remaining % width != 0:
            drop += 1
        H = A[i] - drop
        print(H)
        break

    wood += possible
else:
    print(0)
