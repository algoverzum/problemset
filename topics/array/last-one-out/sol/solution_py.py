#!/usr/bin/env python3
# @check-accepted: *

line = input().split()
n = int(line[0])
m = int(line[1])
numbers = []
for i in range(n):
    numbers.append(i + 1)
counting = 0
while len(numbers) > 1:
    counting += m
    counting %= len(numbers)
    print(numbers[counting], end=" ")
    numbers.pop(counting)
print("")
print(numbers[0])
