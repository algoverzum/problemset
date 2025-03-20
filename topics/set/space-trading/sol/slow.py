#!/usr/bin/env pypy3

n, m = map(int, input().split())
first_ship = list(map(int, input().split()))
second_ship = list(map(int, input().split()))
inters = []
first_ship.sort()
for id in first_ship:
    if id not in inters:
        if id in second_ship:
            inters.append(id)
print(len(inters))
print(*sorted(inters))
