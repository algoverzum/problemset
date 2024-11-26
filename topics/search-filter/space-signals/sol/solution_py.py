#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
received = []
for i in range(n):
    source = input()
    frequency = int(input())
    if frequency >= 500:
        received.append(source)

print(len(received), " ".join(received))
