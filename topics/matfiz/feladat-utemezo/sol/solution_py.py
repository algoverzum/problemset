#!/usr/bin/env python3
# @check-accepted: *

import heapq


def main():
    n = int(input())
    pq = []
    for i in range(n):
        nev, p = input().split()
        heapq.heappush(pq, (-int(p), i, nev))

    while pq:
        # a heap legkisebb elemét adja vissza, ami nálunk egy háromelemű tuple, például (-5, 0, 'A')
        _, _, nev = heapq.heappop(pq)  # prioritas, sorszam, nev, de az első kettő nem kell.
        print(nev)


if __name__ == "__main__":
    main()
