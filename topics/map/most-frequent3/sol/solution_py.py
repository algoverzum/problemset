#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
histogram = {}
for i in range(n):
    ship = input()
    histogram[ship] = histogram.get(ship, 0) + 1
maxi = max(histogram.values())
most_frequent = []
for ship in histogram:
    if histogram[ship] == maxi:
        most_frequent.append(ship)
most_frequent.sort()
for ship in most_frequent:
    print(ship)
