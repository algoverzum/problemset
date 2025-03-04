#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
first_ship = set(map(int, input().split()))
second_ship = set(map(int, input().split()))
inters = first_ship.intersection(second_ship)
print(*sorted(inters))
