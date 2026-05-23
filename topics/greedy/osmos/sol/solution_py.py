#!/usr/bin/env python3
# @check-accepted: *


def solve():
    cursize, N = map(int, input().split())
    motes = sorted(map(int, input().split()))

    if cursize == 1:
        return N

    ans = N  # remove everything
    ops = 0

    for i, m in enumerate(motes):
        # current option: remove all remaining motes
        ans = min(ans, ops + (N - i))

        # grow until we can absorb m
        while cursize <= m:
            cursize += cursize - 1
            ops += 1

        cursize += m

    ans = min(ans, ops)
    return ans


print(solve())
