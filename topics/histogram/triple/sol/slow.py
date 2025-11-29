#!/usr/bin/env pypy3

n = int(input())
a = [int(x) for x in input().split()]

answer = -1
for num in range(1, n + 1):
    if a.count(num) >= 3:
        answer = num
        break

print(answer)
