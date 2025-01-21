#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
moons = [int(x) for x in input().split()]
print(n + 1 + sum(moons))
