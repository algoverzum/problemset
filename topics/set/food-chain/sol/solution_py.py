#!/usr/bin/env python3
# @check-accepted: *

n = int(input())

animals = set()
predators = set()
pairs = []

for _ in range(n):
    eater, food = input().split()
    animals.add(eater)
    pairs.append([eater, food])

for eater, food in pairs:
    if food in animals:
        predators.add(eater)

print(len(predators))
for name in sorted(predators):
    print(name)
