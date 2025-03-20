#!/usr/bin/env pypy3
# @check-accepted: examples
# @check-time-limit-exceeded: all

n = int(input())
words = input().split()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print(len(unique))
