#!/usr/bin/env pypy3


N = int(input())
fruits1 = [input() for _ in range(N)]

M = int(input())
fruits2 = [input() for _ in range(M)]

unique_fruits = []

for fruit in fruits1:
    if fruit not in unique_fruits and fruit not in fruits2:
        unique_fruits.append(fruit)
for fruit in fruits2:
    if fruit not in unique_fruits and fruit not in fruits1:
        unique_fruits.append(fruit)

unique_fruits.sort()

print(len(unique_fruits))
for fruit in unique_fruits:
    print(fruit)
