#!/usr/bin/env python3
# @check-accepted: *
# O(NlogN)

n = int(input())
votes = []
for _ in range(n):
    name, vote = input().split()
    votes.append((name, int(vote)))

votes.sort()
last = votes[0][0]
i = 0

while i < n:
    count = 0
    while i < n and votes[i][0] == last:
        count += votes[i][1]
        i += 1
    print(last, count)
    if i < n:
        last = votes[i][0]
