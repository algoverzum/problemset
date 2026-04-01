#!/usr/bin/env python3
# @check-accepted: *

E, N, K = map(int, input().split())
floors = []
sums = [0] * E
for i in range(E):
    row = list(map(int, input().split()))
    floors.append(row)
    sums[i] = sum(row)  # soronkénti összegzés

# Legkisebb összegű szint kiválasztása
best = 0
for i in range(1, E):
    if sums[i] < sums[best]:
        best = i
# A legjobbb szint teremlétszámai rendezve
rooms = floors[best][:]
rooms.sort()

print(best + 1)
print(" ".join(map(str, rooms)))
