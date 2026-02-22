#!/usr/bin/env python3
# @check-accepted: *

N = int(input())

max_sum = -1
legcsapadekosabb = 1

for i in range(1, N + 1):
    adatok = list(map(int, input().split()))
    heti_sum = sum(adatok)
    if heti_sum > max_sum:
        max_sum = heti_sum
        legcsapadekosabb = i

print(legcsapadekosabb)
