#!/usr/bin/env python3


N = int(input())
fruits = [input() for _ in range(N)]

M = int(input())
fruits += [input() for _ in range(M)]

# fruits.sort()
fruits = sorted(set(fruits))

print(len(fruits))
for fruit in fruits:
    print(fruit)
