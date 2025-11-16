#!/usr/bin/env python3

S = 1000
M = 2000
speed = int(input())
altitude = int(input())
lepesszam = 0

while speed <= S and altitude < M:
    speed += 2
    altitude += 4
    lepesszam += 1

print(lepesszam)
