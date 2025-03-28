#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
ships = list(map(int, input().split()))
histogram = {}
for ship in ships:
    histogram[ship] = histogram.get(ship, 0) + 1
maxi = max(histogram.values())
most_frequent = []
for ship in histogram:
    if histogram[ship] == maxi:
        most_frequent.append(ship)
most_frequent.sort()
print(*most_frequent)
