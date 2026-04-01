#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
weeks = []
for i in range(N):
    row = list(map(int, input().split()))
    weeks.append(row)

# Összegzés + maximális hét keresése
maxSum = -1
maxWeek = -1
for i in range(N):
    current_sum = sum(weeks[i])

    if current_sum >= maxSum:  # >= mert ha egyenlő, a kisebb sorszám marad
        maxSum = current_sum
        maxWeek = i + 1  # +1 mert sorszám 1-től indul
print(maxWeek)
