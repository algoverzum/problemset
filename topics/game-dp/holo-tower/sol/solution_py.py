#!/usr/bin/env python3
# @check-accepted: *

T = int(input())

for _ in range(T):
    N = int(input())
    win = [True] * (N + 12)

    for i in range(N, -1, -1):
        win[i] = not win[i + 4] or not win[i + 5] or not win[i + 11]

    print("R2-D2" if win[0] else "C-3PO")
