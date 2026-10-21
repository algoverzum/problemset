#!/usr/bin/env python3
# @check-accepted: *
import heapq


def main():
    n = int(input())
    szamok = list(map(int, input().split()))

    pq = []
    for x in szamok:
        heapq.heappush(pq, x)

    osszeg = 0

    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)

        c = a + b
        osszeg += c

        heapq.heappush(pq, c)

    print(osszeg)


if __name__ == "__main__":
    main()
