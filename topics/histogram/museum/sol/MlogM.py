#!/usr/bin/env python3
# @check-accepted: *

N, M = [int(x) for x in input().split()]
A = []
for i in range(M):
    F, L = [int(x) for x in input().split()]
    A.append((F, 1))
    A.append((L, 2))
A.sort()
start = end = 0
longest = 0
j = 0
cur = 0
B = []
while j < len(A):
    if A[j][1] == 1:
        count = 1
        while A[j + 1] == A[j]:
            j += 1
            count += 1
        cur += count
    else:
        cur -= 1
    j += 1
    B.append((A[j - 1][0], cur))

i = 0
small = False
while i < len(B) and B[i][1] < 2:
    i += 1
if i == len(B):
    print(1, N)
    exit()
if B[i][0] > 1:
    start = 1
    end = B[i][0] - 1
    longest = end - start + 1
lastlarge = B[i][0]

while i < len(B):
    if B[i][1] >= 2:
        if B[i - 1][1] < 2:
            if B[i][0] - 1 - lastlarge > longest:
                start = lastlarge + 1
                end = B[i][0] - 1
                longest = B[i][0] - 1 - lastlarge
            lastlarge = B[i][0]
    else:
        if B[i - 1][1] >= 2:
            lastlarge = B[i][0]
        if B[i][0] - lastlarge > longest:
            start = lastlarge + 1
            end = B[i][0]
            longest = B[i][0] - lastlarge
    i += 1

if N - lastlarge > longest:
    start = lastlarge + 1
    end = N
    longest = N - lastlarge

if longest > 0:
    print(start, end)
else:
    print(0)
