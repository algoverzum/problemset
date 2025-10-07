#!/usr/bin/env python3

a = int(input())
b = int(input())

for i in range(a + 1, b + 1):
    if i % 7 == 0:
        print(i)
print()
