#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
ans = "No"
elso = []
masodik = []
for i in range(N):
    A, B = [int(x) for x in input().split()]
    elso.append(A)
    masodik.append(B)

for i in range(2, N):
    if elso[i] == masodik[i] and elso[i - 1] == masodik[i - 1] and elso[i - 2] == masodik[i - 2]:
        ans = "Yes"

print(ans)
