#!/usr/bin/env python3
# @check-accepted: *
import heapq


def main():
    n = int(input())
    hosszak = list(map(int, input().split()))

    pq = []
    for h in hosszak:
        heapq.heappush(pq, h)

    koltseg = 0

    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)

        uj = a + b
        koltseg += uj

        heapq.heappush(pq, uj)

    print(koltseg)


if __name__ == "__main__":
    main()
