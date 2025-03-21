#!/usr/bin/env python3
# @check-accepted: *
import random

const = random.randint(10**5, 10**9)


def wrap(x):
    return x ^ const


n = int(input())
ships = list(map(int, input().split()))
histogram = {}
for ship in ships:
    w = wrap(ship)
    histogram[w] = histogram.get(w, 0) + 1
maxi = max(histogram.values())
most_frequent = []
for ship in histogram:
    if histogram[ship] == maxi:
        most_frequent.append(wrap(ship))
most_frequent.sort()
print(*most_frequent)
