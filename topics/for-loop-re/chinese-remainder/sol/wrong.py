#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

ans = -1
for i in range(0, 10**5):
    if i % 5 == a and i % 7 == b and i % 11 == c:
        ans = i
        break

print(i)
