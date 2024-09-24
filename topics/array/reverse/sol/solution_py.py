#!/usr/bin/env python3
# @check-accepted: *

numbers = list(map(int, input().split()))
# print(*numbers)
# print(*numbers[::-1])
for i in range(12):
    print(numbers[i], end=" ")
print(numbers[12])
for i in range(12, 0, -1):
    print(numbers[i], end=" ")
print(numbers[0])
