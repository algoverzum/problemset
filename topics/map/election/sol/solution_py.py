#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
votecount = {}
for _ in range(n):
    name, votes = input().split()
    if votecount.get(name) is not None:
        votecount[name] += int(votes)
    else:
        votecount[name] = int(votes)
for key in sorted(votecount.keys()):
    print(key, end=" ")
    print(votecount[key])
