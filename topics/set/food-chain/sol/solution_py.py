#!/usr/bin/env python3
# @check-accepted: *

n = int(input())

animals = set()
carnivores = set()
pairs = []

for _ in range(n):
    predator, prey = input().split()
    animals.add(predator)
    pairs.append((predator, prey))

for predator, prey in pairs:
    if prey in animals:
        carnivores.add(predator)

print(len(carnivores))
sorted_carnivores = sorted(carnivores)
for i in range(len(carnivores)):
    print(sorted_carnivores[i])
