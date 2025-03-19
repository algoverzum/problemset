#!/usr/bin/env python3
# @check-accepted: *

n, m = [int(x) for x in input().split()]
first_ship = set([int(x) for x in input().split()])
second_ship = set([int(x) for x in input().split()])
inters = first_ship.intersection(second_ship)
print(len(inters))
print(*sorted(inters))
