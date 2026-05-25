#!/usr/bin/env python3


def solve():
    currsize, N = map(int, input().split())
    if N < 50:
        return -1
    motes = sorted(map(int, input().split()))
    result = 0
    for i, mote in enumerate(motes):
        for _ in range(N - max(i, result)):
            if currsize > mote:
                currsize += mote
                break
            currsize += currsize - 1
            result += 1
        else:
            break
    return result


print(solve())
