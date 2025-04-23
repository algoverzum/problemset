#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
intervals = [[int(x) for x in input().split()] for i in range(N)]

intervals.sort(key=lambda x: x[1])

photos = []
last_photo_time = -1

for start, end in intervals:
    if last_photo_time < start:
        last_photo_time = end - 1
        photos.append(last_photo_time)

print(len(photos))
print(*photos)
