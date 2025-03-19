#!/usr/bin/env python3
# @check-accepted: *
# works for 10^100 x 10^100 board...

for i in range(int(input())):
    x, y = map(int, input().split())
    if ((x + 1) // 2) % 2 == 1 and ((y + 1) // 2) % 2 == 1:
        print("Second")
    else:
        print("First")
