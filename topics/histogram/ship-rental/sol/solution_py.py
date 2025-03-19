#!/usr/bin/env python3
# @check-accepted: *

no_of_ships, days, rentals = [int(x) for x in input().split()]

ships = [-1] + [0] * days

for i in range(rentals):
    ship_ID, firstday, lastday = [int(x) for x in input().split()]
    for j in range(firstday, lastday + 1):
        ships[j] += 1

print(ships.index(max(ships)))
