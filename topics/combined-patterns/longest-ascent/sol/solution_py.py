#!/usr/bin/env python3
# @check-accepted: *


n = int(input())
heights = [int(input()) for i in range(n)]
max_length = 1
end_index = -1
current_length = 1
for i in range(1, n):
    if heights[i] > heights[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            end_index = i
        current_length = 1

if current_length > max_length:
    max_length = current_length
    end_index = n

if max_length > 1:
    print(end_index - max_length + 1, end_index)
else:
    print(-1)
