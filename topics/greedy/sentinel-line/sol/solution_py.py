#!/usr/bin/env python3
# @check-accepted: *

N, H = [int(x) for x in input().split()]
stations = [int(x) for x in input().split()]

i = 0
generators = []
while i < N:
    start = stations[i]
    while i < N and stations[i] <= start + H:
        i += 1

    center = stations[i - 1]
    generators.append(i)

    while i < N and stations[i] <= center + H:
        i += 1

print(len(generators))
print(*generators)
