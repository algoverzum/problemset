#!/usr/bin/env python3

n = int(input())
k = int(input())

while n % 2 == 1:
    if n - k >= 0:
        n -= k
    else:
        print("NO")
        exit()
if n % 2 == 0:
    print("YES")
else:
    print("NO")
