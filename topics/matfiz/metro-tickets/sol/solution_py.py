#!/usr/bin/env python3
# @check-accepted: *

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    count_ways = 0

    # brute force két ciklussal
    for x in b:
        for y in c:
            if x + y <= k:
                count_ways += 1

    print(count_ways)
