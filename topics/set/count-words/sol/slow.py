#!/usr/bin/env python3

n = int(input())
words = input().split()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print(len(unique))
