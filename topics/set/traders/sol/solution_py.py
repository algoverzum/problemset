#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
fruits1 = set([input() for _ in range(N)])

M = int(input())
fruits2 = set([input() for _ in range(M)])

unique_fruits = sorted((fruits1 - fruits2) | (fruits2 - fruits1))

print(len(unique_fruits))
for fruit in unique_fruits:
    print(fruit)
