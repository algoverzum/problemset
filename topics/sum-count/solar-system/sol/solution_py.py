#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
moons = []
for _ in range(n):
    moon = int(input())
    moons.append(moon)
print(n + 1 + sum(moons))
