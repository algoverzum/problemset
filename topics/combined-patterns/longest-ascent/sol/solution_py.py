#!/usr/bin/env python3
# @check-accepted: *


n = int(input())
heights = [int(input()) for i in range(n)]
max_length = 0
start_index = -1
end_index = -1
current_length = 1
current_start = 0
for i in range(1, n):
    if heights[i] > heights[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            start_index = current_start
            end_index = i - 1
        current_length = 1
        current_start = i

if current_length > max_length:
    max_length = current_length
    start_index = current_start
    end_index = n - 1

if max_length > 1:
    print(start_index + 1, end_index + 1)
else:
    print(-1)
