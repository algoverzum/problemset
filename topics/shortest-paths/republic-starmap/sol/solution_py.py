#!/usr/bin/env python3
# @check-accepted: *


def main():
    n, k = map(int, input().split())
    dist = []
    for i in range(n):
        row = list(map(int, input().split()))
        dist.append(row)

    # Floyd-Warshall algorithm
    for mid in range(k):
        for i in range(n):
            for j in range(n):
                if dist[i][mid] != -1 and dist[mid][j] != -1:
                    new_dist = dist[i][mid] + dist[mid][j]
                    if dist[i][j] == -1 or new_dist < dist[i][j]:
                        dist[i][j] = new_dist

    for i in range(n):
        print(*dist[i])


main()
