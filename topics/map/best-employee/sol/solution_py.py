#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
ID_to_time = {}
max_time, max_ID = 0, 0

for _ in range(n):
    ID, event, time = [int(x) for x in input().split()]
    if event == 1:
        ID_to_time[ID] = time
    else:
        diff = time - ID_to_time[ID]
        if diff > max_time:
            max_time = diff
            max_ID = ID

print(max_ID, max_time)
