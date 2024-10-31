#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
sections = input().split(" ")

count = 0
for i in range(1, n - 1):
    if int(sections[i - 1]) < int(sections[i]) and int(sections[i]) > int(
        sections[i + 1]
    ):
        count += 1

print(count)
