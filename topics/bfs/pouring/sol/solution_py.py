#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
a, b = map(int, input().split())
distance = [[-1] * (b + 1) for _ in range(a + 1)]
distance[0][0] = 0
queue = [(0, 0)]
idx = 0
solution = -1

while idx < len(queue) and solution == -1:
    x, y = queue[idx]
    idx += 1
    for i in range(6):
        if i == 0:
            nx, ny = a, y
        elif i == 1:
            nx, ny = x, b
        elif i == 2:
            nx, ny = 0, y
        elif i == 3:
            nx, ny = x, 0
        elif i == 4:
            nx, ny = x - min(x, b - y), y + min(x, b - y)
        else:
            nx, ny = x + min(y, a - x), y - min(y, a - x)

        if ny == n:
            solution = distance[x][y] + 1

        if distance[nx][ny] == -1:
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

print(solution)
