#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
words = input().split()
count = 0
for word in words:
    if "o" in word:
        count += 1
print(count)
