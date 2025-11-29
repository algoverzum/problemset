#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
C = [int(x) for x in input().split()]

cubes = 0
for container in C:
    if container > 0:
        cubes += container - 1

print(cubes)
