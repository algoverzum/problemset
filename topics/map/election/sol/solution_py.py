#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
votecount = {}
for _ in range(n):
    name, votes = input().split()
    votecount[name] = votecount.get(name, 0) + int(votes)

for name in sorted(votecount.keys()):
    print(name, votecount[name])
