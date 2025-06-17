#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
teams = []

for i in range(1, n + 1):
    line = input().split()
    teams.append((-int(line[0]), int(line[1]), i))

teams.sort()

print(*[x[2] for x in teams])
