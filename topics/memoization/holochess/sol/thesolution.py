#!/usr/bin/env python3

# works for 10^100 x 10^100 board...

size = 100

for i in range(int(input())):
    x, y = map(int, input().split())
    if size % 4 == 0 and x == y == size:
        print("Second")
    elif size % 4 == 1 and (x == size or y == size):
        if x + y != 2 * size - 1:
            print("Second")
        else:
            print("First")
    elif ((x + 1) // 2) % 2 == 1 and ((y + 1) // 2) % 2 == 1:
        print("Second")
    else:
        print("First")
