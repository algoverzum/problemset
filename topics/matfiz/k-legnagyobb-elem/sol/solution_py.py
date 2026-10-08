#!/usr/bin/env python3
# @check-accepted: *
import heapq


def main():
    n, k = map(int, input().split())
    szamok = list(map(int, input().split()))

    # Min-heap a k legnagyobb elem tárolására
    pq = []

    for x in szamok:
        if len(pq) < k:
            heapq.heappush(pq, x)
        elif x > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, x)

    # A kupacban lévő elemek a k legnagyobbak, de növekvő sorrendben
    # A kimenethez csökkenő sorrendbe kell rakni őket
    eredmeny = sorted(pq, reverse=True)
    print(" ".join(map(str, eredmeny)))


if __name__ == "__main__":
    main()
